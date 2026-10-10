#!/usr/bin/env python3
"""Audit the structure and open obligations of a scientific-dialogue JSONL ledger.

The audit is deliberately narrower than scientific review: it proves that
requests, responses and requester dispositions are linked and visible.  It
does not decide whether the cited evidence is true or sufficient for a Gate.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover
    raise SystemExit("jsonschema is required to audit dialogue messages") from exc


REQUEST_TYPES = {"QUESTION", "COUNTER_QUESTION", "RUN_REQUEST"}
RESPONSE_TYPES = {"RESPONSE", "RUN_RESPONSE"}
FOLLOWUP_TYPES = {"COUNTER_QUESTION", "RUN_REQUEST", "CLOSURE"}
ALLOWED_PREDECESSOR_TYPES = {
    "QUESTION": set(),
    "RUN_REQUEST": {"RESPONSE", "RUN_RESPONSE"},
    "RESPONSE": {"QUESTION", "COUNTER_QUESTION"},
    "RUN_RESPONSE": {"RUN_REQUEST"},
    "COUNTER_QUESTION": {"RESPONSE", "RUN_RESPONSE", "CLOSURE"},
    "CLOSURE": {"RESPONSE", "RUN_RESPONSE"},
}
NONBLOCKING_CLOSURES = {
    "ANSWERED_BY_SOURCE",
    "ANSWERED_BY_REANALYSIS",
    "ANSWERED_BY_DISCRIMINATING_RUN",
    "CORRECTED_CANDIDATE",
    "SCOPED_LIMITATION",
}
SUCCESS_CLOSURES = {
    "ANSWERED_BY_SOURCE",
    "ANSWERED_BY_REANALYSIS",
    "ANSWERED_BY_DISCRIMINATING_RUN",
    "CORRECTED_CANDIDATE",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--fail-open-obligations",
        action="store_true",
        help="return non-zero when requests, requester dispositions, or stop-lines remain open",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict]:
    messages: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at {path}:{line_number}: {exc}") from exc
        message["_ledger_line"] = line_number
        messages.append(message)
    return messages


def audit(messages: list[dict], schema: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )

    identifiers: dict[str, dict] = {}
    children: dict[str, list[dict]] = defaultdict(list)
    threads: dict[str, list[dict]] = defaultdict(list)

    for message in messages:
        clean = {key: value for key, value in message.items() if key != "_ledger_line"}
        for problem in validator.iter_errors(clean):
            errors.append(
                f"line {message['_ledger_line']} schema: {problem.json_path}: {problem.message}"
            )
        message_id = message.get("message_id")
        if message_id in identifiers:
            errors.append(f"duplicate message_id: {message_id}")
        else:
            identifiers[message_id] = message
        threads[message.get("thread_id", "<missing>")].append(message)

    for message in messages:
        predecessor_id = message.get("predecessor_message_id")
        if predecessor_id is None:
            if message.get("message_type") not in {"QUESTION", "RUN_REQUEST"}:
                errors.append(
                    f"{message.get('message_id')} illegally starts with {message.get('message_type')}"
                )
            continue
        predecessor = identifiers.get(predecessor_id)
        if predecessor is None:
            errors.append(f"{message.get('message_id')} has unknown predecessor {predecessor_id}")
            continue
        if predecessor.get("_ledger_line", 0) >= message.get("_ledger_line", 0):
            errors.append(
                f"{message.get('message_id')} predecessor {predecessor_id} "
                "does not precede it in append order"
            )
        children[predecessor_id].append(message)
        if predecessor.get("message_type") not in ALLOWED_PREDECESSOR_TYPES.get(
            message.get("message_type"), set()
        ):
            errors.append(
                f"illegal transition {predecessor.get('message_type')} -> "
                f"{message.get('message_type')} at {message.get('message_id')}"
            )
        is_reopen = (
            message.get("message_type") == "COUNTER_QUESTION"
            and predecessor.get("message_type") == "CLOSURE"
        )
        if is_reopen:
            if message.get("reopens_closure_id") != predecessor_id:
                errors.append(
                    f"{message.get('message_id')} must set reopens_closure_id to {predecessor_id}"
                )
            if message.get("sender_role") != predecessor.get("sender_role"):
                errors.append(
                    f"{message.get('message_id')} reopen sender is not the original requester"
                )
        elif message.get("reopens_closure_id") is not None:
            errors.append(
                f"{message.get('message_id')} sets reopens_closure_id outside CLOSURE -> COUNTER_QUESTION"
            )
        for field in ("thread_id", "project_id", "candidate_revision"):
            if message.get(field) != predecessor.get(field):
                errors.append(
                    f"{message.get('message_id')} changes {field} from predecessor {predecessor_id}"
                )
        try:
            previous_time = datetime.fromisoformat(
                predecessor["timestamp"].replace("Z", "+00:00")
            )
            current_time = datetime.fromisoformat(message["timestamp"].replace("Z", "+00:00"))
            if current_time < previous_time:
                errors.append(f"{message.get('message_id')} timestamp precedes {predecessor_id}")
        except (KeyError, TypeError, ValueError):
            pass

        if message.get("message_type") in RESPONSE_TYPES | {"COUNTER_QUESTION", "CLOSURE"} and not is_reopen:
            if message.get("sender_role") not in predecessor.get("receiver_roles", []):
                errors.append(
                    f"{message.get('message_id')} sender was not a receiver of {predecessor_id}"
                )
            if predecessor.get("sender_role") not in message.get("receiver_roles", []):
                errors.append(
                    f"{message.get('message_id')} does not route back to {predecessor_id} sender"
                )

        if message.get("message_type") == "CLOSURE":
            closure_kind = message.get("closure_kind")
            predecessor_status = predecessor.get("status")
            if closure_kind in SUCCESS_CLOSURES and predecessor_status != "ANSWERED":
                errors.append(
                    f"{message.get('message_id')} {closure_kind} cannot close "
                    f"{predecessor_status} response {predecessor_id}"
                )

    # A thread obligation is rooted in the initial request.  All messages retain
    # the complete set; narrowing is recorded by a SCOPED_LIMITATION closure and
    # continued in a separate thread rather than silently deleting obligations.
    for thread_id, items in threads.items():
        roots = [item for item in items if item.get("predecessor_message_id") is None]
        if len(roots) == 1:
            root = roots[0]
            for item in items:
                for field in ("affected_claims", "affected_gates"):
                    if set(item.get(field, [])) != set(root.get(field, [])):
                        errors.append(
                            f"{item.get('message_id')} changes root {field} in thread {thread_id}"
                        )

    unanswered_requests: list[str] = []
    missing_receiver_obligations: list[dict] = []
    missing_requester_dispositions: list[str] = []
    open_stop_lines: list[str] = []
    thread_summaries: list[dict] = []

    for thread_id, items in threads.items():
        roots = [item for item in items if item.get("predecessor_message_id") is None]
        if len(roots) != 1:
            errors.append(f"thread {thread_id} has {len(roots)} roots; expected exactly one")

        closures = [item for item in items if item.get("message_type") == "CLOSURE"]
        terminal_closures = [
            item for item in closures if not children.get(item.get("message_id"), [])
        ]
        presently_closed = bool(terminal_closures) and all(
            item.get("closure_kind") in NONBLOCKING_CLOSURES for item in terminal_closures
        )
        if any(item.get("stop_line") for item in items) and not presently_closed:
            open_stop_lines.append(thread_id)

        thread_unanswered: list[str] = []
        thread_missing_disposition: list[str] = []
        for item in items:
            item_id = item.get("message_id")
            item_children = children.get(item_id, [])
            if item.get("message_type") in REQUEST_TYPES:
                responding_roles = {
                    child.get("sender_role")
                    for child in item_children
                    if child.get("message_type") in RESPONSE_TYPES
                }
                missing_roles = sorted(set(item.get("receiver_roles", [])) - responding_roles)
                if missing_roles:
                    unanswered_requests.append(item_id)
                    thread_unanswered.append(item_id)
                    missing_receiver_obligations.append(
                        {
                            "request_id": item_id,
                            "thread_id": thread_id,
                            "missing_receiver_roles": missing_roles,
                            "affected_claims": item.get("affected_claims", []),
                            "affected_gates": item.get("affected_gates", []),
                        }
                    )
            if item.get("message_type") in RESPONSE_TYPES:
                requester = identifiers.get(item.get("predecessor_message_id"), {}).get(
                    "sender_role"
                )
                has_requester_disposition = any(
                    child.get("sender_role") == requester
                    and child.get("message_type") in FOLLOWUP_TYPES
                    for child in item_children
                )
                if not has_requester_disposition:
                    missing_requester_dispositions.append(item_id)
                    thread_missing_disposition.append(item_id)
                requester_dispositions = [
                    child for child in item_children
                    if child.get("sender_role") == requester
                    and child.get("message_type") in FOLLOWUP_TYPES
                ]
                if len(requester_dispositions) > 1:
                    errors.append(
                        f"{item_id} has multiple requester dispositions: "
                        + ", ".join(child.get("message_id", "<missing>") for child in requester_dispositions)
                    )

        thread_summaries.append(
            {
                "thread_id": thread_id,
                "message_count": len(items),
                "root_ids": [item.get("message_id") for item in roots],
                "closure_ids": [item.get("message_id") for item in closures],
                "unanswered_request_ids": thread_unanswered,
                "response_ids_missing_requester_disposition": thread_missing_disposition,
                "open_stop_line": thread_id in open_stop_lines,
            }
        )

    if unanswered_requests:
        warnings.append(f"unanswered requests: {', '.join(unanswered_requests)}")
        warnings.extend(
            f"request {item['request_id']} missing accountable receiver(s) "
            f"{', '.join(item['missing_receiver_roles'])} for claims "
            f"{', '.join(item['affected_claims'])}"
            for item in missing_receiver_obligations
        )
    if missing_requester_dispositions:
        warnings.append(
            "responses awaiting requester disposition: "
            + ", ".join(missing_requester_dispositions)
        )
    if open_stop_lines:
        warnings.append(f"open stop-line threads: {', '.join(open_stop_lines)}")

    return {
        "structural_status": "PASS" if not errors else "FAIL",
        "claim_promotion_status": (
            "BLOCKED"
            if errors or unanswered_requests or missing_requester_dispositions or open_stop_lines
            else "DIALOGUE_COMPLETE"
        ),
        "message_count": len(messages),
        "thread_count": len(threads),
        "errors": errors,
        "warnings": warnings,
        "unanswered_request_ids": unanswered_requests,
        "missing_receiver_obligations": missing_receiver_obligations,
        "response_ids_missing_requester_disposition": missing_requester_dispositions,
        "open_stop_line_threads": open_stop_lines,
        "threads": sorted(thread_summaries, key=lambda item: item["thread_id"]),
        "scope_note": (
            "This audit checks dialogue structure and open obligations only; it does not "
            "establish evidence truth, numerical adequacy, physical validation, or mechanism truth."
        ),
    }


def main() -> int:
    args = parse_args()
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    messages = load_jsonl(args.ledger)
    report = audit(messages, schema)
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    if report["structural_status"] == "FAIL":
        return 1
    if args.fail_open_obligations and report["claim_promotion_status"] != "DIALOGUE_COMPLETE":
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
