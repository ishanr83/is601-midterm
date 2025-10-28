from app.calculation import Calculation
from app.persistence import save_history, load_history

def test_save_load_roundtrip(tmp_path, monkeypatch):
    hist_dir = tmp_path
    hist_file = hist_dir / "h.csv"
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(hist_dir))
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", str(hist_file))
    items = [Calculation.of("add",1,2,3)]
    save_history(items)
    out = load_history()
    assert len(out)==1 and out[0].result==3
