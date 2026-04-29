from __future__ import annotations

import pytest

from core.hub import process
from utils.format import format_value

def test_process_happy_path() -> None:
    assert process({"x": 1}) == {"ok": True, "size": 1}

def test_process_rejects_non_dict() -> None:
    with pytest.raises(TypeError):
        process("not a dict")  # type: ignore[arg-type]

def test_format_value_int() -> None:
    assert format_value(42) == "42"

def test_format_value_none() -> None:
    assert format_value(None) == "<none>"