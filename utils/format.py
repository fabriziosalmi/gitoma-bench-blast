"""A leaf utility — used by exactly ONE caller. Φ should rate this
as low-impact (high Φ score) compared to core.hub.process()."""

from __future__ import annotations

def format_value(value: object) -> str:
    """Converts a Python object into its stable string representation.

    Handles None, numeric types, and general objects gracefully.

    Parameters
    ----------
    value : object
        The input value of any type.

    Returns
    -------
    str
        A string representation of the input value.
    """
    if value is None:
        return "<none>"
    if isinstance(value, (int, float)):
        return f"{value:g}"
    return str(value)
