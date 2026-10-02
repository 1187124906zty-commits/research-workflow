"""Integrate reviewed R4 candidates into the existing open LaTeX source."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT.parent
before = (ROOT / 'manuscript-input.tex').read_text(encoding='utf-8')
candidate = (ROOT / 'integration/body-candidate.tex').read_text(encoding='utf-8')
title = 'Thermophysical-property effects on melt-pool geometry and cooling histories in IN625 laser processing'
candidate = re.sub(r'\\title\{[^\n]+\}', lambda _: '\\title{' + title + '}', candidate, count=1)
abstract = (ROOT / 'argument/abstract.tex').read_text(encoding='utf-8').strip()
candidate = re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}', lambda _: abstract, candidate, count=1, flags=re.S)
intro = (ROOT / 'argument/introduction.tex').read_text(encoding='utf-8').strip()
recent = (ROOT / 'argument/recent-assessment.tex').read_text(encoding='utf-8').strip()
intro = intro.replace('The material description supplies another basis', recent + '\n\nThe material description supplies another basis', 1)
start = candidate.index('\\section{Introduction}')
end = candidate.index('\\section{Materials and methods}', start)
candidate = candidate[:start] + intro + '\n\n' + candidate[end:]

# Scientific formulas, property/geometry tables and figure input paths remain
# the same; prose progress does not create a new numerical result.
preserved = {}
for environment in ['equation', 'align', 'tabular']:
    pattern = r'\\begin\{' + environment + r'\}.*?\\end\{' + environment + r'\}'
    blocks = re.findall(pattern, before, flags=re.S)
    assert blocks == re.findall(pattern, candidate, flags=re.S), environment
    preserved[environment] = len(blocks)
images = r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}'
assert re.findall(images, before) == re.findall(images, candidate)
preserved['figure_inputs'] = len(re.findall(images, candidate))
assert re.findall(r'\\bibliography\{([^}]+)\}', before) == re.findall(r'\\bibliography\{([^}]+)\}', candidate)
(PAPER / 'manuscript.tex').write_text(candidate, encoding='utf-8')
record = {'title': title, 'source': 'Existing canonical manuscript.tex, edited in place',
          'guides': ['guidance/source-ledger.json', 'guidance/section-guides.md'],
          'candidates': ['argument/introduction.tex', 'argument/abstract.tex', 'integration/body-candidate.tex'],
          'unchanged_scientific_blocks': preserved,
          'cited_keys': sorted({key.strip() for group in re.findall(r'\\cite\{([^}]+)\}', candidate) for key in group.split(',')}),
          'new_pde_solves': 0,
          'scope': 'Evidence-bound manuscript revision, not new data or independent thermal validation'}
(ROOT / 'integration/integration-record.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(record, ensure_ascii=True, indent=2))
