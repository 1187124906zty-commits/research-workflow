"""Coordinate the editable Word delivery without revising accepted science."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
TASKS = {
    'R11_WORD_BUILD': ('writer', 'word/build/', [], 'Can the accepted structured manuscript be supplied as editable Word with preserved mathematics, tables, figures and reference identities, using its PDF as visual reference?'),
    'R11_WORD_REVIEW': ('reviewer', 'word/review/', ['R11_WORD_BUILD'], 'What actual scientific content, editability and visual differences exist between the accepted source/PDF and the converted Word document?'),
    'R11_WORD_DELIVERY': ('coordinator', 'word/delivery/', ['R11_WORD_REVIEW'], 'Does the final editable Word match the reviewed conversion, with material differences and capability limits accurately delivered?'),
}
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('action', choices=['dispatch', 'accept', 'audit'])
p.add_argument('task', nargs='?')
p.add_argument('--reason')
p.add_argument('--paths', nargs='*')
a = p.parse_args()
if a.action == 'dispatch':
    if a.task not in TASKS:
        p.error('Unknown Word task')
    if a.task not in runtime.context(PAPER)['tasks']:
        role, output, deps, question = TASKS[a.task]
        (PAPER/'revision-r11'/output).mkdir(parents=True,exist_ok=True)
        inputs = [{'path':name} for name in ('manuscript.tex','manuscript.pdf','manuscript.aux','manuscript.bbl')]
        if a.task != 'R11_WORD_BUILD':
            inputs += [{'path':'revision-r11/word/build/manuscript-editable.docx'}]
        runtime.task(PAPER, {'id':a.task,'role':role,'owner':role,'question':question,
            'purpose':'Deliver editable format and fidelity assessment; scientific content remains the accepted R11 revision.',
            'claim_ids':[],'inputs':inputs,'outputs':['revision-r11/'+output],
            'writes':['revision-r11/'+output],'depends_on':deps,
            'acceptance':['Native editable prose/tables/equations where supported; full accepted scientific content and current references; actual render and independent content/layout comparison; honest pagination/representation differences.'],
            'budget':{'max_attempts':2,'max_no_progress':2}})
elif a.action == 'accept':
    if not a.reason or not a.paths:
        p.error('accept needs reason and paths')
    if runtime.context(PAPER)['tasks'][a.task]['status'] != 'accepted':
        runtime.record(PAPER,a.task,{'attempt':1,'changed_understanding':False,'reason':a.reason,
            'evidence':[{'path':path,'level':'observation','kind':'observation','claim_ids':[],'summary':a.reason} for path in a.paths],
            'blockers':[]})
        runtime.decide(PAPER,a.task,{'action':'accept','reason':a.reason})
audit = runtime.audit(PAPER)
print(json.dumps({'protocol_ok':audit['protocol_ok'],'blocking':[r for r in audit['risks'] if r['blocking']]}))
