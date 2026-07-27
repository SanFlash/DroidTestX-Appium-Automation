"""Screenshot capture utility."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from appium.webdriver.webdriver import WebDriver

from core.config.config_manager import ConfigManager
from core.logging.logger import get_logger


logger = get_logger(__name__)


class ScreenshotManager:
    """Capture timestamped screenshots."""

    @staticmethod
    def capture(
        driver: WebDriver,
        name: str,
    ) -> Path:
        config = ConfigManager()

        directory = (
            config.root_dir
            / "screenshots"
        )

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        safe_name = "".join(
            character
            if character.isalnum()
            or character in ("-", "_")
            else "_"
            for character in name
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        path = (
            directory
            / f"{safe_name}_{timestamp}.png"
        )

        success = driver.save_screenshot(
            str(path)
        )

        if not success:
            raise RuntimeError(
                f"Appium failed to save screenshot: {path}"
            )

        logger.info(
            "Screenshot saved: %s",
            path,
        )

        return path