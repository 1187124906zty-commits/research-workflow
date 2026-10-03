"""Persist accepted R9 delivery without rewriting earlier version dispositions."""
from pathlib import Path
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / 'revision-r9'
context = runtime.context(PAPER)
required = ['R9_RULES', 'R9_BODY_PREP', 'R9_BODY', 'R9_FRAMING',
            'R9_INTEGRATION', 'R9_REVIEW', 'R9_COMPRESSION', 'R9_RECHECK', 'R9_DELIVERY']
if any(context['tasks'].get(key, {}).get('status') != 'accepted' for key in required):
    raise RuntimeError('Required requester dispositions remain open')
metrics = json.loads((REV / 'integration/reading-metrics.json').read_text(encoding='utf-8'))
package = json.loads((REV / 'delivery/human-package-check.json').read_text(encoding='utf-8'))
if package['unresolved_delivery_defects']:
    raise RuntimeError('Current local delivery defects remain')
facts = ['Historical R8 delivery: ' + item if item.startswith('Current R8 same-file') else item
         for item in context['research']['facts']]
facts.extend([
    f"Current R9 same-file manuscript: {metrics['pages']} pages, {metrics['abstract_words']}-word abstract, {metrics['figures']} vector figures, {metrics['tables']} tables and {metrics['cited_identities']} actual citation identities.",
    'R9 applies original-article and institutional writing-source learning to research rationale, narrowing scientific tension, condition-specific factor interpretation and sentence/paragraph continuity. The article contributes editorial moves, not current-study science or AM journal rules.',
    'Generic MAF guidance remains subject-neutral; exemplar decisions are task notes, and intervention comparisons remain conditional alongside observational and latent-factor evidence roles. Actual reviewer follow-up closed both low guidance findings.',
    'The body and framing writers loaded relevant current checkout MAF scopes and returned complete bounded candidates. Desktop agents performed manuscript writing and independent review; the previous 98-test suite and real two-cycle offline MAF demo, plus 15 post-repair writing tests, retain their actual execution identity. No remote native MAF manuscript batch is claimed.',
    'R9 retains all prior mathematical/field identities and four R8 displays. It adds no PDE or experiment. The local conductivity and storage diagnostic values contextualize the tested changes rather than establish unique transport cause or intrinsic factor rankings.',
    'The final independent review, source read scopes and requester interpretation are retained in revision-r9/review. The final source archive rebuilt independently with matching used figures and page texts, and the local reading bundle matches current artifacts and bibliography order.',
    'Current R9 manuscript, official guide and actual reading materials stay local for human evaluation. Human approval, journal acceptance and physical thermal-history validation have not been established. Native compiler still reported its platform-directory error; existing Windows TeX Live compiled the same source and the original editor remains open.',
])
runtime.plan(PAPER, {
    'stage': 'human_review', 'facts': facts,
    'reason': 'Reference-informed generic criteria, complete same-source revision, actual independent review and local delivery checks completed and accepted.',
    'next_decision': 'Await human evaluation of human-review-r9 and the existing manuscript. Preserve reading/evidence boundaries; no automatic rerun, publishing or submission.',
})
audit = runtime.audit(PAPER)
(REV / 'delivery/final-researchflow-audit.json').write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'protocol_ok': audit['protocol_ok'],
                  'blocking': [risk for risk in audit['risks'] if risk['blocking']],
                  'r9_tasks': {key: runtime.context(PAPER)['tasks'][key]['status'] for key in required}},
                 ensure_ascii=True))
