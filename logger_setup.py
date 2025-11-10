import logging
from pathlib import Path



def setup_logger():
    BASE_DIR = Path(__file__).resolve().parent
    logs_dir = BASE_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "app.log"

    logger = logging.getLogger("converter_logger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger 