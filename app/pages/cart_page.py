from appium.webdriver.webdriver import WebDriver

from app.locators.cart_locators import CartLocators
from core.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        return self.is_displayed(
            CartLocators.SCREEN
        )

    def contains_product(
        self,
        name: str,
    ) -> bool:

        return self.is_displayed(
            CartLocators.product(name)
        )

    def get_total_items(self) -> str:
        return self.get_text(
            CartLocators.TOTAL_NUMBER
        )

    def get_total_price(self) -> str:
        return self.get_text(
            CartLocators.TOTAL_PRICE
        )

    def get_product_names(
        self,
    ) -> list[str]:

        elements = self.driver.find_elements(
            *CartLocators.PRODUCT_LABELS
        )

        return [
            element.text
            for element in elements
        ]

    def checkout(self) -> None:
        self.click(
            CartLocators.CHECKOUT_BUTTON
        )