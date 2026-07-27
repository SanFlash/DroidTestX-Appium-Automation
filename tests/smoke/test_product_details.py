"""Product details tests."""

import pytest
from appium.webdriver.webdriver import WebDriver

from app.pages.product_details_page import ProductDetailsPage
from app.pages.products_page import ProductsPage


@pytest.mark.smoke
class TestProductDetails:

    def test_open_backpack(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        assert products.is_loaded()

        products.open_product(
            "Sauce Labs Backpack"
        )

        details = ProductDetailsPage(driver)

        assert details.is_loaded(), (
            "Product details screen did not load."
        )

    def test_default_quantity_is_one(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        products.open_product(
            "Sauce Labs Backpack"
        )

        details = ProductDetailsPage(driver)

        assert details.get_quantity() == "1"
    
    
    def test_increase_product_quantity(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        products.open_product(
            "Sauce Labs Backpack"
        )

        details = ProductDetailsPage(driver)

        assert details.get_quantity() == "1"

        details.increase_quantity()

        assert details.get_quantity() == "2"

        details.increase_quantity(2)

        assert details.get_quantity() == "4"