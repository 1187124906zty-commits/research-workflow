import importlib.util
import json
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
    def make_repo(self, root, migrations=None):
        repo = Path(root) / "fixture-repo"
        (repo / "skills").mkdir(parents=True)
        (repo / "templates/agents").mkdir(parents=True)
        (repo / "templates/AGENTS.research.md").write_text(
            installer.BEGIN + "\nManaged.\n" + installer.END + "\n", encoding="utf-8")
        (repo / "templates/agents/rf_test.toml").write_text("name = 'test'\n", encoding="utf-8")
        for name in ("simulation-project-orchestrator", "simulation-evidence-preparation",
                     "simulation-tool-execution", "simulation-result-validation"):
            skill = repo / "skills" / name
            skill.mkdir()
            (skill / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")
        if migrations is not None:
            (repo / "templates/skill-migrations.json").write_text(
                json.dumps(migrations), encoding="utf-8")
        return repo

    def install_from(self, repo, **kwargs):
        previous = installer.REPO
        installer.REPO = repo
        try:
            return installer.install(**kwargs)
        finally:
            installer.REPO = previous

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

    def test_update_installs_four_skills_and_retires_only_allowlisted_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self.make_repo(root, {
                "simulation-project-orchestrator": ["references/old-mechanism.md"]
            })
            home = root / "home"
            installed = home / "skills/simulation-project-orchestrator"
            (installed / "references").mkdir(parents=True)
            retired = installed / "references/old-mechanism.md"
            retired.write_text("legacy mechanism\n", encoding="utf-8")
            custom = installed / "user-notes.md"
            custom.write_text("keep me\n", encoding="utf-8")

            self.install_from(repo, codex_home=home, update=True)

            for name in ("simulation-project-orchestrator", "simulation-evidence-preparation",
                         "simulation-tool-execution", "simulation-result-validation"):
                self.assertTrue((home / "skills" / name / "SKILL.md").is_file())
            backup = home / "researchflow-migration-backup/simulation-project-orchestrator/references/old-mechanism.md"
            self.assertEqual("legacy mechanism\n", backup.read_text(encoding="utf-8"))
            self.assertFalse(retired.exists())
            self.assertEqual("keep me\n", custom.read_text(encoding="utf-8"))

            # A second update neither recreates the retirement nor replaces its backup.
            self.install_from(repo, codex_home=home, update=True)
            self.assertEqual("legacy mechanism\n", backup.read_text(encoding="utf-8"))
            self.assertFalse(retired.exists())

    def test_without_update_existing_skill_and_retirement_are_untouched(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self.make_repo(root, {
                "simulation-project-orchestrator": ["references/old-mechanism.md"]
            })
            home = root / "home"
            retired = home / "skills/simulation-project-orchestrator/references/old-mechanism.md"
            retired.parent.mkdir(parents=True)
            retired.write_text("legacy\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                self.install_from(repo, codex_home=home)

            self.assertEqual("legacy\n", retired.read_text(encoding="utf-8"))
            self.assertFalse((home / "researchflow-migration-backup").exists())
            self.assertFalse((home / "AGENTS.md").exists())

    def test_invalid_migration_path_is_rejected_before_any_change(self):
        for invalid in ("../outside.md", str(Path.cwd().anchor + "outside.md"), "C:outside.md"):
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                repo = self.make_repo(root, {
                    "simulation-project-orchestrator": [invalid]
                })
                home = root / "home"

                with self.assertRaises(ValueError):
                    self.install_from(repo, codex_home=home, update=True)

                self.assertFalse(home.exists())

    def test_migration_directory_and_backup_conflict_fail_before_mutation(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self.make_repo(root, {
                "simulation-project-orchestrator": ["references/retired"]
            })
            home = root / "home"
            target = home / "skills/simulation-project-orchestrator/references/retired"
            target.mkdir(parents=True)

            with self.assertRaises(ValueError):
                self.install_from(repo, codex_home=home, update=True)
            self.assertTrue(target.is_dir())
            self.assertFalse((home / "AGENTS.md").exists())

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo = self.make_repo(root, {
                "simulation-project-orchestrator": ["references/old.md"]
            })
            home = root / "home"
            target = home / "skills/simulation-project-orchestrator/references/old.md"
            target.parent.mkdir(parents=True)
            target.write_text("current\n", encoding="utf-8")
            backup = home / "researchflow-migration-backup/simulation-project-orchestrator/references/old.md"
            backup.parent.mkdir(parents=True)
            backup.write_text("different history\n", encoding="utf-8")

            with self.assertRaises(ValueError):
                self.install_from(repo, codex_home=home, update=True)
            self.assertEqual("current\n", target.read_text(encoding="utf-8"))
            self.assertEqual("different history\n", backup.read_text(encoding="utf-8"))
            self.assertFalse((home / "AGENTS.md").exists())


if __name__ == "__main__":
    unittest.main()
