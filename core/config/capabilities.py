"""Appium Android capability builder."""

from __future__ import annotations

from appium.options.android import UiAutomator2Options

from core.config.config_manager import ConfigManager


class AndroidCapabilities:
    """
    Build Android UiAutomator2 capabilities.

    Framework strategy:
        - Start every Appium session with a clean application state.
        - Do not uninstall/reinstall the APK for every test.
        - Automatically grant required permissions.
        - Launch the configured application package/activity.
        - Keep the framework suitable for isolated pytest execution.
    """

    def __init__(
        self,
        config: ConfigManager | None = None,
    ) -> None:
        self.config = config or ConfigManager()

    def build(self) -> UiAutomator2Options:
        """Build and return UiAutomator2Options."""

        options = UiAutomator2Options()

        # ---------------------------------------------------------
        # PLATFORM / AUTOMATION
        # ---------------------------------------------------------

        options.platform_name = self.config.require(
            "device.platform_name"
        )

        options.automation_name = self.config.require(
            "device.automation_name"
        )

        # ---------------------------------------------------------
        # DEVICE
        # ---------------------------------------------------------

        options.device_name = self.config.require(
            "device.device_name"
        )

        options.udid = self.config.require(
            "device.udid"
        )

        # ---------------------------------------------------------
        # APPLICATION
        # ---------------------------------------------------------

        options.app_package = self.config.require(
            "application.package"
        )

        options.app_activity = self.config.require(
            "application.activity"
        )

        # ---------------------------------------------------------
        # APPLICATION STATE MANAGEMENT
        # ---------------------------------------------------------
        #
        # noReset=False
        #
        # Do not preserve application data between Appium sessions.
        # This helps tests start from a predictable application
        # state instead of inheriting cart/quantity/session data.
        #
        # fullReset=False
        #
        # Do NOT uninstall/reinstall the APK for every test.
        # Reinstalling would make the suite unnecessarily slow.
        # ---------------------------------------------------------

        options.no_reset = bool(
            self.config.get(
                "capabilities.no_reset",
                False,
            )
        )

        options.full_reset = bool(
            self.config.get(
                "capabilities.full_reset",
                False,
            )
        )

        # ---------------------------------------------------------
        # PERMISSIONS
        # ---------------------------------------------------------

        options.auto_grant_permissions = bool(
            self.config.get(
                "capabilities.auto_grant_permissions",
                True,
            )
        )

        # ---------------------------------------------------------
        # SESSION TIMEOUT
        # ---------------------------------------------------------

        options.new_command_timeout = int(
            self.config.get(
                "capabilities.new_command_timeout",
                300,
            )
        )

        return options