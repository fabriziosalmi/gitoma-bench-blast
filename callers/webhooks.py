"""External webhook receivers — every event hits core.process."""

from __future__ import annotations

from core.hub import process


def on_push(event: dict) -> dict:
    return process({"hook": "push", "event": event})


def on_pull_request(event: dict) -> dict:
    return process({"hook": "pull_request", "event": event})


def on_issue(event: dict) -> dict:
    return process({"hook": "issue", "event": event})


def on_release(event: dict) -> dict:
    return process({"hook": "release", "event": event})


def on_deploy(event: dict) -> dict:
    return process({"hook": "deploy", "event": event})
