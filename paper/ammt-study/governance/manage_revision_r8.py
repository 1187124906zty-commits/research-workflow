"""Coordinate reference-led R8 revision with actual visual comparisons."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER/'revision-r8'
TASKS={
 'R8_REFERENCE':('literature','reference-analysis/',[], 'What does the supplied Xiong et al. article actually do in each abstract, Introduction, model and results unit, and what transferable reader/visual/linguistic decisions differ from our manuscript?'),
 'R8_VISUAL':('writer','visual/',[], 'Which direct views and paired comparisons in the retained data make the core geometry and rear-position/time findings visible without implying new experimental/physical evidence?'),
 'R8_FRAMING':('writer','framing/',['R8_REFERENCE'], 'How should the actual supplied reference diagnosis guide a concise problem, route, result and use narrative in our abstract/Introduction/conclusion without transferring its mechanism or innovation claims?'),
 'R8_INTEGRATION':('coordinator','integration/',['R8_REFERENCE','R8_VISUAL','R8_FRAMING'], 'Does the same-file revised paper lead with intuitive evidence and locally interpret direct comparisons while retaining equations, data identity and limits?'),
 'R8_REVIEW':('reviewer','review/',['R8_INTEGRATION'], 'Does the actual new paper and its displays close the reference-led weaknesses and match raw evidence, without visual or scientific exaggeration?'),
 'R8_RECHECK':('reviewer','review/',['R8_REVIEW'], 'Do the repaired source and actual PDF close the located obsolete figure-label sentence and orphan-line defect without changing scientific outputs or claims?'),
 'R8_DELIVERY':('coordinator','delivery/',['R8_RECHECK'], 'Are the current PDF/source, reference dissection, actual data/figure sources and local human-review package complete and internally consistent?'),
}
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('action',choices=['start','dispatch','accept','audit'])
p.add_argument('task',nargs='?')
p.add_argument('--reason')
p.add_argument('--paths',nargs='*')
args=p.parse_args()
if args.action=='start':
 REV.mkdir(exist_ok=True)
 frozen=REV/'manuscript-input.tex'
 if not frozen.exists():frozen.write_bytes((PAPER/'manuscript.tex').read_bytes())
 runtime.plan(PAPER,{'stage':'paper_revision','reason':'User supplies a complete related paper and asks for section-by-section diagnosis before optimization, emphasizing direct visible comparisons and clearer language.', 'next_decision':'Read actual reference text/figures; derive a bounded reader/visual redesign; integrate retained data and review the revised same-file paper.'})
 ids=['R8_REFERENCE','R8_VISUAL']
elif args.action=='dispatch':ids=[args.task]
else:ids=[]
for tid in ids:
 role,folder,deps,question=TASKS[tid]
 if tid in runtime.context(PAPER)['tasks']:continue
 (REV/folder).mkdir(parents=True,exist_ok=True)
 inputs=[{'path':'revision-r8/manuscript-input.tex'}, {'path':'revision-r6/sources/support-ledger.json'},
         {'path':'revision-r6/simulation-supplement/observations-matched.json'},
         {'path':'C:/Users/Administrator/Downloads/main (1).pdf'}]
 if tid in {'R8_REVIEW','R8_RECHECK'}:inputs += [{'path':'manuscript.tex'},{'path':'manuscript.pdf'}]
 runtime.task(PAPER,{'id':tid,'role':role,'owner':role,'question':question,
  'purpose':'Reference-led scientific communication revision using authentic retained evidence.',
  'claim_ids':[],'inputs':inputs,'outputs':['revision-r8/'+folder],'writes':['revision-r8/'+folder],
  'depends_on':deps,'acceptance':['Actual original/text/render use; actionable transferable comparison; no invented evidence; complete bounded output and accurate scientific/visual identities.'],
  'budget':{'max_attempts':2,'max_no_progress':2}})
if args.action=='accept':
 if not args.reason or not args.paths:p.error('accept needs reason and paths')
 if runtime.context(PAPER)['tasks'][args.task]['status']!='accepted':
  runtime.record(PAPER,args.task,{'attempt':1,'changed_understanding':True,'reason':args.reason,
    'evidence':[{'path':name,'level':'observation','kind':'observation','claim_ids':[], 'summary':args.reason} for name in args.paths],'blockers':[]})
  runtime.decide(PAPER,args.task,{'action':'accept','reason':args.reason})
audit=runtime.audit(PAPER)
print(json.dumps({'protocol_ok':audit['protocol_ok'],'blocking':[r for r in audit['risks'] if r['blocking']]},ensure_ascii=True))
