"""Coordinate complementary chapter responsibilities in the existing manuscript."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / 'revision-r10'
TASKS = {
    'R10_RULES': ('writer', 'guidance/', [], 'What do actual published section boundaries show about complementary explanatory depth, and which missing coordination decision belongs in the generic chapter guidance?'),
    'R10_INTRO': ('writer', 'framing/', ['R10_RULES'], 'Does the Introduction closing establish the objective and broad route while handing operational decisions to Methods, without losing the source-supported scientific question?'),
    'R10_METHODS': ('writer', 'methods/', ['R10_RULES'], 'Does Methods start advance to the executed study structure rather than repeat the introductory promise, with design rationale retained at its proper location?'),
    'R10_INTEGRATION': ('coordinator', 'integration/', ['R10_INTRO', 'R10_METHODS'], 'Do reciprocally checked chapter interfaces add complementary information across the same complete paper and preserve all scientific identities?'),
    'R10_REVIEW': ('reviewer', 'review/', ['R10_INTEGRATION'], 'Does the actual source and PDF fulfill the reusable chapter contract without redundant route recital, missing rationale, or scientific overstatement?'),
    'R10_DELIVERY': ('coordinator', 'delivery/', ['R10_REVIEW'], 'Are the reviewed same-source manuscript and local human-reading materials current and reproducible?'),
}
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('action', choices=['start', 'dispatch', 'accept', 'audit'])
p.add_argument('task', nargs='?')
p.add_argument('--reason')
p.add_argument('--paths', nargs='*')
a = p.parse_args()
if a.action == 'start':
    REV.mkdir(exist_ok=True)
    for name in ('manuscript.tex', 'manuscript.pdf'):
        target = REV / ('manuscript-input.' + name.rsplit('.', 1)[1])
        if not target.exists():
            target.write_bytes((PAPER / name).read_bytes())
    runtime.plan(PAPER, {'stage': 'paper_revision', 'reason': 'User identifies repeated study route at Introduction/Methods boundary and requests complementary chapter responsibilities with multi-agent handoffs grounded in published examples.', 'next_decision': 'Read actual section boundaries, improve the missing generic allocation decision, revise complementary passages, reciprocally check, independently review and deliver the same manuscript.'})
    ids = ['R10_RULES']
elif a.action == 'dispatch':
    ids = [a.task]
else:
    ids = []
for tid in ids:
    if tid in runtime.context(PAPER)['tasks']:
        continue
    role, folder, deps, question = TASKS[tid]
    (REV / folder).mkdir(parents=True, exist_ok=True)
    inputs = [{'path': 'revision-r10/manuscript-input.tex'},
              {'path': 'revision-r8/reference/supplied-xiong2022.pdf'},
              {'path': 'revision-r9/sources/support-ledger.json'}]
    if tid != 'R10_RULES':
        inputs += [{'path': 'revision-r10/guidance/chapter-contracts.md'}]
    if tid in {'R10_REVIEW', 'R10_DELIVERY'}:
        inputs += [{'path': 'manuscript.tex'}, {'path': 'manuscript.pdf'},
                   {'path': 'revision-r10/integration/chapter-handoff.md'}]
    runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role, 'question': question,
        'purpose': 'Allocate explanatory depth across complementary chapter responsibilities; correct actual duplication without changing the science or adding rigid templates.',
        'claim_ids': [], 'inputs': inputs, 'outputs': ['revision-r10/' + folder],
        'writes': ['revision-r10/' + folder], 'depends_on': deps,
        'acceptance': ['Located original-paper comparison; generic criteria with no case-specific physics; actual complementary prose and reciprocal check; preserved definitions, numbers, citations and scientific limits; complete bounded return.'],
        'budget': {'max_attempts': 2, 'max_no_progress': 2}})
if a.action == 'accept':
    if not a.reason or not a.paths:
        p.error('accept needs reason and paths')
    if runtime.context(PAPER)['tasks'][a.task]['status'] != 'accepted':
        runtime.record(PAPER, a.task, {'attempt': 1, 'changed_understanding': True,
            'reason': a.reason, 'evidence': [{'path': path, 'level': 'observation',
                'kind': 'observation', 'claim_ids': [], 'summary': a.reason} for path in a.paths], 'blockers': []})
        runtime.decide(PAPER, a.task, {'action': 'accept', 'reason': a.reason})
audit = runtime.audit(PAPER)
print(json.dumps({'protocol_ok': audit['protocol_ok'], 'blocking': [x for x in audit['risks'] if x['blocking']]}, ensure_ascii=True))
