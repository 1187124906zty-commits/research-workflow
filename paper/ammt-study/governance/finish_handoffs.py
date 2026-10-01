"""Record actual literature and MAF returns, plus root's artifact-level integration."""
from pathlib import Path
import json
import sys
REPO = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parents[1]
MAF = REPO.parent/'research-assistant-maf'
sys.path.insert(0,str(REPO/'src'))
from researchflow import runtime

def complete(tid, paths, answer):
    entry=runtime.context(ROOT,tid)
    if entry['status']=='active':
        runtime.record(ROOT,tid,{'attempt':1,'changed_understanding':True,'reason':answer,
            'evidence':[{'path':p,'level':'observation','kind':'observation','claim_ids':[], 'summary':answer} for p in paths],
            'blockers':[],'contribution':{'answer':answer,'effect_on_project':'Concrete manuscript input accepted within its stated scope',
                'uncertainties':['Physical predictive validation and current journal-specific submission checklist remain unresolved'],
                'next_options':['Assemble and inspect actual draft'],'cost_note':'No PDE reruns'}})
    if runtime.context(ROOT,tid)['status']=='awaiting_decision':
        runtime.decide(ROOT,tid,{'action':'accept','reason':answer+' Delivery acceptance does not promote physical validation.'})

def main():
    complete('T_JOURNAL',['literature/journal-dossier.md','literature/exemplar-notes.md','literature/bibliography.bib'],
             'Read journal dossier and six distinct originals via specialists; chose AM-oriented full research paper, with current venue-guide access gap explicit.')
    summary=MAF/'examples/ammt-manuscript/run-summary.json'
    data=json.loads(summary.read_text(encoding='utf-8'))
    assert data['status']=='complete', 'Do not falsely close an incomplete MAF session'
    tid='T_MAF_INPUTS'
    if tid not in runtime.context(ROOT)['tasks']:
        runtime.task(ROOT,{'id':tid,'role':'mechanism_and_writer','question':'Can bounded MAF returns improve the interpretation and manuscript without new simulations?',
            'purpose':'Integrate actual native-graph mechanism, writing and separate review/disposition results', 'claim_ids':[],
            'inputs':[{'path':str(summary)}], 'outputs':['governance/maf-integration.md'],
            'acceptance':['Actual model calls and returns exist; root reads and records substantive use and limitations'],
            'budget':{'max_attempts':1,'max_no_progress':1}, 'depends_on':['T_EVIDENCE','T_JOURNAL']})
    complete(tid,['governance/maf-integration.md',str(summary)],
             'Actual MAF/Codex session delivered mechanism and results/discussion inputs. Root integrated source/operator/data-role limits, B/C-only speed attribution, and bulk/recovery distinction; full paper independently reviewed separately.')
    print(json.dumps(runtime.audit(ROOT),indent=2))

if __name__=='__main__':main()
