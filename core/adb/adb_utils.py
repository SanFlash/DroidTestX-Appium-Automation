"""ADB command utilities."""

from __future__ import annotations

import subprocess

from core.exceptions.framework_exceptions import ADBError
from core.logging.logger import get_logger


logger = get_logger(__name__)


class ADBUtils:
    """Execute controlled ADB commands."""

    @staticmethod
    def execute(
        *arguments: str,
        timeout: int = 30,
    ) -> str:
        command = [
            "adb",
            *arguments,
        ]

        logger.debug(
            "Executing ADB command: %s",
            " ".join(command),
        )

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                timeout=timeout,
            )

        except (
            subprocess.TimeoutExpired,
            OSError,
        ) as exc:
            raise ADBError(
                f"Unable to execute ADB command: "
                f"{' '.join(command)}"
            ) from exc

        if result.returncode != 0:
            raise ADBError(
                result.stderr.strip()
                or "ADB command failed."
            )

        return result.stdout.strip()

    @classmethod
    def devices(cls) -> str:
        return cls.execute("devices")

    @classmethod
    def current_activity(cls) -> str:
        return cls.execute(
            "shell",
            "dumpsys",
            "window",
            "windows",
        )

    @classmethod
    def install_apk(
        cls,
        apk_path: str,
        replace: bool = True,
    ) -> str:
        arguments = ["install"]

        if replace:
            arguments.append("-r")

        arguments.append(apk_path)

        return cls.execute(*arguments)

    @classmethod
    def clear_app(
        cls,
        package: str,
    ) -> str:
        return cls.execute(
            "shell",
            "pm",
            "clear",
            package,
        )

    @classmethod
    def force_stop(
        cls,
        package: str,
    ) -> str:
        return cls.execute(
            "shell",
            "am",
            "force-stop",
            package,
        )