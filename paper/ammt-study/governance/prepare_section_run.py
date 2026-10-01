"""Freeze coordinator-accepted R2 research for native MAF section contracts."""
from pathlib import Path
import json
import sys

PAPER = Path(__file__).resolve().parents[1]
REPO = PAPER.parents[1]
sys.path.insert(0, str(REPO / "src"))
from researchflow import runtime


def main():
    current = runtime.context(PAPER)
    for task_id in ("R2_LITERATURE", "T_JOURNAL", "R2_METHODS_RESULTS"):
        if current["tasks"][task_id]["status"] != "accepted":
            raise SystemExit(f"Root must read and accept {task_id} before this dispatch.")
    revision = PAPER / "revision-r2"
    inputs = []
    files = [revision / "argument-r001.md", revision / "journal-dispatch-profile.md",
             PAPER / "literature/journal-dossier.md", PAPER / "literature/exemplar-notes.md",
             PAPER / "evidence/evidence-dossier.md",
             PAPER / "evidence/verified-data.json", PAPER / "literature/bibliography-r2.bib"]
    for folder in ("literature", "journal", "methods-results"):
        files.extend(sorted((revision / folder).glob("*.md")))
        files.extend(sorted((revision / folder).glob("*.bib")))
        files.extend(sorted((revision / folder).glob("section-*.tex")))
        files.extend(sorted((revision / folder / "text").glob("*.txt")))
        files.extend(sorted((revision / folder / "texts").glob("*.txt")))
    files.extend([revision / "methods-results/computed-audit.json"])
    for path in files:
        if path.is_file():
            inputs.append({"source": str(path), "path": "inputs/" + path.relative_to(PAPER).as_posix()})
    manifest = {
        "brief": (
            "Produce two versioned English section candidates for the existing AMMT IN625 research article. "
            "Use the accepted argument-r001 and source notes, then selectively inspect consequential original text. "
            "Introduction owns the literature-grounded scientific tension and study necessity; Discussion owns synthesis, "
            "specific prior-work comparison, mechanism conditions and alternatives. Read the actual executed Methods/Results. "
            "The coordinator already owns direction and full-paper integration. Do not invent a new gap or major novelty. "
            "No PDE, new numerical experiment, internet retrieval, or installed-skill modification. "
            "Use existing BibTeX keys only. Separate observed/calibrated/derived quantities, nonblind data roles and verification/validation. "
            "You are not alone: use only assigned writes, never revert others or edit canonical manuscript.tex. "
            "Use local PaperSpine scholarly methods as directed by the frozen argument, with no managed-product operation. "
            "Pure editorial gains set changed_understanding=false and are explained in memory. Evidence is observation, no physical promotion. "
            "Write r001 for attempt 1 and r002 for attempt 2; never overwrite a returned version. "
            "Return actual candidate file paths as evidence and the accepted candidate files as completion deliverables. "
            "After the two candidates, actual independent role reviews and requester dispositions, complete this bounded section session. "
            "Do not add downstream tasks or claim the whole manuscript reviewed; root performs targeted exchange and whole-paper review next."
        ),
        "inputs": inputs, "parallel": 2, "max_cycles": 3, "timeout_seconds": 1500,
        "tasks": []
    }
    questions = {
        "introduction": (
            "Write a substantial but focused Introduction with literature depth comparable to Additive Manufacturing original research. "
            "Start from the shared scientific tension and relevant prior progress; articulate the bounded need with declarative prose. "
            "Do not open with why/how/which or make high-temperature k/cp the first field-level problem. "
            "Discuss genuine 2024-2026 near neighbours and do not repeat disproven novelty. "
            "Finish with a precise study response whose every promise is answered by Methods/Results. "
            "Cite substantive specific source groups with their actual conditions; avoid unrelated reference padding. "
            "Draft approximately 900-1300 useful words if the argument requires them, rather than a fixed word quota. "
            "Return draft.tex with section heading and semantic citations, argument.md, and memory.md with source-use and interface concerns."
        ),
        "discussion": (
            "Write a detailed, specific Discussion from the actual Methods/Results and literature. "
            "Answer the scientific tension: what does geometry calibration constrain, and how does fixed-source closure decomposition improve interpretation? "
            "Compare Myers, Kollmannsberger, new 2026 reliability/fitting-free diagnosis and relevant thermal-property/calibration studies on actual conditions. "
            "Explain rear-boundary translation versus phase separation, latent-inclusive storage, k changing surface recovery, "
            "and the retained flux counterexample; do not assert exclusive bulk causality or experimental property identification. "
            "Separate the speed-time coordinate mapping from independent physical validation. "
            "Develop a small set of surviving explanations and informative next tests; consolidate interpretation-changing limitations. "
            "Approximately 1400-2000 useful words may be appropriate; do not pad. Return draft.tex with subsection logic, argument.md and memory.md."
        )
    }
    for section, question in questions.items():
        directory = f"sections/{section}"
        manifest["tasks"].append({
            "id": "R2_" + section.upper(), "role": "writer", "question": question,
            "purpose": "Close the field-tension/design/evidence argument in one coherent research first draft",
            "outputs": [directory + "/"],
            "writes": [directory + "/"],
            "acceptance": [
                "Read and actually use verified sources, accepted argument and executed evidence; exact citation identities and claim scope are retained",
                "Candidate is substantive scholarly prose, not production-status narration; memory explains source decisions, editorial delta and unresolved interfaces",
                "Semantic LaTeX is usable and no promised physical prediction exceeds the existing study"
            ],
            "budget": {"max_attempts": 2, "max_no_progress": 2}
        })
    output = revision / "maf-drafts.json"
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {output}; {len(inputs)} real frozen input files. Native run still required.")


if __name__ == "__main__":
    main()
