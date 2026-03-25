"""Template plugin — copy this directory to create a new plugin."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from testpilot.core.plugin_base import PluginBase


class Plugin(PluginBase):
    """Minimal plugin template. Replace stubs with real implementation."""

    @property
    def name(self) -> str:
        return "template"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def cases_dir(self) -> Path:
        return Path(__file__).parent / "cases"

    def discover_cases(self) -> list[dict[str, Any]]:
        cases: list[dict[str, Any]] = []
        if not self.cases_dir.is_dir():
            return cases
        for yaml_file in sorted(self.cases_dir.glob("*.yaml")):
            if yaml_file.stem.startswith("_"):
                continue
            import yaml
            data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("id", yaml_file.stem)
                cases.append(data)
        return cases

    def setup_env(self, case: dict[str, Any], topology: Any) -> bool:
        return True

    def verify_env(self, case: dict[str, Any], topology: Any) -> bool:
        return True

    def execute_step(self, case: dict[str, Any], step: dict[str, Any], topology: Any) -> dict[str, Any]:
        return {"success": True, "output": "", "captured": {}, "timing": 0.0}

    def evaluate(self, case: dict[str, Any], results: dict[str, Any]) -> bool:
        return True

    def teardown(self, case: dict[str, Any], topology: Any) -> None:
        pass
