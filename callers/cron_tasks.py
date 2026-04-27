from __future__ import annotations

from core.hub import process


def daily_report_generator() -> dict:
    """Handles the task of generating the daily operational report."""
    return process({"job": "generate_daily_report"})

def weekly_maintenance_scheduler() -> dict:
    """Handles the task of scheduling weekly system maintenance."""
    return process({"job": "schedule_weekly_maintenance"})

def monthly_backup_initiator() -> dict:
    """Handles the task of initiating the monthly data backup."""
    return process({"job": "initiate_monthly_backup"})