"""Coordinate functional method prose and economical scientific references."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / 'revision-r11'
TASKS = {
    'R11_RULES': ('writer', 'guidance/', [], 'What do actual original paragraphs and current guidance establish about functional Methods prose, placed limitations, stable referents and readable topic openings?'),
    'R11_PREP': ('writer', 'prose/', [], 'Which actual passages overload readers with repeated qualifier chains or defensive design summaries, and which identities must remain distinct?'),
    'R11_PROSE': ('writer', 'prose/', ['R11_RULES', 'R11_PREP'], 'Does the candidate positively explain the actual study capability and use defined concise referents without obscuring controls, scientific limitations or evidence status?'),
    'R11_INTEGRATION': ('coordinator', 'integration/', ['R11_PROSE'], 'Does the same-source integrated candidate preserve the study while making Methods, topic openings and data identities easier to read?'),
    'R11_REVIEW': ('reviewer', 'review/', ['R11_INTEGRATION'], 'Do actual prose, rendered pages and current generic criteria improve referent economy and section purpose without overstating generality or novelty?'),
    'R11_REVIEW_CURRENT': ('reviewer', 'review/', ['R11_REVIEW'], 'Does the final PDF rebuilt for synchronized reproduction notes have the same actual page content as the independently reviewed manuscript, and does the review apply to this bound current version?'),
    'R11_DELIVERY': ('coordinator', 'delivery/', ['R11_REVIEW', 'R11_REVIEW_CURRENT'], 'Are the accepted current manuscript and editable local author-guide/reference package consistent and rebuildable?'),
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
    runtime.plan(PAPER, {'stage': 'paper_revision', 'reason': 'User requests constructive method explanation, appropriate limitation placement, concise established referents and simple connected topic openings instead of accumulated noun qualifiers.', 'next_decision': 'Read relevant originals and diagnose current prose, apply bounded generic criteria, revise the same manuscript and independently assess scientific identity and readability.'})
    ids = ['R11_RULES', 'R11_PREP']
elif a.action == 'dispatch':
    ids = [a.task]
else:
    ids = []
for tid in ids:
    if tid in runtime.context(PAPER)['tasks']:
        continue
    role, folder, deps, question = TASKS[tid]
    (REV / folder).mkdir(parents=True, exist_ok=True)
    inputs = [{'path': 'revision-r11/manuscript-input.tex'},
              {'path': 'revision-r8/reference/supplied-xiong2022.pdf'},
              {'path': 'revision-r10/sources/support-ledger.json'}]
    if tid not in {'R11_RULES', 'R11_PREP'}:
        inputs += [{'path': 'revision-r11/guidance/applied-criteria.md'}]
    if tid in {'R11_REVIEW', 'R11_REVIEW_CURRENT', 'R11_DELIVERY'}:
        inputs += [{'path': 'manuscript.tex'}, {'path': 'manuscript.pdf'},
                   {'path': 'revision-r11/integration/terminology-and-scope.md'}]
    runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role, 'question': question,
        'purpose': 'Improve research prose and reusable writing decisions through actual original-source reading; distinguish operational definitions from interpretive limitations and naming from novelty.',
        'claim_ids': [], 'inputs': inputs, 'outputs': ['revision-r11/' + folder],
        'writes': ['revision-r11/' + folder], 'depends_on': deps,
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
