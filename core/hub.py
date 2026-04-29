"""The hub function. 31 cross-file callers across `callers/`.

Touching the signature of `process()` is the canonical "blast radius" change — every caller would need updating in lockstep.
gitoma's BLAST RADIUS prompt block + Ψ-full Φ component should
make this risk visible to the worker BEFORE it emits a patch."""

from __future__ import annotations


def process(payload: dict, *, validate: bool = True) -> dict:
    """The hub. Called by every caller module under callers/.

    Processes incoming payloads from various callers, performing validation if requested.

    Args:
        payload: The action payload received from the caller.
        validate: If True, performs schema validation on the payload. Defaults to True.

    Returns:
        A dictionary indicating success or failure of the operation.

    Raises:
        TypeError: If validation is enabled and payload is not a dictionary.
    """
    if validate and not isinstance(payload, dict):
        raise TypeError("payload must be a dict")
    return {"ok": True, "size": len(payload)}
