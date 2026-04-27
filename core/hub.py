"""Core hub module."""

from __future__ import annotations


def process(data: dict) -> dict:
    """Process the given data.

    Takes a dictionary of input data and returns a standardized response
    indicating success with the original data included.

    Args:
        data: A dictionary containing the input data to be processed.

    Returns:
        A dictionary with a 'status' key set to 'ok' and a 'data' key
        containing the original input data.

    Example:
        >>> process({"key": "value"})
        {'status': 'ok', 'data': {'key': 'value'}}
    """
    return {"status": "ok", "data": data}
