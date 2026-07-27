"""JSON test-data reader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from core.config.config_manager import ConfigManager


class JsonReader:
    """Read framework JSON resources."""

    @staticmethod
    def read(relative_path: str) -> dict[str, Any]:
        root = ConfigManager().root_dir

        path = root / relative_path

        if not path.exists():
            raise FileNotFoundError(
                f"JSON file not found: {path}"
            )

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError(
                f"Expected JSON object in {path}"
            )

        return data