#!/usr/bin/env python3
"""Validate and atomically append one scientific-dialogue JSON message.

This utility never rewrites an existing JSONL ledger.  A short-lived exclusive
lock serializes concurrent agents; message IDs and predecessor links are
checked again while the lock is held.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from contextlib import suppress
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - environment-dependent failure path
    raise SystemExit("jsonschema is required to validate dialogue messages") from exc


from audit_scientific_dialogue import audit


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--message", type=Path, required=True)
    parser.add_argument("--lock-timeout", type=float, default=10.0)
    return parser.parse_args()


def acquire_lock(path: Path, timeout: float) -> int:
    deadline = time.monotonic() + timeout
    while True:
        try:
            return os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise TimeoutError(
                    f"Timed out waiting for dialogue ledger lock: {path}"
                ) from None
            time.sleep(0.05)


def load_ledger(path: Path) -> list[dict]:
    if not path.exists():
        return []
    messages: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            messages.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at {path}:{line_number}: {exc}") from exc
    return messages


def main() -> int:
    args = parse_args()
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    message = json.loads(args.message.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    validator.validate(message)

    args.ledger.parent.mkdir(parents=True, exist_ok=True)
    lock_path = args.ledger.with_name(args.ledger.name + ".lock")
    lock_fd = acquire_lock(lock_path, args.lock_timeout)
    try:
        os.write(lock_fd, f"pid={os.getpid()}\n".encode())
        os.fsync(lock_fd)
        existing = load_ledger(args.ledger)
        proposed = [dict(item, _ledger_line=index) for index, item in enumerate(existing, 1)]
        proposed.append(dict(message, _ledger_line=len(proposed) + 1))
        report = audit(proposed, schema)
        if report["structural_status"] != "PASS":
            raise ValueError("Dialogue validation failed: " + "; ".join(report["errors"]))

        encoded = json.dumps(message, ensure_ascii=False, separators=(",", ":")) + "\n"
        with args.ledger.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        os.close(lock_fd)
        with suppress(FileNotFoundError):
            lock_path.unlink()

    print(f"APPENDED {message['message_id']} -> {args.ledger}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
