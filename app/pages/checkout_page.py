from appium.webdriver.webdriver import WebDriver

from app.locators.checkout_address_locators import (
    CheckoutAddressLocators,
)
from core.base_page import BasePage


class CheckoutAddressPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        return self.is_displayed(
            CheckoutAddressLocators.SCREEN
        )

    def enter_address(
        self,
        full_name: str,
        address1: str,
        city: str,
        state: str,
        zip_code: str,
        country: str,
        address2: str = "",
    ) -> None:

        self.type(
            CheckoutAddressLocators.FULL_NAME,
            full_name,
        )

        self.type(
            CheckoutAddressLocators.ADDRESS_LINE_1,
            address1,
        )

        if address2:
            self.type(
                CheckoutAddressLocators.ADDRESS_LINE_2,
                address2,
            )

        self.type(
            CheckoutAddressLocators.CITY,
            city,
        )

        self.type(
            CheckoutAddressLocators.STATE_REGION,
            state,
        )

        self.type(
            CheckoutAddressLocators.ZIP_CODE,
            zip_code,
        )

        self.type(
            CheckoutAddressLocators.COUNTRY,
            country,
        )

        self.hide_keyboard()

    def continue_to_payment(self) -> None:
        self.click(
            CheckoutAddressLocators.TO_PAYMENT
        )