"""Page object for the Checkout Payment screen."""

from appium.webdriver.webdriver import WebDriver

from app.locators.checkout_payment_locators import (
    CheckoutPaymentLocators,
)
from core.base_page import BasePage
from core.logging.logger import get_logger


logger = get_logger(__name__)


class CheckoutPaymentPage(BasePage):
    """Checkout Payment page actions."""

    def __init__(
        self,
        driver: WebDriver,
    ) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """Verify that the payment screen is displayed."""

        return self.is_displayed(
            CheckoutPaymentLocators.SCREEN
        )

    def enter_full_name(
        self,
        full_name: str,
    ) -> None:
        """Enter cardholder full name."""

        self.type(
            CheckoutPaymentLocators.FULL_NAME,
            full_name,
        )

    def enter_card_number(
        self,
        card_number: str,
    ) -> None:
        """Enter payment card number."""

        self.type(
            CheckoutPaymentLocators.CARD_NUMBER,
            card_number,
        )

    def enter_expiration_date(
        self,
        expiration: str,
    ) -> None:
        """Enter card expiration date."""

        self.type(
            CheckoutPaymentLocators.EXPIRATION_DATE,
            expiration,
        )

    def enter_security_code(
        self,
        security_code: str,
    ) -> None:
        """Enter card security code."""

        self.type(
            CheckoutPaymentLocators.SECURITY_CODE,
            security_code,
        )

    def enter_payment_details(
        self,
        full_name: str,
        card_number: str,
        expiration: str,
        security_code: str,
    ) -> None:
        """Enter all required payment information."""

        self.enter_full_name(
            full_name
        )

        self.enter_card_number(
            card_number
        )

        self.enter_expiration_date(
            expiration
        )

        self.enter_security_code(
            security_code
        )

        self.hide_keyboard()

    def use_shipping_as_billing(
        self,
    ) -> None:
        """
        Select shipping address as billing address.

        The React Native checkbox may not reliably expose
        its checked/selected state through UiAutomator2.

        Therefore, the framework performs the user action
        and validates the result through successful
        navigation to the Review Order screen.
        """

        self.hide_keyboard()

        logger.info(
            "Selecting billing address same as shipping."
        )

        self.click(
            CheckoutPaymentLocators.BILLING_SAME_AS_SHIPPING
        )

        logger.info(
            "Billing address checkbox tapped."
        )

    def review_order(
        self,
    ) -> None:
        """Continue from Payment to Review Order."""

        self.hide_keyboard()

        logger.info(
            "Continuing to Review Order."
        )

        self.click(
            CheckoutPaymentLocators.REVIEW_ORDER
        )