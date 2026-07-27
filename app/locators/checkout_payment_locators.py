"""Locators for the Checkout Payment screen."""

from appium.webdriver.common.appiumby import AppiumBy


class CheckoutPaymentLocators:
    """Checkout Payment screen locators."""

    SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "checkout payment screen",
    )

    FULL_NAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "Full Name* input field",
    )

    CARD_NUMBER = (
        AppiumBy.ACCESSIBILITY_ID,
        "Card Number* input field",
    )

    EXPIRATION_DATE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Expiration Date* input field",
    )

    SECURITY_CODE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Security Code* input field",
    )

    BILLING_SAME_AS_SHIPPING = (
        AppiumBy.ACCESSIBILITY_ID,
        "checkbox for My billing address is the same as my shipping address.",
    )

    CARD_NUMBER_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Card Number*-error-message",
    )

    EXPIRATION_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Expiration Date*-error-message",
    )

    SECURITY_CODE_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Security Code*-error-message",
    )

    REVIEW_ORDER = (
        AppiumBy.ACCESSIBILITY_ID,
        "Review Order button",
    )