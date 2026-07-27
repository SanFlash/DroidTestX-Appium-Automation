"""Page object for the Checkout Review Order screen."""

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy

from app.locators.review_order_locators import (
    ReviewOrderLocators,
)
from core.base_page import BasePage
from core.logging.logger import get_logger


logger = get_logger(__name__)


class ReviewOrderPage(BasePage):
    """Checkout Review Order page actions."""

    def __init__(
        self,
        driver: WebDriver,
    ) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Verify that the Review Order screen is displayed."""

        return self.is_displayed(
            ReviewOrderLocators.SCREEN
        )

    def contains_product(
        self,
        product_name: str,
    ) -> bool:
        """
        Verify that a product exists on the Review Order screen.

        If the product is below the visible viewport,
        UiScrollable scrolls until the product becomes visible.
        """

        logger.info(
            "Searching Review Order for product: %s",
            product_name,
        )

        # First try the currently visible screen.
        try:
            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{product_name}")',
            )

            if elements:
                logger.info(
                    "Product visible on Review Order: %s",
                    product_name,
                )
                return True

        except Exception:
            logger.debug(
                "Initial product lookup failed: %s",
                product_name,
            )

        # Product may be below the visible viewport.
        try:
            logger.info(
                "Product not currently visible. "
                "Scrolling to locate: %s",
                product_name,
            )

            scroll_locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    'new UiScrollable('
                    'new UiSelector().scrollable(true)'
                    ').scrollIntoView('
                    f'new UiSelector().text("{product_name}")'
                    ')'
                ),
            )

            element = self.driver.find_element(
                *scroll_locator
            )

            if element.is_displayed():
                logger.info(
                    "Product found after scrolling: %s",
                    product_name,
                )
                return True

        except Exception:
            logger.warning(
                "Product was not found on Review Order: %s",
                product_name,
            )

        return False

    def get_total_items(
        self,
    ) -> str:
        """Return total item count displayed on Review Order."""

        return self.get_text(
            ReviewOrderLocators.TOTAL_NUMBER
        )

    def get_total_price(
        self,
    ) -> str:
        """Return total order price."""

        return self.get_text(
            ReviewOrderLocators.TOTAL_PRICE
        )

    def scroll_to_place_order(
        self,
    ) -> None:
        """Scroll until the Place Order button becomes visible."""

        logger.info(
            "Scrolling to Place Order button."
        )

        locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            (
                'new UiScrollable('
                'new UiSelector().scrollable(true)'
                ').scrollIntoView('
                'new UiSelector().description('
                '"Place Order button")'
                ')'
            ),
        )

        try:
            self.driver.find_element(
                *locator
            )

            logger.info(
                "Place Order button is visible."
            )

        except Exception:
            logger.warning(
                "Unable to scroll directly to "
                "Place Order button."
            )

    def place_order(
        self,
    ) -> None:
        """Scroll to and tap Place Order."""

        logger.info(
            "Preparing to place order."
        )

        self.scroll_to_place_order()

        self.click(
            ReviewOrderLocators.PLACE_ORDER
        )

        logger.info(
            "Place Order button clicked."
        )
        
        self.click(
            ReviewOrderLocators.CONTINUE_SHOPPING
        )   
        
        logger.info(
            "Continue Shopping button clicked."
        )