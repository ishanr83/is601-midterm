import pytest
from app.input_validators import ensure_number, ensure_within_bounds, ensure_two_numbers
from app.exceptions import ValidationError

def test_ensure_number_ok():
    assert ensure_number("3.5", "x") == 3.5

def test_ensure_number_bad():
    with pytest.raises(ValidationError):
        ensure_number("abc", "x")

def test_within_bounds_ok():
    assert ensure_within_bounds(9.9, 10, "x") == 9.9

def test_within_bounds_exceed():
    with pytest.raises(ValidationError):
        ensure_within_bounds(11, 10, "x")

def test_ensure_two_numbers_bounds_and_cast():
    a, b = ensure_two_numbers("2", 3, 10)
    assert a == 2.0 and b == 3.0

def test_ensure_two_numbers_exceed():
    with pytest.raises(ValidationError):
        ensure_two_numbers(1e13, 1, 1e12)
