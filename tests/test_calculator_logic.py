import pytest
from app.calculator import Calculator

def test_perform_add_and_history():
    c = Calculator()
    out = c.perform("add", "2", "3")
    assert out.result == 5 and len(c.items())==1

def test_invalid_operation():
    c = Calculator()
    with pytest.raises(Exception):
        c.perform("nope", 1, 2)

def test_bounds_check():
    c = Calculator()
    with pytest.raises(Exception):
        c.perform("add", 1e13, 1)  # beyond max input
