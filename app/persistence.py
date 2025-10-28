import pandas as pd
from .calculation import Calculation
from .calculator_config import load_config

REQUIRED_COLS = {"operation", "a", "b", "result", "timestamp"}

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
    except Exception as e:
        # Any read/parse-level failure surfaces as RuntimeError
        raise RuntimeError(f"Failed to load history: {e}")

    # Validate schema
    if not REQUIRED_COLS.issubset(set(df.columns)):
        raise RuntimeError(f"Malformed history: missing required columns {REQUIRED_COLS - set(df.columns)}")

    # Convert rows → Calculation instances with strict typing
    records = []
    for idx, r in df.iterrows():
        try:
            records.append(Calculation(
                operation=str(r["operation"]),
                a=float(r["a"]),
                b=float(r["b"]),
                result=float(r["result"]),
                timestamp=str(r["timestamp"])
            ))
        except Exception as e:
            # Any row-level conversion issue → RuntimeError with index details
            raise RuntimeError(f"Malformed history row at index {idx}: {e}")
    return records
