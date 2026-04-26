"""Cron-scheduled task handlers."""

from __future__ import annotations

from core.hub import process


def hourly() -> dict:
    return process({"cron": "hourly"})


def daily() -> dict:
    return process({"cron": "daily"})


def weekly() -> dict:
    return process({"cron": "weekly"})


def monthly() -> dict:
    return process({"cron": "monthly"})


def yearly() -> dict:
    return process({"cron": "yearly"})
