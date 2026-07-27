"""Locators for the Review Order screen."""

from appium.webdriver.common.appiumby import AppiumBy


class ReviewOrderLocators:
    """Review Order screen locators."""

    SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "checkout review order screen",
    )

    PRODUCT_ROWS = (
        AppiumBy.ACCESSIBILITY_ID,
        "product row",
    )

    PRODUCT_LABELS = (
        AppiumBy.ACCESSIBILITY_ID,
        "product label",
    )

    PRODUCT_PRICES = (
        AppiumBy.ACCESSIBILITY_ID,
        "product price",
    )

    TOTAL_NUMBER = (
        AppiumBy.ACCESSIBILITY_ID,
        "total number",
    )

    TOTAL_PRICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "total price",
    )

    PLACE_ORDER = (
        AppiumBy.ACCESSIBILITY_ID,
        "Place Order button",
    )
    
    CONTINUE_SHOPPING = (
        AppiumBy.ACCESSIBILITY_ID,
        "Continue Shopping button",
    )

    @staticmethod
    def product(
        name: str,
    ) -> tuple[str, str]:

        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")',
        )