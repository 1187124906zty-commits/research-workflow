"""Check this concrete manuscript package and public introduction links."""
from pathlib import Path
import json
import re
import zipfile
import pymupdf
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
MAF=REPO.parent/'research-assistant-maf'
issues=[]
source=(ROOT/'manuscript.tex').read_text(encoding='utf-8')
bibliography=re.search(r'\\bibliography\{([^}]+)\}',source).group(1)
bib=(ROOT/(bibliography+'.bib')).read_text(encoding='utf-8')
keys=set(re.findall(r'@\w+\s*\{\s*([^,]+)',bib))
cited=set(k.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',source) for k in group.split(','))
if cited-keys:issues.append('Unresolved BibTeX identities: '+str(cited-keys))
for figure in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source):
    if not (ROOT/figure).is_file():issues.append('Missing figure '+figure)
doc=pymupdf.open(ROOT/'manuscript.pdf')
text='\n'.join(page.get_text() for page in doc)
if '\ufffd' in text:issues.append('Replacement glyph in PDF')
if re.search(r'\[\s*\?\s*\]',text):issues.append('Unresolved citation in PDF')
log=(ROOT/'manuscript.log').read_text(encoding='utf-8',errors='replace')
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
           MAF/'examples/ammt-manuscript/README.md',MAF/'examples/ammt-deep-revision/README.md']
links=0
for path in documents:
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        if re.match(r'^(?:https?://|mailto:|#)',target):continue
        links+=1
        name=target.split('#')[0].strip('<>')
        if not (path.parent/name).exists():issues.append(f'Broken local link {path.name}: {target}')
summary={'latex_pdf_pages':len(doc),'pdf_bytes':(ROOT/'manuscript.pdf').stat().st_size,
         'verified_cited_sources':len(cited),'bibliography_candidates':len(keys),
         'scientific_figures':len(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source)),
         'checked_document_links':links,'unresolved_delivery_defects':issues,
         'limits':['Current AM-specific author-guide terms unverified','Authorship/human final verification pending',
                   'Full PDE replay requires original case fields and environment','Scientific novelty/acceptance not certified']}
(ROOT/'governance/delivery-check.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=True,indent=2))
if issues:raise SystemExit(1)
