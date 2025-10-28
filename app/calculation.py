from dataclasses import dataclass
from datetime import datetime

@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float
    timestamp: str

    @classmethod
    def of(cls, operation, a, b, result):
        return cls(operation, a, b, result, datetime.utcnow().isoformat(timespec="seconds"))
