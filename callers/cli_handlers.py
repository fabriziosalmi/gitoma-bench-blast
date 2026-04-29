"""CLI command handlers — invoke core.process for each subcommand."""

from __future__ import annotations

from core.hub import process


def cmd_status() -> dict:
    """Handles the command to check the current operational status."""
    return process({"cmd": "status"})


def cmd_init(repo: str) -> dict:
    """Handles the command to initialize a repository context.

    Args:
        repo: The path or identifier of the repository to initialize.

    Returns:
        A dictionary indicating the result of the initialization attempt.
    """
    return process({"cmd": "init", "repo": repo})


def cmd_run(args: list[str]) -> dict:
    """Handles the command to execute a process with provided arguments.

    Args:
        args: A list of string arguments passed to the execution command.

    Returns:
        A dictionary indicating the result of the run attempt.
    """
    return process({"cmd": "run", "args": args})


def cmd_stop() -> dict:
    """Handles the command to gracefully stop a running process or service."""
    return process({"cmd": "stop"})


def cmd_doctor() -> dict:
    """Handles the command to run diagnostic checks on the system state."""
    return process({"cmd": "doctor"})
