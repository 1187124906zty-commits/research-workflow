"""Record actual R3 returns and bounded coordinator dispositions."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]

def accept(tid, paths, reason):
    if runtime.context(PAPER)['tasks'][tid]['status'] == 'accepted':
        return
    runtime.record(PAPER, tid, {
        'attempt': 1, 'changed_understanding': False, 'reason': reason,
        'evidence': [{'path': p, 'level': 'observation', 'kind': 'observation',
                      'claim_ids': [], 'summary': reason} for p in paths],
        'blockers': []})
    runtime.decide(PAPER, tid, {'action': 'accept', 'reason': reason})

def register(tid, inputs, output, question, dependencies):
    if tid in runtime.context(PAPER)['tasks']:
        return
    runtime.task(PAPER, {
        'id': tid, 'role': 'reviewer', 'owner': 'reviewer',
        'question': question,
        'purpose': 'Check the actual source, source support and rendered scientific argument',
        'claim_ids': [], 'inputs': [{'path': p} for p in inputs],
        'outputs': [output], 'writes': [output],
        'acceptance': ['Actual resulting files are read; source support and reader defects are located and repaired within their evidence scope'],
        'budget': {'max_attempts': 2, 'max_no_progress': 2},
        'depends_on': dependencies})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=['sources', 'review', 'dispatch-delivery', 'delivery'])
    parser.add_argument('--compiled-pdf',default='manuscript.pdf',
                        help='Actual compiled PDF input if canonical file is temporarily reader-locked')
    args = parser.parse_args()
    stage = args.stage
    if stage == 'sources':
        accept('R3_EDITORIAL', [f'revision-r3/editorial/{p}' for p in
            ('methods.tex','discussion.tex','appendix-additions.tex',
             'reproduction-notes.md','venue-structure-audit.md','results-guidance.md')],
            'Root read the returned candidates and original-source structure audit. Integrated four Methods and four Discussion units, relocated software details, and retained physical/observation/numerical boundaries. Source support is governed separately; sample practice is not an official AM rule. No scientific evidence promotion.')
        accept('R3_CITATIONS', [f'revision-r3/citations/{p}' for p in
            ('support-ledger.json','citation-audit.md','recommended-replacements.tex')],
            'Root inspected actual 19-assertion ledger and direct enthalpy, parameter and benchmark passages, then integrated point-of-use sources and derivation labels. Accept as scoped literature support, not independent thermal validation. The mistaken DOI was a retrieval hint, not a cited identity; no bibliography padding or physical promotion.')
        register('R3_INDEPENDENT',
            ['revision-r3/review/manuscript-reviewed.tex',
             'revision-r3/citations/support-ledger.json',
             'revision-r3/editorial/venue-structure-audit.md','evidence/verified-data.json'],
            'revision-r3/review/',
            'Does the integrated actual R3 source/PDF repair detail allocation, chapter flow and focused citation support while preserving model/measurement/validation boundaries?',
            ['R3_EDITORIAL','R3_CITATIONS'])
    elif stage == 'review':
        accept('R3_INDEPENDENT', ['revision-r3/review/independent-review.md',
            'revision-r3/review/review-response.md','revision-r3/review/repair-verification.md'],
            'Root read the independent current-manuscript/page review, repaired actionable findings and inspected the actual revised outputs. Accept the documented automated review scope; no human peer review, official submission compliance or new physical evidence inferred.')
    elif stage == 'dispatch-delivery':
        register('R3_DELIVERY', ['manuscript.tex',args.compiled_pdf,'submission-source.zip',
            'reproduction-notes.md','literature/bibliography-r3.bib',
            'revision-r3/review/independent-review.md','revision-r3/review/repair-verification.md'],
            'revision-r3/delivery/',
            'Does the actual final package compile/rebuild, preserve correct scientific provenance and expose working public introduction links?',
            ['R3_INDEPENDENT'])
    else:
        accept('R3_DELIVERY', ['revision-r3/delivery/delivery-check.json',
            'revision-r3/delivery/package-rebuild-check.json','revision-r3/delivery/provenance.md'],
            'Root inspected the final compiled PDF, package rebuild and publication link/provenance checks. Delivery acceptance is limited to this actual first-draft package and tested environment; scientific novelty, independent thermal validation and journal acceptance remain unestablished.')
    print(json.dumps(runtime.audit(PAPER), ensure_ascii=True, indent=2))

if __name__ == '__main__':
    main()
