"""Page Object for the Sauce Labs My Demo App login screen."""

from __future__ import annotations

from appium.webdriver.webdriver import WebDriver

from app.locators.login_locators import LoginLocators
from core.base_page import BasePage


class LoginPage(BasePage):
    """Page Object representing the Login screen."""

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def is_loaded(self) -> bool:
        """
        Verify that the Login screen is displayed using
        actual interactive elements on the screen.
        """

        username_visible = self.is_displayed(
            LoginLocators.USERNAME,
            timeout=10,
        )

        password_visible = self.is_displayed(
            LoginLocators.PASSWORD,
            timeout=5,
        )

        login_button_visible = self.is_displayed(
            LoginLocators.LOGIN_BUTTON,
            timeout=5,
        )

        return (
            username_visible
            and password_visible
            and login_button_visible
        )

    def enter_username(
        self,
        username: str,
    ) -> None:
        self.type(
            LoginLocators.USERNAME,
            username,
        )

    def enter_password(
        self,
        password: str,
    ) -> None:
        self.type(
            LoginLocators.PASSWORD,
            password,
        )

    def tap_login(self) -> None:
        self.hide_keyboard()

        self.click(
            LoginLocators.LOGIN_BUTTON
        )

    def login(
        self,
        username: str,
        password: str,
    ) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

    def autofill_standard_user(self) -> None:
        self.click(
            LoginLocators.BOB_AUTOFILL
        )

    def autofill_locked_user(self) -> None:
        self.click(
            LoginLocators.LOCKED_USER_AUTOFILL
        )

    def get_generic_error(self) -> str:
        return self.get_text(
            LoginLocators.GENERIC_ERROR
        )

    def get_username_error(self) -> str:
        return self.get_text(
            LoginLocators.USERNAME_ERROR
        )

    def get_password_error(self) -> str:
        return self.get_text(
            LoginLocators.PASSWORD_ERROR
        )