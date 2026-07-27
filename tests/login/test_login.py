"""Login integration tests."""

import pytest
from appium.webdriver.webdriver import WebDriver

from app.pages.cart_page import CartPage
from app.pages.checkout_address_page import CheckoutAddressPage
from app.pages.login_page import LoginPage
from app.pages.product_details_page import ProductDetailsPage
from app.pages.products_page import ProductsPage
from core.utils.json_reader import JsonReader


@pytest.mark.regression
class TestLogin:

    def test_valid_login_during_checkout(
        self,
        driver: WebDriver,
    ) -> None:
        """
        Verify checkout navigation for a valid user.

        Flow:
            Products
            -> Product Details
            -> Add To Cart
            -> Cart
            -> Checkout
            -> Login (when required)
            -> Checkout Address
        """

        users = JsonReader.read(
            "resources/json/users.json"
        )

        user = users["standard_user"]

        # --------------------------------------------------
        # Step 1: Products screen
        # --------------------------------------------------

        products = ProductsPage(driver)

        assert products.is_loaded(), (
            "Products screen was not displayed."
        )

        # --------------------------------------------------
        # Step 2: Open product
        # --------------------------------------------------

        products.open_product(
            "Sauce Labs Backpack"
        )

        details = ProductDetailsPage(driver)

        # --------------------------------------------------
        # Step 3: Add product to cart
        # --------------------------------------------------

        details.add_to_cart()
        details.open_cart()

        # --------------------------------------------------
        # Step 4: Verify cart
        # --------------------------------------------------

        cart = CartPage(driver)

        assert cart.is_loaded(), (
            "Cart screen was not displayed."
        )

        # --------------------------------------------------
        # Step 5: Proceed to checkout
        # --------------------------------------------------

        cart.checkout()

        login = LoginPage(driver)
        address = CheckoutAddressPage(driver)

        # --------------------------------------------------
        # Step 6: Handle authentication state
        # --------------------------------------------------

        if login.is_loaded():

            login.login(
                user["username"],
                user["password"],
            )

            assert address.is_loaded(), (
                "Valid login did not navigate "
                "to checkout address screen."
            )

        else:

            # User may already be authenticated.
            assert address.is_loaded(), (
                "Checkout did not navigate to either "
                "the login screen or checkout address screen."
            )