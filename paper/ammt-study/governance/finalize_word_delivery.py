"""Persist the reviewed Word delivery without reopening accepted science."""
from pathlib import Path
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
WORD = PAPER / 'revision-r11/word'
context = runtime.context(PAPER)
required = ('R11_WORD_BUILD', 'R11_WORD_REVIEW', 'R11_WORD_DELIVERY')
if any(context['tasks'].get(task, {}).get('status') != 'accepted' for task in required):
    raise RuntimeError('Word production, independent review and delivery must be accepted')
manifest = json.loads((PAPER / 'human-review-r11/manifest.json').read_text(encoding='utf-8'))
package = json.loads((WORD / 'delivery/human-package-check.json').read_text(encoding='utf-8'))
render = json.loads((WORD / 'build/word-render-report.json').read_text(encoding='utf-8-sig'))
if not manifest.get('editable_word_available') or manifest.get('editable_word_review_status') != 'accepted':
    raise RuntimeError('Current local reading package lacks reviewed Word')
if package['unresolved_delivery_defects']:
    raise RuntimeError('Local reading package has unresolved defects')
if (PAPER / 'manuscript.docx').read_bytes() != (WORD / 'build/manuscript-editable.docx').read_bytes():
    raise RuntimeError('Canonical Word differs from the reviewed candidate')
if not (WORD / 'delivery/format-report.md').is_file():
    raise RuntimeError('Material conversion differences must be recorded')
facts = context['research']['facts'][:]
word_facts = [
    f"Current R11 additional editable Word: {render['pages']} pages under Microsoft Word, with native prose, nine tables, thirteen numbered display equations and four original SVG figures with PNG fallback. Accepted scientific text, values and reference identities are preserved within the reported conversion review scope.",
    'Editable Word uses Letter dimensions, Times New Roman prose and native OMML math; the accepted PDF remains twenty pages with Latin Modern typography. Citations and cross-reference numbers are static. Actual Word rendering and content/layout review are recorded; exact pagination and compatibility with untested engines are not certified.',
    'Generic editable-document guidance is confined to the new MAF repository. Desktop conversion and independent review read actual current-checkout MAF guidance; the deterministic native MAF demo verifies software flow, not a native remote manuscript conversion or measured efficiency.',
    'The local human-review-r11 directory and archive now also include reviewed manuscript.docx and its conversion report. Human review, author approval and external publication remain pending; accepted LaTeX/PDF and scientific evidence were not revised for this conversion.',
]
for fact in word_facts:
    if fact not in facts:
        facts.append(fact)
runtime.plan(PAPER, {'stage': 'human_review', 'facts': facts,
    'reason': 'Reviewed editable representation and current local package have accepted requester dispositions; the scientific R11 revision remains unchanged.',
    'next_decision': 'Await human reading of the accepted R11 PDF, editable Word and human-review-r11. No automatic simulation, publishing or submission.'})
audit = runtime.audit(PAPER)
(WORD / 'delivery/final-researchflow-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'protocol_ok': audit['protocol_ok'], 'blocking': [risk for risk in audit['risks'] if risk['blocking']],
    'word_tasks': {task: runtime.context(PAPER)['tasks'][task]['status'] for task in required}}, ensure_ascii=True))
