"""Bounded R6 manuscript/skill handoffs; only the coordinator writes shared state."""
import argparse
import json
from pathlib import Path
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
TASKS = {
    'R6_SOURCES': ('literature', 'revision-r6/sources/', [],
        'Which concrete predecessor findings, property definitions and measurement populations justify this study and its scientific vocabulary?'),
    'R6_ARCHITECTURE': ('editor', 'revision-r6/architecture/', [],
        'How should evidence type, section dependencies and the reverse outline determine coherent chapter ownership and the argument?'),
    'R6_GUIDANCE': ('reviewer', 'revision-r6/guidance/', [],
        'Which source-grounded writing methods are missing or unenforced in the current project skills, especially object continuity and section architecture?'),
    'R6_APPLICATION': ('writer', 'revision-r6/application/', ['R6_SOURCES', 'R6_ARCHITECTURE', 'R6_GUIDANCE'],
        'Do workers actually apply the revised guides to a connected Introduction, methods/results and discussion while preserving the scientific evidence?'),
    'R6_SIMULATION_SUPPLEMENT': ('simulation', 'revision-r6/simulation-supplement/', [],
        'Do matched refined property branches preserve the rear-boundary displacement and resolve the small separation response at retained source power?'),
    'R6_REVIEW': ('reviewer', 'revision-r6/review/', ['R6_APPLICATION'],
        'Does the integrated source resolve object identity, predecessor lineage, sentence relations and whole-paper continuity?'),
    'R6_SUPPLEMENT_APPLICATION': ('writer', 'revision-r6/application/', ['R6_SIMULATION_SUPPLEMENT'],
        'How do accepted supplementary observations change the actual methods, result units, figures, abstract and conclusions in the existing manuscript?'),
    'R6_SUPPLEMENT_REVIEW': ('reviewer', 'revision-r6/review/', ['R6_SUPPLEMENT_APPLICATION'],
        'Does the integrated manuscript use the completed supplementary evidence accurately, with connected interpretation and legible affected pages?'),
    'R6_DELIVERY': ('coordinator', 'revision-r6/delivery/', ['R6_REVIEW', 'R6_SUPPLEMENT_REVIEW'],
        'Do the revised local PDF/source package, human-reading bundle and packaged skills pass their actual affected checks while publication remains pending human assessment?'),
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['start', 'dispatch', 'accept', 'audit'])
    p.add_argument('task', nargs='?')
    p.add_argument('--reason')
    p.add_argument('--paths', nargs='*')
    p.add_argument('--scientific-change', action='store_true',
                   help='Use only when inspected evidence changes the research understanding')
    a = p.parse_args()
    if a.action == 'start':
        folder = PAPER / 'revision-r6'
        folder.mkdir(exist_ok=True)
        frozen = folder / 'manuscript-input.tex'
        if not frozen.exists():
            frozen.write_bytes((PAPER / 'manuscript.tex').read_bytes())
        runtime.plan(PAPER, {'reason': 'R6 responds to fragmented Results/Discussion, weak study-unit motivations, limited citations and evidence-dependent section order.',
            'next_decision': 'Audit target-journal structures and citation needs; establish Methods versus integrated Results/Discussion handoffs; then revise and review the existing evidence.'})
        ids = ['R6_SOURCES', 'R6_ARCHITECTURE', 'R6_GUIDANCE']
    elif a.action == 'dispatch':
        ids = [a.task]
    else:
        ids = []
    for tid in ids:
        role, output, deps, question = TASKS[tid]
        existing = runtime.context(PAPER)['tasks'].get(tid)
        if existing is not None:
            contract = runtime.context(PAPER, tid)['task']
            registered_deps = [d if isinstance(d, str) else d['task_id'] for d in contract['depends_on']]
            if registered_deps != deps:
                raise RuntimeError(f'{tid} is already registered with different dependencies; reconcile its recorded contract before dispatching this revised plan')
            continue
        (PAPER / output).mkdir(parents=True, exist_ok=True)
        inputs = [{'path': 'revision-r6/manuscript-input.tex'},
                  {'path': 'evidence/verified-data.json'}, {'path': 'revision-r3/citations/support-ledger.json'}]
        if tid in {'R6_SUPPLEMENT_APPLICATION', 'R6_SUPPLEMENT_REVIEW'}:
            inputs += [{'path': 'revision-r6/simulation-supplement/observations-matched.json'},
                       {'path': 'revision-r6/simulation-supplement/acceptance-disposition.json'}]
        if tid == 'R6_SUPPLEMENT_REVIEW':
            inputs += [{'path': 'manuscript.tex'}, {'path': 'manuscript.pdf'}]
        runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role,
            'question': question, 'purpose': 'Integrate observation and interpretation by evidence dependencies, broaden specific citation support, and keep reusable skills topic-neutral.',
            'claim_ids': [], 'inputs': inputs,
            'outputs': [output], 'writes': [output], 'depends_on': deps,
            'acceptance': ['Located sources, stable scientific objects, truthful comparators and a complete bounded return; no new model performance or physical validation claim.'],
            'budget': {'max_attempts': 2, 'max_no_progress': 2}})
    if a.action == 'accept':
        if not a.reason or not a.paths:
            p.error('accept requires --reason and --paths for an inspected handoff')
        if runtime.context(PAPER)['tasks'][a.task]['status'] != 'accepted':
            runtime.record(PAPER, a.task, {'attempt': 1, 'changed_understanding': a.scientific_change, 'reason': a.reason,
                'evidence': [{'path': x, 'level': 'observation', 'kind': 'observation', 'claim_ids': [], 'summary': a.reason} for x in a.paths], 'blockers': []})
            runtime.decide(PAPER, a.task, {'action': 'accept', 'reason': a.reason})
    check = runtime.audit(PAPER)
    print(json.dumps({'protocol_ok': check['protocol_ok'], 'blocking': [x for x in check.get('risks', []) if x.get('blocking')]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
