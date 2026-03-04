# Phase 5：CLI & Integration

## Scope

強化 CLI、整合測試與 plugin agent case-level 選擇/降級留痕。

## Current Status

1. CLI 已有 `run/list` 與 `wifi-llapi build-template-report`。
2. Orchestrator 對 `wifi_llapi` 已有專屬流程。
3. 已定案策略：每個 test case 各自呼叫 agent，並採 sequential 執行。

## Gaps

1. 非 `wifi_llapi` plugin 仍為 skeleton run。
2. integration tests 尚未補齊。
3. plugin agent-config 的 per-case runtime selector 尚未實作。
4. retry-aware timeout（依 attempt 調整）尚未實作。
5. per-case trace artifact writer 尚未實作。

## Acceptance Criteria

1. CLI 行為與文件一致。
2. 具備 integration tests（mock transport + 主要流程）。
3. 每個 case 都有獨立的 agent selection/fallback trace 可供稽核。
4. scheduler 可保證 sequential（`max_concurrency=1`）。
5. case failure 採 retry 後 fail and continue，不中止整批 run。

## Related Todo IDs

- `P5-01` ~ `P5-09`
