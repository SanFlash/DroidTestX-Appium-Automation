"""Framework logging configuration."""

from __future__ import annotations

import logging
from pathlib import Path

from core.config.config_manager import ConfigManager


_LOGGER_CONFIGURED = False


def _configure_logging() -> None:
    global _LOGGER_CONFIGURED

    if _LOGGER_CONFIGURED:
        return

    config = ConfigManager()

    log_directory = config.root_dir / "logs"
    log_directory.mkdir(parents=True, exist_ok=True)

    log_file = log_directory / "automation.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | "
        "%(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    if not root_logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(
            Path(log_file),
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)

        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)

    _LOGGER_CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """Return a configured framework logger."""

    _configure_logging()

    return logging.getLogger(name)