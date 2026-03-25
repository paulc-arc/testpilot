"""ExecutionEngine — case execution with retry, timeout escalation, and trace writing."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from testpilot.core.case_utils import safe_float
from testpilot.core.runner_selector import RunnerSelector

log = logging.getLogger(__name__)


class ExecutionEngine:
    """Execute a single case through plugin hooks with retry and timeout escalation."""

    def __init__(self, config: Any) -> None:
        self.config = config

    @staticmethod
    def attempt_timeout_seconds(
        *,
        steps_count: int,
        attempt_index: int,
        execution_policy: dict[str, Any],
    ) -> float:
        timeout = execution_policy.get("timeout", {})
        if not isinstance(timeout, dict):
            timeout = {}
        base_seconds = max(1.0, safe_float(timeout.get("base_seconds"), 120.0))
        per_step_seconds = max(0.0, safe_float(timeout.get("per_step_seconds"), 45.0))
        retry_multiplier = max(1.0, safe_float(timeout.get("retry_multiplier"), 1.25))
        max_seconds = max(1.0, safe_float(timeout.get("max_seconds"), 900.0))

        raw_timeout = (base_seconds + max(0, steps_count) * per_step_seconds) * (
            retry_multiplier ** max(0, attempt_index - 1)
        )
        return min(max_seconds, raw_timeout)

    def execute_case_once(
        self,
        plugin: Any,
        case: dict[str, Any],
        *,
        attempt_index: int,
        attempt_timeout_seconds: float,
        runner: dict[str, Any],
    ) -> dict[str, Any]:
        """Run setup → verify → steps → evaluate → teardown for one attempt."""
        commands: list[str] = []
        outputs: list[str] = []
        verdict = False
        comment = ""

        runtime_case = dict(case)
        runtime_case["_agent_runner"] = RunnerSelector.runner_summary(runner)
        runtime_case["_attempt_index"] = attempt_index
        runtime_case["_attempt_timeout_seconds"] = attempt_timeout_seconds

        try:
            setup_ok = bool(plugin.setup_env(runtime_case, topology=self.config))
            if not setup_ok:
                comment = "setup_env failed"
            env_ok = setup_ok and bool(plugin.verify_env(runtime_case, topology=self.config))
            if setup_ok and not env_ok:
                comment = "env_verify gate failed"

            step_results: dict[str, Any] = {}
            raw_steps = runtime_case.get("steps", [])
            steps = raw_steps if isinstance(raw_steps, list) else []
            if env_ok:
                for step in steps:
                    step_data = dict(step) if isinstance(step, dict) else {"id": "step", "command": str(step)}
                    step_id = str(step_data.get("id", "step"))
                    command = str(step_data.get("command", "")).strip()
                    if command:
                        commands.append(command)

                    step_payload = dict(step_data)
                    step_payload.setdefault("timeout", attempt_timeout_seconds)
                    step_payload["_attempt_index"] = attempt_index
                    step_payload["_attempt_timeout_seconds"] = attempt_timeout_seconds

                    result = plugin.execute_step(runtime_case, step_payload, topology=self.config)
                    step_results[step_id] = result
                    out = str(result.get("output", "")).strip()
                    if out:
                        outputs.append(out)
                    if not bool(result.get("success", False)):
                        comment = f"step failed: {step_id}"
                        break

                if not comment:
                    verdict = bool(plugin.evaluate(runtime_case, {"steps": step_results}))
                    if not verdict:
                        comment = "pass_criteria not satisfied"

        except Exception as exc:  # pragma: no cover - defensive catch for runtime errors
            comment = f"exception: {exc}"
        finally:
            try:
                plugin.teardown(runtime_case, topology=self.config)
            except Exception:
                log.exception("teardown failed: %s", runtime_case.get("id", "?"))

        return {
            "verdict": verdict,
            "comment": comment,
            "commands": commands,
            "outputs": outputs,
        }

    @staticmethod
    def write_case_trace(path: Path, payload: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
