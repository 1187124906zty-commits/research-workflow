"""Install owned skills, role charters and an idempotent AGENTS entry.

No config.toml edits, permission changes or PaperSpine product writes.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]
BEGIN, END = "<!-- researchflow:begin -->", "<!-- researchflow:end -->"
MIGRATIONS = "skill-migrations.json"


def native_path(path: Path) -> Path:
    """Use the Windows extended namespace for IO without changing shown paths."""
    if os.name != "nt":
        return path
    text = str(path.absolute())
    if text.startswith("\\\\?\\"):
        return Path(text)
    if text.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + text[2:])
    return Path("\\\\?\\" + text)


def merge_rules(existing: str, block: str) -> str:
    """Preserve user instructions; reject ambiguous or broken owned blocks."""
    starts, ends = existing.count(BEGIN), existing.count(END)
    if starts != ends or starts > 1:
        raise ValueError("Malformed ResearchFlow block: repair the markers before installing")
    if starts:
        start, end = existing.index(BEGIN), existing.index(END) + len(END)
        if end < start:
            raise ValueError("ResearchFlow markers are out of order")
        return existing[:start] + block.strip() + existing[end:]
    return existing.rstrip() + ("\n\n" if existing.strip() else "") + block.strip() + "\n"


def load_skill_migrations() -> dict[str, tuple[Path, ...]]:
    """Load and validate the explicit retired-file allowlist."""
    manifest = REPO / "templates" / MIGRATIONS
    if not manifest.exists():
        return {}
    try:
        raw = json.loads(manifest.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError(f"Invalid {MIGRATIONS}: {exc}") from exc
    if not isinstance(raw, dict):
        raise ValueError(f"Invalid {MIGRATIONS}: expected an object")
    migrations: dict[str, tuple[Path, ...]] = {}
    for skill_name, entries in raw.items():
        skill_path = Path(skill_name) if isinstance(skill_name, str) else Path(".")
        if (not isinstance(skill_name, str) or not skill_name
                or skill_path.is_absolute() or len(skill_path.parts) != 1
                or skill_name in (".", "..")):
            raise ValueError(f"Invalid skill name in {MIGRATIONS}: {skill_name!r}")
        if not isinstance(entries, list):
            raise ValueError(f"Invalid migration list for {skill_name}")
        paths: list[Path] = []
        for entry in entries:
            relative = Path(entry) if isinstance(entry, str) else Path(".")
            if (not isinstance(entry, str) or not entry or relative.is_absolute()
                    or relative.drive or relative.anchor
                    or ".." in relative.parts or relative == Path(".")):
                raise ValueError(f"Invalid migration path for {skill_name}: {entry!r}")
            paths.append(relative)
        migrations[skill_name] = tuple(paths)
    return migrations


def migration_candidates(skills_root: Path, migrations: dict[str, tuple[Path, ...]]) -> list[tuple[Path, Path]]:
    """Preflight retired files and backup conflicts without changing anything."""
    backup_root = skills_root.parent / "researchflow-migration-backup"
    candidates: list[tuple[Path, Path]] = []
    for skill_name, entries in migrations.items():
        target_root = skills_root / skill_name
        skill_backup_root = backup_root / skill_name
        for relative in entries:
            source = REPO / "skills" / skill_name / relative
            target = target_root / relative
            backup = skill_backup_root / relative
            if (not target.resolve().is_relative_to(target_root.resolve())
                    or not backup.resolve().is_relative_to(skill_backup_root.resolve())):
                raise ValueError(f"Migration path resolves outside its root: {skill_name}/{relative}")
            if native_path(source).is_dir() or native_path(target).is_dir():
                raise ValueError(f"Migration entry must name a file: {skill_name}/{relative}")
            if native_path(source).exists() or not native_path(target).exists():
                continue
            if not native_path(target).is_file():
                raise ValueError(f"Migration entry must name a file: {skill_name}/{relative}")
            if native_path(backup).exists():
                if not native_path(backup).is_file():
                    raise ValueError(f"Migration backup is not a file: {backup}")
                if native_path(backup).read_bytes() != native_path(target).read_bytes():
                    raise ValueError(f"Migration backup conflict: {backup}")
            candidates.append((target, backup))
    return candidates


def install(*, codex_home: Path, project: Path | None = None,
            skill_layout: str = "codex", update: bool = False) -> list[str]:
    codex_home = codex_home.expanduser().resolve()
    if project is not None:
        project = project.expanduser().resolve()
        if not project.is_dir():
            raise ValueError("Project must be an existing directory")
        skills_root = project / ".agents" / "skills"
        roles_root = project / ".codex" / "agents"
        rules = project / "AGENTS.md"
        override = project / "AGENTS.override.md"
    else:
        skills_root = (codex_home / "skills" if skill_layout == "codex"
                       else codex_home.parent / ".agents" / "skills")
        roles_root = codex_home / "agents"
        rules = codex_home / "AGENTS.md"
        override = codex_home / "AGENTS.override.md"
    if native_path(override).exists() and native_path(override).read_text(encoding="utf-8-sig").strip():
        # Codex chooses override in preference to AGENTS; put the entry where loaded.
        rules = override
    block = (REPO / "templates" / "AGENTS.research.md").read_text(encoding="utf-8")
    old = native_path(rules).read_text(encoding="utf-8-sig") if native_path(rules).exists() else ""
    merged = merge_rules(old, block)
    migrations = load_skill_migrations()
    skills = list((REPO / "skills").iterdir())
    role_files = list((REPO / "templates" / "agents").glob("rf_*.toml"))
    # Preflight all conflicts before any mutation.
    for source in skills:
        if source.is_dir() and native_path(skills_root / source.name).exists() and not update:
            raise ValueError(f"Existing skill {source.name}; use --update for an authorized update")
        if source.is_dir() and source.resolve() == (skills_root / source.name).resolve():
            raise ValueError("Install destination must be separate from source")
    for source in role_files:
        target = roles_root / source.name
        if native_path(target).exists() and native_path(target).read_bytes() != source.read_bytes() and not update:
            raise ValueError(f"Existing role {target.name}; use --update to replace this role")
    retirements = migration_candidates(skills_root, migrations) if update else []
    # Preserve every explicitly retired file before updating its owning skill.
    for target, backup in retirements:
        if not native_path(backup).exists():
            native_path(backup.parent).mkdir(parents=True, exist_ok=True)
            shutil.copyfile(native_path(target), native_path(backup))
    written = []
    for source in skills:
        if source.is_dir():
            target = skills_root / source.name
            shutil.copytree(source, native_path(target), dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            written.append(str(target))
    for target, _backup in retirements:
        native_path(target).unlink()
    native_path(roles_root).mkdir(parents=True, exist_ok=True)
    for source in role_files:
        target = roles_root / source.name
        shutil.copyfile(source, native_path(target))
        written.append(str(target))
    native_path(rules.parent).mkdir(parents=True, exist_ok=True)
    tmp = rules.with_name(rules.name + ".researchflow-tmp")
    native_path(tmp).write_text(merged, encoding="utf-8", newline="\n")
    os.replace(native_path(tmp), native_path(rules))
    written.append(str(rules))
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path,
                        default=Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))))
    parser.add_argument("--project", type=Path, help="Install scoped rules/roles and .agents/skills")
    parser.add_argument("--skill-layout", choices=("codex", "agents"), default="codex",
                        help="User discovery: desktop compatibility or current official layout")
    parser.add_argument("--update", action="store_true", help="Update existing owned skills/roles")
    args = parser.parse_args()
    try:
        for path in install(codex_home=args.codex_home, project=args.project,
                            skill_layout=args.skill_layout, update=args.update):
            print(path)
    except (OSError, ValueError) as exc:
        print(f"Installation failed: {exc}", file=sys.stderr)
        return 2
    print("Skills and role charters installed. Start a new Codex run to reload instructions.")
    print("Install the runtime separately: python -m pip install -e <repository-path>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
