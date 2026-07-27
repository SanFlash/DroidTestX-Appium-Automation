"""Page object for the checkout address screen."""

from __future__ import annotations

from appium.webdriver.webdriver import WebDriver

from app.locators.checkout_address_locators import (
    CheckoutAddressLocators,
)
from core.base_page import BasePage


class CheckoutAddressPage(BasePage):
    """Interactions with the checkout address screen."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Return True when the checkout address screen is displayed."""
        return self.is_displayed(
            CheckoutAddressLocators.SCREEN
        )

    def enter_full_name(
        self,
        full_name: str,
    ) -> None:
        """Enter customer's full name."""
        self.type(
            CheckoutAddressLocators.FULL_NAME,
            full_name,
        )

    def enter_address_line_1(
        self,
        address: str,
    ) -> None:
        """Enter primary address."""
        self.type(
            CheckoutAddressLocators.ADDRESS_LINE_1,
            address,
        )

    def enter_address_line_2(
        self,
        address: str,
    ) -> None:
        """Enter optional secondary address."""
        if address:
            self.type(
                CheckoutAddressLocators.ADDRESS_LINE_2,
                address,
            )

    def enter_city(
        self,
        city: str,
    ) -> None:
        """Enter city."""
        self.type(
            CheckoutAddressLocators.CITY,
            city,
        )

    def enter_state_region(
        self,
        state_region: str,
    ) -> None:
        """Enter state or region."""
        self.type(
            CheckoutAddressLocators.STATE_REGION,
            state_region,
        )

    def enter_zip_code(
        self,
        zip_code: str,
    ) -> None:
        """Enter ZIP or postal code."""
        self.type(
            CheckoutAddressLocators.ZIP_CODE,
            zip_code,
        )

    def enter_country(
        self,
        country: str,
    ) -> None:
        """Enter country."""
        self.type(
            CheckoutAddressLocators.COUNTRY,
            country,
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
        """
        Fill the complete checkout address form.

        This method uses the individual field methods so both
        approaches remain available to tests.
        """

        self.enter_full_name(full_name)

        self.enter_address_line_1(address1)

        if address2:
            self.enter_address_line_2(address2)

        self.enter_city(city)

        self.enter_state_region(state)

        self.enter_zip_code(zip_code)

        self.enter_country(country)

        self.hide_keyboard()

    def continue_to_payment(self) -> None:
        """Submit address information and continue to payment."""
        self.hide_keyboard()

        self.click(
            CheckoutAddressLocators.TO_PAYMENT
        )