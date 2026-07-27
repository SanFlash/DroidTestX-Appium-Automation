"""Shopping cart integration tests."""

import pytest
from appium.webdriver.webdriver import WebDriver

from app.locators.common_locators import CommonLocators
from app.pages.cart_page import CartPage
from app.pages.product_details_page import ProductDetailsPage
from app.pages.products_page import ProductsPage


@pytest.mark.smoke
class TestCart:

    def test_add_backpack_to_cart(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        assert products.is_loaded()

        products.open_product(
            "Sauce Labs Backpack"
        )

        details = ProductDetailsPage(driver)

        assert details.is_loaded()

        details.add_to_cart()

        details.click(
            CommonLocators.CART_BUTTON
        )

        cart = CartPage(driver)

        assert cart.is_loaded(), (
            "Cart screen did not load."
        )

        assert cart.contains_product(
            "Sauce Labs Backpack"
        ), "Backpack was not found in cart."