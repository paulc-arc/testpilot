# D283 getScanResults() RSSI blocker

## Status

- case id: `d283-getscanresults-rssi`
- current YAML: `plugins/wifi_llapi/cases/D283_getscanresults_rssi.yaml`
- workbook authority: `0401.xlsx` `Wifi_LLAPI` row `283`
- current YAML row metadata: `285`
- latest full-run evidence: `20260409T213837737224`
- latest isolated rerun: `20260411T214050136894` (hung after `setup_env`)
- status: blocked
- blocker type: **the committed full-payload replay still hangs on the 6G scan path, and the active public `RSSI` field is the same `ssid->rssi` family already shared with `D286 SignalStrength`**

## Why this case is blocked

The old D283 blocker said this row was blocked on the same raw 6G scan transport issue as D277. That is no longer precise enough.

`D277` was eventually unblocked by switching its workbook-style replay to a transport-safe first-object capture. `D283` has now been re-tested on the current repo state, and the **committed generic full-payload case still hangs** after `setup_env`. So the old transport problem is still real for the current D283 shape, even though D277 itself has since been aligned with a different replay strategy.

At the same time, active 0403 source tracing shows D283 is not an isolated source path:

1. `wld_nl80211_parser.c` fills `pResult->rssi` from `NL80211_BSS_SIGNAL_UNSPEC` or `NL80211_BSS_SIGNAL_MBM`
2. `wld_rad_scan.c` serializes public `RSSI` from `ssid->rssi`
3. the same file also serializes public `SignalStrength` from that same `ssid->rssi`

So `D283 RSSI` and `D286 SignalStrength` are the same public field family on the active ubus path. Until a transport-safe replay exists for D283 and a durable same-source oracle exists for the shared `ssid->rssi` family, no YAML rewrite is justified.

## Active public 0403 source path

Key citations:

- `src/nl80211/wld_nl80211_parser.c:1471-1482`
  - fills `pResult->rssi` from `NL80211_BSS_SIGNAL_UNSPEC` or `NL80211_BSS_SIGNAL_MBM`
- `src/RadMgt/wld_rad_scan.c:584`
  - serializes public `RSSI = ssid->rssi`
- `src/RadMgt/wld_rad_scan.c:588`
  - serializes public `SignalStrength = ssid->rssi`
- `src/RadMgt/wld_rad_scan.c:1510`
  - the diagnostic scan map also serializes `SignalStrength = pSsid->rssi`

The older Broadcom path still exists:

- `bcmdrivers/.../wldm_lib_wifi.c:892`
  - maps neighboring diagnostic `SignalStrength` to raw `RSSI: `
- `bcmdrivers/.../wldm_lib_wifi.c:4928-4933`
  - parses that token into `neighbor[i].ap_SignalStrength`

But that legacy parser is not enough to treat D283 as an independent source line anymore; the active public ubus model clearly exposes both `RSSI` and `SignalStrength` from the same `ssid->rssi` field.

## Live evidence

### Historical full-run evidence (`20260409T213837737224`)

- `0410summary.md` rows `277-290` already showed `step_6g_scan (failed after 2/2 attempts)`
- `bgw720-0403-verify_wifi_llapi_20260409t213837737224.md` recorded D283 as `step failed: step_6g_scan`, with failure snapshot `serialwrap cmd status timeout`

### Older isolated rerun (`20260410T164405221878`)

- run never emitted step output after `setup_env`
- no per-case agent-trace JSON was written
- after the hung run was stopped, `COM0` briefly regressed to `ATTACHED / PROMPT_TIMEOUT` before self-test recovered it to `READY`

### Current isolated rerun on the aligned repo state (`20260411T214050136894`)

Command:

```bash
uv run python -m testpilot.cli run wifi_llapi --case d283-getscanresults-rssi --dut-fw-ver BGW720-0403
```

Observed shape:

1. runner reached only:

```text
[wifi_llapi] setup_env: d283-getscanresults-rssi connected=True devices=['DUT']
```

2. no step output followed
3. no top-level markdown/json/xlsx report files were produced
4. `plugins/wifi_llapi/reports/agent_trace/20260411T214050136894/` was created but remained empty
5. after the hung run was stopped:
   - `COM1` recovered back to `READY / OK`
   - `COM0` became `TARGET_UNRESPONSIVE` and required recovery before returning to `READY / OK`

So the current committed D283 shape still reproduces a real transport-stage hang.

## Decision

1. keep `D283` blocked on the current committed full-payload transport issue
2. do not rewrite `plugins/wifi_llapi/cases/D283_getscanresults_rssi.yaml` yet
3. if this row is reopened, the first step should be a **local-only transport-safe first-object replay** (like the eventual D277 strategy), not another full-payload generic rerun
4. after transport is made safe, treat D283 together with the shared `ssid->rssi` field family already evidenced in `D286_block.md`
