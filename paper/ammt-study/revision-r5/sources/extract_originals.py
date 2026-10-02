from pathlib import Path
import json
import fitz

ROOT = Path(__file__).resolve().parents[2]
DEST = Path(__file__).resolve().parent
FILES = {
    'kollmannsberger2019': ROOT / 'revision-r3/citations/pdfs/kollmannsberger2019.pdf',
    'vanelsen2007': ROOT / 'revision-r3/citations/pdfs/vanelsen2007.pdf',
    'specialmetals625': ROOT / 'revision-r3/citations/pdfs/specialmetals625.pdf',
    'dynamic2024': ROOT / 'revision-r2/literature/pdfs/dynamic2024.pdf',
    'myers2023': ROOT / 'literature/myers2023-published.pdf',
}
for key, path in FILES.items():
    doc = fitz.open(path)
    pages = [{'pdf_page': n + 1, 'text': page.get_text()} for n, page in enumerate(doc)]
    (DEST / f'{key}-pages.json').write_text(json.dumps(pages, indent=2, ensure_ascii=False), encoding='utf-8')
    print(key, len(pages), path)
