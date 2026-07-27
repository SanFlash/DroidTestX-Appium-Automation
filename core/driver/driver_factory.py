"""Appium driver creation and destruction."""

from __future__ import annotations

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from core.config.capabilities import AndroidCapabilities
from core.config.config_manager import ConfigManager
from core.exceptions.framework_exceptions import DriverCreationError
from core.logging.logger import get_logger


logger = get_logger(__name__)


class DriverFactory:
    """Create Appium WebDriver sessions."""

    @staticmethod
    def create_android_driver() -> WebDriver:
        config = ConfigManager()

        server_url = config.require(
            "appium.server_url"
        )

        options = AndroidCapabilities(
            config
        ).build()

        logger.info(
            "Creating Android Appium session."
        )

        logger.info(
            "Device UDID: %s",
            config.require("device.udid"),
        )

        logger.info(
            "Application package: %s",
            config.require("application.package"),
        )

        try:
            driver = webdriver.Remote(
                command_executor=server_url,
                options=options,
            )

            logger.info(
                "Appium session created successfully. Session ID=%s",
                driver.session_id,
            )

            return driver

        except Exception as exc:
            logger.exception(
                "Unable to create Appium session."
            )

            raise DriverCreationError(
                "Failed to create Android Appium driver. "
                "Verify Appium server, ADB device status, "
                "UiAutomator2 installation, package and activity."
            ) from exc

    @staticmethod
    def quit_driver(
        driver: WebDriver | None,
    ) -> None:
        if driver is None:
            return

        try:
            session_id = driver.session_id

            driver.quit()

            logger.info(
                "Appium session closed. Session ID=%s",
                session_id,
            )

        except Exception:
            logger.exception(
                "Error while closing Appium driver."
            )