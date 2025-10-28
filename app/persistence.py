import pandas as pd
from .calculation import Calculation
from .calculator_config import load_config

def save_history(items):
    cfg = load_config()
    df = pd.DataFrame([{
        "operation": c.operation, "a": c.a, "b": c.b,
        "result": c.result, "timestamp": c.timestamp
    } for c in items])
    df.to_csv(cfg.history_file, index=False, encoding=cfg.default_encoding)

def load_history():
    cfg = load_config()
    try:
        df = pd.read_csv(cfg.history_file, encoding=cfg.default_encoding)
    except FileNotFoundError:
        return []
    recs = []
    for _, r in df.iterrows():
        recs.append(Calculation(
            operation=str(r.get("operation","")),
            a=float(r.get("a",0.0)), b=float(r.get("b",0.0)),
            result=float(r.get("result",0.0)), timestamp=str(r.get("timestamp",""))
        ))
    return recs
