"""Boundary tests: export provenance and transport errors cannot promote science."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from integrations.paperspine.adapter import (
    AdapterError, HostClient, _domain_error, export_handoff, read_json, validate_call, write_json,
)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = {
            "schema_version": 1, "revision": 8,
            "project": {"question": "Does a low-cost model preserve ordering?", "purpose": "compare two regimes",
                        "target_journal": None},
            "research": {"facts": [], "hypotheses": ["ordering is robust"],
                         "uncertainties": ["physical validity is untested"], "next_decision": "check the reversal"},
            "claims": {
                "C1": {"id": "C1", "statement": "The ordering reverses under the tested range.", "status": "narrowed",
                       "support": {"observation": [], "numerical_verification": [
                           {"task_id": "T1", "attempt": 2, "path": "evidence/order.csv", "revision": "r2",
                            "reason": "ordering unchanged under one refinement"}], "physical_validation": []},
                       "challenges": [{"id": "N1", "task_id": "T1", "attempt": 1, "reason": "original hypothesis contradicted",
                                       "level": "observation"}], "limitations": ["not experimentally validated"]},
                "C2": {"id": "C2", "statement": "An unrelated effect", "status": "hypothesis", "support": {}},
            },
            "tasks": {
                "T1": {"contract": {"id": "T1", "role": "simulation", "claim_ids": ["C1"], "purpose": "discriminate ordering",
                                    "inputs": [{"path": "inputs/model.py", "revision": "r1"}], "outputs": ["evidence/order.csv"],
                                    "budget": {"max_attempts": 2, "max_no_progress": 1}},
                       "status": "accepted", "attempts": [{"index": 1}, {"index": 2}],
                       "decisions": [{"disposition": "accept", "reason": "useful negative evidence"}]},
                "T2": {"contract": {"id": "T2", "claim_ids": ["C2"]}, "status": "active"},
            },
        }
        write_json(self.root / ".researchflow/research-state.json", self.state)

    def test_export_preserves_levels_negative_evidence_and_claim_meaning(self):
        result = export_handoff(self.root, self.root / "handoff", "T1")
        packet = read_json(Path(result["handoff"]))
        self.assertEqual(packet["claims"]["C1"], self.state["claims"]["C1"])
        self.assertEqual(packet["claims"]["C1"]["status"], "narrowed")
        self.assertEqual(packet["claims"]["C1"]["support"]["physical_validation"], [])
        self.assertEqual(packet["tasks"]["T1"]["status"], "accepted")
        self.assertFalse(packet["authority"]["web_user_confirmation"])
        self.assertFalse(result["backend_called"])

    def test_task_specific_context_and_source_remain_unchanged(self):
        before = (self.root / ".researchflow/research-state.json").read_text(encoding="utf-8")
        packet = read_json(Path(export_handoff(self.root, self.root / "handoff", "T1")["handoff"]))
        self.assertEqual(set(packet["claims"]), {"C1"})
        self.assertEqual(set(packet["tasks"]), {"T1"})
        self.assertEqual(packet["tasks"]["T1"]["latest_attempt"], [{"index": 2}])
        self.assertEqual(packet["authority"]["project_revision"], 8)
        self.assertEqual((self.root / ".researchflow/research-state.json").read_text(encoding="utf-8"), before)

    def test_unknown_claim_is_rejected(self):
        with self.assertRaises(AdapterError):
            export_handoff(self.root, self.root / "handoff", claim_ids=["invented"])

    def test_schema_is_not_silently_upgraded(self):
        self.state["schema_version"] = 2
        write_json(self.root / ".researchflow/research-state.json", self.state)
        with self.assertRaises(AdapterError):
            export_handoff(self.root, self.root / "handoff")


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "skill/scripts").mkdir(parents=True)
        (self.root / "skill/scripts/paperspine5_web.py").write_text("# fixture", encoding="utf-8")
        self.client = HostClient(self.root / "skill", self.root / "profile", python="python")

    def test_task_mismatch_and_identity_spoofing_are_rejected(self):
        for arguments in ({"task_id": "OTHER"}, {"request": {"task_id": "T", "reviewer_id": "writer"}},
                          {"request": {"task_id": "T", "payload": {"source": "web_user"}}},
                          {"request": {"task_id": "T", "payload": {"user_confirmed": True}}}):
            with self.subTest(arguments=arguments), self.assertRaises(AdapterError):
                validate_call("paperspine_bind_evidence", arguments, "T")

    def test_review_and_configuration_tools_are_not_impersonated(self):
        for tool in ("paperspine_submit_review", "paperspine_save_configuration", "paperspine_resolve_decision"):
            with self.subTest(tool=tool), self.assertRaises(AdapterError):
                validate_call(tool, {}, "T")

    def test_nonzero_schema_output_is_not_success(self):
        result = subprocess.CompletedProcess([], 1, json.dumps({"name": "paperspine_open_task", "inputSchema": {}}), "transport failed")
        with patch("integrations.paperspine.adapter.subprocess.run", return_value=result) as run:
            with self.assertRaises(AdapterError):
                self.client.schema("paperspine_open_task")
            self.assertEqual(run.call_count, 1)

    def test_domain_error_inside_successful_mcp_is_failure(self):
        value = {"content": [{"type": "text", "text": json.dumps({"error": {"code": "version_conflict"}})}]}
        self.assertEqual(_domain_error(value), {"code": "version_conflict"})
        result = subprocess.CompletedProcess([], 0, json.dumps(value), "")
        with patch("integrations.paperspine.adapter.subprocess.run", return_value=result):
            with self.assertRaises(AdapterError):
                self.client._run(["host", "call"])

    def test_input_and_versions_are_passed_without_retry_or_rewriting(self):
        args = {"request": {"task_id": "T", "schema_version": "1.1", "expected_version": 3,
                            "payload": {"claim_id": "C1", "evidence_id": "E1", "relation": "challenges"}}}
        original = copy.deepcopy(args)
        with patch.object(self.client, "schema", return_value={}), patch.object(self.client, "_run", return_value={"ok": True}) as run:
            self.client.call("paperspine_bind_evidence", args, "T")
            self.assertEqual(json.loads(run.call_args.args[1]), original)
            self.assertEqual(run.call_count, 1)
        self.assertEqual(args, original)

    def test_doctor_reports_ancestor_layout_and_distinguishes_host_from_web(self):
        self.client.pointer = {"suite_root": str(self.root / "profile/.lifecycle/install"), "product_version": "fixture"}
        with patch.object(self.client, "schema", return_value={}), patch.object(self.client, "_run", side_effect=AdapterError("STOPPED")):
            report = self.client.doctor()
        self.assertTrue(report["host_schema_verified"])
        self.assertFalse(report["web_start_verified"])
        self.assertFalse(report["agent_started"])
        self.assertTrue(any("ancestor_conflict" in note for note in report["notes"]))


if __name__ == "__main__":
    unittest.main()
