from typing import Callable, List, Dict
from .operations import make_operation_table
from .input_validators import ensure_two_numbers
from .calculation import Calculation
from .history import History
from .exceptions import OperationError
from .calculator_config import load_config

class Observer:  # pragma: no cover
    def update(self, calc: Calculation): ...

class Calculator:
    def __init__(self):
        self.config = load_config()
        self.history = History(self.config.max_history_size)
        self.ops: Dict[str, Callable] = make_operation_table()
        self.observers: List[Observer] = []
        self.history_provider = lambda: self.history.items()

    def register(self, obs: Observer): self.observers.append(obs)

    def _notify(self, calc: Calculation):
        for obs in self.observers: obs.update(calc)

    def perform(self, op_name: str, a, b) -> Calculation:
        if op_name not in self.ops: raise OperationError(f"Unknown operation: {op_name}")
        a,b = ensure_two_numbers(a,b,self.config.max_input_value)
        res = self.ops[op_name](a,b)
        calc = Calculation.of(op_name, a, b, round(res, self.config.precision))
        self.history.push(calc); self._notify(calc); return calc

    def undo(self): return self.history.undo()
    def redo(self): return self.history.redo()
    def items(self): return self.history.items()
    def clear(self): self.history.clear()
