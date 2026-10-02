"""Publish only the minimal, attributed writing-source ledger, not full pages."""
import argparse
import json
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1]
IDS = {'DUKE_RESOURCE', 'DUKE_SUBJECTS_ACTIONS', 'DUKE_COHESION_COHERENCE',
       'PURDUE_REVERSE_OUTLINE', 'UNC_SCIENTIFIC_STYLE_R5'}
FIELDS = {'id', 'title', 'url', 'authority', 'read_scope', 'locators', 'license', 'transfer_limits'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('output', type=Path)
    a = p.parse_args()
    src = json.loads((PAPER / 'revision-r5/guidance/source-ledger.json').read_text(encoding='utf-8'))
    entries = [{k: v for k, v in s.items() if k in FIELDS} for s in src['sources'] if s['id'] in IDS]
    data = {'date': src['read_date'], 'scope': 'Five entries used by the compact cohesion method; complete R5 investigation has 13 scoped reading records. No full extracts redistributed.',
            'sources': entries, 'unavailable_original': 'Gopen/Swan publisher503, candidate mirror404; not read or replaced by memory.'}
    a.output.mkdir(parents=True, exist_ok=True)
    (a.output / 'cohesion-source-ledger.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    lines = ['# Sources for scientific-object and continuity methods', '',
        'These are actual reading scopes and source-specific licenses. The project methods are independently written editorial procedures, not journal requirements or scientific evidence for a study. Full pages are not redistributed. This compact ledger contains five entries used by the new sentence method; existing chapter sources remain in source-ledger.md.', '']
    for s in entries:
        lines.extend(['## '+s['id'], '', '['+s['title']+']('+s['url']+')', '',
                      'Authority: '+s['authority'], '', 'Actual read scope: '+s['read_scope'], ''])
        for q in s['locators']:
            lines.append('- '+q['section']+': '+q['supported_principle']+' Short quotation: "'+q['short_quote']+'"')
        lines.extend(['', 'Source license: '+s['license']['name']+'. '+s['license']['limit'], ''])
        lines.extend('- Transfer boundary: '+v for v in s.get('transfer_limits', []))
        lines.append('')
    lines.append('Gopen/Swan original was not obtained (publisher503, candidate mirror404). Duke is the institutional source actually read; its credit to earlier authors does not establish reading their original works.')
    (a.output / 'cohesion-source-ledger.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print('Packaged minimal source ledger:', len(entries), 'entries')


if __name__ == '__main__':
    main()
