"""Render the actual LaTeX PDF for page-level visual inspection (PyMuPDF/Pillow)."""
from pathlib import Path
import argparse
import json
import fitz
from PIL import Image, ImageOps, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--pdf', type=Path, default=ROOT/'manuscript.pdf')
parser.add_argument('--output', type=Path, default=ROOT/'qa')
args = parser.parse_args()
QA = args.output.resolve()
QA.mkdir(parents=True,exist_ok=True)
doc = fitz.open(args.pdf)
# Remove only stale numbered renders from this owned QA directory.
for path in QA.glob('page-*.png'):
    if path.stem[5:].isdigit() and int(path.stem[5:]) > len(doc):
        path.unlink()
for path in QA.glob('contact-sheet-*.png'):
    if path.stem[14:].isdigit() and int(path.stem[14:]) > (len(doc)+8)//9:
        path.unlink()
pages = []
for number, page in enumerate(doc, 1):
    pix = page.get_pixmap(dpi=110)
    path = QA / f'page-{number:02d}.png'
    pix.save(path)
    pages.append(path)
for offset in range(0, len(pages), 9):
    sheet = Image.new('RGB', (1200, 1740), '#bfc8d0')
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(pages[offset:offset+9]):
        im = Image.open(path).convert('RGB')
        im.thumbnail((390, 550))
        x, y = (i % 3) * 400, (i // 3) * 580
        sheet.paste(im, (x + (400-im.width)//2, y+23))
        draw.text((x+10,y+6), f'Page {offset+i+1}', fill='black')
    sheet.save(QA / f'contact-sheet-{offset//9+1}.png')
metrics = {'pages': len(doc), 'bytes': args.pdf.stat().st_size,
           'pages_with_images': [i+1 for i,p in enumerate(doc) if p.get_images()],
           'characters_per_page': [len(p.get_text()) for p in doc]}
(QA/'pdf-inspection.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
print(json.dumps(metrics,indent=2))
