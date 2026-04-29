"""The hub function. 31 cross-file callers across `callers/`.

Touching the signature of `process()` is the canonical "blast radius" change — every caller would need updating in lockstep.
gitoma's BLAST RADIUS prompt block + Ψ-full Φ component should
make this risk visible to the worker BEFORE it emits a patch."""

from __future__ import annotations

def process(payload: dict, *, validate: bool = True) -> dict:
    """The hub. Called by every caller module under callers/.

    Processes incoming payloads from various API routes and orchestrates the action.

    Parameters
    ----------
    payload : dict
        A dictionary containing the action and necessary data.
    validate : bool, optional
        If True (default), validates the payload structure before processing.

    Returns
    -------
    dict
        A standardized response dictionary indicating success or failure.

    Raises
    -------
    TypeError
        If the payload is not a dictionary and validation is enabled.
    """
    if validate and not isinstance(payload, dict):
        raise TypeError("payload must be a dict")
    return {"ok": True, "size": len(payload)}
