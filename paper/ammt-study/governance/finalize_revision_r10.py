"""Persist the verified same-manuscript chapter revision and current delivery."""
from pathlib import Path
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / 'revision-r10'
context = runtime.context(PAPER)
required = ['R10_RULES', 'R10_INTRO', 'R10_METHODS', 'R10_INTEGRATION', 'R10_REVIEW', 'R10_DELIVERY']
if any(context['tasks'].get(key, {}).get('status') != 'accepted' for key in required):
    raise RuntimeError('Required requester dispositions remain open')
metrics = json.loads((REV / 'integration/reading-metrics.json').read_text(encoding='utf-8'))
package = json.loads((REV / 'delivery/human-package-check.json').read_text(encoding='utf-8'))
if package['unresolved_delivery_defects']:
    raise RuntimeError('Current local delivery defects remain')
facts = ['Historical R9 delivery: ' + item if item.startswith('Current R9 same-file') else item
         for item in context['research']['facts']]
facts.extend([
    f"Current R10 same-file manuscript: {metrics['pages']} pages, {metrics['abstract_words']}-word abstract, {metrics['figures']} vector figures, {metrics['tables']} tables and {metrics['cited_identities']} actual citation identities.",
    'R10 coordinates complementary explanatory depth across Introduction, Methods and Conclusions using located original-paper boundary comparisons. Generic rules assign a main explanatory home, assess new information on recurrence and reciprocally read actual adjoining passages; no case-specific physics or rigid no-repetition rule enters shared skills.',
    'R10 changes only the Introduction final paragraph, Methods entry and adjoining Experimental data opening. Actual post-first-table scientific source, Results, Conclusions, formulas, figures, numbers and scientific limits are unchanged. Length and transverse target references retain their separate identities.',
    'Current checkout MAF writer scopes were genuinely loaded for Introduction and Methods; the full-manuscript reviewer scope was loaded and the handoff method separately read. Desktop agents perform actual manuscript writing/review. The standard 98 tests, skill validation and real two-cycle native offline demo passed; no remote native MAF manuscript execution or measured research-efficiency improvement is claimed.',
    'The independent reviewer read actual source and rendered pages before producer interface reports where practical, retained disclosed R9 exposure, and accepted the complementary boundary after reading the current corrected handoff subsection name. That record changed after review dispatch; the old binding remains historical and does not silently become current scientific support.',
    'Current R10 PDF, editable sources, official 30-page guide, actual reference materials and R6 accepted supplement are held in human-review-r10 for human evaluation. Independent source archive rebuild matched current 20-page text and four figures. Native compiler reported its known platform-directory failure; existing Windows TeX Live compiled the same source successfully, original editor remains open.',
])
runtime.plan(PAPER, {'stage': 'human_review', 'facts': facts,
    'reason': 'Complementary chapter criteria, same-source revision, actual reciprocal handoff and independent review, and current local package checks completed.',
    'next_decision': 'Await human reading of the current manuscript and human-review-r10. Preserve unresolved scientific limits and human approval status; no automatic rerun, publishing or submission.'})
audit = runtime.audit(PAPER)
(REV / 'delivery/final-researchflow-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'protocol_ok': audit['protocol_ok'], 'blocking': [risk for risk in audit['risks'] if risk['blocking']],
                  'r10_tasks': {key: runtime.context(PAPER)['tasks'][key]['status'] for key in required}}, ensure_ascii=True))
