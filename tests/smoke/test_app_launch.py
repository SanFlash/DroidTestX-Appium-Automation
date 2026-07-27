"""Framework smoke test."""

from appium.webdriver.webdriver import WebDriver

from core.config.config_manager import ConfigManager


def test_application_launches(
    driver: WebDriver,
) -> None:
    config = ConfigManager()

    expected_package = config.require(
        "application.package"
    )

    assert (
        driver.current_package
        == expected_package
    ), (
        f"Expected package "
        f"{expected_package}, "
        f"but found "
        f"{driver.current_package}"
    )