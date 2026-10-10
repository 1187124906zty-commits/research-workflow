"""Regression tests for scientific-dialogue metadata and lifecycle rules."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "tests" / "fixtures" / "simulation-dialogue"
CANDIDATE = ROOT / "skills" / "simulation-project-orchestrator"
REVIEW = HERE
SCHEMA_PATH = CANDIDATE / "references" / "scientific-dialogue-message.schema.json"
AUDIT_PATH = CANDIDATE / "scripts" / "audit_scientific_dialogue.py"
APPEND_PATH = CANDIDATE / "scripts" / "append_scientific_dialogue.py"

spec = importlib.util.spec_from_file_location("candidate_dialogue_audit", AUDIT_PATH)
audit_module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(audit_module)
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def audit_fixture(path: Path) -> dict:
    return audit_module.audit(audit_module.load_jsonl(path), SCHEMA)


class DialogueAuditTests(unittest.TestCase):
    def assert_complete(self, name: str) -> None:
        report = audit_fixture(REVIEW / name)
        self.assertEqual(report["structural_status"], "PASS", report["errors"])
        self.assertEqual(report["claim_promotion_status"], "DIALOGUE_COMPLETE", report)

    def test_review_positive_fixtures_remain_complete(self) -> None:
        for name in (
            "positive_source.jsonl",
            "positive_scoped_limitation.jsonl",
            "positive_reopen_closed_again.jsonl",
        ):
            with self.subTest(name=name):
                self.assert_complete(name)

    def test_all_terminal_branches_must_be_nonblocking(self) -> None:
        report = audit_fixture(REVIEW / "unrelated_terminal_closure_masks_unresolved_branch.jsonl")
        self.assertEqual(report["structural_status"], "PASS")
        self.assertEqual(report["claim_promotion_status"], "BLOCKED")
        self.assertIn("independent-thread", report["open_stop_line_threads"])

    def test_one_response_has_only_one_requester_disposition(self) -> None:
        report = audit_fixture(REVIEW / "old_closure_masks_new_branch.jsonl")
        self.assertEqual(report["structural_status"], "FAIL")
        self.assertTrue(any("multiple requester dispositions" in error for error in report["errors"]))

    def test_request_contract_fields_are_required(self) -> None:
        report = audit_fixture(REVIEW / "missing_request_contract.jsonl")
        self.assertEqual(report["structural_status"], "FAIL")
        joined = "\n".join(report["errors"])
        for field in ("competing_explanations", "requested_evidence_or_action", "response_condition"):
            self.assertIn(field, joined)

    def test_closure_kind_is_required(self) -> None:
        report = audit_fixture(REVIEW / "missing_closure_kind.jsonl")
        self.assertEqual(report["structural_status"], "FAIL")
        self.assertTrue(any("closure_kind" in error for error in report["errors"]))

    def test_every_accountable_receiver_must_respond(self) -> None:
        report = audit_fixture(REVIEW / "second_accountable_receiver_unanswered.jsonl")
        self.assertEqual(report["structural_status"], "PASS")
        self.assertEqual(report["claim_promotion_status"], "BLOCKED")
        obligation = report["missing_receiver_obligations"][0]
        self.assertEqual(obligation["missing_receiver_roles"], ["experiment"])
        self.assertEqual(obligation["affected_claims"], ["claim-a"])

    def test_original_regressions_and_reopen_lifecycle(self) -> None:
        contradiction = audit_fixture(HERE / "status-contradiction.jsonl")
        claim_drop = audit_fixture(HERE / "claim-drop.jsonl")
        reopened = audit_fixture(HERE / "reopen-after-closure.jsonl")
        reclosed = audit_fixture(HERE / "reopen-complete.jsonl")
        self.assertEqual(contradiction["structural_status"], "FAIL")
        self.assertEqual(claim_drop["structural_status"], "FAIL")
        self.assertEqual(reopened["structural_status"], "PASS")
        self.assertEqual(reopened["claim_promotion_status"], "BLOCKED")
        self.assertEqual(reclosed["claim_promotion_status"], "DIALOGUE_COMPLETE")

    def test_append_rejects_duplicate_and_unknown_predecessor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            ledger = Path(directory) / "ledger.jsonl"
            common = [sys.executable, str(APPEND_PATH), "--ledger", str(ledger), "--schema", str(SCHEMA_PATH)]
            first = subprocess.run(common + ["--message", str(HERE / "append-root-a.json")], capture_output=True)
            duplicate = subprocess.run(common + ["--message", str(HERE / "append-root-a.json")], capture_output=True)
            unknown = subprocess.run(common + ["--message", str(HERE / "append-unknown.json")], capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertNotEqual(duplicate.returncode, 0)
            self.assertNotEqual(unknown.returncode, 0)
            self.assertEqual(len(ledger.read_text(encoding="utf-8").splitlines()), 1)

    def test_concurrent_append_does_not_lose_messages(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            ledger = Path(directory) / "ledger.jsonl"
            base = [sys.executable, str(APPEND_PATH), "--ledger", str(ledger), "--schema", str(SCHEMA_PATH), "--message"]
            processes = [
                subprocess.Popen(base + [str(HERE / name)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for name in ("append-root-a.json", "append-root-b.json")
            ]
            results = [process.communicate(timeout=15) + (process.returncode,) for process in processes]
            self.assertEqual([result[2] for result in results], [0, 0], results)
            messages = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines()]
            self.assertEqual({message["message_id"] for message in messages}, {"append-a", "append-b"})


if __name__ == "__main__":
    unittest.main()
