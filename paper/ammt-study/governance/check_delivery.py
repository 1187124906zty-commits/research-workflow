"""Check this concrete manuscript package and public introduction links."""
from pathlib import Path
import argparse
import json
import re
import zipfile
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
MAF=REPO.parent/'research-assistant-maf'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=ROOT/'governance/delivery-check.json')
parser.add_argument('--pdf',type=Path,default=ROOT/'manuscript.pdf')
parser.add_argument('--log',type=Path,default=ROOT/'manuscript.log')
args=parser.parse_args()
issues=[]
source=(ROOT/'manuscript.tex').read_text(encoding='utf-8')
bibliography=re.search(r'\\bibliography\{([^}]+)\}',source).group(1)
bib=(ROOT/(bibliography+'.bib')).read_text(encoding='utf-8')
keys=set(re.findall(r'@\w+\s*\{\s*([^,]+)',bib))
cited=set(k.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',source) for k in group.split(','))
if cited-keys:issues.append('Unresolved BibTeX identities: '+str(cited-keys))
for figure in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source):
    if not (ROOT/figure).is_file():issues.append('Missing figure '+figure)
doc=pymupdf.open(args.pdf)
text='\n'.join(page.get_text() for page in doc)
if '\ufffd' in text:issues.append('Replacement glyph in PDF')
if re.search(r'\[\s*\?\s*\]',text):issues.append('Unresolved citation in PDF')
log=args.log.read_text(encoding='utf-8',errors='replace')
if re.search('Overfull|Missing character|undefined',log):issues.append('Unresolved TeX diagnostics')
with zipfile.ZipFile(ROOT/'submission-source.zip') as archive:
    if any('/' in name for name in archive.namelist()):issues.append('Source archive not flat')
    archive_tex=archive.read('manuscript.tex').decode('utf-8')
    for figure in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',archive_tex):
        if figure not in archive.namelist():issues.append('Archive figure unresolved '+figure)
    if 'bibliography.bib' not in archive.namelist():issues.append('Archive bibliography missing')
# Check new/updated curated documents; raw provenance notes can contain local original locators.
documents=[REPO/'README.md',REPO/'CONTRIBUTING.md',REPO/'docs/COMMUNITY.md',ROOT/'README.md',
           ROOT/'revision-r2/README.md',ROOT/'revision-r2/review/review-response.md',
           MAF/'README.md',MAF/'CONTRIBUTING.md',MAF/'docs/COMMUNITY.md',
           MAF/'docs/manuscript-collaboration.zh.md',MAF/'docs/abstract-introduction-positioning.zh.md',
           MAF/'examples/ammt-manuscript/README.md',MAF/'examples/ammt-deep-revision/README.md',
           REPO/'docs/manuscript-audit.md',ROOT/'revision-r3/README.md',
           ROOT/'revision-r3/review/review-response.md',MAF/'docs/manuscript-audit.zh.md']
links=0
for path in documents:
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        if re.match(r'^(?:https?://|mailto:|#)',target):continue
        links+=1
        name=target.split('#')[0].strip('<>')
        if not (path.parent/name).exists():issues.append(f'Broken local link {path.name}: {target}')
summary={'latex_pdf_pages':len(doc),'pdf_bytes':args.pdf.stat().st_size,
         'checked_pdf_input':str(args.pdf.resolve().relative_to(ROOT)),
         'local_canonical_pdf_matches_checked':(ROOT/'manuscript.pdf').read_bytes()==args.pdf.read_bytes(),
         'resolved_cited_identities':len(cited),'bibliography_candidates':len(keys),
         'scientific_figures':len(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source)),
         'checked_document_links':links,'unresolved_delivery_defects':issues,
         'limits':['Current AM-specific author-guide terms unverified','Authorship/human final verification pending',
                   'Full PDE replay requires original case fields and environment','Scientific novelty/acceptance not certified']}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=True,indent=2))
if issues:raise SystemExit(1)
