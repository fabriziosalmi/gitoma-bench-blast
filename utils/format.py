"""A leaf utility — used by exactly ONE caller. Φ should rate this
as low-impact (high Φ score) compared to core.hub.process()."""

from __future__ import annotations


def format_value(value: object) -> str:
    """Stringify a value with a stable representation."""
    if value is None:
        return "<none>"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (int, float)):
        return f"{value:g}"
    return str(value)
