import pytest
from app.operations import make_operation_table
ops = make_operation_table()

def test_add(): assert ops["add"](2,3) == 5
def test_divide_zero(): 
    with pytest.raises(Exception): ops["divide"](1,0)

def test_required_ops_exist():
    assert all(k in ops for k in ["power","root","modulus","int_divide","percent","abs_diff"])

def test_root_cube(): assert round(ops["root"](27,3),6) == 3.0  # pragma: no cover
