"""Evidence-writing CLI regression checks; these do not score scientific prose."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from researchflow import GovernanceError, audit, context, decide, task


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evidence_writing_demo", REPO / "examples/evidence-writing/run.py")
DEMO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DEMO)


class EvidenceWritingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "demo"
        self.summary = DEMO.run(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_cli_editorial_acceptance_does_not_promote_validation(self):
        self.assertFalse(self.summary["pending_audit_protocol_ok"])
        self.assertTrue(self.summary["final_audit_protocol_ok"])
        claims = self.summary["claims"]
        self.assertEqual(claims["C_MATCH"], {"status": "supported", "support_levels": ["observation"]})
        self.assertEqual(claims["C_MECHANISM"]["status"], "narrowed")
        self.assertEqual(claims["C_EDIT"], {"status": "hypothesis", "support_levels": []})
        self.assertEqual(self.summary["scientific_validation"], "not performed")
        commands = json.loads((self.root / "cli-transcript.json").read_text(encoding="utf-8"))["commands"]
        self.assertEqual({item["arguments"][0] for item in commands},
                         {"init", "task", "record", "decide", "context", "audit"})
        self.assertEqual([item["exit_code"] for item in commands if item["arguments"][0] == "audit"], [2, 0])

    def test_editorial_trace_cannot_promote_physical_validation(self):
        before = context(self.root)["revision"]
        with self.assertRaises(GovernanceError):
            decide(self.root, "WRITE", {"action": "accept", "reason": "Try a stronger evidence level",
                   "promotions": [{"claim_id": "C_EDIT", "level": "physical_validation",
                                   "evidence_indices": [0], "reason": "A fluent paragraph is insufficient"}]})
        self.assertEqual(context(self.root)["revision"], before)

    def test_changed_observation_blocks_downstream_evidence_use(self):
        (self.root / "fixture.json").write_text('{"changed": true}', encoding="utf-8")
        self.assertFalse(audit(self.root)["protocol_ok"])
        with self.assertRaises(GovernanceError):
            task(self.root, {"id": "NEXT", "role": "writer", "question": "Can we reuse the old comparison?",
                            "purpose": "Catch invalidated support at a consequential handoff", "claim_ids": ["C_EDIT"],
                            "inputs": [], "outputs": ["results/NEXT/"], "acceptance": ["Fresh upstream support"],
                            "budget": {"max_attempts": 1, "max_no_progress": 1},
                            "depends_on": [{"task_id": "REVIEW", "claim_ids": ["C_MATCH"],
                                            "required_level": "observation", "affects_claim_ids": ["C_EDIT"]}]})

    def test_existing_state_is_preserved_on_rerun(self):
        before = context(self.root)["revision"]
        with self.assertRaises(ValueError):
            DEMO.run(self.root)
        self.assertEqual(context(self.root)["revision"], before)


if __name__ == "__main__":
    unittest.main()
