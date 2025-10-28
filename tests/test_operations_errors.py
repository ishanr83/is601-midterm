import pytest
from app.operations import make_operation_table
ops = make_operation_table()

@pytest.mark.parametrize("op,a,b", [
    ("divide", 1, 0),
    ("modulus", 1, 0),
    ("int_divide", 1, 0),
    ("percent", 1, 0),
])
def test_division_like_zero_errors(op, a, b):
    with pytest.raises(Exception):
        ops[op](a, b)

def test_root_even_negative_errors():
    with pytest.raises(Exception):
        ops["root"](-8, 2)

def test_power_and_abs_diff_nominal():
    assert ops["power"](2, 5) == 32
    assert ops["abs_diff"](10, 3) == 7
