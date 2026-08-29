import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from pythonjsonlogger.json import JsonFormatter

from app.core.config import settings


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.

    The logger writes:
    - Human-readable logs to the console.
    - JSON formatted logs to logs/app.log.
    """

    logger = logging.getLogger(settings.APP_NAME)

    if logger.hasHandlers():
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    # -----------------------------
    # Console Handler
    # -----------------------------
    console_handler = logging.StreamHandler()

    console_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(console_formatter)

    # -----------------------------
    # File Handler (JSON)
    # -----------------------------
    log_directory = Path("logs")
    log_directory.mkdir(exist_ok=True)

    file_handler = RotatingFileHandler(
        filename=log_directory / "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )

    json_formatter = JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    file_handler.setFormatter(json_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


logger = setup_logger()