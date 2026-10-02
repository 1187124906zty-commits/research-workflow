"""Register actual R4 writing-guide, forward-use, review and delivery handoffs."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]


def accept(tid, paths, reason):
    entry = runtime.context(PAPER)['tasks'][tid]
    if entry['status'] == 'accepted':
        return
    runtime.record(PAPER, tid, {
        'attempt': 1, 'changed_understanding': False, 'reason': reason,
        'evidence': [{'path': p, 'level': 'observation', 'kind': 'observation',
                      'claim_ids': [], 'summary': reason} for p in paths], 'blockers': []})
    runtime.decide(PAPER, tid, {'action': 'accept', 'reason': reason})


def register(tid, inputs, output, question, dependencies, role='reviewer'):
    if tid in runtime.context(PAPER)['tasks']:
        return
    runtime.task(PAPER, {
        'id': tid, 'role': role, 'owner': role,
        'question': question,
        'purpose': 'Evaluate reusable writing methods on actual manuscript artifacts and bounded framework execution',
        'claim_ids': [], 'inputs': [{'path': p} for p in inputs],
        'outputs': [output], 'writes': [output],
        'acceptance': ['Read the actual artifacts; preserve source identity, numerical quantities and calibration/measurement roles; distinguish editorial progress from new scientific evidence'],
        'budget': {'max_attempts': 2, 'max_no_progress': 2}, 'depends_on': dependencies})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=['guidance', 'argument', 'dispatch-review', 'review', 'forward', 'dispatch-delivery', 'delivery'])
    args = parser.parse_args()
    if args.stage == 'guidance':
        accept('R4_GUIDANCE', [f'revision-r4/guidance/{name}' for name in
               ['institution-guidance.md', 'section-guides.md', 'synthesis.md', 'source-ledger.json', 'source-ledger.md']],
               'Root inspected the returned original-source guidance, precise locators, short quotations, heuristic and license boundaries. Accept independently worded reusable methods from 12 read guides; no venue compliance or scientific quality certification. Private full extracts remain excluded.')
        register('R4_FORWARD_USE', ['revision-r4/manuscript-input.tex', 'evidence/verified-data.json',
                 'revision-r4/guidance/section-guides.md'], 'revision-r4/forward-use/',
                 'Does a new real MAF writing task consume selected guides, produce actual bounded text and complete review/requester handoffs, and what does the actual text establish?', ['R4_GUIDANCE'])
    elif args.stage == 'argument':
        accept('R4_ARGUMENT', [f'revision-r4/argument/{name}' for name in
               ['introduction.tex', 'abstract.tex', 'title-logic.md', 'argument-map.md', 'synthesis-trace.json']],
               'Root inspected original-source relationships and the resulting linked paragraphs, qualitative-first abstract and title semantics. Accept as editorial candidates integrated within retained evidence scope; no broad novelty, model improvement or independent thermal validation asserted.')
    elif args.stage == 'dispatch-review':
        register('R4_INDEPENDENT', ['revision-r4/review/manuscript-reviewed.tex',
                 'revision-r4/review/manuscript-reviewed.pdf', 'revision-r4/guidance/section-guides.md',
                 'revision-r3/citations/support-ledger.json', 'evidence/verified-data.json'],
                 'revision-r4/review/',
                 'Does the actual integrated R4 source and PDF resolve title semantics, abstract synthesis, connected Introduction and objective scientific narrative while preserving evidence scope?', ['R4_GUIDANCE', 'R4_ARGUMENT'])
    elif args.stage == 'review':
        accept('R4_INDEPENDENT', [f'revision-r4/review/{name}' for name in
               ['independent-review.md', 'review-response.md', 'repair-verification.md']],
               'Root inspected the current full-manuscript review, consequential source/evidence defects and actual repairs/rechecks. Accept only the documented automated readership and evidence review scope; human review, journal acceptance and independent scientific validation are separate.')
    elif args.stage == 'forward':
        accept('R4_FORWARD_USE', ['revision-r4/forward-use/execution-summary.json',
               'revision-r4/forward-use/coordinator-evaluation.md'],
               'Root read the actual native MAF execution, saved selected instructions, produced manuscript candidate and review/requester dispositions. The bounded case evaluates role/skill delivery and editorial response, not general writing efficacy or a complete autonomous publication pipeline.')
    elif args.stage == 'dispatch-delivery':
        register('R4_DELIVERY', ['manuscript.tex', 'manuscript.pdf', 'submission-source.zip',
                 'revision-r4/review/repair-verification.md'], 'revision-r4/delivery/',
                 'Does the current PDF/source archive rebuild and preserve located scientific and tool provenance, with working introduction links?', ['R4_INDEPENDENT', 'R4_FORWARD_USE'])
    else:
        accept('R4_DELIVERY', ['revision-r4/delivery/delivery-check.json',
               'revision-r4/delivery/package-rebuild-check.json', 'revision-r4/delivery/provenance.md'],
               'Root inspected the actual compiled and rebuilt package, final source and published links. Delivery is the revised research draft plus tested role-scoped guides; no human peer review, broad tool efficacy or AM submission-readiness inference.')
    audit = runtime.audit(PAPER)
    print(json.dumps({'protocol_ok': audit['protocol_ok'], 'risk_count': len(audit.get('risks', [])),
                      'blocking': [r for r in audit.get('risks', []) if r.get('blocking')]}, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
