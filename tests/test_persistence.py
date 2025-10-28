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

def test_load_history_malformed(tmp_path, monkeypatch):
    hist_file = tmp_path / "bad.csv"
    hist_file.write_text("not,a,valid,csv\n{", encoding="utf-8")
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path))
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", str(hist_file))
    # Should raise RuntimeError per implementation
    from app.persistence import load_history
    try:
        load_history()
        assert False, "Expected load_history to raise"
    except RuntimeError:
        assert True
