"""Dead helpers — public functions with ZERO callers anywhere in the
repo. G16 (when shipped) would flag patches that ADD MORE OF THESE.
For the current bench, they exist as a baseline so the agent can
see what dead code looks like and ideally not propose to add more.
"""

from __future__ import annotations


def unused_one() -> int:
    """Never called by anything."""
    return 1


def unused_two(x: int) -> int:
    """Never called by anything."""
    return x * 2


def unused_three() -> str:
    """Never called by anything."""
    return "dead"
