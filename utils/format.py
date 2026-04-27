"""A leaf utility — used by exactly ONE caller. Φ should rate this
as low-impact (high Φ score) compared to core.hub.process()."""

from __future__ import annotations


def format_value(value: object) -> str:
    """Stringify a value with a stable representation.

    Converts various Python objects into a string representation.
    Handles None, numeric types (int, float), and other objects.

    Args:
        value: The object to format. Can be any Python object.

    Returns:
        A string representation of the value:
            - None returns '<none>'
            - Integers and floats are formatted using general notation
              (removing trailing zeros)
            - Other objects use their standard str() representation.

    Example:
        >>> format_value(None)
        '<none>'
        >>> format_value(3.14159)
        '3.14159'
        >>> format_value("hello")
        'hello'
    """
    if value is None:
        return "<none>"
    if isinstance(value, (int, float)):
        return f"{value:g}"
    return str(value)
