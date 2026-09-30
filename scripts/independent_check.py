"""Portable independent stdlib checks; generated projects stay under local-runs."""
from __future__ import annotations

import copy
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import tomllib
import unittest

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PYTHON = Path(sys.executable)
RUN = REPO / "local-runs" / "independent-check" / time.strftime("%Y%m%d-%H%M%S")
RUN.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, str(REPO / "src"))
from researchflow import runtime as rf


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


installer = module("review_installer", REPO / "scripts/install.py")
adapter = module("review_adapter", REPO / "integrations/paperspine/adapter.py")


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def run_command(command):
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": str(REPO / "src")}
    result = subprocess.run([str(PYTHON), "-B", "-X", "utf8", *map(str, command)],
                            cwd=REPO, env=env, capture_output=True, text=True,
                            encoding="utf-8", timeout=60)
    return {"command": list(map(str, command)), "returncode": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr}


class IndependentReview(unittest.TestCase):
    def setUp(self):
        names = unittest.defaultTestLoader.getTestCaseNames(type(self))
        self.root = RUN / f"{names.index(self._testMethodName) + 1:02d}"
        self.root.mkdir()

    def init(self, claims=("C1", "C2")):
        self.project = self.root / "study"
        rf.initialize(self.project, "Does B improve flux under these conditions?", {
            "claims": [{"id": cid, "statement": f"Bounded claim {cid}"} for cid in claims]})
        (self.project / "model.txt").write_text("declared equation and units v1\n", encoding="utf-8")

    def task(self, tid, claims=("C1",), **extra):
        value = {"id": tid, "role": "executor", "question": "Bound the relevant error.",
                 "purpose": "Determine whether the comparison survives uncertainty.",
                 "claim_ids": list(claims), "inputs": [{"path": "model.txt"}],
                 "outputs": [f"out/{tid}"], "acceptance": "Error small relative to stated effect.",
                 "budget": {"max_attempts": 2, "max_no_progress": 2}, **extra}
        return rf.task(self.project, value)

    def result(self, tid, attempt=1, kind="support", level="numerical_verification", claims=("C1",), changed=True, blockers=None):
        path = self.project / f"out/{tid}/evidence-{attempt}.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"Actual synthetic returned evidence {tid}, attempt {attempt}\n", encoding="utf-8")
        return {"attempt": attempt, "changed_understanding": changed, "reason": "Located result changes this bounded question.",
                "evidence": [{"path": path.relative_to(self.project).as_posix(), "level": level,
                              "kind": kind, "claim_ids": list(claims), "summary": "Synthetic numerical evidence, not experimental data."}],
                "blockers": blockers or []}

    def promote(self, tid, cid="C1", level="numerical_verification"):
        return rf.decide(self.project, tid, {"action": "accept", "reason": "Interpret returned evidence for declared scope.",
            "promotions": [{"claim_id": cid, "level": level, "evidence_indices": [0], "reason": "Located supporting evidence matches this level."}]})

    def test_install_preserves_rules_config_and_uses_override(self):
        home = self.root / ".codex"
        home.mkdir()
        original = "# User rules\nNever alter raw observations.\n"
        (home / "AGENTS.md").write_text(original, encoding="utf-8")
        (home / "AGENTS.override.md").write_text("# Effective local rules\nRespect previous authorization.\n", encoding="utf-8")
        (home / "config.toml").write_text('model = "existing-user-setting"\n', encoding="utf-8")
        before_config = (home / "config.toml").read_bytes()
        command = [REPO / "scripts/install.py", "--codex-home", home]
        first = run_command(command)
        write_json(self.root / "first-install.json", first)
        self.assertEqual(first["returncode"], 0, first)
        self.assertEqual((home / "AGENTS.md").read_text(encoding="utf-8"), original)
        rules = (home / "AGENTS.override.md").read_text(encoding="utf-8")
        self.assertIn("Respect previous authorization.", rules)
        self.assertEqual(rules.count(installer.BEGIN), 1)
        self.assertEqual((home / "config.toml").read_bytes(), before_config)
        second = run_command([*command, "--update"])
        write_json(self.root / "second-install.json", second)
        self.assertEqual(second["returncode"], 0, second)
        self.assertEqual((home / "AGENTS.override.md").read_text(encoding="utf-8"), rules)
        self.assertEqual(len(list((home / "agents").glob("rf_*.toml"))), 5)

    def test_install_conflict_and_malformed_markers_are_preflighted(self):
        home = self.root / ".codex"
        existing = home / "skills/research-workflow-governor"
        existing.mkdir(parents=True)
        sentinel = existing / "SKILL.md"
        sentinel.write_text("User-owned current skill", encoding="utf-8")
        with self.assertRaises(ValueError):
            installer.install(codex_home=home)
        self.assertEqual(sentinel.read_text(), "User-owned current skill")
        self.assertFalse((home / "AGENTS.md").exists())
        broken = self.root / "broken"
        broken.mkdir()
        (broken / "AGENTS.md").write_text(installer.BEGIN + "missing closing marker", encoding="utf-8")
        with self.assertRaises(ValueError):
            installer.install(codex_home=broken, update=True)
        self.assertFalse((broken / "skills").exists())

    def test_project_install_keeps_global_home_untouched(self):
        project = self.root / "project"
        project.mkdir()
        global_home = self.root / "global-home"
        global_home.mkdir()
        sentinel = global_home / "config.toml"
        sentinel.write_text("existing user configuration", encoding="utf-8")
        installer.install(codex_home=global_home, project=project)
        self.assertEqual([p.name for p in global_home.iterdir()], ["config.toml"])
        self.assertTrue((project / ".agents/skills/research-workflow-governor/SKILL.md").is_file())

    def test_accept_negative_result_does_not_support_hypothesis(self):
        self.init()
        self.task("negative")
        rf.record(self.project, "negative", self.result("negative", kind="negative", level="observation"))
        rf.decide(self.project, "negative", {"action": "accept", "reason": "Negative evidence answers the actual question."})
        context = rf.context(self.project)
        self.assertEqual(context["claims"]["C1"]["status"], "hypothesis")
        self.assertEqual(context["claims"]["C1"]["support"], {})
        self.assertTrue(rf.audit(self.project)["protocol_ok"])

    def test_wrong_level_missing_files_and_stale_inputs_reject_promotion(self):
        self.init()
        self.task("verification")
        rf.record(self.project, "verification", self.result("verification"))
        with self.assertRaises(rf.GovernanceError):
            self.promote("verification", level="physical_validation")
        (self.project / "model.txt").write_text("changed physics model v2\n", encoding="utf-8")
        with self.assertRaises(rf.GovernanceError):
            self.promote("verification")
        self.assertFalse(rf.audit(self.project)["protocol_ok"])
        self.task("missing", claims=("C2",))
        value = self.result("missing", claims=("C2",))
        (self.project / value["evidence"][0]["path"]).unlink()
        with self.assertRaises(rf.GovernanceError):
            rf.record(self.project, "missing", value)

    def test_return_boundary_needs_reasoned_extension(self):
        self.init()
        self.task("stalled")
        rf.record(self.project, "stalled", self.result("stalled", changed=False))
        rf.decide(self.project, "stalled", {"action": "continue", "reason": "One distinct follow-up within original budget."})
        rf.record(self.project, "stalled", self.result("stalled", attempt=2, changed=False))
        with self.assertRaises(rf.GovernanceError):
            rf.decide(self.project, "stalled", {"action": "continue", "reason": "Refine once more without useful rationale."})
        rf.decide(self.project, "stalled", {"action": "continue", "reason": "Test an alternative explanation.",
            "reassessment": {"reason": "Uncertainty could still reverse the weak comparison.",
                             "strategy_change": "Change from precision refinement to boundary-condition control.", "additional_attempts": 1}})
        self.assertEqual(rf.context(self.project, "stalled")["attempt_limit"], 3)

    def test_counterevidence_invalidates_dependency_but_preserves_unrelated_work(self):
        self.init(claims=("C1", "C2", "C3"))
        self.task("source")
        rf.record(self.project, "source", self.result("source"))
        self.promote("source")
        self.task("derived", claims=("C2",), depends_on=[{"task_id": "source", "claim_ids": ["C1"], "required_level": "numerical_verification"}])
        rf.record(self.project, "derived", self.result("derived", claims=("C2",)))
        self.promote("derived", cid="C2")
        self.task("unrelated", claims=("C3",))
        self.task("challenge")
        rf.record(self.project, "challenge", self.result("challenge", kind="counterevidence", level="observation"))
        context = rf.context(self.project)
        self.assertEqual(context["claims"]["C1"]["status"], "invalidated")
        self.assertEqual(context["claims"]["C2"]["status"], "invalidated")
        self.assertEqual(rf.context(self.project, "unrelated")["status"], "active")
        rf.record(self.project, "unrelated", self.result("unrelated", claims=("C3",)))
        self.promote("unrelated", cid="C3")
        self.assertEqual(rf.context(self.project)["claims"]["C3"]["status"], "supported")

    def test_blocker_cannot_be_cleared_by_same_result_or_old_artifact(self):
        self.init()
        self.task("repair")
        first = self.result("repair", blockers=[{"claim_ids": ["C1"], "kind": "units", "reason": "Length used as metres instead of millimetres."}])
        rf.record(self.project, "repair", first)
        resolution = {"claim_id": "C1", "challenge_id": "repair:1:blocker:0", "evidence_indices": [0], "reason": "Try to claim the same result corrects itself."}
        with self.assertRaises(rf.GovernanceError):
            rf.decide(self.project, "repair", {"action": "accept", "reason": "No actual correction.", "resolutions": [resolution]})
        rf.decide(self.project, "repair", {"action": "continue", "reason": "Perform a real unit correction."})
        second = copy.deepcopy(first)
        second.update(attempt=2, blockers=[])
        rf.record(self.project, "repair", second)
        with self.assertRaises(rf.GovernanceError):
            rf.decide(self.project, "repair", {"action": "accept", "reason": "Old artifact reused.", "resolutions": [resolution]})

    def test_pending_handoffs_and_write_scope_are_enforced(self):
        self.init()
        self.task("source")
        with self.assertRaises(rf.GovernanceError):
            self.task("overlap", outputs=["out/source/child"], writes=["out/source/child"])
        with self.assertRaises(rf.GovernanceError):
            self.task("state-writer", outputs=[".researchflow/worker.json"])
        rf.record(self.project, "source", self.result("source"))
        with self.assertRaises(rf.GovernanceError):
            self.task("dependent", claims=("C2",), depends_on=["source"])
        self.assertIn("unclosed_handoff", {risk["code"] for risk in rf.audit(self.project)["risks"]})

    def test_export_keeps_negative_claim_levels_and_authority(self):
        self.init()
        self.task("challenge")
        rf.record(self.project, "challenge", self.result("challenge", kind="counterevidence", level="observation"))
        rf.decide(self.project, "challenge", {"action": "accept", "reason": "Accept falsifying result; retire strong interpretation."})
        source = self.project / ".researchflow/research-state.json"
        before = source.read_bytes()
        output = self.root / "handoff"
        command = run_command([REPO / "integrations/paperspine/adapter.py", "export", "--project", self.project,
                               "--output", output, "--research-task", "challenge"])
        write_json(self.root / "export-cli.json", command)
        self.assertEqual(command["returncode"], 0, command)
        packet = json.loads((output / "handoff.json").read_text(encoding="utf-8"))
        self.assertEqual(source.read_bytes(), before)
        self.assertEqual(set(packet["claims"]), {"C1"})
        self.assertEqual(packet["claims"]["C1"]["status"], "invalidated")
        self.assertFalse(packet["authority"]["web_user_confirmation"])
        self.assertFalse(json.loads(command["stdout"])["backend_called"])
        self.assertEqual(packet["tasks"]["challenge"]["latest_attempt"][0]["evidence"][0]["kind"], "counterevidence")
        self.assertEqual(packet["tasks"]["challenge"]["latest_attempt"][0]["evidence"][0]["level"], "observation")
        with self.assertRaises(adapter.AdapterError):
            adapter.export_handoff(self.project, self.root / "unknown", claim_ids=["C999"])

    def test_adapter_identity_task_and_transport_boundaries(self):
        for args in ({"task_id": "wrong"}, {"request": {"task_id": "wrong"}},
                     {"request": {"payload": {"requested_task_id": "wrong"}}},
                     {"request": {"payload": {"source": "web_user"}}},
                     {"payload": {"nested": [{"trusted_reviewer_id": "author"}]}},
                     {"payload": {"user_confirmed": True}}):
            with self.subTest(arguments=args), self.assertRaises(adapter.AdapterError):
                adapter.validate_call("paperspine_get_task", args, "same-task")
        with self.assertRaises(adapter.AdapterError):
            adapter.validate_call("paperspine_submit_review", {}, "same-task")
        skill = self.root / "fake-skill"
        entry = skill / "scripts/paperspine5_web.py"
        entry.parent.mkdir(parents=True)
        entry.write_text("import json, sys\nargs = sys.argv[1:]\n"
                         "if args[:2] == ['host', 'tools']:\n print(json.dumps({'name': args[args.index('--tool')+1], 'inputSchema': {'type':'object'}}))\n"
                         "else:\n print(json.dumps({'structuredContent': {'error':'version-conflict'}}))\n", encoding="utf-8")
        client = adapter.HostClient(skill, self.root / "fake-profile", python=str(PYTHON))
        with self.assertRaisesRegex(adapter.AdapterError, "version-conflict"):
            client.call("paperspine_get_task", {}, "same-task")

    def test_real_cli_context_audit_and_example(self):
        project = self.root / "cli-study"
        config = write_json(self.root / "config.json", {"claims": [{"id": "C1", "statement": "Explicit synthetic assertion."}]})
        init = run_command(["-m", "researchflow", "init", project, "--question", "Independent CLI project", "--config", config])
        self.assertEqual(init["returncode"], 0, init)
        context = run_command(["-m", "researchflow", "context", project])
        self.assertEqual(json.loads(context["stdout"])["claims"]["C1"]["status"], "hypothesis")
        audit = run_command(["-m", "researchflow", "audit", project])
        self.assertEqual(audit["returncode"], 0, audit)
        self.assertEqual(json.loads(audit["stdout"])["scientific_validity"], "not_judged")
        example = run_command([REPO / "examples/steady_diffusion/run.py", "--project", self.root / "numeric-example"])
        write_json(self.root / "cli-transcript.json", {"init": init, "context": context, "audit": audit, "example": example})
        self.assertEqual(example["returncode"], 0, example)
        value = json.loads(example["stdout"])
        self.assertTrue(value["protocol_ok"])
        self.assertAlmostEqual(value["summary"]["effect_fraction"], 1 - 1 / (2.718281828459045 - 1), delta=0.0001)
        self.assertEqual(value["summary"]["physical_validation"], "not performed")
        note = Path(value["manuscript"]).read_text(encoding="utf-8")
        self.assertIn("does not call an LLM, live PaperSpine", note)
        self.assertIn("## Interpretation and limits", note)

    def test_complete_cli_handoff_and_actor_rejection(self):
        project = self.root / "cli-project"
        config = write_json(self.root / "config.json", {"claims": [{"id": "C1", "statement": "Synthetic prediction."}]})
        commands = []
        def cli(*args, code=0):
            value = run_command(["-m", "researchflow", *args])
            commands.append(value)
            self.assertEqual(value["returncode"], code, value)
            return json.loads(value["stdout"] or value["stderr"])
        cli("init", project, "--question", "CLI handoff", "--config", config)
        model = project / "model.txt"
        model.write_text("declared synthetic model", encoding="utf-8")
        snapshot = cli("snapshot", project, "model.txt")
        plan = write_json(self.root / "plan.json", {"reason": "Evidence is model-internal only.", "stage": "paper_formation", "next_decision": "Can the bounded note use this result?"})
        cli("--actor", "worker", "plan", project, plan, code=1)
        cli("plan", project, plan)
        contract = write_json(self.root / "contract.json", {
            "id": "pilot", "role": "executor", "question": "Return one synthetic observation.",
            "purpose": "Exercise truthful CLI handoff.", "claim_ids": ["C1"], "inputs": snapshot,
            "outputs": ["out/result.txt"], "acceptance": "Artifact records its actual evidence level.",
            "budget": {"max_attempts": 1, "max_no_progress": 1}})
        cli("task", project, contract)
        raw = project / "out/result.txt"
        raw.parent.mkdir()
        raw.write_text("No experimental validation is available.", encoding="utf-8")
        result = write_json(self.root / "result.json", {
            "attempt": 1, "changed_understanding": True, "reason": "Know the limit of the available evidence.",
            "evidence": [{"path": "out/result.txt", "level": "observation", "kind": "negative", "claim_ids": ["C1"], "summary": "A useful synthetic negative result."}], "blockers": []})
        cli("record", project, "pilot", result)
        pending = cli("audit", project, code=2)
        self.assertIn("unclosed_handoff", {risk["code"] for risk in pending["risks"]})
        decision = write_json(self.root / "decision.json", {"action": "accept", "reason": "Receive the negative answer without supporting the hypothesis."})
        cli("decide", project, "pilot", decision)
        context = cli("context", project, "--task", "pilot")
        self.assertEqual(context["status"], "accepted")
        self.assertEqual(context["claims"]["C1"]["status"], "hypothesis")
        self.assertTrue(cli("audit", project)["protocol_ok"])
        write_json(self.root / "complete-cli-transcript.json", commands)

    def test_skill_links_roles_and_numerical_oracle(self):
        for skill in (REPO / "skills").iterdir():
            if not skill.is_dir():
                continue
            source = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
            self.assertTrue(source.startswith("---\n"))
            frontmatter = source.split("---", 2)[1]
            self.assertIn(f"name: {skill.name}", frontmatter)
            self.assertIn("description:", frontmatter)
            import re
            for target in re.findall(r"\]\(([^)]+)\)", source):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((skill / target.split("#", 1)[0]).exists(), f"Broken skill link: {target}")
        for role in (REPO / "templates/agents").glob("rf_*.toml"):
            data = tomllib.loads(role.read_text(encoding="utf-8"))
            self.assertTrue(data["developer_instructions"].strip())
            self.assertNotIn("model", data)
        example = module("review_diffusion", REPO / "examples/steady_diffusion/run.py")
        evidence = []
        for alpha in (-1.0, -0.2, 0.0, 0.2, 1.0):
            values = [example.solve(n, alpha) for n in (8, 16, 32)]
            for value in values:
                n = value["n"]
                q_discrete = 1e-9 * n / sum(math.exp(-alpha * (i + 0.5) / n) for i in range(n))
                self.assertAlmostEqual(value["flux_m_per_s"] / q_discrete, 1.0, places=11)
                self.assertTrue(value["bounds_ok"])
                self.assertLess(value["relative_flux_spread"], 1e-10)
                self.assertTrue(all(a >= b for a, b in zip(value["concentration"], value["concentration"][1:])))
            if alpha != 0:
                self.assertAlmostEqual(values[0]["relative_flux_error"] / values[1]["relative_flux_error"], 4.0, delta=0.01)
                self.assertAlmostEqual(values[1]["relative_flux_error"] / values[2]["relative_flux_error"], 4.0, delta=0.01)
            evidence.append({"alpha": alpha, "flux_errors": [r["relative_flux_error"] for r in values]})
        write_json(self.root / "numerical-oracle.json", evidence)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(IndependentReview)
    with (RUN / "unittest-output.txt").open("w", encoding="utf-8") as stream:
        outcome = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    summary = {"run_directory": str(RUN), "tests_run": outcome.testsRun,
               "failures": len(outcome.failures), "errors": len(outcome.errors),
               "successful": outcome.wasSuccessful(), "python": sys.version}
    write_json(RUN / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print((RUN / "unittest-output.txt").read_text(encoding="utf-8"))
    sys.exit(0 if outcome.wasSuccessful() else 1)
