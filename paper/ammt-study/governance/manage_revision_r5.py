"""Bounded R5 manuscript/skill handoffs; only the coordinator writes shared state."""
import argparse
import json
from pathlib import Path
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
TASKS = {
    'R5_SOURCES': ('literature', 'revision-r5/sources/', [],
        'Which concrete predecessor findings, property definitions and measurement populations justify this study and its scientific vocabulary?'),
    'R5_ARCHITECTURE': ('editor', 'revision-r5/architecture/', [],
        'How should evidence type, section dependencies and the reverse outline determine coherent chapter ownership and the argument?'),
    'R5_GUIDANCE': ('reviewer', 'revision-r5/guidance/', [],
        'Which source-grounded writing methods are missing or unenforced in the current project skills, especially object continuity and section architecture?'),
    'R5_APPLICATION': ('writer', 'revision-r5/application/', ['R5_SOURCES', 'R5_ARCHITECTURE', 'R5_GUIDANCE'],
        'Do workers actually apply the revised guides to a connected Introduction, methods/results and discussion while preserving the scientific evidence?'),
    'R5_REVIEW': ('reviewer', 'revision-r5/review/', ['R5_APPLICATION'],
        'Does the integrated source resolve object identity, predecessor lineage, sentence relations and whole-paper continuity?'),
    'R5_DELIVERY': ('coordinator', 'revision-r5/delivery/', ['R5_REVIEW'],
        'Do the revised PDF/source package, packaged skills and published repositories pass their actual affected checks?'),
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['start', 'dispatch', 'accept', 'audit'])
    p.add_argument('task', nargs='?')
    p.add_argument('--reason')
    p.add_argument('--paths', nargs='*')
    a = p.parse_args()
    if a.action == 'start':
        folder = PAPER / 'revision-r5'
        folder.mkdir(exist_ok=True)
        frozen = folder / 'manuscript-input.tex'
        if not frozen.exists():
            frozen.write_bytes((PAPER / 'manuscript.tex').read_bytes())
        runtime.plan(PAPER, {'reason': 'R5 responds to concrete object ambiguity and broken argument continuity before chapter revision.',
            'next_decision': 'Locate predecessor gaps, audit writing guidance and agree section dependencies; then apply and independently review on the existing six-solution case.'})
        ids = ['R5_SOURCES', 'R5_ARCHITECTURE', 'R5_GUIDANCE']
    elif a.action == 'dispatch':
        ids = [a.task]
    else:
        ids = []
    for tid in ids:
        role, output, deps, question = TASKS[tid]
        if tid in runtime.context(PAPER)['tasks']:
            continue
        (PAPER / output).mkdir(parents=True, exist_ok=True)
        runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role,
            'question': question, 'purpose': 'Improve scientific argument and reusable skill execution, rather than substituting fluent language for evidence.',
            'claim_ids': [], 'inputs': [{'path': 'revision-r5/manuscript-input.tex'},
                {'path': 'evidence/verified-data.json'}, {'path': 'revision-r3/citations/support-ledger.json'}],
            'outputs': [output], 'writes': [output], 'depends_on': deps,
            'acceptance': ['Located sources, stable scientific objects, truthful comparators and a complete bounded return; no new model performance or physical validation claim.'],
            'budget': {'max_attempts': 2, 'max_no_progress': 2}})
    if a.action == 'accept':
        if not a.reason or not a.paths:
            p.error('accept requires --reason and --paths for an inspected handoff')
        if runtime.context(PAPER)['tasks'][a.task]['status'] != 'accepted':
            runtime.record(PAPER, a.task, {'attempt': 1, 'changed_understanding': False, 'reason': a.reason,
                'evidence': [{'path': x, 'level': 'observation', 'kind': 'observation', 'claim_ids': [], 'summary': a.reason} for x in a.paths], 'blockers': []})
            runtime.decide(PAPER, a.task, {'action': 'accept', 'reason': a.reason})
    check = runtime.audit(PAPER)
    print(json.dumps({'protocol_ok': check['protocol_ok'], 'blocking': [x for x in check.get('risks', []) if x.get('blocking')]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
