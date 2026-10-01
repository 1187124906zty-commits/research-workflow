"""Register actual source-inspection contracts; no model or PDE result is invented."""
from pathlib import Path
import json
import sys

REPOSITORY = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY / "src"))
from researchflow import runtime

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02")


def main():
    config = {"purpose": "Develop the existing IN625 moving-source enthalpy study into a journal-facing first manuscript from located evidence",
              "stage": "paper_formation", "constraints": ["Original SimAgent case and installed skills remain unmodified", "No new PDE runs unless a consequential gap requires them", "No invented authors, references, blind validation or agent efficacy"],
              "claims": [
                  {"id": "C_GEOMETRY", "statement": "Fixed-parameter conduction model exhibits condition-dependent melt-pool geometry discrepancies"},
                  {"id": "C_TIME", "statement": "Similar rear mushy spatial spans correspond to distinct material passage times at different scan speeds"},
                  {"id": "C_CLOSURE", "statement": "Within the computed B-condition factorial, high-temperature conductivity and heat-capacity extensions change the thermal tail through opposing effects"}],
              "uncertainties": ["Claim-specific numerical adequacy", "Published novelty and target fit", "Observation-operator compatibility"],
              "next_decision": "Inspect originals, target literature and figure needs before writing"}
    if not (ROOT / ".researchflow" / "research-state.json").exists():
        runtime.initialize(ROOT, "How do scan conditions and high-temperature closure alter geometry and solidification history in a conduction-based IN625 single-track model?", config)
    definitions = [
        {"id": "T_EVIDENCE", "role": "evidence", "question": "Which results, equations and verification evidence survive direct inspection?", "purpose": "Determine permissible manuscript claims and unresolved limitations", "claim_ids": ["C_GEOMETRY", "C_TIME", "C_CLOSURE"],
         "inputs": [{"path": str(SOURCE / "report" / name)} for name in ("current-results.json", "experimental-comparison.csv", "constitutive-factorial-effects.csv", "constitutive-factorial-results.json")], "outputs": ["evidence"], "acceptance": ["Exact values with original locators; distinguish calibration, diagnostic comparison, numerical verification and physical inference"]},
        {"id": "T_JOURNAL", "role": "literature", "question": "Which venue and prior works provide a defensible reader argument and current format?", "purpose": "Set target, novelty scope and manuscript requirements", "claim_ids": [], "inputs": [{"path": str(SOURCE / "README.md")}], "outputs": ["literature"], "acceptance": ["Verified citations and primary instructions; actual fulltext/exemplar availability and unresolved access stated"]},
    ]
    current = runtime.context(ROOT)
    for contract in definitions:
        if contract["id"] not in current["tasks"]:
            contract.update(budget={"max_attempts": 2, "max_no_progress": 2}, depends_on=[])
            runtime.task(ROOT, contract)
    (ROOT / "governance" / "intake.json").write_text(json.dumps({"scope": "User delegated target, contribution and visual choices; LaTeX and PDF requested", "source_case": str(SOURCE), "paper_root": str(ROOT), "original_case_execution": "SimAgent; this manuscript process is prospective ResearchFlow/MAF work", "paperspine_use": "Local scholarly methods and ResearchFlow file handoff; no Web user clicks or managed-skill update claimed"}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(runtime.audit(ROOT), ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
