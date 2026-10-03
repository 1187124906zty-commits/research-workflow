"""Coordinate R7 argument-first writing with bounded, disjoint candidates."""
import argparse
import json
from pathlib import Path
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
TASKS = {
    'R7_GUIDANCE': ('editor', 'revision-r7/guidance/', [], 'Which reusable writing decisions are missing or not applied, and how should task-scoped instructions improve argument compression, paragraph progression and design narration?'),
    'R7_FRAMING': ('writer', 'revision-r7/framing/', [], 'How should a primarily numerical study build a focused literature-to-gap introduction and an abstract that connects the approach, grouped findings and defensible future use?'),
    'R7_BODY': ('writer', 'revision-r7/body/', [], 'How should model rationale, premises, scenario definitions and evidence units make Methods and combined Results/Discussion coherent without repetitive parameter inventories?'),
    'R7_TRANSFER': ('reviewer', 'revision-r7/forward/', ['R7_GUIDANCE'], 'Can the actual task-scoped writing guide produce coherent prose for a supplied theory fixture without inventing empirical evidence or treating this manuscript topic as a universal template?'),
    'R7_INTEGRATION': ('coordinator', 'revision-r7/integration/', ['R7_GUIDANCE', 'R7_FRAMING', 'R7_BODY'], 'Do the candidates form one evidence-preserving argument with stable object names, source support and appropriate information depth in each section?'),
    'R7_REVIEW': ('reviewer', 'revision-r7/review/', ['R7_INTEGRATION', 'R7_TRANSFER'], 'Does the actual revised manuscript communicate a focused numerical argument, and do the generic instructions transfer to another research type without reproducing topic specialization?'),
    'R7_RECHECK': ('reviewer', 'revision-r7/review/', ['R7_REVIEW'], 'Does the actual notation-repaired manuscript close the located initial review finding, with unchanged scientific values, current source/PDF bindings and independently rechecked guide G1?'),
    'R7_DELIVERY': ('coordinator', 'revision-r7/delivery/', ['R7_REVIEW', 'R7_RECHECK'], 'Do the same-file PDF/source package, local guide/reference bundle and actual guidance distribution pass necessary checks while human assessment remains pending?'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['start', 'dispatch', 'accept', 'audit'])
    parser.add_argument('task', nargs='?')
    parser.add_argument('--reason')
    parser.add_argument('--paths', nargs='*')
    args = parser.parse_args()
    if args.action == 'start':
        folder = PAPER / 'revision-r7'
        folder.mkdir(exist_ok=True)
        frozen = folder / 'manuscript-input.tex'
        if not frozen.exists():
            frozen.write_bytes((PAPER / 'manuscript.tex').read_bytes())
        runtime.plan(PAPER, {
            'reason': 'User identifies excessive abstract detail, diffuse introduction, weak positional sentence roles, archive-led case labels and repetitive method parameters. Diagnose generic design first, then revise the same evidence-bound paper.',
            'next_decision': 'Establish argument and information responsibilities, task-scoped reusable guides and literature-supported section candidates; integrate, independently review and deliver the same manuscript locally.',
        })
        ids = ['R7_GUIDANCE', 'R7_FRAMING', 'R7_BODY']
    elif args.action == 'dispatch':
        ids = [args.task]
    else:
        ids = []
    for tid in ids:
        role, output, deps, question = TASKS[tid]
        existing = runtime.context(PAPER)['tasks'].get(tid)
        if existing:
            contract = runtime.context(PAPER, tid)['task']
            if contract['depends_on'] != deps:
                raise RuntimeError('Existing dependency contract differs: ' + tid)
            continue
        (PAPER / output).mkdir(parents=True, exist_ok=True)
        inputs = [{'path': 'revision-r7/manuscript-input.tex'},
                  {'path': 'revision-r6/sources/support-ledger.json'},
                  {'path': 'revision-r6/simulation-supplement/observations-matched.json'},
                  {'path': 'revision-r6/simulation-supplement/acceptance-disposition.json'}]
        if tid in {'R7_REVIEW', 'R7_RECHECK'}:
            inputs += [{'path': 'manuscript.tex'}, {'path': 'manuscript.pdf'}]
        runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role,
            'question': question, 'purpose': 'Explain a complete scientific argument with section-appropriate specificity, honest source/evidence scope and reusable topic-neutral guidance.',
            'claim_ids': [], 'inputs': inputs, 'outputs': [output], 'writes': [output],
            'depends_on': deps,
            'acceptance': ['Real source and guidance use; connected section candidates; preserve accepted results and limitations; return specific candidate and missing decisions rather than indefinite polish.'],
            'budget': {'max_attempts': 2, 'max_no_progress': 2}})
    if args.action == 'accept':
        if not args.reason or not args.paths:
            parser.error('accept requires located paths and requester reason')
        if runtime.context(PAPER)['tasks'][args.task]['status'] != 'accepted':
            runtime.record(PAPER, args.task, {'attempt': 1, 'changed_understanding': False,
                'reason': args.reason, 'evidence': [{'path': path, 'level': 'observation', 'kind': 'observation', 'claim_ids': [], 'summary': args.reason} for path in args.paths], 'blockers': []})
            runtime.decide(PAPER, args.task, {'action': 'accept', 'reason': args.reason})
    audit = runtime.audit(PAPER)
    print(json.dumps({'protocol_ok': audit['protocol_ok'], 'blocking': [r for r in audit['risks'] if r['blocking']]}, ensure_ascii=True))


if __name__ == '__main__':
    main()
