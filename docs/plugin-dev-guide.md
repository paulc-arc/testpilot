# Plugin 開發指南

## 1. 建立新 Plugin

目錄範例：

```text
plugins/
  your_plugin/
    __init__.py
    plugin.py
    agent-config.yaml   # 選配，若需 CLI agent/model 優先序
    cases/
      _template.yaml
      your_test.yaml
```

`plugin.py` 需定義 `Plugin` 並繼承 `PluginBase`。

```python
from pathlib import Path
from testpilot.core.plugin_base import PluginBase
from testpilot.schema.case_schema import load_cases_dir

class Plugin(PluginBase):
    @property
    def name(self) -> str:
        return "your_plugin"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def cases_dir(self) -> Path:
        return Path(__file__).parent / "cases"

    def discover_cases(self):
        return load_cases_dir(self.cases_dir)

    def setup_env(self, case, topology) -> bool:
        ...

    def verify_env(self, case, topology) -> bool:
        ...

    def execute_step(self, case, step, topology) -> dict:
        ...

    def evaluate(self, case, results) -> bool:
        ...

    def teardown(self, case, topology) -> None:
        ...
```

## 2. Test Case YAML 最低欄位

必要欄位：`id`, `name`, `topology`, `steps`, `pass_criteria`

```yaml
id: "unique-case-id"
name: "Human-readable name"
topology:
  devices:
    DUT:
      role: ap
      transport: serial
steps:
  - id: step1
    action: exec
    target: DUT
    command: "..."
pass_criteria:
  - field: result
    operator: contains
    value: expected
```

變數可用 `{{VAR}}`，由 `testbed.variables` 替換。

## 3. 判讀責任契約（重要）

1. `plugin.evaluate()`：主判預期內條件（pass_criteria）。
2. `agent audit`：補判預期外異常（身份錯配、資料來源不一致、上下文異常）。
3. 合併輸出：`Pass` / `Fail` / `Inconclusive`。

建議每步至少保留以下證據欄位：

1. `band`
2. `target identity`（DUT/STA 實體識別）
3. `raw output`
4. `step trace`（命令、時間、回傳碼）

## 4. Agent Config（plugin 級）

若 plugin 需要指定 CLI agent/model 優先序，使用：

- `plugins/<plugin>/agent-config.yaml`

格式：

```yaml
version: 1
default_mode: headless
selection_policy:
  fallback: automatic
  on_unavailable: next_priority
execution:
  scope: per_case
  mode: sequential
  max_concurrency: 1
  failure_policy: retry_then_fail_and_continue
  retry:
    max_attempts: 2
    backoff_seconds: 5
  timeout:
    base_seconds: 120
    per_step_seconds: 45
    retry_multiplier: 1.25
    max_seconds: 900
runners:
  - priority: 1
    cli_agent: codex
    model: gpt-5.3-codex
    effort: high
    enabled: true
  - priority: 2
    cli_agent: copilot
    model: sonnet-4.6
    effort: high
    enabled: true
```

規則：

1. 依 `priority` 選擇。
2. 第一優先不可用時可自動降級。
3. `scope=per_case` 時，每個 case 都需獨立做 runner 選擇與呼叫。
4. `mode=sequential` 時，`max_concurrency` 應為 `1`。
5. `failure_policy=retry_then_fail_and_continue` 時，單 case 失敗不得中止整批 run。
6. 必須記錄 per-case selection trace（含降級原因）。
7. timeout 應隨 retry attempt 調整（建議採倍增或倍率增長並設上限）。

## 5. Transport 類型慣例

| 類型 | 用途 | config key |
|---|---|---|
| serial | UART/serialwrap 控 DUT | `transport: serial` |
| adb | 控制 Android STA | `transport: adb` |
| ssh | 控制 EndpointPC/遠端設備 | `transport: ssh` |

參考：`plugins/wifi_llapi/cases/_template.yaml`
