"""Coordinator-only R2 handoff recording; scientific dispositions remain explicit."""
from pathlib import Path
import argparse
import json
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]

def accept(tid, paths, reason, changed=False):
    state = runtime.context(PAPER)
    if state['tasks'][tid]['status'] == 'accepted':
        return
    runtime.record(PAPER, tid, {
        'attempt': 1, 'changed_understanding': changed, 'reason': reason,
        'evidence': [{'path': p, 'level': 'observation', 'kind': 'observation',
                      'claim_ids': [], 'summary': reason} for p in paths], 'blockers': []})
    runtime.decide(PAPER, tid, {'action': 'accept', 'reason': reason})

def register(tid, role, paths, output, question, dependencies):
    if tid in runtime.context(PAPER)['tasks']:
        return
    runtime.task(PAPER, {'id': tid, 'role': role, 'owner': role, 'question': question,
        'purpose': 'Close the literature-grounded scientific argument in the existing manuscript',
        'claim_ids': [], 'inputs': [{'path': p} for p in paths],
        'outputs': [output], 'writes': [output],
        'acceptance': ['Actual current prose, consequential original evidence and explicit limitations are read; defects require source-level repair'],
        'budget': {'max_attempts': 2, 'max_no_progress': 2}, 'depends_on': dependencies})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=['journal', 'native', 'exchange', 'dispatch-review', 'review'])
    stage = parser.parse_args().stage
    if stage == 'journal':
        accept('R2_JOURNAL', [f'revision-r2/journal/{p}' for p in
            ('journal-learning.md', 'source-use.md', 'source-index.json', 'locators.md', 'new-sources.bib')],
            'Root read the actual journal-learning/source-use/index/locators and key Hou original passages. Accept as bounded writing support: five final VoR plus one substantively read corrected proof, not six final papers; current AM-specific guide remains inaccessible. Counts are coverage observations, not official quotas.')
        register('R2_CROSS_SECTION', 'mechanism',
            ['revision-r2/argument-r001.md', 'revision-r2/methods-results/section-methods.tex',
             'revision-r2/methods-results/section-results.tex', 'revision-r2/journal/source-use.md'],
            'revision-r2/exchange/',
            'Do Introduction promises, quantitative design and Discussion interpretations close the scientific tension without causal overreach?',
            ['R2_LITERATURE', 'R2_METHODS_RESULTS', 'R2_JOURNAL'])
    elif stage == 'native':
        accept('R2_NATIVE_SECTION_DRAFTS', ['revision-r2/native-drafts-record.md',
            'revision-r2/sections/introduction-r001.tex', 'revision-r2/sections/discussion-r001.tex'],
            'Root inspected the real native writer ledger and files: Introduction returned; Discussion wrote its candidate but timed out before a structured return. Native reviews/dispositions did not run in this batch. Accept these inspected files only as integration candidates, with timeout retained and separate cross-section/whole-manuscript review required; no physical validation or full native completion inferred.')
    elif stage == 'exchange':
        accept('R2_CROSS_SECTION', [f'revision-r2/exchange/{p}' for p in
            ('cross-section-review.md', 'proposed-additions.tex', 'citation-use.md')],
            'Root read the actual exchange. Adopt bounded wording/source additions and evidence order; restrict geometry residual and selected-face Pe causality. Whole-current-manuscript review remains separate.')
    elif stage == 'dispatch-review':
        register('R2_WHOLE_REVIEW', 'reviewer',
            ['manuscript.tex', 'manuscript.pdf', 'literature/bibliography-r2.bib',
             'evidence/verified-data.json', 'revision-r2/methods-results/computed-audit.json'],
            'revision-r2/review/',
            'Does the actual complete current source/PDF close a literature-grounded scientific argument with adequate quantitative evidence, readable figures and honest journal/validation limits?',
            ['R2_NATIVE_SECTION_DRAFTS', 'R2_CROSS_SECTION'])
    else:
        accept('R2_WHOLE_REVIEW', ['revision-r2/review/whole-review.md',
            'revision-r2/review/review-response.md'],
            'Root inspected actual independent whole-manuscript findings, applied consequential repairs and checked the rebuilt current PDF. Accept this first-draft review scope, with journal-specific submission compliance and human authorship approval still unresolved.')
    print(json.dumps(runtime.audit(PAPER), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
