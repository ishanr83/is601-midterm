from app.history import History
from app.calculation import Calculation

def test_undo_redo_cycle():
    h = History(10)
    a = Calculation.of("add",1,2,3)
    b = Calculation.of("mul",2,3,6)
    h.push(a); h.push(b)
    assert h.undo() == b
    assert h.redo() == b
