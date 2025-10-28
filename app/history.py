from typing import List
from .calculation import Calculation
from .calculator_memento import Memento

class History:
    def __init__(self, max_size=1000):
        self._items: List[Calculation] = []
        self._redo: List[Calculation] = []
        self._max = max_size
    def push(self, calc: Calculation):
        if len(self._items) >= self._max: self._items.pop(0)
        self._items.append(calc); self._redo.clear()
    def items(self) -> List[Calculation]: return list(self._items)
    def save(self) -> Memento: return Memento(self._items)
    def restore(self, mem: Memento): self._items = mem.get_state(); self._redo.clear()
    def undo(self):
        if not self._items: return None
        c = self._items.pop(); self._redo.append(c); return c
    def redo(self):
        if not self._redo: return None
        c = self._redo.pop(); self._items.append(c); return c
    def clear(self): self._items.clear(); self._redo.clear()
