"""Install owned skills, role charters and an idempotent AGENTS entry.

No config.toml edits, permission changes or PaperSpine product writes.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]
BEGIN, END = "<!-- researchflow:begin -->", "<!-- researchflow:end -->"


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
    skills = list((REPO / "skills").iterdir())
    role_files = list((REPO / "templates" / "agents").glob("rf_*.toml"))
    # Preflight all conflicts before any mutation.
    for source in skills:
        if source.is_dir() and native_path(skills_root / source.name).exists() and not update:
            raise ValueError(f"Existing skill {source.name}; use --update for an authorized update")
    for source in role_files:
        target = roles_root / source.name
        if native_path(target).exists() and native_path(target).read_bytes() != source.read_bytes() and not update:
            raise ValueError(f"Existing role {target.name}; use --update to replace this role")
    written = []
    for source in skills:
        if source.is_dir():
            target = skills_root / source.name
            if source.resolve() == target.resolve():
                raise ValueError("Install destination must be separate from source")
            shutil.copytree(source, native_path(target), dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            written.append(str(target))
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
