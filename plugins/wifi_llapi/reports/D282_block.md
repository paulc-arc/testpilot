# D282 getScanResults() OperatingStandards blocker

## Status

- case id: `d282-getscanresults-operatingstandards`
- current YAML: `plugins/wifi_llapi/cases/D282_getscanresults_operatingstandards.yaml`
- workbook authority: `0401.xlsx` `Wifi_LLAPI` row `282`
- current YAML row metadata: `284`
- disposition: **blocked / keep YAML unchanged**
- blocker type: **active 0403 public `OperatingStandards` is derived from nl80211 beacon/probe IE parsing, but there is still no durable external oracle that replays the same parsed bitmask path on all three bands**

## Why this case is blocked

The old blocker explanation mixed the legacy Broadcom `_wldm_get_standards()` helper with the active public `ubus-cli "WiFi.Radio.{i}.getScanResults()"` path. New source tracing shows the current public path is different.

For the active 0403 public getter, `OperatingStandards` is carried in `wld_scanResultSSID_t.operatingStandards`, copied out of parsed beacon/probe IEs, cached in `pRad->scanState.lastScanResults`, and finally serialized with `swl_radStd_toChar(..., SWL_RADSTD_FORMAT_STANDARD, 0)`.

That matters because the shared radio-standards model is a **bitmask**, not a single-value enum, and the shared header explicitly marks the older "legacy representation" as something to avoid. So cumulative LLAPI shapes such as `a,n,ac,ax`, `ax,be`, or `b,g,n,ax` are expected on the active public path and do not need to match the older Broadcom helper's `if / else-if` output shape.

The blocker is now narrower:

1. the old `wl escanresults`-style replay is not guaranteed to be the same-source oracle for public `OperatingStandards`
2. 6G still lacks a durable same-target external replay
3. 2.4G still shows an extra `be` on the external replay, which is more consistent with a capability/supported-family readout than with the active public `OperatingStandards` bitmask serialization

## Active public 0403 path

The active `ubus-cli "WiFi.Radio.{i}.getScanResults()"` chain is:

1. `wld_nl80211_getScanResultsPerFreqBand(...)` returns band-filtered scan results through the nl80211 scan callback path
2. `wld_nl80211_parser.c` parses `NL80211_BSS_INFORMATION_ELEMENTS` / `NL80211_BSS_BEACON_IES` with `swl_80211_parseInfoElementsBuffer(...)`
3. `s_copyScanInfoFromIEs(...)` copies `pWirelessDevIE->operatingStandards` into `wld_scanResultSSID_t.operatingStandards`
4. `wifiGen_rad_getScanResults(...)` returns copies of `pRad->scanState.lastScanResults`
5. `wld_rad_scan.c` serializes `ssid->operatingStandards` to the public `OperatingStandards` string with `SWL_RADSTD_FORMAT_STANDARD`

Key citations:

- `src/nl80211/wld_nl80211_scan.c:325-352`
- `src/nl80211/wld_nl80211_parser.c:1409-1426`
- `src/nl80211/wld_nl80211_parser.c:1524-1539`
- `src/Plugin/wifiGen_rad.c:1110-1119`
- `src/RadMgt/wld_rad_scan.c:602-605`
- `targets/BGW720-300/fs.build/public/include/prplos/swl/swl_common_radioStandards.h:128-172`

The critical shared-model points are:

- `swl_wirelessDevice_infoElements_t` stores both `operatingStandards` and `supportedStandards` as `swl_radioStandard_m` bitmasks
- `SWL_RADSTD_FORMAT_STANDARD` is the active public serialization format
- the shared header explicitly says the old legacy representation should be avoided

## Legacy Broadcom path that must not be treated as the active public authority

The older Broadcom helper still exists:

- `bcmdrivers/.../wldm_lib_wifi.c:4350-4418`

It parses `HT / VHT / HE / EHT` markers using an `if / else-if` chain and then does:

```c
/* Set OperatingStandards same as SupportedStandards */
strncpy(neighbor[i].ap_OperatingStandards, neighbor[i].ap_SupportedStandards,
        sizeof(neighbor[i].ap_OperatingStandards));
```

This helper is useful as a legacy comparison point, but it is not the same model as the active public ubus path:

1. it collapses `OperatingStandards` into the same string as `SupportedStandards`
2. it is based on Broadcom raw scan text heuristics
3. it does not express the shared-model bitmask semantics used by the active public path

So the older `_wldm_get_standards()` logic cannot be treated as the definitive authority for the current ubus row.

## Live replay that was tested and rejected

### Attempted command

```bash
uv run python -m testpilot.cli run wifi_llapi --case d282-getscanresults-operatingstandards --dut-fw-ver BGW720-0403
```

### Isolated rerun `20260410T163026194231`

Observed output shape:

```text
5G:
  LlapiOperatingStandards5g=a,n,ac,ax
  WlOperatingStandards5g=a,n,ac,ax

6G:
  LlapiOperatingStandards6g=ax,be
  WlOperatingStandards6g=(missing)

2.4G:
  LlapiOperatingStandards24g=b,g,n,ax
  WlOperatingStandards24g=b,g,n,ax,be
```

So the workbook-style replay still failed in two different ways:

1. 6G never produced a same-target external compare block
2. 2.4G external replay kept one extra family (`be`) beyond the public LLAPI value

### Controlled baseline probes

The follow-up baseline probes also did not close the gap:

- `testpilot5G`: LLAPI `a,n,ac,ax,be`, external replay `a,n,ac,ax`
- `testpilot6G`: not found in the same LLAPI/external replay snapshot
- `testpilot2G`: not found in LLAPI scan output, but the external replay still showed an EHT-capable baseline BSSID

This reinforces that the current external replay is not a durable same-source oracle for the active public field.

## Why no YAML rewrite landed

1. the active public source is now traced to nl80211 IE parsing plus shared bitmask serialization, not to the old Broadcom helper
2. 6G still does not yield a deterministic same-target external replay
3. 2.4G still suggests a supported/capability-family drift (`...,+be`) rather than a clean replay of the public `OperatingStandards` bitmask
4. there is still no live-authoritative basis to:
   - refresh `source.row` from `284` to `282`
   - commit any new workbook-style equality semantics
   - declare raw `wl escanresults`-derived standards as the authoritative 0403 oracle for this row

So D282 must remain blocked and the committed YAML stays unchanged for now.

## Best next direction if this row is reopened

1. find a replayable external oracle that preserves the same beacon/probe IE semantics as `swl_80211_parseInfoElementsBuffer(...)`
2. on the same target BSSID, compare LLAPI `OperatingStandards` and `SupportedStandards` together before inferring anything from external `HT/VHT/HE/EHT` capability text
3. only after a same-source oracle exists, decide whether D282 should become:
   - a workbook-style plain `Pass`, or
   - a source-backed mixed verdict / fail-shaped mismatch
