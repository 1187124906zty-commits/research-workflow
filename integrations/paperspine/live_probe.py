#!/usr/bin/env python3
"""Opt-in integration probe in a new isolated temporary profile, never user tasks.

Starts a hidden loopback Web, opens one explicitly synthetic task, reads it,
binds a synthetic file reference, verifies it, and stops only that owned Web.
No configuration confirmation, independent-review signature or paper is made.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
import uuid

from adapter import AdapterError, HostClient, write_json


def projection(value):
    if isinstance(value, dict):
        if isinstance(value.get("projection"), dict):
            return value["projection"]
        if "task_version" in value:
            return value
        for key in ("structuredContent", "result"):
            if key in value:
                result = projection(value[key])
                if result:
                    return result
        for item in value.get("content", []):
            if item.get("type") == "text":
                try:
                    result = projection(json.loads(item.get("text", "")))
                except ValueError:
                    continue
                if result:
                    return result
    return None


def probe(skill_root: Path, python: str | None = None) -> dict:
    report = {"fixture": "synthetic protocol test only", "isolated_profile": True,
              "user_tasks_modified": False, "web_launch": False, "open_task": False,
              "get_task": False, "bind_evidence_roundtrip": False,
              "scientific_validation": False, "web_configuration_tested": False,
              "independent_review_tested": False, "cleanup": False, "notes": []}
    with tempfile.TemporaryDirectory(prefix="researchflow-paperspine-probe-", ignore_cleanup_errors=True) as temp:
        profile = Path(temp) / "profile"
        client = HostClient(skill_root, profile, python)
        task_id = "rf-probe-" + uuid.uuid4().hex[:16]
        owned_pid = None
        try:
            launch = client._run(["launch", "--profile-root", str(profile), "--no-open", "--wait-seconds", "15"])
            if launch.get("status") != "READY" or launch.get("browser_opened") or launch.get("scientific_agent_started"):
                raise AdapterError("Unexpected launch identity/result")
            owned_pid = launch.get("process_id")
            if not isinstance(owned_pid, int) or launch.get("profile_root") != str(profile.resolve()):
                raise AdapterError("Cannot verify this probe's owned Web process")
            report["web_launch"] = True
            report["product_version"] = client.pointer.get("product_version")
            opened = client.call("paperspine_open_task", {"request": {
                "schema_version": "1.1", "task_id": task_id,
                "command_id": "open-synthetic-probe", "expected_version": 0,
                "payload": {"mode": "open", "requested_task_id": task_id,
                            "title": "Researchflow adapter synthetic protocol probe",
                            "description": "Test local transport identity and reference roundtrip; no scientific finding or paper."},
            }}, task_id)
            current = projection(opened)
            if not current or current.get("task_id") != task_id:
                raise AdapterError("Open did not return the requested task identity")
            report["open_task"] = True
            current = projection(client.call("paperspine_get_task", {}, task_id))
            if not current or current.get("task_id") != task_id:
                raise AdapterError("Read did not preserve the task identity")
            report["get_task"] = True
            workspace = Path(current["workspace_root"])
            evidence = workspace / "paper/synthetic-transport-fixture.csv"
            evidence.parent.mkdir(parents=True, exist_ok=True)
            evidence.write_text("x,y\n0,0\n1,1\n", encoding="utf-8")
            client.call("paperspine_bind_evidence", {"request": {
                "schema_version": "1.1", "task_id": task_id,
                "command_id": "bind-synthetic-fixture", "expected_version": current["task_version"],
                "payload": {"claim_id": "synthetic-fixture-claim", "evidence_id": "synthetic-fixture-file",
                            "relation": "limits", "locator": "paper/synthetic-transport-fixture.csv:2"},
            }}, task_id)
            current = projection(client.call("paperspine_get_task", {}, task_id))
            expected = {"claim_id": "synthetic-fixture-claim", "evidence_id": "synthetic-fixture-file", "relation": "limits"}
            links = current.get("evidence_links", []) if current else []
            report["bind_evidence_roundtrip"] = any(all(link.get(k) == v for k, v in expected.items()) for link in links)
            if not report["bind_evidence_roundtrip"]:
                raise AdapterError("Read-back did not contain the bound evidence relation")
            report["locator_preserved_in_projection"] = any(
                link.get("locator") == "paper/synthetic-transport-fixture.csv:2" for link in links)
            report["notes"].append("Evidence links are reference metadata, not source reading or scientific support verification.")
        except (AdapterError, KeyError, OSError, ValueError) as exc:
            # The saved report is shareable: remove local temporary path strings.
            report["notes"].append(str(exc).replace(str(Path(temp)), "<isolated-probe>"))
        finally:
            # Startup may have launched a child before returning an error. Recover
            # its identity only from this newly created probe's own state files.
            if owned_pid is None:
                for filename in ("public-workspace.json", "public-starting.json"):
                    state = profile / ".paperspine5-web" / filename
                    if not state.is_file():
                        continue
                    saved = json.loads(state.read_text(encoding="utf-8"))
                    user_root = saved.get("binding", {}).get("user_data_root")
                    if user_root and profile.resolve() in Path(user_root).resolve().parents:
                        owned_pid = saved.get("process_id")
                        break
            if owned_pid:
                owned = any(
                    path.is_file() and json.loads(path.read_text(encoding="utf-8")).get("process_id") == owned_pid
                    for path in (profile / ".paperspine5-web/public-workspace.json",
                                 profile / ".paperspine5-web/public-starting.json"))
                if owned:
                    if os.name == "nt":
                        stopped = subprocess.run(["taskkill", "/PID", str(owned_pid), "/F"],
                                                 capture_output=True,
                                                 creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                        report["cleanup"] = stopped.returncode == 0
                    else:
                        os.kill(owned_pid, signal.SIGTERM)
                        report["cleanup"] = True
            elif not report["web_launch"]:
                report["cleanup"] = True
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, required=True)
    parser.add_argument("--python")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = probe(args.skill_root, args.python)
    if args.report:
        write_json(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(report[k] for k in ("web_launch", "open_task", "get_task", "bind_evidence_roundtrip", "cleanup")) else 1


if __name__ == "__main__":
    raise SystemExit(main())
