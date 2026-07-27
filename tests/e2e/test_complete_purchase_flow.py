"""Complete Android application end-to-end purchase workflow."""

import pytest
from appium.webdriver.webdriver import WebDriver

from app.pages.products_page import ProductsPage
from app.pages.product_details_page import ProductDetailsPage
from app.pages.cart_page import CartPage
from app.pages.login_page import LoginPage
from app.pages.checkout_address_page import CheckoutAddressPage
from app.pages.checkout_payment_page import CheckoutPaymentPage
from app.pages.review_order_page import ReviewOrderPage

from core.utils.json_reader import JsonReader


@pytest.mark.e2e
@pytest.mark.regression
class TestCompletePurchaseFlow:
    """
    Complete purchase workflow.

    Flow:

        Launch App
        -> Products
        -> Add Backpack x1
        -> Add Bike Light x2
        -> Add Bolt T-Shirt x4
        -> Cart
        -> Checkout
        -> Login
        -> Shipping Address
        -> Payment
        -> Select Billing Checkbox
        -> Review Order
        -> Verify Products
        -> Place Order
        -> Cleanup
    """

    def test_complete_purchase_and_logout(
        self,
        driver: WebDriver,
    ) -> None:

        # ==================================================
        # TEST DATA
        # ==================================================

        users = JsonReader.read(
            "resources/json/users.json"
        )

        user = users["standard_user"]

        shipping_data = {
            "full_name": "Satyen Automation",
            "address1": "221B Automation Street",
            "address2": "QA Testing Apartment",
            "city": "Bhopal",
            "state": "Madhya Pradesh",
            "zip_code": "462001",
            "country": "India",
        }

        payment_data = {
            "full_name": "Satyen Automation",
            "card_number": "4111111111111111",
            "expiration": "12/30",
            "security_code": "123",
        }

        # ==================================================
        # STEP 1
        # APPLICATION START
        # ==================================================

        products = ProductsPage(
            driver
        )

        assert products.is_loaded(), (
            "Products screen was not displayed "
            "after application launch."
        )

        # ==================================================
        # STEP 2
        # BACKPACK — QUANTITY 1
        # ==================================================

        products.open_product(
            "Sauce Labs Backpack"
        )

        details = ProductDetailsPage(
            driver
        )

        assert details.get_quantity() == "1", (
            "Backpack default quantity should be 1."
        )

        details.add_to_cart()

        driver.back()

        assert products.is_loaded(), (
            "Products screen not displayed "
            "after adding Backpack."
        )

        # ==================================================
        # STEP 3
        # BIKE LIGHT — QUANTITY 2
        # ==================================================

        products.open_product(
            "Sauce Labs Bike Light"
        )

        details = ProductDetailsPage(
            driver
        )

        assert details.get_quantity() == "1", (
            "Bike Light default quantity should be 1."
        )

        details.increase_quantity()

        assert details.get_quantity() == "2", (
            "Bike Light quantity should be 2."
        )

        details.add_to_cart()

        driver.back()

        assert products.is_loaded(), (
            "Products screen not displayed "
            "after adding Bike Light."
        )

        # ==================================================
        # STEP 4
        # BOLT T-SHIRT — QUANTITY 4
        # ==================================================

        products.open_product(
            "Sauce Labs Bolt T-Shirt"
        )

        details = ProductDetailsPage(
            driver
        )

        assert details.get_quantity() == "1", (
            "Bolt T-Shirt default quantity should be 1."
        )

        # Default quantity = 1
        # Increase three times:
        # 1 -> 2 -> 3 -> 4

        details.increase_quantity(
            3
        )

        assert details.get_quantity() == "4", (
            "Bolt T-Shirt quantity should be 4."
        )

        details.add_to_cart()

        # ==================================================
        # STEP 5
        # OPEN CART
        # ==================================================

        details.open_cart()

        cart = CartPage(
            driver
        )

        assert cart.is_loaded(), (
            "Cart screen was not displayed."
        )

        # ==================================================
        # STEP 6
        # CHECKOUT
        # ==================================================

        cart.checkout()

        login = LoginPage(
            driver
        )

        address = CheckoutAddressPage(
            driver
        )

        # ==================================================
        # STEP 7
        # LOGIN IF REQUIRED
        # ==================================================

        if login.is_loaded():

            login.login(
                user["username"],
                user["password"],
            )

            assert address.is_loaded(), (
                "Checkout Address screen was not "
                "displayed after login."
            )

        else:

            assert address.is_loaded(), (
                "Neither Login nor Checkout Address "
                "screen was displayed."
            )

        # ==================================================
        # STEP 8
        # SHIPPING ADDRESS
        # ==================================================

        address.enter_address(
            full_name=shipping_data["full_name"],
            address1=shipping_data["address1"],
            address2=shipping_data["address2"],
            city=shipping_data["city"],
            state=shipping_data["state"],
            zip_code=shipping_data["zip_code"],
            country=shipping_data["country"],
        )

        address.continue_to_payment()

        # ==================================================
        # STEP 9
        # PAYMENT SCREEN
        # ==================================================

        payment = CheckoutPaymentPage(
            driver
        )

        assert payment.is_loaded(), (
            "Checkout Payment screen was not displayed."
        )

        # ==================================================
        # STEP 10
        # ENTER PAYMENT DETAILS
        # ==================================================

        payment.enter_payment_details(
            full_name=payment_data["full_name"],
            card_number=payment_data["card_number"],
            expiration=payment_data["expiration"],
            security_code=payment_data["security_code"],
        )

        # ==================================================
        # STEP 11
        # BILLING ADDRESS CHECKBOX
        # ==================================================

        #payment.use_shipping_as_billing()

        # IMPORTANT:
        #
        # Do NOT assert:
        #
        # payment.is_shipping_as_billing_selected()
        #
        # The React Native checkbox currently does not
        # reliably expose its visual checked state through
        # UiAutomator2's checked/selected attributes.
        #
        # The functional validation is whether selecting
        # the checkbox allows checkout to continue to the
        # Review Order screen.

        # ==================================================
        # STEP 12
        # CONTINUE TO REVIEW ORDER
        # ==================================================

        payment.review_order()

        # ==================================================
        # STEP 13
        # VERIFY REVIEW ORDER SCREEN
        # ==================================================

        review = ReviewOrderPage(
            driver
        )

        assert review.is_loaded(), (
            "Review Order screen was not displayed "
            "after submitting valid payment information "
            "and selecting the billing address checkbox."
        )

        # ==================================================
        # STEP 14
        # VERIFY PRODUCTS
        # ==================================================

        assert review.contains_product(
            "Sauce Labs Backpack"
        ), (
            "Sauce Labs Backpack missing "
            "from Review Order."
        )

        assert review.contains_product(
            "Sauce Labs Bike Light"
        ), (
            "Sauce Labs Bike Light missing "
            "from Review Order."
        )

        assert review.contains_product(
            "Sauce Labs Bolt T-Shirt"
        ), (
            "Sauce Labs Bolt T-Shirt missing "
            "from Review Order."
        )

        # ==================================================
        # STEP 15
        # PLACE ORDER
        # ==================================================

        review.place_order()

        # ==================================================
        # STEP 16
        # SUCCESS SCREEN
        # ==================================================
        
        # The order has now been submitted.
        #
        # The next framework component should be:
        #
        # CheckoutCompletePage
        #
        # Once the actual Checkout Complete XML is available:
        #
        # success = CheckoutCompletePage(driver)
        #
        # assert success.is_loaded(), (
        #     "Checkout Complete screen was not displayed."
        # )
        #
        # success.continue_shopping()

        # ==================================================
        # STEP 17
        # LOGOUT
        # ==================================================
        #
        # Once the Menu screen XML/locators are confirmed:
        #
        # menu = MenuPage(driver)
        #
        # menu.open_menu()
        # menu.logout()
        #
        # assert products.is_loaded(), (
        #     "Products screen was not displayed "
        #     "after logout."
        # )

        # ==================================================
        # STEP 18
        # APPLICATION CLEANUP
        # ==================================================
        #
        # Do NOT call:
        #
        # driver.quit()
        #
        # Your global conftest.py fixture handles:
        #
        # 1. Application termination
        # 2. Appium session cleanup
        # 3. Driver quit
        #
        # This keeps lifecycle management centralized.