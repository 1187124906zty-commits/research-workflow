import importlib.util
import os
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("researchflow_install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    @unittest.skipUnless(os.name == "nt", "Windows extended path behavior")
    def test_install_handles_long_windows_skill_paths(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / ("research-" + "x" * 145)
            project.mkdir()
            try:
                installer.install(codex_home=Path(td) / "unused", project=project)
                target = project / ".agents/skills/simulation-project-orchestrator/references/scientific-dialogue-message.schema.json"
                self.assertGreater(len(str(target)), 260)
                self.assertTrue(installer.native_path(target).is_file())
            finally:
                # TemporaryDirectory's ordinary Windows path cleanup also needs
                # the extended namespace. Delete only this named test child.
                self.assertTrue(project.resolve().is_relative_to(Path(td).resolve()))
                shutil.rmtree(installer.native_path(project))

    def test_preserves_rules_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            home = Path(td) / ".codex"
            home.mkdir()
            rules = home / "AGENTS.md"
            rules.write_text("User research preference.\n", encoding="utf-8")
            installer.install(codex_home=home)
            first = rules.read_text(encoding="utf-8")
            installer.install(codex_home=home, update=True)
            self.assertEqual(first, rules.read_text(encoding="utf-8"))
            self.assertTrue(first.startswith("User research preference."))
            self.assertEqual(first.count(installer.BEGIN), 1)
            self.assertTrue((home / "skills/research-workflow-governor/SKILL.md").is_file())
            self.assertTrue((home / "agents/rf_evidence.toml").is_file())

    def test_active_override_gets_rule(self):
        with tempfile.TemporaryDirectory() as td:
            project = Path(td)
            (project / "AGENTS.override.md").write_text("Active override.\n", encoding="utf-8")
            installer.install(codex_home=project / "unused", project=project)
            self.assertIn(installer.BEGIN, (project / "AGENTS.override.md").read_text())
            self.assertFalse((project / "AGENTS.md").exists())
            self.assertTrue((project / ".agents/skills/research-workflow-governor").exists())

    def test_conflicts_fail_before_mutation(self):
        with tempfile.TemporaryDirectory() as td:
            home = Path(td)
            (home / "skills/research-workflow-governor").mkdir(parents=True)
            with self.assertRaises(ValueError):
                installer.install(codex_home=home)
            self.assertFalse((home / "AGENTS.md").exists())

    def test_broken_marker_preserves_existing(self):
        with self.assertRaises(ValueError):
            installer.merge_rules("user\n" + installer.BEGIN, "new")
        with self.assertRaises(ValueError):
            installer.merge_rules(installer.END + "\n" + installer.BEGIN, "new")


if __name__ == "__main__":
    unittest.main()
