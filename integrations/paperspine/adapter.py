#!/usr/bin/env python3
"""PaperSpine file handoff and explicit public-host transport, using only stdlib.

The research state remains authoritative. This adapter neither executes a writer
nor approves science, invents Web decisions, or signs an independent review.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

PUBLIC_TOOLS = {
    "paperspine_open_task", "paperspine_get_task", "paperspine_list_task_events",
    "paperspine_bind_evidence", "paperspine_publish_artifact",
    "paperspine_commit_milestone",
}


class AdapterError(RuntimeError):
    pass


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def export_handoff(project_root: Path, output_dir: Path, research_task: str | None = None,
                   claim_ids: list[str] | None = None) -> dict[str, Any]:
    """Create a bounded writer packet; preserve claim meaning and evidence levels."""
    state_path = project_root.resolve() / ".researchflow/research-state.json"
    state = read_json(state_path)
    if state.get("schema_version") != 1 or not isinstance(state.get("revision"), int):
        raise AdapterError("Unsupported research state; use the runtime's actual schema")
    tasks = state.get("tasks", {})
    claims = state.get("claims", {})
    if research_task:
        if research_task not in tasks:
            raise AdapterError(f"Unknown research task: {research_task}")
        selected = tasks[research_task]
        selected_ids = list(selected["contract"].get("claim_ids", []))
    else:
        selected = None
        selected_ids = list(claims)
    if claim_ids:
        selected_ids = list(dict.fromkeys(claim_ids))
    if any(item not in claims for item in selected_ids):
        raise AdapterError("Unknown claim ID; never invent a claim to fill the outline")
    selected_claims = {item: copy.deepcopy(claims[item]) for item in selected_ids}
    relevant = {}
    for task_id, task in tasks.items():
        if task_id == research_task or set(task["contract"].get("claim_ids", [])) & set(selected_ids):
            relevant[task_id] = {
                "contract": copy.deepcopy(task["contract"]), "status": task.get("status"),
                "latest_attempt": copy.deepcopy(task.get("attempts", [])[-1:]),
                "latest_decision": copy.deepcopy(task.get("decisions", [])[-1:]),
                "no_progress_count": task.get("no_progress_count", 0),
            }
    packet = {
        "schema_version": "researchflow.paperspine-handoff/1",
        "authority": {"state_path": str(state_path), "project_revision": state["revision"],
                      "selection_source": "agent_export", "web_user_confirmation": False},
        "project": copy.deepcopy(state.get("project", {})),
        "research": copy.deepcopy(state.get("research", {})),
        "research_task_id": research_task, "claims": selected_claims, "tasks": relevant,
        "boundaries": [
            "Task acceptance is handoff acceptance, not hypothesis confirmation.",
            "Observation, numerical verification and physical validation remain distinct.",
            "Read referenced files/revisions before citing them; this packet is not evidence reading.",
            "Return missing evidence as a bounded proposal to the coordinator; do not launch an unlimited refinement loop.",
            "Counterevidence may narrow or change the paper argument; do not conceal it for venue fit.",
            "Independent manuscript review requires another actual agent/context and the actual draft/renders.",
        ],
    }
    output_dir = output_dir.resolve()
    if output_dir == project_root.resolve() / ".researchflow":
        raise AdapterError("Export to a handoff directory, not over the authoritative state directory")
    write_json(output_dir / "handoff.json", packet)
    lines = ["# PaperSpine 科研交接", "", f"研究问题：{packet['project'].get('question', '')}",
             f"研究用途：{packet['project'].get('purpose', '')}",
             f"目标期刊：{packet['project'].get('target_journal') or '待依据读者、主题和结果确定'}",
             f"状态版本：{state['revision']}；来源为 agent 导出，不能当作用户 Web 点击。", "",
             "先读 handoff.json 的研究理解和任务目的，再读本任务涉及的 claim 及其实际证据文件。",
             "PaperSpine 在探索期组织期刊读者、贡献和论证方案，在结果返回后修正结构、讨论和成稿。",
             "依照本项目约定选择必要方法；只加载当前任务需要的原始方法文件。", "",
             "| Claim | 当前判断 | 论断 |", "|---|---|---|"]
    for claim_id, claim in selected_claims.items():
        statement = str(claim.get("statement", "")).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {claim_id} | {claim.get('status', 'unknown')} | {statement} |")
    lines += ["", "证据不足时返回一个提案：哪个论断受影响、需要辨别什么、已有证据、最低可行试验或分析、",
              "预期输出与使用位置、预算和返回条件、能否通过收窄论断解决。由协调者决定下一步。",
              "不把期刊叙述习惯当作证据；不把数值误差的减小当作科研贡献；保留否定结果和边界。", "",
              "本导出不创建 PaperSpine Web task，也不调用 backend；上游 UI/host 可用性单独由 doctor 检测。", ""]
    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    return {"handoff": str(output_dir / "handoff.json"), "project_revision": state["revision"],
            "claims": selected_ids, "backend_called": False}


def _domain_error(value: Any) -> Any:
    if isinstance(value, dict):
        if value.get("error") or value.get("isError"):
            return value.get("error") or "MCP isError"
        for key in ("structuredContent", "result"):
            if key in value:
                found = _domain_error(value[key])
                if found:
                    return found
        for item in value.get("content", []):
            if isinstance(item, dict) and item.get("type") == "text":
                try:
                    found = _domain_error(json.loads(item.get("text", "")))
                except (ValueError, TypeError):
                    continue
                if found:
                    return found
    return None


def validate_call(tool: str, arguments: dict[str, Any], task_id: str) -> None:
    if tool not in PUBLIC_TOOLS:
        raise AdapterError("Tool outside adapter scope; configuration/decisions/review use their real upstream identity boundary")
    if not task_id.strip():
        raise AdapterError("An explicit task_id is required; latest task is never selected")
    target = arguments.get("request", arguments)
    if not isinstance(target, dict):
        raise AdapterError("Tool arguments must contain an object")
    payload = target.get("payload", {})
    if not isinstance(payload, dict):
        raise AdapterError("A mutation payload must be an object")
    for value in (arguments.get("task_id"), target.get("task_id"),
                  payload.get("requested_task_id")):
        if value is not None and value != task_id:
            raise AdapterError("Task mismatch; preserve the existing task binding")

    def inspect(value: Any) -> None:
        if isinstance(value, dict):
            if any(key in value for key in ("trusted_reviewer_id", "reviewer_id", "principal_id")):
                raise AdapterError("Identity is supplied by the real host/reviewer, never by a request")
            if value.get("source") == "web_user" or value.get("user_confirmed") is True:
                raise AdapterError("The adapter cannot manufacture a user Web confirmation")
            for item in value.values():
                inspect(item)
        elif isinstance(value, list):
            for item in value:
                inspect(item)
    inspect(arguments)


class HostClient:
    def __init__(self, skill_root: Path, profile_root: Path, python: str | None = None,
                 timeout: float = 45):
        self.skill_root = skill_root.resolve()
        self.profile_root = profile_root.resolve()
        self.entry = self.skill_root / "scripts/paperspine5_web.py"
        self.timeout = timeout
        self._schemas: dict[str, dict[str, Any]] = {}
        self.pointer = {}
        pointer = self.skill_root / "references/installed-suite.json"
        if pointer.is_file():
            self.pointer = read_json(pointer)
        suite = Path(self.pointer["suite_root"]) if self.pointer.get("suite_root") else None
        bundled = suite / "runtime_vendor/windows-py312/python.exe" if suite else None
        self.python = python or os.environ.get("PAPERSPINE5_PYTHON") or (
            str(bundled) if bundled and bundled.is_file() else sys.executable)

    def _run(self, command: list[str], stdin: str | None = None) -> Any:
        if not self.entry.is_file():
            raise AdapterError("Installed PaperSpine public CLI is missing")
        try:
            result = subprocess.run(
                [self.python, "-B", "-X", "utf8", str(self.entry), *command],
                input=stdin, capture_output=True, text=True, encoding="utf-8", errors="replace",
                timeout=self.timeout, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise AdapterError(f"Public CLI failed: {exc}; no automatic retry or task replacement") from exc
        if result.returncode != 0:
            detail = (result.stderr.strip() or result.stdout.strip())[-3000:]
            raise AdapterError(f"Public CLI exit {result.returncode}: {detail}")
        try:
            value = json.loads(result.stdout)
        except ValueError as exc:
            raise AdapterError("Public CLI did not return a complete JSON result") from exc
        failure = _domain_error(value)
        if failure:
            raise AdapterError(f"PaperSpine rejected request: {failure}")
        return value

    def schema(self, tool: str) -> dict[str, Any]:
        if tool not in PUBLIC_TOOLS:
            raise AdapterError("Tool outside adapter scope")
        if tool in self._schemas:
            return self._schemas[tool]
        value = self._run(["host", "tools", "--profile-root", str(self.profile_root), "--tool", tool])
        if not isinstance(value, dict) or value.get("name") != tool or "inputSchema" not in value:
            raise AdapterError("The live tool inventory did not return the requested schema")
        self._schemas[tool] = value
        return value

    def call(self, tool: str, arguments: dict[str, Any], task_id: str) -> Any:
        validate_call(tool, arguments, task_id)
        # Do not translate unknown schema versions or rewrite user/agent decisions.
        self.schema(tool)
        return self._run(["host", "call", "--profile-root", str(self.profile_root),
                          "--task-id", task_id, "--tool", tool, "--arguments-file", "-"],
                         json.dumps(arguments, ensure_ascii=False))

    def doctor(self) -> dict[str, Any]:
        result = {"product_version": self.pointer.get("product_version"),
                  "cli_present": self.entry.is_file(), "host_schema_verified": False,
                  "web_start_verified": False, "agent_started": False, "notes": []}
        if self.pointer.get("suite_root"):
            suite = Path(self.pointer["suite_root"]).resolve()
            if suite == self.profile_root or suite in self.profile_root.parents or self.profile_root in suite.parents:
                result["notes"].append(
                    "profile_product_ancestor_conflict: upstream web_launch rejects this layout; "
                    "do not move the task database or silently select another profile")
        config = next((p for p in (self.profile_root / "data/product-config.json",
                                  self.profile_root / "product-config.json") if p.is_file()), None)
        result["profile_binding_present"] = config is not None
        try:
            self.schema("paperspine_open_task")
            result["host_schema_verified"] = True
        except AdapterError as exc:
            result["notes"].append(str(exc))
        # Read-only status is distinct from tool/schema discovery and never launches Web.
        try:
            status = self._run(["status", "--profile-root", str(self.profile_root)])
            result["web_start_verified"] = status.get("status") == "READY"
        except AdapterError as exc:
            result["notes"].append(str(exc))
        return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    export = sub.add_parser("export")
    export.add_argument("--project", type=Path, required=True)
    export.add_argument("--output", type=Path, required=True)
    export.add_argument("--research-task")
    export.add_argument("--claim", action="append", default=[])
    for action in ("doctor", "call", "schema"):
        command = sub.add_parser(action)
        command.add_argument("--skill-root", type=Path, required=True)
        command.add_argument("--profile-root", type=Path, required=True)
        command.add_argument("--python")
        if action != "doctor":
            command.add_argument("--tool", choices=sorted(PUBLIC_TOOLS), required=True)
        if action == "call":
            command.add_argument("--task-id", required=True)
            command.add_argument("--arguments", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.action == "export":
            value = export_handoff(args.project, args.output, args.research_task, args.claim)
            print(json.dumps(value, ensure_ascii=False, indent=2))
            return 0
        client = HostClient(args.skill_root, args.profile_root, args.python)
        if args.action == "doctor":
            value = client.doctor()
        elif args.action == "schema":
            value = client.schema(args.tool)
        else:
            value = client.call(args.tool, read_json(args.arguments), args.task_id)
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return 0
    except (AdapterError, OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
