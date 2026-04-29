"""The hub function. 31 cross-file callers across `callers/`.

Touching the signature of `process()` is the canonical "blast radius" change — every caller would need updating in lockstep.
gitoma's BLAST RADIUS prompt block + Ψ-full Φ component should
make this risk visible to the worker BEFORE it emits a patch."""

from __future__ import annotations


def process(payload: dict, *, validate: bool = True) -> dict:
    """The central processing unit. Receives payloads from all callers and executes the required action.

    Args:
        payload: A dictionary containing the command and necessary data for execution.
        validate: If True (default), checks if payload is a dictionary before proceeding.

    Returns:
        A success indicator dictionary from the processing pipeline.

    Raises:
        TypeError: If validation is enabled and payload is not a dictionary.
    """
    if validate and not isinstance(payload, dict):
        raise TypeError("payload must be a dict")
    return {"ok": True, "size": len(payload)}
