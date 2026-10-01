"""Rebuild the flat delivered archive and compare actual rendered text/assets."""
from pathlib import Path
import argparse
import json
import re
import subprocess
import tempfile
import zipfile
import pymupdf

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--xelatex',default='xelatex')
    parser.add_argument('--bibtex',default='bibtex')
    parser.add_argument('--pdf',type=Path,default=ROOT/'manuscript.pdf')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    parent=ROOT/'submission-source'
    parent.mkdir(exist_ok=True)
    build=Path(tempfile.mkdtemp(prefix='rebuild-r3-',dir=parent))
    source=(ROOT/'manuscript.tex').read_text(encoding='utf-8')
    bibliography=re.search(r'\\bibliography\{([^}]+)\}',source).group(1)
    expected=source.replace('{figures/','{').replace('{'+bibliography+'}','{bibliography}')
    with zipfile.ZipFile(ROOT/'submission-source.zip') as archive:
        names=archive.namelist()
        assert all('/' not in n and '\\' not in n for n in names),'Archive must be flat'
        assert archive.read('manuscript.tex').decode('utf-8')==expected
        assert archive.read('bibliography.bib')==(ROOT/(bibliography+'.bib')).read_bytes()
        assert archive.read('reproduction-notes.md')==(ROOT/'reproduction-notes.md').read_bytes()
        figures=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source)
        for figure in figures:
            assert archive.read(Path(figure).name)==(ROOT/figure).read_bytes()
        archive.extractall(build)
    latex=[args.xelatex,'-interaction=nonstopmode','-halt-on-error','manuscript.tex']
    for command in (latex,[args.bibtex,'manuscript'],latex,latex):
        r=subprocess.run(command,cwd=build,capture_output=True,text=True,encoding='utf-8',errors='replace')
        if r.returncode:
            raise RuntimeError(r.stdout[-5000:]+'\n'+r.stderr[-2000:])
    log=(build/'manuscript.log').read_text(encoding='utf-8',errors='replace')
    diagnostics=re.findall(r'(?:Overfull[^\n]*|Missing character[^\n]*|[^\n]*undefined[^\n]*)',log)
    with pymupdf.open(args.pdf) as canonical,pymupdf.open(build/'manuscript.pdf') as rebuilt:
        pages=len(rebuilt)
        same=len(canonical)==pages and all(a.get_text()==b.get_text() for a,b in zip(canonical,rebuilt))
    report={'source_package_matches_canonical':True,'used_vector_figures':len(figures),
            'reproduction_notes_included':True,'archive_files':names,
            'extracted_package_build':'XeLaTeX/BibTeX/XeLaTeX/XeLaTeX',
            'package_pdf_pages':pages,'page_text_matches_compiled_pdf':same,
            'tex_diagnostics':diagnostics,
            'scope':'Existing Windows TeX Live 2026; source/figure/content parity, not cross-platform or PDE replay verification'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=True,indent=2))
    if diagnostics or not same:
        raise SystemExit(1)

if __name__=='__main__':
    main()
