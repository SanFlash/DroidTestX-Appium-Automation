"""Global Pytest configuration and Appium fixtures."""

from __future__ import annotations

from typing import Generator

import pytest
from appium.webdriver.webdriver import WebDriver

from core.driver.driver_factory import DriverFactory
from core.logging.logger import get_logger
from core.reporting.screenshot_manager import ScreenshotManager


logger = get_logger(__name__)

APP_PACKAGE = "com.saucelabs.mydemoapp.rn"


def _prepare_application(driver: WebDriver) -> None:
    """
    Put the application into a predictable state before each test.

    This method restarts the application process so every test begins
    from the application's launch flow rather than the screen left
    behind by the previous test.

    Important:
        Application data reset is controlled separately by the Appium
        capabilities configured in DriverFactory.
    """

    logger.info("Preparing application for test execution.")

    try:
        driver.terminate_app(APP_PACKAGE)
        logger.info("Application terminated successfully.")

    except Exception:
        logger.debug(
            "Application was not running or could not be terminated.",
            exc_info=True,
        )

    try:
        driver.activate_app(APP_PACKAGE)
        logger.info("Application activated successfully.")

    except Exception:
        logger.exception(
            "Unable to activate application: %s",
            APP_PACKAGE,
        )
        raise


def _cleanup_application(driver: WebDriver) -> None:
    """
    Perform safe cleanup after a test.

    Cleanup failures must not hide the original test result.
    """

    try:
        driver.terminate_app(APP_PACKAGE)
        logger.info("Application terminated during cleanup.")

    except Exception:
        logger.debug(
            "Unable to terminate application during cleanup.",
            exc_info=True,
        )


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """
    Create an isolated Appium session for every test.

    Lifecycle:
        create driver
            ->
        prepare application
            ->
        execute test
            ->
        capture failure evidence through pytest hook
            ->
        cleanup application
            ->
        quit driver

    The function scope guarantees that each test receives its own
    Appium WebDriver session.
    """

    logger.info("=" * 70)
    logger.info("Starting new test session")

    appium_driver: WebDriver | None = None

    try:
        # ---------------------------------------------------------
        # 1. CREATE DRIVER
        # ---------------------------------------------------------
        appium_driver = DriverFactory.create_android_driver()

        logger.info(
            "Appium driver created. Session ID=%s",
            appium_driver.session_id,
        )

        # ---------------------------------------------------------
        # 2. PREPARE APPLICATION
        # ---------------------------------------------------------
        _prepare_application(appium_driver)

        # ---------------------------------------------------------
        # 3. PROVIDE DRIVER TO TEST
        # ---------------------------------------------------------
        yield appium_driver

    finally:
        # ---------------------------------------------------------
        # 4. CLEANUP
        # ---------------------------------------------------------
        if appium_driver is not None:

            _cleanup_application(appium_driver)

            try:
                DriverFactory.quit_driver(appium_driver)

            except Exception:
                logger.exception(
                    "Unable to quit Appium driver cleanly."
                )

        logger.info("Test session finished")
        logger.info("=" * 70)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(
    item: pytest.Item,
    call: pytest.CallInfo,
):
    """
    Process pytest test results.

    Automatically capture a screenshot when the actual test body
    fails.

    Reports are also attached to the pytest item as:

        item.rep_setup
        item.rep_call
        item.rep_teardown
    """

    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report,
    )

    # We only capture screenshots for failures occurring during
    # the actual test execution.
    if (
        report.when == "call"
        and report.failed
        and "driver" in item.funcargs
    ):

        appium_driver = item.funcargs["driver"]

        if appium_driver is None:
            logger.error(
                "Cannot capture screenshot because driver is None."
            )
            return

        try:
            screenshot_path = ScreenshotManager.capture(
                appium_driver,
                item.name,
            )

            logger.error(
                "Failure screenshot captured: %s",
                screenshot_path,
            )

        except Exception:
            logger.exception(
                "Unable to capture failure screenshot."
            )