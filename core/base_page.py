"""Base Page Object implementation.

Provides reusable UI operations shared by all page objects in the
Android automation framework.
"""

from __future__ import annotations

from typing import Any

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.remote.webelement import WebElement

from core.gestures.gesture_utils import GestureUtils
from core.logging.logger import get_logger
from core.waits.wait_utils import Locator, WaitUtils


class BasePage:
    """Common functionality shared by application page objects."""

    def __init__(
        self,
        driver: WebDriver,
    ) -> None:
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.gestures = GestureUtils(driver)
        self.logger = get_logger(
            self.__class__.__name__
        )

    # ============================================================
    # ELEMENT FINDING
    # ============================================================

    def find(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        """Find a visible element."""

        self.logger.debug(
            "Finding visible element: %s",
            locator,
        )

        return self.wait.visible(
            locator,
            timeout,
        )

    def find_present(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        """Find an element that exists in the UI hierarchy."""

        self.logger.debug(
            "Finding present element: %s",
            locator,
        )

        return self.wait.present(
            locator,
            timeout,
        )

    def find_all(
        self,
        locator: Locator,
    ) -> list[WebElement]:
        """Return all matching elements."""

        self.logger.debug(
            "Finding all elements: %s",
            locator,
        )

        return self.driver.find_elements(
            *locator
        )

    # ============================================================
    # CLICK
    # ============================================================

    def click(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> None:
        """Wait until an element is clickable and click it."""

        self.logger.info(
            "Clicking element: %s",
            locator,
        )

        try:
            element = self.wait.clickable(
                locator,
                timeout,
            )

            element.click()

        except Exception:
            self.logger.exception(
                "Failed to click element: %s",
                locator,
            )
            raise

    # ============================================================
    # TEXT INPUT
    # ============================================================

    def type(
        self,
        locator: Locator,
        value: str,
        clear_first: bool = True,
        timeout: int | None = None,
    ) -> None:
        """Enter text into an input field."""

        self.logger.info(
            "Typing into element: %s",
            locator,
        )

        try:
            element = self.wait.visible(
                locator,
                timeout,
            )

            if clear_first:
                element.clear()

            element.send_keys(value)

        except Exception:
            self.logger.exception(
                "Failed typing into element: %s",
                locator,
            )
            raise

    def clear(
        self,
        locator: Locator,
    ) -> None:
        """Clear an input element."""

        self.logger.info(
            "Clearing element: %s",
            locator,
        )

        element = self.wait.visible(
            locator
        )

        element.clear()

    # ============================================================
    # TEXT RETRIEVAL
    # ============================================================

    def get_text(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> str:
        """
        Return element text.

        React Native frequently exposes visible values through
        content-desc instead of Selenium's text property, so this
        method supports both.
        """

        element = self.wait.visible(
            locator,
            timeout,
        )

        text = element.text

        if text:
            return text.strip()

        content_description = element.get_attribute(
            "content-desc"
        )

        if content_description:
            return content_description.strip()

        return ""

    # ============================================================
    # ATTRIBUTES
    # ============================================================

    def get_attribute(
        self,
        locator: Locator,
        attribute: str,
    ) -> str | None:
        """Return an element attribute."""

        element = self.wait.present(
            locator
        )

        return element.get_attribute(
            attribute
        )

    def get_content_description(
        self,
        locator: Locator,
    ) -> str:
        """Return Android content-desc."""

        value = self.get_attribute(
            locator,
            "content-desc",
        )

        return value or ""

    # ============================================================
    # ELEMENT STATE
    # ============================================================

    def is_displayed(
        self,
        locator: Locator,
        timeout: int = 5,
    ) -> bool:
        """Return True when an element becomes visible."""

        try:
            element = self.wait.visible(
                locator,
                timeout,
            )

            return element.is_displayed()

        except (
            TimeoutException,
            StaleElementReferenceException,
        ):
            return False

        except WebDriverException:
            self.logger.debug(
                "Unable to determine visibility: %s",
                locator,
            )

            return False

    def is_enabled(
        self,
        locator: Locator,
    ) -> bool:
        """Return whether an element is enabled."""

        try:
            return self.wait.present(
                locator
            ).is_enabled()

        except WebDriverException:
            return False

    def is_selected(
        self,
        locator: Locator,
    ) -> bool:
        """Return whether an element is selected."""

        try:
            return self.wait.present(
                locator
            ).is_selected()

        except WebDriverException:
            return False

    def exists(
        self,
        locator: Locator,
        timeout: int = 3,
    ) -> bool:
        """Check whether an element exists in the hierarchy."""

        try:
            self.wait.present(
                locator,
                timeout,
            )

            return True

        except TimeoutException:
            return False

    # ============================================================
    # WAITS
    # ============================================================

    def wait_until_visible(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        """Wait until an element becomes visible."""

        return self.wait.visible(
            locator,
            timeout,
        )

    def wait_until_clickable(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> WebElement:
        """Wait until an element becomes clickable."""

        return self.wait.clickable(
            locator,
            timeout,
        )

    def wait_until_invisible(
        self,
        locator: Locator,
        timeout: int | None = None,
    ) -> bool:
        """Wait until an element disappears."""

        return self.wait.invisible(
            locator,
            timeout,
        )

    # ============================================================
    # SCROLLING / SWIPING
    # ============================================================

    def swipe_up(self) -> None:
        """Swipe upward."""

        self.logger.info(
            "Performing swipe up."
        )

        self.gestures.swipe("up")

    def swipe_down(self) -> None:
        """Swipe downward."""

        self.logger.info(
            "Performing swipe down."
        )

        self.gestures.swipe("down")

    def swipe_left(self) -> None:
        """Swipe left."""

        self.logger.info(
            "Performing swipe left."
        )

        self.gestures.swipe("left")

    def swipe_right(self) -> None:
        """Swipe right."""

        self.logger.info(
            "Performing swipe right."
        )

        self.gestures.swipe("right")

    # ============================================================
    # KEYBOARD
    # ============================================================

    def hide_keyboard(self) -> None:
        """Hide Android software keyboard when displayed."""

        try:
            self.driver.hide_keyboard()

            self.logger.debug(
                "Keyboard hidden."
            )

        except WebDriverException:
            self.logger.debug(
                "Keyboard was not visible."
            )

    # ============================================================
    # ANDROID NAVIGATION
    # ============================================================

    def press_back(self) -> None:
        """Press Android back."""

        self.logger.info(
            "Pressing Android back button."
        )

        self.driver.back()

    # ============================================================
    # APPLICATION INFORMATION
    # ============================================================

    def current_package(self) -> str:
        """Return currently active Android package."""

        return self.driver.current_package

    def current_activity(self) -> str:
        """Return currently active Android activity."""

        return self.driver.current_activity

    # ============================================================
    # PAGE SOURCE
    # ============================================================

    def get_page_source(self) -> str:
        """Return current Appium XML hierarchy."""

        return self.driver.page_source

    # ============================================================
    # MOBILE COMMANDS
    # ============================================================

    def execute_mobile_command(
        self,
        command: str,
        arguments: dict[str, Any] | None = None,
    ) -> Any:
        """Execute an Appium mobile command."""

        self.logger.debug(
            "Executing mobile command: %s",
            command,
        )

        return self.driver.execute_script(
            f"mobile: {command}",
            arguments or {},
        )