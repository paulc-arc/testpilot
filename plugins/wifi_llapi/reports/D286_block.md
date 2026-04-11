# D286 getScanResults() SignalStrength blocker

- case file: `plugins/wifi_llapi/cases/D286_getscanresults_signalstrength.yaml`
- compare mapping: workbook row `286`
- committed YAML row: `288` (stale; no rewrite landed)
- status: blocked

## Source survey

- `targets/BGW720-300/fs.install/etc/amx/wld/wld_radio.odl:72-86` declares `scanresult_t` with both `RSSI` and `SignalStrength`.
- `src/nl80211/wld_nl80211_parser.c:1471-1482` fills `pResult->rssi` from `NL80211_BSS_SIGNAL_UNSPEC` or `NL80211_BSS_SIGNAL_MBM`.
- `src/RadMgt/wld_rad_scan.c:584` serializes public `RSSI = ssid->rssi`.
- `src/RadMgt/wld_rad_scan.c:588` serializes public `SignalStrength = ssid->rssi`.
- `src/RadMgt/wld_rad_scan.c:1510` also serializes diagnostic `SignalStrength = pSsid->rssi`.
- therefore, on the active public ubus path, `D286 SignalStrength` is not an independent field from `D283 RSSI`; both are the same `ssid->rssi` family.
- the older Broadcom parser still exists (`bcmdrivers/.../wldm_lib_wifi.c:4928-4933` fills neighboring `SignalStrength` from raw `RSSI: ` text), but it is no longer sufficient to treat the current public ubus row as a raw-text-only authority.

## Live evidence

### Isolated workbook-style replay (`20260410T181105027445`)

```text
5G
BSSID=38:88:71:2f:f6:a7
LlapiSignalStrength=-64
IwSignalStrength=-65
```

```text
6G
BSSID=3a:06:e6:2b:a3:1a
LlapiSignalStrength=-93
IwSignalStrength=<missing>
```

```text
2.4G
BSSID=8c:19:b5:6e:85:e1
LlapiSignalStrength=-46
IwSignalStrength=-55 (attempt 1) / -56 (attempt 2)
```

### Raw driver replay

```text
wl -i wl0 escanresults | grep -B1 -A2 -im1 'BSSID: 38:88:71:2F:F6:A7'
Mode: Managed  RSSI: -64 dBm  SNR: 35 dB  noise: -100 dBm  Channel: 36/80
BSSID: 38:88:71:2F:F6:A7
```

```text
wl -i wl1 escanresults | grep -B1 -A2 -im1 'BSSID: 3A:06:E6:2B:A3:1A'
stdout: <empty>
```

```text
wl -i wl2 escanresults | grep -B1 -A2 -im1 'BSSID: 8C:19:B5:6E:85:E1'
Mode: Managed  RSSI: -54 dBm  SNR: 22 dB  noise: -76 dBm  Channel: 1l
BSSID: 8C:19:B5:6E:85:E1
```

## Why blocked

1. the active public field is `ssid->rssi`, not a separate SignalStrength-only source path, so any rewrite must be justified against the shared `RSSI`/`SignalStrength` family rather than against the old raw-text helper alone.
2. 5G only closes partially: same-target raw replay can match `-64`, but the same-target `iw` replay still stays at `-65`, so there is no single deterministic oracle that survives the workbook-style path.
3. 6G same-target replay does not close at all: both `iw` and direct raw `wl -i wl1 escanresults` fail to replay the LLAPI first BSSID `3A:06:E6:2B:A3:1A`.
4. 2.4G same-target replay still drifts badly even when the BSSID matches: LLAPI returns `-46`, `iw` drifts to `-55/-56`, and raw `wl` still reports `-54 dBm`.
5. Because the active public `ssid->rssi` replay is not deterministic across bands, D286 cannot be rewritten safely and the stale row cannot be refreshed yet.

## Next ready

- `D287 getScanResults() SSID`
