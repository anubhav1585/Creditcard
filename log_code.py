import logging
import os
from fileinput import filename

from fontTools.unicodedata import script_name


def setup_logging(script_name):
    # Create logs directory if it doesn't exist
    log_dir = "log_files"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(script_name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        log_file_path = os.path.join(log_dir, f"{script_name}.log")

        handler = logging.FileHandler(f'/Users/ishamittal/Desktop/creditcard/logs/{script_name}.log', mode='w')
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger
