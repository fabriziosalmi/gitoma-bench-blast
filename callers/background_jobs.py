"""Background job handlers — heavy users of core.process."""

from __future__ import annotations

from core.hub import process


def cleanup_stale() -> dict:
    return process({"job": "cleanup_stale"})


def reindex_search() -> dict:
    return process({"job": "reindex_search"})


def aggregate_stats() -> dict:
    return process({"job": "aggregate_stats"})


def rotate_logs() -> dict:
    return process({"job": "rotate_logs"})


def expire_sessions() -> dict:
    return process({"job": "expire_sessions"})
