"""Persist the actual accepted R8 delivery and keep earlier version history."""
from pathlib import Path
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER/'revision-r8'
context = runtime.context(PAPER)
required = ['R8_REFERENCE','R8_VISUAL','R8_FRAMING','R8_INTEGRATION',
            'R8_REVIEW','R8_RECHECK','R8_DELIVERY']
if any(context['tasks'].get(key,{}).get('status')!='accepted' for key in required):
    raise RuntimeError('Required requester dispositions remain open')
metrics = json.loads((REV/'integration/reading-metrics.json').read_text(encoding='utf-8'))
package = json.loads((REV/'delivery/human-package-check.json').read_text(encoding='utf-8'))
if package['unresolved_delivery_defects']:
    raise RuntimeError('Current local delivery defects remain')
facts = ['Historical R7 delivery: '+item if item.startswith(('Current R7 same-file','Current flat source package')) else item
         for item in context['research']['facts']]
facts += [
    f"Current R8 same-file manuscript: {metrics['pages']} pages, {metrics['abstract_words']}-word abstract, {metrics['figures']} vector main figures, {metrics['tables']} tables and {metrics['cited_identities']} actual citation identities.",
    'R8 reference agent read the supplied Xiong 2022 main article all 17 pages and real figures; supplementary full text was not read. Its JMPT conventions and scientific evidence were separated from current AM journal requirements and conduction evidence.',
    'The user clarified the primary learning priority at delivery: source-supported scientific tension, the rationale connecting the research route to that tension, and factor analyses that progressively distinguish explanations. Actual article/Introduction mapping and the remaining depth difference are retained in delivery/argument-learning.md; intuitive displays remain a communication tool.',
    'R8 uses actual retained-field spatial comparisons before their metrics: calibrated geometry, crossed material-function rear boundaries, then spatial interval and stationary-material passage time. Detailed geometry and original factorial inventories remain in the appendix.',
    'Visual producer recovered 11 indexed fields and six original passage envelopes. Independent reviewer recoded field recovery for all 11 fields and the A/B/C passage observers, then checked actual manuscript and figure pages. These are postprocessing checks, not new PDE runs or physical validation.',
    'Actual current MAF checkout instructions were delivered by explicit writer/reviewer scopes; desktop agents executed the manuscript. 98 standard tests and the real two-cycle offline MAF demo passed. No additional remote native MAF manuscript batch was claimed.',
    'Independent R8 review located an obsolete figure-label sentence and a lone word after a float. The current source/PDF repair was separately bound to R8_RECHECK and accepted; earlier bindings retain their historical warning rather than being rewritten.',
    'The flat package independently rebuilt with current source/bibliography/all four used figures and matching page texts. The human-review-r8 local directory and ZIP match the actual files and rendered reference order.',
    'Current R8 manuscript, official guide, citation originals and user-supplied exemplar stay local awaiting human assessment. No GitHub push, external submission or duplication of simulation work. Original editor remains open; native compiler still has a platform-directory error and existing TeX Live compiled the same source.',
]
runtime.plan(PAPER, {'stage':'human_review','facts':facts,
    'next_decision':'Await human assessment of human-review-r8 and the same-file manuscript. Preserve scientific boundaries and source reading identities; do not automatically rerun simulation, publish or submit.',
    'reason':'Reference-led diagnosis, authentic direct figures, integrated manuscript, independent located repairs, source rebuild and current local bundle were actually completed and accepted.'})
audit = runtime.audit(PAPER)
(REV/'delivery/final-researchflow-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'protocol_ok':audit['protocol_ok'],'blocking':[x for x in audit['risks'] if x['blocking']],
                  'r8_tasks':{key:runtime.context(PAPER)['tasks'][key]['status'] for key in required}},ensure_ascii=True))
