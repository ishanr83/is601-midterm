import os
import pandas as pd
from app.calculation import Calculation
from app.observers import LoggingObserver, AutoSaveObserver
from app.calculator_config import load_config

def test_logging_observer_writes_file(tmp_path, monkeypatch):
    log_file = tmp_path / "calc.log"
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path))
    monkeypatch.setenv("CALCULATOR_LOG_FILE", str(log_file))
    obs = LoggingObserver()
    obs.update(Calculation.of("add", 1, 2, 3))
    assert log_file.exists()
    assert log_file.read_text(encoding="utf-8")

def test_autosave_observer_writes_csv(tmp_path, monkeypatch):
    hist_file = tmp_path / "hist.csv"
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path))
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", str(hist_file))
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "true")
    obs = AutoSaveObserver()
    # provide a fake history
    items = [Calculation.of("add", 1, 2, 3), Calculation.of("multiply", 2, 3, 6)]
    obs.history_provider = lambda: items
    # trigger save
    obs.update(items[-1])
    assert hist_file.exists()
    df = pd.read_csv(hist_file)
    assert len(df) == 2 and set(df.columns) >= {"operation","a","b","result","timestamp"}
