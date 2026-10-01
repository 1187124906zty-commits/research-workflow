"""Register real section-research work and preserve the pre-revision manuscript."""
from pathlib import Path
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO / 'src'))
from researchflow import runtime

def main():
    revision = ROOT / 'revision-r2'
    (revision / 'inputs').mkdir(parents=True, exist_ok=True)
    previous = revision / 'inputs' / 'manuscript-r1.tex'
    if not previous.exists():
        shutil.copy2(ROOT / 'manuscript.tex', previous)
    runtime.plan(ROOT, {
        'reason': 'User authorizes actual complete revision using the investigated multi-agent design: literature-grounded scientific tension, controlled quantitative response, specific discussion and conclusions that close the argument.',
        'next_decision': 'Accept new research-line, journal-learning and methods/results returns, then freeze the argument and use actual MAF section writing and targeted exchange before integrating the open LaTeX source.'
    })
    common = [{'path': 'revision-r2/inputs/manuscript-r1.tex'}, {'path': 'evidence/evidence-dossier.md'}]
    specs = [
        ('R2_LITERATURE', 'literature', 'paperspine_section_design', 'literature',
         'Locate foundational and recent near-neighbour evidence; establish a scientific tension and a useful bounded increment rather than inventing an unprecedented gap.',
         ['Verified identities and read scopes, actual prior-work comparison and contrary evidence', 'Useful bibliography scale and substantive sources for Introduction and Discussion']),
        ('R2_JOURNAL', 'literature', 'ammt_manuscript_review', 'journal',
         'Learn recent comparable Additive Manufacturing original articles and applicable current guidance; transfer paragraph, abstract, evidence and figure decisions to this paper.',
         ['Real PDFs and original passages distinguish requirements, conventions and choices', 'Six distinct target research exemplars pursued with actual access limitations preserved']),
        ('R2_METHODS_RESULTS', 'evidence', 'section_runtime_diagnosis', 'methods-results',
         'Audit actual executed properties, model, observation operators and retained quantitative comparisons; deliver reproducible Methods and evidence-ordered Results candidates without new PDE solves.',
         ['Original code/data and quantitative effects checked with claim-specific numerical scope', 'Actual section candidates, design rationale and explicit affected-section questions'])
    ]
    existing = runtime.context(ROOT)['tasks']
    for tid, role, owner, folder, question, acceptance in specs:
        (revision / folder).mkdir(exist_ok=True)
        if tid not in existing:
            runtime.task(ROOT, {
                'id': tid, 'role': role, 'owner': owner, 'question': question,
                'purpose': 'Close the field-tension, study-design and evidence argument in the revised full manuscript',
                'claim_ids': [], 'inputs': common,
                'outputs': [f'revision-r2/{folder}/'], 'writes': [f'revision-r2/{folder}/'],
                'acceptance': acceptance, 'budget': {'max_attempts': 2, 'max_no_progress': 2},
                'depends_on': ['T_EVIDENCE', 'T_JOURNAL']
            })
    print(json.dumps(runtime.audit(ROOT), indent=2))

if __name__ == '__main__':
    main()
