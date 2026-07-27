from appium.webdriver.common.appiumby import AppiumBy


class CommonLocators:
    """Locators shared across application screens."""

    MENU_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "open menu",
    )

    CART_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "cart badge",
    )

    RESET_APP = (
        AppiumBy.ACCESSIBILITY_ID,
        "longpress reset app",
    )

    CONTAINER_HEADER = (
        AppiumBy.ACCESSIBILITY_ID,
        "container header",
    )