"""Products screen smoke tests."""

import pytest
from appium.webdriver.webdriver import WebDriver

from app.pages.products_page import ProductsPage


@pytest.mark.smoke
class TestProducts:

    def test_products_screen_loads(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        assert products.is_loaded(), (
            "Products screen did not load."
        )

    def test_products_title(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        assert products.get_title() == "Products"

    def test_backpack_is_displayed(
        self,
        driver: WebDriver,
    ) -> None:

        products = ProductsPage(driver)

        assert products.product_is_visible(
            "Sauce Labs Backpack"
        )