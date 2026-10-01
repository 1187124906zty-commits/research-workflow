"""Build the canonical LaTeX PDF and a flat publisher-source archive."""
from pathlib import Path
import argparse
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parent
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--xelatex', default='xelatex')
    parser.add_argument('--bibtex', default='bibtex')
    args = parser.parse_args()
    for command in ([args.xelatex,'-interaction=nonstopmode','-halt-on-error','manuscript.tex'],
                    [args.bibtex,'manuscript'],
                    [args.xelatex,'-interaction=nonstopmode','-halt-on-error','manuscript.tex'],
                    [args.xelatex,'-interaction=nonstopmode','-halt-on-error','manuscript.tex']):
        result = subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace')
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-2000:])
            raise SystemExit(result.returncode)
    log = (ROOT/'manuscript.log').read_text(encoding='utf-8',errors='replace')
    defects = re.findall(r'(?:Overfull[^\n]*|Missing character[^\n]*|[^\n]*undefined[^\n]*)',log)
    print('PDF compiled. Diagnostics:', defects)
    if any('undefined' in x or 'Missing character' in x for x in defects):
        raise SystemExit('Unresolved references or missing glyphs')
    # Generic official Elsevier source instructions request one-folder assets.
    source = (ROOT/'manuscript.tex').read_text(encoding='utf-8')
    bibliography = re.search(r'\\bibliography\{([^}]+)\}',source).group(1)
    source = source.replace('{figures/','{').replace('{'+bibliography+'}','{bibliography}')
    with zipfile.ZipFile(ROOT/'submission-source.zip','w',zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('manuscript.tex',source)
        archive.write(ROOT/(bibliography+'.bib'),'bibliography.bib')
        archive.write(ROOT/'highlights.txt','highlights.txt')
        for path in sorted((ROOT/'figures').glob('*.pdf')):
            archive.write(path,path.name)
        archive.writestr('README.txt','Research first draft; authorship and current Additive Manufacturing-specific submission requirements remain to be completed. Build with XeLaTeX, BibTeX, XeLaTeX twice. Uses standard elsarticle, geometry and siunitx packages. The author-reading surface is single-column 12pt, 180 mm wide and 245 mm high to preserve vector-figure readability; this geometry is not asserted to be an AM submission requirement.\n')
    print('Created submission-source.zip (flat TeX/BibTeX/figure assets).')

if __name__=='__main__':
    main()
