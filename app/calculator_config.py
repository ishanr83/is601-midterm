from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(frozen=True)
class Config:
    log_dir: str
    history_dir: str
    log_file: str
    history_file: str
    max_history_size: int
    auto_save: bool
    precision: int
    max_input_value: float
    default_encoding: str

def _ensure_dir(path: str) -> None:
    if path and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def load_config() -> Config:
    log_dir = os.getenv("CALCULATOR_LOG_DIR", "./logs")
    history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "./history")
    log_file = os.getenv("CALCULATOR_LOG_FILE", os.path.join(log_dir, "calculator.log"))
    history_file = os.getenv("CALCULATOR_HISTORY_FILE", os.path.join(history_dir, "history.csv"))
    max_history_size = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "1000"))
    auto_save = os.get_

WQ
wq
q
