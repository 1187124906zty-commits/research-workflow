"""Integrate separately owned R5 candidates in the existing source document."""
from pathlib import Path
import json
import re

PAPER = Path(__file__).resolve().parents[1]
APP = PAPER / 'revision-r5/application'


def main():
    source_path = PAPER / 'manuscript.tex'
    original = (PAPER / 'revision-r5/manuscript-input.tex').read_text(encoding='utf-8')
    source = original
    title_abstract = (APP / 'title-abstract.tex').read_text(encoding='utf-8').strip()
    source = re.sub(r'\\title\{[^\n]*\}.*?\\end\{abstract\}',
                    lambda _: title_abstract, source, count=1, flags=re.S)
    begin = source.index(r'\section{Introduction}')
    end = source.index(r'\section*{Data and code availability}')
    source = source[:begin] + '\n\n'.join((APP / name).read_text(encoding='utf-8').strip()
        for name in ['introduction.tex', 'methods-results.tex', 'discussion-conclusions.tex']) + '\n\n' + source[end:]
    # Preserve the verified appendix, but align its names with the now-defined mathematical rules.
    source = source.replace('The continuation slopes from the final tabulated pairs',
                            'The linear-extrapolation slopes from the final tabulated pairs')
    source = source.replace('using the corresponding property continuation.',
                            'using the corresponding property extrapolation.')
    source = source.replace('the same continuation rules.', 'the same extrapolation rules.')
    source = source.replace('change with the continuation.', 'change with the property extrapolation.')
    if source_path.read_text(encoding='utf-8') != source:
        source_path.write_text(source, encoding='utf-8')
    for pattern, expected in [(r'\\begin\{table\}', 5), (r'\\includegraphics', 5)]:
        assert len(re.findall(pattern, source)) == expected
    assert source[source.index(r'\section*{Data and code availability}'):].count(r'\begin{equation}') == original[original.index(r'\section*{Data and code availability}'):].count(r'\begin{equation}')
    report = {'source': 'manuscript.tex', 'candidate_owners': {'introduction': 'r5_architecture',
        'methods_results': 'r5_sources', 'discussion_conclusions_title_abstract': 'root editor'},
        'retained_scientific_figures': 5, 'retained_tables': 5,
        'new_definition': 'Study-defined final-secant linear extrapolation and constant endpoint extrapolation',
        'new_production_PDE_runs': 0, 'scientific_support_promoted': False}
    (APP / 'integration.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
