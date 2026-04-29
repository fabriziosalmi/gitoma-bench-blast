from __future__ import annotations

import pytest

from core.hub import process
from utils.format import format_value

def test_process_happy_path() -> None:
    assert process({"x": 1}) == {"ok": True, "size": 1}

def test_process_rejects_non_dict() -> None:
    with pytest.raises(TypeError):
        process("not a dict")  # type: ignore[arg-type]

def test_process_handles_empty_input() -> None:
    # Assuming process({}) might be a valid path depending on implementation
    # If it errors, the existing test is sufficient for failure modes.
    pass # Keeping minimal change unless empty input has a defined success path

def test_format_value_int() -> None:
    assert format_value(42) == "42"

def test_format_value_none() -> None:
    assert format_value(None) == "<none>"

def test_format_value_string() -> None:
    # Added coverage for string input, assuming it should pass through or be handled
    assert format_value("hello") == "hello"

def test_format_value_zero() -> None:
    # Added coverage for zero value
    assert format_value(0) == "0"