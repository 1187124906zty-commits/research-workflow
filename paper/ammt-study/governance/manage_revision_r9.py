"""Coordinate the reference-led argument and expression revision of the same paper."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / 'revision-r9'
TASKS = {
    'R9_RULES': ('writer', 'guidance/', [], 'Which concrete reference paragraph and sentence moves are still missing from the reusable writing criteria, and how can they improve reasoning without transferring the reference science?'),
    'R9_BODY_PREP': ('writer', 'body/', [], 'Where do current methods and factor analyses fail to express adoption rationale, inherited objects, or a supported change in understanding, compared with the actual reference?'),
    'R9_BODY': ('writer', 'body/', ['R9_RULES', 'R9_BODY_PREP'], 'Do revised methods and results/discussion use the accepted guidance to connect scientific rationale, controlled comparisons and progressively deeper bounded interpretation?'),
    'R9_FRAMING': ('writer', 'framing/', ['R9_RULES'], 'Do title, abstract, Introduction and conclusions state a source-supported tension, a consequential route and a grouped answer with natural object continuity?'),
    'R9_INTEGRATION': ('coordinator', 'integration/', ['R9_BODY', 'R9_FRAMING'], 'Does the same-file complete draft apply the reference-informed rules across section boundaries and preserve all evidence identities?'),
    'R9_REVIEW': ('reviewer', 'review/', ['R9_INTEGRATION'], 'Does the actual revision improve research reasoning and sentence/paragraph continuity rather than merely restyling displays, without inventing mechanism or novelty?'),
    'R9_COMPRESSION': ('writer', 'body/', ['R9_INTEGRATION'], 'Does every paragraph of each extended result analysis add a necessary evidence-supported distinction, interpretation or consequential qualification, and can redundant prose be merged without losing the quantitative argument?'),
    'R9_RECHECK': ('reviewer', 'review/', ['R9_REVIEW', 'R9_COMPRESSION'], 'Does the actual final compressed source/PDF retain supported results and reasoning while closing the located independent-review and paragraph-density issues?'),
    'R9_DELIVERY': ('coordinator', 'delivery/', ['R9_RECHECK'], 'Are the final same-source PDF and editable sources, applied reusable criteria, reference learning and local review materials consistent?'),
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
    runtime.plan(PAPER, {'stage': 'paper_revision', 'reason': 'User clarifies that the main learning is research rationale, scientific tension, factor-analysis depth and expression; revise reusable guidance and actual manuscript accordingly.', 'next_decision': 'Read actual exemplar and current sentences; accept concrete topic-neutral guidance before writing candidates, integrate and independently review the same paper.'})
    ids = ['R9_RULES', 'R9_BODY_PREP']
elif a.action == 'dispatch':
    ids = [a.task]
else:
    ids = []
for tid in ids:
    if tid in runtime.context(PAPER)['tasks']:
        continue
    role, folder, deps, question = TASKS[tid]
    (REV / folder).mkdir(parents=True, exist_ok=True)
    inputs = [{'path': 'revision-r9/manuscript-input.tex'},
              {'path': 'revision-r8/reference/supplied-xiong2022.pdf'},
              {'path': 'revision-r6/sources/support-ledger.json'},
              {'path': 'revision-r6/simulation-supplement/observations-matched.json'}]
    if tid in {'R9_BODY', 'R9_FRAMING', 'R9_REVIEW', 'R9_COMPRESSION', 'R9_RECHECK'}:
        inputs += [{'path': 'revision-r9/guidance/section-specific-guidance.md'}]
    if tid in {'R9_REVIEW', 'R9_COMPRESSION', 'R9_RECHECK'}:
        inputs += [{'path': 'manuscript.tex'}, {'path': 'manuscript.pdf'},
                   {'path': 'revision-r9/integration/applied-guidance.md'}]
    if tid == 'R9_RECHECK':
        inputs += [{'path': 'revision-r9/integration/final-applied-guidance.md'}]
    if tid == 'R9_DELIVERY':
        inputs += [{'path': 'manuscript.tex'}, {'path': 'manuscript.pdf'},
                   {'path': 'submission-source.zip'},
                   {'path': 'revision-r9/integration/final-applied-guidance.md'},
                   {'path': 'revision-r9/review/review-response.md'}]
    runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role, 'question': question,
        'purpose': 'Improve real research reasoning and expression using actual reference reading and evidence-bound, reusable criteria.',
        'claim_ids': [], 'inputs': inputs, 'outputs': ['revision-r9/' + folder],
        'writes': ['revision-r9/' + folder], 'depends_on': deps,
        'acceptance': ['Actual passage learning and source comparison; useful generic criteria; improved consequential prose; preserved science, numbers, citations and limits; best complete bounded return.'],
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
