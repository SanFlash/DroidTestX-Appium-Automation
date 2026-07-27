"""Central configuration loader."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

from core.exceptions.framework_exceptions import ConfigurationError


class ConfigManager:
    """Load and expose framework configuration."""

    _instance: "ConfigManager | None" = None

    def __new__(cls) -> "ConfigManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        self._root_dir = Path(__file__).resolve().parents[2]

        config_override = os.getenv("FRAMEWORK_CONFIG")

        if config_override:
            self._config_path = Path(config_override).resolve()
        else:
            self._config_path = (
                self._root_dir
                / "resources"
                / "env"
                / "config.yaml"
            )

        self._data = self._load_yaml()
        self._initialized = True

    def _load_yaml(self) -> dict[str, Any]:
        if not self._config_path.exists():
            raise ConfigurationError(
                f"Configuration file does not exist: "
                f"{self._config_path}"
            )

        try:
            with self._config_path.open(
                "r",
                encoding="utf-8",
            ) as config_file:
                data = yaml.safe_load(config_file) or {}
        except yaml.YAMLError as exc:
            raise ConfigurationError(
                f"Invalid YAML in {self._config_path}: {exc}"
            ) from exc

        if not isinstance(data, dict):
            raise ConfigurationError(
                "Root configuration must be a YAML mapping."
            )

        return data

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a configuration value using dot notation.

        Example:
            config.get("device.udid")
            config.get("timeouts.explicit_wait", 15)
        """

        current: Any = self._data

        for part in key.split("."):
            if not isinstance(current, dict) or part not in current:
                return default

            current = current[part]

        return current

    def require(self, key: str) -> Any:
        """Return a required value or raise ConfigurationError."""

        value = self.get(key)

        if value is None or value == "":
            raise ConfigurationError(
                f"Required configuration is missing: {key}"
            )

        return value

    @property
    def root_dir(self) -> Path:
        return self._root_dir

    @property
    def config_path(self) -> Path:
        return self._config_path