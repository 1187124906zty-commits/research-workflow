"""Revalidate changed dashboard content from immutable numerical originals."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
from researchflow import runtime

PAPER = Path(__file__).resolve().parents[1]
OUT = PAPER / 'revision-r6/evidence-refresh'
CASE = Path('C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02')
CLAIMS = ['C_GEOMETRY', 'C_TIME', 'C_CLOSURE']

def main():
    OUT.mkdir(exist_ok=True)
    # Preserve the earlier audit as history; execute a current copy in owned R6 paths.
    shutil.copy2(PAPER/'revision-r3/evidence-refresh/inspect_current.py', OUT/'inspect_current.py')
    result = subprocess.run([sys.executable, '-X', 'utf8', str(OUT/'inspect_current.py')], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    check = json.loads((OUT/'verified-current.json').read_text(encoding='utf-8'))
    if any(value for key, value in check['comparison_checks'].items() if key != 'factorial_metrics_vs_verified'):
        raise ValueError('Changed retained numerical evidence: inspect before support refresh')
    if any(check['comparison_checks']['factorial_metrics_vs_verified'].values()):
        raise ValueError('Changed constitutive corners')
    # Bind stable primary results rather than the mutable presentation dashboard.
    original = json.loads((PAPER/'evidence/verified-data.json').read_text(encoding='utf-8'))
    inputs = [{'path': 'evidence/verified-data.json'}, {'path': 'revision-r2/methods-results/computed-audit.json'},
              {'path': str(CASE/'report/constitutive-factorial-results.json')},
              {'path': str(CASE/'report/experimental-comparison.csv')}]
    inputs += [{'path': run['result_source']} for run in original['runs']]
    tid = 'R6_EVIDENCE_REFRESH'
    if tid not in runtime.context(PAPER)['tasks']:
        runtime.task(PAPER, {'id': tid, 'role': 'evidence', 'owner': 'coordinator',
            'question': 'Did changes to the presentation dashboard change the retained primary geometry, time or constitutive comparison?',
            'purpose': 'Refresh only support inspected against primary numerical originals, preserving earlier stale-input history.',
            'claim_ids': CLAIMS, 'inputs': inputs, 'outputs': ['revision-r6/evidence-refresh/'],
            'writes': ['revision-r6/evidence-refresh/'], 'acceptance': ['Direct original checks agree with retained quantities; no physical validation or precision upgrade.'],
            'budget': {'max_attempts': 2, 'max_no_progress': 2}, 'depends_on': []})
    if runtime.context(PAPER)['tasks'][tid]['status'] != 'accepted':
        reason = 'Root reread primary CSV, factorial results and six result records; numerical values agree. Dashboard changes are presentation additions. Support binds stable originals, not an actively edited presentation report.'
        runtime.record(PAPER, tid, {'attempt': 1, 'changed_understanding': False, 'reason': reason,
            'evidence': [{'path': 'revision-r6/evidence-refresh/verified-current.json', 'level': 'numerical_verification',
                          'kind': 'support', 'claim_ids': CLAIMS, 'summary': reason}], 'blockers': []})
        runtime.decide(PAPER, tid, {'action': 'accept', 'reason': reason, 'promotions': [
            {'claim_id': cid, 'level': 'numerical_verification', 'evidence_indices': [0],
             'reason': 'Same retained numerical claim under inspected conditions; no added physical support or convergence bound.'} for cid in CLAIMS]})
    audit = runtime.audit(PAPER)
    (OUT/'governance-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'checks_current': True, 'protocol_ok': audit['protocol_ok'],
                      'blocking': [r for r in audit['risks'] if r['blocking']]}, ensure_ascii=False))

if __name__ == '__main__':
    main()
