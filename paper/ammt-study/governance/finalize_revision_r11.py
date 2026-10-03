"""Persist the accepted same-source R11 prose revision and local delivery."""
from pathlib import Path
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
REV = PAPER / 'revision-r11'
context = runtime.context(PAPER)
required = ['R11_RULES', 'R11_PREP', 'R11_PROSE', 'R11_INTEGRATION', 'R11_REVIEW', 'R11_REVIEW_CURRENT', 'R11_DELIVERY']
if any(context['tasks'].get(key, {}).get('status') != 'accepted' for key in required):
    raise RuntimeError('Required requester dispositions remain open')
metrics = json.loads((REV / 'integration/reading-metrics.json').read_text(encoding='utf-8'))
package = json.loads((REV / 'delivery/human-package-check.json').read_text(encoding='utf-8'))
rebuild = json.loads((REV / 'delivery/package-rebuild-check.json').read_text(encoding='utf-8'))
if package['unresolved_delivery_defects'] or not rebuild['page_text_matches_compiled_pdf']:
    raise RuntimeError('Current local delivery defects remain')
facts = ['Historical R10 delivery: ' + item if item.startswith('Current R10 same-file') else item
         for item in context['research']['facts']]
facts.extend([
    f"Current R11 same-file manuscript: {metrics['pages']} pages, {metrics['abstract_words']}-word abstract, {metrics['figures']} vector figures, {metrics['tables']} tables and {metrics['cited_identities']} actual citation identities.",
    'R11 uses actual prior-paper passages and Duke/MIT original guidance to define concise stable referents, familiar topic entries and functional method explanations. Wider selection and validity consequences are developed with the affected findings; actual operational assumptions and scientific counterevidence remain explicit.',
    'R11 preserves the title, display equations, table values, appendix, used figure assets, numerical tokens and citation-key counts. It changes explanatory prose and captions, moves and condenses the property-selection discussion, and distinguishes condition codes, property codes and grid names. No new numerical or physical evidence is generated.',
    'R11 does not claim a new general extrapolation law, new enthalpy method or universal empirical validation. It positively explains consistent function use and a retained-fit crossed comparison; accepted large boundary displacement, unresolved small separation direction and physical-observation requirements retain their actual scope.',
    'Desktop writing and independent review use genuinely loaded current-checkout MAF guidance; the handoff guide is separately read. R11 standard 98 tests, skill validation and two-cycle deterministic native MAF offline demo passed. This is not remote native MAF manuscript execution or a measured research-efficiency study.',
    'A same-source rebuild after review dispatch changed the PDF binary revision. The old task binding remains historical; a current-PDF check rebinds and independently compares all page text before delivery. It does not silently replace the old input revision or repeat the scientific review.',
    'R11 local delivery includes the same manuscript, editable flat source archive, 30-page official guide, actually cited reference materials and accepted R6 supplement in human-review-r11. The source package rebuilt independently with matching page text and four figure assets. Human review and author approval remain pending; the revised manuscript and third-party originals were not pushed or submitted.',
])
runtime.plan(PAPER, {'stage': 'human_review', 'facts': facts,
    'reason': 'Actual prose revision, source preservation, independent reading and current local package verification have accepted requester dispositions.',
    'next_decision': 'Await human reading of the R11 manuscript and human-review-r11. Preserve unresolved scientific scope; no automatic simulation, publishing or submission.'})
audit = runtime.audit(PAPER)
(REV / 'delivery/final-researchflow-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'protocol_ok': audit['protocol_ok'], 'blocking': [risk for risk in audit['risks'] if risk['blocking']],
                  'r11_tasks': {key: runtime.context(PAPER)['tasks'][key]['status'] for key in required}}, ensure_ascii=True))
