"""Build the canonical LaTeX PDF and a flat publisher-source archive."""
from pathlib import Path
import argparse
import os
import re
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--xelatex', default='xelatex')
    parser.add_argument('--bibtex', default='bibtex')
    parser.add_argument('--defer-pdf-replace', action='store_true',
                        help='Keep compiled outputs in the build directory when a reader locks the delivered PDF')
    args = parser.parse_args()
    # Stage compiler outputs so an open PDF reader does not interrupt TeX.
    # The canonical source and delivered PDF retain their existing names.
    stage = Path(tempfile.mkdtemp(prefix='.latex-build-', dir=ROOT))
    latex = [args.xelatex,'-interaction=nonstopmode','-halt-on-error',
             '-output-directory='+str(stage),'manuscript.tex']
    environment = os.environ.copy()
    environment['BIBINPUTS'] = str(ROOT)+os.pathsep+environment.get('BIBINPUTS','')
    for command in (latex, [args.bibtex,'manuscript'], latex, latex):
        cwd = stage if command[0] == args.bibtex else ROOT
        result = subprocess.run(command,cwd=cwd,env=environment,capture_output=True,text=True,encoding='utf-8',errors='replace')
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-2000:])
            print('Failed build retained at',stage)
            raise SystemExit(result.returncode)
    log = (stage/'manuscript.log').read_text(encoding='utf-8',errors='replace')
    defects = re.findall(r'(?:Overfull[^\n]*|Missing character[^\n]*|[^\n]*undefined[^\n]*)',log)
    print('PDF compiled. Diagnostics:', defects)
    if any('undefined' in x or 'Missing character' in x for x in defects):
        raise SystemExit('Unresolved references or missing glyphs')
    if not args.defer_pdf_replace:
        try:
            os.replace(stage/'manuscript.pdf', ROOT/'manuscript.pdf')
        except PermissionError:
            raise SystemExit(f'PDF compiled, but a reader prevents replacement of manuscript.pdf. Build retained at {stage}')
    for suffix in ('.aux','.bbl','.blg','.log','.out'):
        generated = stage/('manuscript'+suffix)
        if generated.exists():
            shutil.copy2(generated,ROOT/generated.name)
    if args.defer_pdf_replace:
        print('Canonical PDF replacement deferred; actual compiled PDF:',stage/'manuscript.pdf')
        (ROOT/'qa').mkdir(exist_ok=True)
        (ROOT/'qa/build-output.txt').write_text(str(stage),encoding='utf-8')
    else:
        shutil.rmtree(stage)
    # Generic official Elsevier source instructions request one-folder assets.
    source = (ROOT/'manuscript.tex').read_text(encoding='utf-8')
    bibliography = re.search(r'\\bibliography\{([^}]+)\}',source).group(1)
    source = source.replace('{figures/','{').replace('{'+bibliography+'}','{bibliography}')
    with zipfile.ZipFile(ROOT/'submission-source.zip','w',zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('manuscript.tex',source)
        archive.write(ROOT/(bibliography+'.bib'),'bibliography.bib')
        archive.write(ROOT/'highlights.txt','highlights.txt')
        archive.write(ROOT/'reproduction-notes.md','reproduction-notes.md')
        for path in sorted((ROOT/'figures').glob('*.pdf')):
            archive.write(path,path.name)
        archive.writestr('README.txt','Research first draft; authorship and current Additive Manufacturing-specific submission requirements remain to be completed. Build with XeLaTeX, BibTeX, XeLaTeX twice. Uses standard elsarticle, geometry and siunitx packages. The author-reading surface is single-column 12pt, 180 mm wide and 245 mm high to preserve vector-figure readability; this geometry is not asserted to be an AM submission requirement.\n')
    print('Created submission-source.zip (flat TeX/BibTeX/figure/reproduction assets).')

if __name__=='__main__':
    main()
