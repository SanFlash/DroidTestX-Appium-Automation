"""Android gesture helpers using UiAutomator2 mobile commands."""

from __future__ import annotations

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from core.logging.logger import get_logger


logger = get_logger(__name__)


class GestureUtils:
    """Reusable Android gestures."""

    def __init__(
        self,
        driver: WebDriver,
    ) -> None:
        self.driver = driver

    def swipe(
        self,
        direction: str,
        percent: float = 0.75,
    ) -> None:
        size = self.driver.get_window_size()

        self.driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 0,
                "top": 0,
                "width": size["width"],
                "height": size["height"],
                "direction": direction.lower(),
                "percent": percent,
            },
        )

        logger.info(
            "Swipe performed: %s",
            direction,
        )

    def scroll_element(
        self,
        element: WebElement,
        direction: str = "down",
        percent: float = 0.8,
    ) -> bool:
        result = self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "elementId": element.id,
                "direction": direction.lower(),
                "percent": percent,
            },
        )

        return bool(result)

    def long_click(
        self,
        element: WebElement,
        duration: int = 1000,
    ) -> None:
        self.driver.execute_script(
            "mobile: longClickGesture",
            {
                "elementId": element.id,
                "duration": duration,
            },
        )

    def double_click(
        self,
        element: WebElement,
    ) -> None:
        self.driver.execute_script(
            "mobile: doubleClickGesture",
            {
                "elementId": element.id,
            },
        )

    def drag(
        self,
        element: WebElement,
        end_x: int,
        end_y: int,
    ) -> None:
        self.driver.execute_script(
            "mobile: dragGesture",
            {
                "elementId": element.id,
                "endX": end_x,
                "endY": end_y,
            },
        )