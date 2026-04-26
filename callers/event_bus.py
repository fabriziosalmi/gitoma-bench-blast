"""In-process event bus — each event class invokes core.process.

Brings the total caller count to 31 (5 + 5 + 5 + 5 + 5 + 6 across
api_routes / background_jobs / cli_handlers / cron_tasks / webhooks
/ this file). Plus 1 caller of utils.format_value for completeness."""

from __future__ import annotations

from core.hub import process
from utils.format import format_value


def emit_started() -> dict:
    return process({"event": "started"})


def emit_progress(pct: float) -> dict:
    return process({"event": "progress", "pct": format_value(pct)})


def emit_completed() -> dict:
    return process({"event": "completed"})


def emit_failed(reason: str) -> dict:
    return process({"event": "failed", "reason": reason})


def emit_retried(attempt: int) -> dict:
    return process({"event": "retried", "attempt": attempt})


def emit_canceled() -> dict:
    return process({"event": "canceled"})
