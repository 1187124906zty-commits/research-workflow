"""Actual CLI handoffs over an explicit synthetic evidence-writing fixture.

No LLM, solver, source acquisition or scientific-quality classifier is invoked.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]


def write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(project: Path) -> dict:
    project = project.resolve()
    if (project / ".researchflow").exists():
        raise ValueError("Use a fresh output directory; existing research state is not overwritten")
    project.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(REPO / "src") + os.pathsep + env.get("PYTHONPATH", "")
    env["PYTHONIOENCODING"] = "utf-8"
    transcript = []

    def cli(*args: str, expected_exit: int = 0) -> dict:
        result = subprocess.run([sys.executable, "-m", "researchflow", *args], env=env,
                                capture_output=True, text=True, encoding="utf-8", check=False)
        output = json.loads(result.stdout or result.stderr)
        transcript.append({"arguments": list(args), "exit_code": result.returncode, "output": output})
        write(project / "cli-transcript.json", {"fixture_kind": "synthetic", "commands": transcript})
        if result.returncode != expected_exit:
            raise RuntimeError(f"CLI {args[0]} returned {result.returncode}: {output}")
        return output

    write(project / "fixture.json", {
        "fixture_kind": "synthetic comparison; no experiment or solver run",
        "observable": "width_micrometres", "reference": 100, "uncertainty": 5,
        "conditions": "same geometry and scan conditions",
        "models": [{"id": "A", "convection": True, "width": 100},
                   {"id": "B", "convection": False, "width": 100}],
        "unobserved": ["temperature", "velocity"],
    })
    write(project / "config.json", {"stage": "paper_formation", "claims": [
        {"id": "C_MATCH", "statement": "Both models match width within uncertainty in the synthetic fixture"},
        {"id": "C_MECHANISM", "statement": "The fixture's width agreement uniquely identifies convection"},
        {"id": "C_EDIT", "statement": "The editorial paragraph is suitable for the intended manuscript"},
    ]})
    cli("init", str(project), "--question", "What may a paragraph infer from width agreement?",
        "--config", str(project / "config.json"))

    def contract(tid: str, role: str, claims: list[str], inputs: list[dict], dependencies: list) -> dict:
        return {"id": tid, "role": role, "question": "Which inference is warranted by the supplied evidence?",
                "purpose": "Keep observation and mechanism interpretation distinct in the writing handoff",
                "claim_ids": claims, "inputs": inputs, "outputs": [f"results/{tid}/"],
                "acceptance": ["Locate evidence and preserve conditions; return permitted and unresolved inference"],
                "budget": {"max_attempts": 1, "max_no_progress": 1}, "depends_on": dependencies}

    write(project / "review-task.json", contract("REVIEW", "evidence_review",
          ["C_MATCH", "C_MECHANISM"], [{"path": "fixture.json"}], []))
    cli("task", str(project), str(project / "review-task.json"))
    write(project / "results/REVIEW/interpretation.json", {
        "fixture_kind": "synthetic", "evidence_unit": "fixture.json:reference/models/uncertainty",
        "permitted_inference": "A and B reproduce the specified width within the fixture's uncertainty",
        "excluded_inference": "Width agreement uniquely identifies convection",
        "reason": "Distinct model mechanisms give the same observed output",
        "next_evidence_question": "Would an independently measured temperature or velocity distinguish A and B?",
    })
    write(project / "review-result.json", {
        "attempt": 1, "changed_understanding": True,
        "reason": "The fixture permits an output comparison but leaves mechanism discrimination unresolved",
        "evidence": [{"path": "results/REVIEW/interpretation.json", "level": "observation",
                      "kind": "support", "claim_ids": ["C_MATCH"],
                      "summary": "Scoped agreement in a synthetic fixture, not physical validation"}], "blockers": []})
    cli("record", str(project), "REVIEW", str(project / "review-result.json"))
    pending = cli("audit", str(project), expected_exit=2)
    write(project / "review-decision.json", {
        "action": "accept", "reason": "The reviewed fixture answers the bounded support question",
        "promotions": [{"claim_id": "C_MATCH", "level": "observation", "evidence_indices": [0],
                        "reason": "These fixture values support only their explicitly synthetic width comparison"}],
        "claim_updates": [{"claim_id": "C_MECHANISM", "status": "narrowed",
                           "reason": "Width alone does not distinguish the two candidate mechanisms"}]})
    cli("decide", str(project), "REVIEW", str(project / "review-decision.json"))
    write(project / "write-task.json", contract("WRITE", "writer", ["C_EDIT"],
          [{"path": "fixture.json"}, {"path": "results/REVIEW/interpretation.json"}],
          [{"task_id": "REVIEW", "claim_ids": ["C_MATCH"], "required_level": "observation",
            "affects_claim_ids": ["C_EDIT"]}]))
    cli("task", str(project), str(project / "write-task.json"))
    write(project / "results/WRITE/paragraph-trace.json", {
        "fixture_kind": "synthetic protocol demonstration, not an LLM forward-test answer",
        "paragraph_task": "Report width agreement and the remaining mechanism ambiguity",
        "evidence_units": [{"path": "fixture.json", "locator": "reference/models/uncertainty",
                            "data_role": "constructed comparison"}],
        "permitted_inference": "Width agreement at the specified conditions",
        "excluded_inference": "Unique mechanism identification or real-world physical validation",
        "language_choice": "Direct evidence-shaped wording; agreement with + reference, under + conditions",
        "context_check": "Methods defines width; following paragraph discusses independent diagnostics",
        "remaining_question": "Which observable would distinguish A and B?",
    })
    (project / "results/WRITE/paragraph.md").write_text(
        "In this synthetic fixture, models A and B both predict a width of 100 micrometres, "
        "agreeing with the reference within its 5-micrometre uncertainty under the same scan conditions. "
        "Because the two models differ in their treatment of convection, this width comparison leaves "
        "the mechanism unresolved. Independent temperature or velocity observations could distinguish "
        "their predictions. No physical validation was performed.\n", encoding="utf-8")
    write(project / "write-result.json", {
        "attempt": 1, "changed_understanding": True, "reason": "Paragraph makes the accepted support boundary explicit",
        "evidence": [{"path": "results/WRITE/paragraph-trace.json", "level": "observation", "kind": "observation",
                      "claim_ids": ["C_EDIT"], "summary": "Editorial trace with conditions and unresolved inference"}],
        "blockers": []})
    cli("record", str(project), "WRITE", str(project / "write-result.json"))
    write(project / "write-decision.json", {"action": "accept",
          "reason": "Editorial handoff is reviewable; acceptance supplies no physical-evidence promotion"})
    cli("decide", str(project), "WRITE", str(project / "write-decision.json"))
    ctx = cli("context", str(project))
    final_audit = cli("audit", str(project))
    summary = {"fixture_kind": "synthetic", "pending_audit_protocol_ok": pending["protocol_ok"],
               "final_audit_protocol_ok": final_audit["protocol_ok"],
               "claims": {cid: {"status": value["status"], "support_levels": list(value["support"])}
                          for cid, value in ctx["claims"].items()},
               "scientific_validation": "not performed", "llm_forward_test": "not performed",
               "paragraph": "results/WRITE/paragraph.md", "trace": "results/WRITE/paragraph-trace.json"}
    write(project / "summary.json", summary)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    print(json.dumps(run(parser.parse_args().output), ensure_ascii=False, indent=2))
