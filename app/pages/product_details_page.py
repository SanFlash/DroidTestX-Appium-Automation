from appium.webdriver.webdriver import WebDriver
from app.locators.common_locators import CommonLocators
from app.locators.product_details_locators import (
    ProductDetailsLocators,
)
from core.base_page import BasePage


class ProductDetailsPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        
    def open_cart(self) -> None:
        self.click(
        CommonLocators.CART_BUTTON
    )

    def is_loaded(self) -> bool:
        return self.is_displayed(
            ProductDetailsLocators.SCREEN
        )

    def get_price(self) -> str:
        return self.get_text(
            ProductDetailsLocators.PRICE
        )

    def get_description(self) -> str:
        return self.get_text(
            ProductDetailsLocators.DESCRIPTION
        )

    def get_quantity(self) -> str:
        element = self.find(
            ProductDetailsLocators.QUANTITY_VALUE
        )

        return element.text.strip()

    def increase_quantity(
        self,
        times: int = 1,
    ) -> None:
        """Increase product quantity by the requested amount."""

        if times < 1:
            raise ValueError(
                "times must be greater than or equal to 1."
            )

        for _ in range(times):
            self.click(
                ProductDetailsLocators.QUANTITY_PLUS
            )

    def decrease_quantity(self):
        self.click(
            ProductDetailsLocators.QUANTITY_MINUS
        )

    def add_to_cart(self):
        self.click(
            ProductDetailsLocators.ADD_TO_CART
        )

    

    def select_black(self) -> None:
        self.click(
            ProductDetailsLocators.BLACK_COLOR
        )

    def select_blue(self) -> None:
        self.click(
            ProductDetailsLocators.BLUE_COLOR
        )

    def select_gray(self) -> None:
        self.click(
            ProductDetailsLocators.GRAY_COLOR
        )

    def select_red(self) -> None:
        self.click(
            ProductDetailsLocators.RED_COLOR
        )