"""Persist the accepted R7 local delivery without erasing prior evidence history."""
from pathlib import Path
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER/'revision-r7'
context = runtime.context(PAPER)
required = ['R7_GUIDANCE','R7_FRAMING','R7_BODY','R7_TRANSFER','R7_INTEGRATION',
            'R7_REVIEW','R7_RECHECK','R7_DELIVERY']
if any(context['tasks'].get(key,{}).get('status')!='accepted' for key in required):
    raise RuntimeError('Do not finalize before actual required requester dispositions')
metrics=json.loads((REV/'integration/reading-metrics.json').read_text(encoding='utf-8'))
facts=[]
for item in context['research']['facts']:
    if item.startswith(('Current R6 manuscript','Final manuscript reviewer','The current flat source package',
                        'ResearchFlow 38 tests','R6 manuscript and third-party')):
        item='Historical R6 delivery: '+item
    facts.append(item)
facts += [
    f"Current R7 same-file manuscript: {metrics['pages']} pages, {metrics['abstract_words']}-word abstract, five vector figures, nine tables and 41 cited identities; no new PDE/experiment or numerical-value changes.",
    'R7 uses source-backed closest predecessors and a numerical introduction route; model decisions and schemes precede parameter/case labels; two writers reciprocally checked design and framing.',
    'Current MAF loader directly supplies section-specific criteria by explicit scope. 98 standard tests passed; G1 resource repair passed 15 focused tests and 42 real Session request combinations. Final wheel installation and two-cycle demo passed outside checkout.',
    'A deliberately supplied standard-theory fixture exposed G1 novelty/gap overconstraint. The four-resource repair was actually reloaded and independently closed; this is bounded compatibility, not causal efficacy evidence.',
    'Independent manuscript reviewer checked all seven retained table values and 11 raw geometry/passage identities, nearest-source passages, all-page overviews and selected full pages. Located notation finding R7-N1 was repaired and current source/PDF rechecked without new simulation.',
    'Current flat source package independently rebuilt with matching 22 page texts and all five figures/bibliography/reproduction notes, no TeX diagnostics. Local human-review-r7 package matches current files and rendered reference order.',
    'R7 manuscript, original author guide and actual reference readings are delivered locally awaiting human assessment; no GitHub push or journal submission. Original editor remains open; native compiler has platform error, existing TeX Live built the same source.',
    'R7_REVIEW retains its superseded input binding after the notation repair; R7_RECHECK binds the actual repaired files. Historical stale warnings remain visible, with no current blocking audit defect.',
]
runtime.plan(PAPER, {'stage':'human_review', 'facts':facts,
    'next_decision':'Await the user’s assessment of human-review-r7 and same-file manuscript. Keep scientific limits and third-party originals local; no automatic rerun, push or submission.',
    'reason':'Actual current manuscript review/repair, guide G1 closure, source rebuild and human bundle checks are accepted. Preserve prior numerical scope and version history.'})
audit=runtime.audit(PAPER)
(REV/'delivery/final-researchflow-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'protocol_ok':audit['protocol_ok'], 'blocking':[risk for risk in audit['risks'] if risk['blocking']],
                  'r7_tasks':{key:runtime.context(PAPER)['tasks'][key]['status'] for key in required}},ensure_ascii=True))
