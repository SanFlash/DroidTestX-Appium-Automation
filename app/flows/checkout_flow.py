from appium.webdriver.webdriver import WebDriver

from app.pages.cart_page import CartPage
from app.pages.checkout_address_page import CheckoutAddressPage
from app.pages.checkout_payment_page import CheckoutPaymentPage
from app.pages.login_page import LoginPage
from app.pages.review_order_page import ReviewOrderPage


class CheckoutFlow:
    """High-level checkout business workflow."""

    def __init__(
        self,
        driver: WebDriver,
    ) -> None:

        self.cart = CartPage(driver)
        self.login = LoginPage(driver)
        self.address = CheckoutAddressPage(driver)
        self.payment = CheckoutPaymentPage(driver)
        self.review = ReviewOrderPage(driver)

    def checkout_cart(self) -> None:
        assert self.cart.is_loaded(), (
            "Cart screen was not displayed."
        )

        self.cart.checkout()

    def login(
        self,
        username: str,
        password: str,
    ) -> None:

        assert self.login.is_loaded(), (
            "Login screen was not displayed."
        )

        self.login.login(
            username,
            password,
        )

    def enter_shipping_address(
        self,
        full_name: str,
        address1: str,
        city: str,
        state: str,
        zip_code: str,
        country: str,
        address2: str = "",
    ) -> None:

        assert self.address.is_loaded(), (
            "Checkout address screen was not displayed."
        )

        self.address.enter_address(
            full_name=full_name,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
        )

        self.address.continue_to_payment()

    def enter_payment(
        self,
        full_name: str,
        card_number: str,
        expiration: str,
        security_code: str,
    ) -> None:

        assert self.payment.is_loaded(), (
            "Payment screen was not displayed."
        )

        self.payment.enter_payment_details(
            full_name=full_name,
            card_number=card_number,
            expiration=expiration,
            security_code=security_code,
        )

        self.payment.review_order()

    def place_order(self) -> None:

        assert self.review.is_loaded(), (
            "Review Order screen was not displayed."
        )

        self.review.place_order()