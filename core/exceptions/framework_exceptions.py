"""Custom exceptions used by the automation framework."""


class FrameworkError(Exception):
    """Base exception for framework-specific errors."""


class ConfigurationError(FrameworkError):
    """Raised when framework configuration is invalid."""


class DriverCreationError(FrameworkError):
    """Raised when an Appium driver session cannot be created."""


class ElementActionError(FrameworkError):
    """Raised when an operation on an application element fails."""


class ADBError(FrameworkError):
    """Raised when execution of an ADB command fails."""