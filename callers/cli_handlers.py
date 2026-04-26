"""CLI command handlers — invoke core.process for each subcommand."""

from __future__ import annotations

from core.hub import process


def cmd_status() -> dict:
    return process({"cmd": "status"})


def cmd_init(repo: str) -> dict:
    return process({"cmd": "init", "repo": repo})


def cmd_run(args: list[str]) -> dict:
    return process({"cmd": "run", "args": args})


def cmd_stop() -> dict:
    return process({"cmd": "stop"})


def cmd_doctor() -> dict:
    return process({"cmd": "doctor"})
