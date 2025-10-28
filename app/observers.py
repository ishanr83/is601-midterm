import pandas as pd
from .logger import get_logger
from .calculator_config import load_config

class LoggingObserver:
    def __init__(self):
        cfg = load_config()
        self.logger = get_logger(cfg.log_file)
    def update(self, calc):
        self.logger.info("op=%s a=%s b=%s result=%s ts=%s",
                         calc.operation, calc.a, calc.b, calc.result, calc.timestamp)

class AutoSaveObserver:
    def __init__(self):
        self.cfg = load_config()
        self.history_provider = lambda: []  # set by Calculator
    def update(self, _calc):
        if not self.cfg.auto_save: return
        items = self.history_provider()
        df = pd.DataFrame([{
            "operation": c.operation, "a": c.a, "b": c.b,
            "result": c.result, "timestamp": c.timestamp
        } for c in items])
        df.to_csv(self.cfg.history_file, index=False, encoding=self.cfg.default_encoding)
