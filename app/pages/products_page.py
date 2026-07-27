from __future__ import annotations

from appium.webdriver.webdriver import WebDriver

from app.locators.common_locators import CommonLocators
from app.locators.products_locators import ProductsLocators
from core.base_page import BasePage


class ProductsPage(BasePage):
    """Page Object representing the Products catalogue."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        return self.is_displayed(
            ProductsLocators.SCREEN
        )

    def get_title(self) -> str:
        return self.get_text(
            ProductsLocators.TITLE
        )

    def open_menu(self) -> None:
        self.click(
            CommonLocators.MENU_BUTTON
        )

    def open_cart(self) -> None:
        self.click(
            CommonLocators.CART_BUTTON
        )

    def open_sort(self) -> None:
        self.click(
            ProductsLocators.SORT_BUTTON
        )

    def open_product(self, name: str) -> None:
        self.click(
            ProductsLocators.product(name)
        )

    def product_is_visible(
        self,
        name: str,
    ) -> bool:
        return self.is_displayed(
            ProductsLocators.product(name)
        )

    def get_visible_product_names(
        self,
    ) -> list[str]:

        elements = self.driver.find_elements(
            *ProductsLocators.PRODUCT_NAMES
        )

        return [
            element.text
            for element in elements
            if element.text
        ]

    def get_visible_prices(
        self,
    ) -> list[str]:

        elements = self.driver.find_elements(
            *ProductsLocators.PRODUCT_PRICES
        )

        return [
            element.text
            for element in elements
            if element.text
        ]