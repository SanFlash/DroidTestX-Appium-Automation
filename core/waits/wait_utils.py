"""Explicit wait utilities for Appium."""

from __future__ import annotations

from typing import Any

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core.config.config_manager import ConfigManager
from core.logging.logger import get_logger


logger = get_logger(__name__)

Locator = tuple[str, str]


class WaitUtils:
    """Reusable explicit waits."""

    def __init__(
        self,
        driver: WebDriver,
        timeout: int | None = None,
    ) -> None:
        self.driver = driver

        config = ConfigManager()

        self.timeout = timeout or int(
            config.get(
                "timeouts.explicit_wait",
                15,
            )
        )

    def _wait(
        self,
        timeout: int | None = None,
    ) -> WebDriverWait:
        return WebDriverWait(
            self.driver,
            timeout or self.timeout,
        )

    def visible(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        try:
            return self._wait(timeout).until(
                EC.visibility_of_element_located(
                    locator
                )
            )
        except TimeoutException:
            logger.error(
                "Element was not visible: %s",
                locator,
            )
            raise

    def clickable(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        try:
            return self._wait(timeout).until(
                EC.element_to_be_clickable(
                    locator
                )
            )
        except TimeoutException:
            logger.error(
                "Element was not clickable: %s",
                locator,
            )
            raise

    def present(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        return self._wait(timeout).until(
            EC.presence_of_element_located(
                locator
            )
        )

    def invisible(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> bool:
        return bool(
            self._wait(timeout).until(
                EC.invisibility_of_element_located(
                    locator
                )
            )
        )

    def text_present(
        self,
        locator: Locator,
        text: str,
        timeout: int | None = None,
    ) -> bool:
        return bool(
            self._wait(timeout).until(
                EC.text_to_be_present_in_element(
                    locator,
                    text,
                )
            )
        )

    def until(
        self,
        condition: Any,
        timeout: int | None = None,
    ) -> Any:
        return self._wait(timeout).until(
            condition
        )