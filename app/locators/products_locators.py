from appium.webdriver.common.appiumby import AppiumBy


class ProductsLocators:
    """Locators for the Products catalogue."""

    SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "products screen",
    )

    TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Products")',
    )

    SORT_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "sort button",
    )

    PRODUCT_ITEMS = (
        AppiumBy.ACCESSIBILITY_ID,
        "store item",
    )

    PRODUCT_NAMES = (
        AppiumBy.ACCESSIBILITY_ID,
        "store item text",
    )

    PRODUCT_PRICES = (
        AppiumBy.ACCESSIBILITY_ID,
        "store item price",
    )

    @staticmethod
    def product(name: str) -> tuple[str, str]:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")',
        )

    @staticmethod
    def price(price: str) -> tuple[str, str]:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{price}")',
        )