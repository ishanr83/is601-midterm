from app.calculation import Calculation
def test_calc_factory():
    c = Calculation.of("add",1,2,3)
    assert c.result == 3 and "T" in c.timestamp  # pragma: no cover
