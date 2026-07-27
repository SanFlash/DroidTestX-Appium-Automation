"""Locators for the Sauce Labs My Demo App login screen."""

from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
    """Locators belonging to the Login screen."""

    USERNAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "Username input field",
    )

    PASSWORD = (
        AppiumBy.ACCESSIBILITY_ID,
        "Password input field",
    )

    LOGIN_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Login button",
    )

    USERNAME_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Username-error-message",
    )

    PASSWORD_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Password-error-message",
    )

    GENERIC_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "generic-error-message",
    )

    BOB_AUTOFILL = (
        AppiumBy.ACCESSIBILITY_ID,
        "bob@example.com-autofill",
    )

    LOCKED_USER_AUTOFILL = (
        AppiumBy.ACCESSIBILITY_ID,
        "alice@example.com (locked out)-autofill",
    )