# D287 getScanResults() SSID blocker

## Status

- case file: `plugins/wifi_llapi/cases/D287_getscanresults_ssid.yaml`
- workbook row: `287`
- committed YAML row: `289` (stale; no rewrite landed)
- status: blocked
- blocker type: **active public `SSID` is the nl80211/IE-parsed scan-result string, but there is still no durable all-band same-source external replay for the 6G target**

## Source survey

The old blocker note treated neighboring `SSID: ` text parsing as if it were the active public ubus authority. The active 0403 public path is broader:

1. `wld_nl80211_parser.c:1409-1424`
   - `s_copyScanInfoFromIEs(...)` copies `pWirelessDevIE->ssid` into `wld_scanResultSSID_t.ssid`
2. `wld_rad_scan.c:577-579`
   - public `getScanResults()` serializes `SSID` from `ssid->ssid / ssidLen` using `wld_ssid_to_string(...)`
3. `wld_radio.odl`
   - public scan-result model declares both `SSID` and `BSSID`

So the active public ubus field is the parsed scan-result model string, not merely the older Broadcom raw-text helper.

The legacy Broadcom path still exists:

- `bcmdrivers/.../wldm_lib_wifi.c:887-889`
  - maps neighboring scan fields from raw `SSID: ` and `BSSID: ` tokens

That helper remains useful as a comparison point, but it is no longer sufficient to treat raw `SSID:` text parsing as the definitive public authority for this row.

## Live evidence

### Isolated workbook-style replay (`20260410T182739821870`)

```text
5G
BSSID=38:88:71:2f:f6:a7
LlapiSSID=Verizon_Z4RY7R
IwSSID=Verizon_Z4RY7R
```

```text
6G
BSSID=3a:06:e6:2b:a3:1a
LlapiSSID=.ROAMTEST_RSNO_P10P_1
IwSSID=<missing>
```

```text
2.4G
BSSID=8c:19:b5:6e:85:e1
LlapiSSID=TMOBILE-85DF-TDK-2G
IwSSID=TMOBILE-85DF-TDK-2G
```

### Raw driver replay

```text
wl -i wl1 escanresults | grep -m1 -B2 -A1 'BSSID: 3A:06:E6:2B:A3:1A'
stdout: <empty>
```

## Why blocked

1. 5G and 2.4G same-target replay can close cleanly, so the trial rewrite itself was a valid probe.
2. The active public `SSID` source is now understood as the parsed scan-result model string, not just the old raw `SSID:` helper.
3. 6G still cannot close the same-target external replay path: LLAPI exposes `3a:06:e6:2b:a3:1a` / `.ROAMTEST_RSNO_P10P_1`, but `iw dev wl1 scan` emits no same-target `SSID`, and direct raw `wl -i wl1 escanresults` cannot replay that BSSID either.
4. Because the all-band same-source replay still fails on 6G, D287 cannot be rewritten safely and the stale row cannot be refreshed yet.

## Next direction

1. keep the committed YAML unchanged for now
2. if this row is reopened, treat the comparison as a parsed-scan-result replay problem, not a pure raw-text parser problem
3. next unresolved blocker after D287 in the current queue: `D290`
