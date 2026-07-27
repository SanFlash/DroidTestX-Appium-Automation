from appium.webdriver.common.appiumby import AppiumBy


class CheckoutAddressLocators:

    SCREEN = (
        AppiumBy.ACCESSIBILITY_ID,
        "checkout address screen",
    )

    FULL_NAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "Full Name* input field",
    )

    ADDRESS_LINE_1 = (
        AppiumBy.ACCESSIBILITY_ID,
        "Address Line 1* input field",
    )

    ADDRESS_LINE_2 = (
        AppiumBy.ACCESSIBILITY_ID,
        "Address Line 2 input field",
    )

    CITY = (
        AppiumBy.ACCESSIBILITY_ID,
        "City* input field",
    )

    STATE_REGION = (
        AppiumBy.ACCESSIBILITY_ID,
        "State/Region input field",
    )

    ZIP_CODE = (
        AppiumBy.ACCESSIBILITY_ID,
        "Zip Code* input field",
    )

    COUNTRY = (
        AppiumBy.ACCESSIBILITY_ID,
        "Country* input field",
    )

    FULL_NAME_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Full Name*-error-message",
    )

    ADDRESS_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "Address Line 1*-error-message",
    )

    CITY_ERROR = (
        AppiumBy.ACCESSIBILITY_ID,
        "City*-error-message",
    )

    TO_PAYMENT = (
        AppiumBy.ACCESSIBILITY_ID,
        "To Payment button",
    )