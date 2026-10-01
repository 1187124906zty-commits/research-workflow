"""Requester disposition, real PaperSpine file handoff and selected original figures."""
from pathlib import Path
import importlib.util
import json
import shutil
import sys
REPO = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'src'))
from researchflow import runtime
SOURCE = Path('C:/Users/Administrator/Documents/ChatGPT/电脑答疑/simulation-agent-mvp/research/reproduction-case/nist-amb2018-02')

def main():
    ctx = runtime.context(ROOT, 'T_EVIDENCE')
    cids = list(ctx['claims'])
    if ctx['status'] == 'active':
        runtime.record(ROOT, 'T_EVIDENCE', {'attempt': 1, 'changed_understanding': True,
            'reason': 'Independent direct inspection distinguished actual FiPy method, calibration role, observation mismatch and claim-specific numerical adequacy.',
            'evidence': [
                {'path': 'evidence/evidence-dossier.md', 'level': 'observation', 'kind': 'observation', 'claim_ids': cids, 'summary': 'Independent interpretation and explicit scientific boundaries'},
                {'path': 'evidence/verified-data.json', 'level': 'numerical_verification', 'kind': 'support', 'claim_ids': cids, 'summary': 'Located retained-model quantities and actual consistency/refinement checks; no physical validation inferred'}],
            'blockers': [], 'contribution': {'answer': 'A bounded discrepancy and closure-sensitivity manuscript can be drafted.', 'effect_on_project': 'Remove predictive validation and exact reproduction claims; retain major tail response, geometry discrepancy and derived passage-time distinction.', 'uncertainties': ['Operator mismatch, combined uncertainty, liquid transport and branch-specific fine convergence remain unresolved'], 'next_options': ['Draft current scoped article'], 'cost_note': 'Read-only inspection; no solver runs'}})
    if runtime.context(ROOT, 'T_EVIDENCE')['status'] == 'awaiting_decision':
        runtime.decide(ROOT, 'T_EVIDENCE', {'action': 'accept', 'reason': 'Accepted located evidence for bounded model diagnostics after coordinator read; broader physical validation is excluded.',
            'promotions': [{'claim_id': cid, 'level': 'numerical_verification', 'evidence_indices': [1], 'reason': 'Supports only the recorded conduction-model result and major-scale comparison, with dossier limits.'} for cid in cids]})
    runtime.plan(ROOT, {'reason': 'Evidence-first journal argument chosen before composing the article', 'target_journal': 'Additive Manufacturing',
        'facts': ['SimAgent generated original numerical case; current ResearchFlow/MAF process prepares and reviews manuscript', 'B length is fitted; A/C are retrospective nonblind fixed-parameter comparisons', 'Six unique current production runs; no new PDE solves during manuscript formation'],
        'hypotheses': ['Beam shape, imaging/fusion operators, constitutive storage and omitted directional heat transport can contribute to geometry discrepancies'],
        'uncertainties': ['Venue contribution sufficiency', 'Journal-specific guide could not be accessed', 'Physical predictive validation not established'],
        'next_decision': 'Use bounded MAF returns, verified literature and actual figures to assemble and independently review an English first draft'})
    adapter_path = REPO / 'integrations/paperspine/adapter.py'
    spec = importlib.util.spec_from_file_location('ps_adapter', adapter_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.export_handoff(ROOT, ROOT / 'governance/paperspine-handoff')
    (ROOT / 'figures').mkdir(exist_ok=True)
    figure_names = ['ammt-application-experiment', 'ammt-research-operating-cases', 'ammt-research-condition-trends', 'ammt-research-constitutive-factorial']
    for name in figure_names:
        for extension in ('pdf', 'png', 'svg'):
            shutil.copy2(SOURCE / 'report/figures' / f'{name}.{extension}', ROOT / 'figures' / f'{name}.{extension}')
    (ROOT / 'governance/prewriting-audit.json').write_text(json.dumps(runtime.audit(ROOT), indent=2), encoding='utf-8')
    print(json.dumps(runtime.audit(ROOT), ensure_ascii=True, indent=2))

if __name__ == '__main__':
    main()
