from appium.webdriver.common.appiumby import AppiumBy


class ProductDetailsLocators:
    """Locators for the product details screen."""

    SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "product screen",
    )

    PRICE = (
        AppiumBy.ACCESSIBILITY_ID,
        "product price",
    )

    DESCRIPTION = (
        AppiumBy.ACCESSIBILITY_ID,
        "product description",
    )

    BLACK_COLOR = (
        AppiumBy.ACCESSIBILITY_ID,
        "black circle",
    )

    BLUE_COLOR = (
        AppiumBy.ACCESSIBILITY_ID,
        "blue circle",
    )

    GRAY_COLOR = (
        AppiumBy.ACCESSIBILITY_ID,
        "gray circle",
    )

    RED_COLOR = (
        AppiumBy.ACCESSIBILITY_ID,
        "red circle",
    )

    QUANTITY_MINUS = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter minus button",
    )
    
    QUANTITY_VALUE = (
    AppiumBy.XPATH,
    '//*[@content-desc="counter amount"]/android.widget.TextView'
)

    QUANTITY_CONTAINER = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter amount",
    )

    QUANTITY_PLUS = (
        AppiumBy.ACCESSIBILITY_ID,
        "counter plus button",
    )

    ADD_TO_CART = (
        AppiumBy.ACCESSIBILITY_ID,
        "Add To Cart button",
    )

    CART_BADGE = (
        AppiumBy.ACCESSIBILITY_ID,
        "cart badge",
    )