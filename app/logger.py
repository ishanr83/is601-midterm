import logging

def get_logger(path: str):
    logger = logging.getLogger("calculator")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(path, encoding="utf-8")
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger
