from appium.webdriver.common.appiumby import AppiumBy


class CartLocators:

    SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "cart screen",
    )

    TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("My Cart")',
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

    QUANTITY_MINUS = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter minus button",
    )

    QUANTITY_AMOUNT = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter amount",
    )

    QUANTITY_PLUS = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter plus button",
    )

    REMOVE_BUTTONS = (
        AppiumBy.ACCESSIBILITY_ID,
        "remove item",
    )

    TOTAL_NUMBER = (
        AppiumBy.ACCESSIBILITY_ID,
        "total number",
    )

    TOTAL_PRICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "total price",
    )

    CHECKOUT_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Proceed To Checkout button",
    )

    @staticmethod
    def product(name: str) -> tuple[str, str]:
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{name}")',
        )