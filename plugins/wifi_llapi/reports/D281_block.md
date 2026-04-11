# D281 block report

## Status

- case id: `d281-getscanresults-noise`
- current YAML: `plugins/wifi_llapi/cases/D281_getscanresults_noise.yaml`
- workbook authority: `0401.xlsx` `Wifi_LLAPI` row `281`
- current YAML row metadata: `283`
- disposition: **blocked / keep YAML unchanged**
- blocker type: **active 0403 public `Noise` path is spectrum-backed, but even same-channel public `getSpectrumInfo()` replay is not yet official-runner durable**

## Why this case is blocked

The old blocker assumption was that public `getScanResults().Noise` should exact-close against the same-target `wl -i wlX escanresults` `noise:` token. New source tracing and new live reruns show that assumption is incomplete for the active 0403 public path.

In the active pWHM/wifiGen path, public `WiFi.Radio.{i}.getScanResults()` returns entries copied from `pRad->scanState.lastScanResults`, and the scan-complete callback then back-fills each entry's `noise` from the radio's spectrum cache on a **per-channel** basis. That means direct `wl escanresults` per-BSSID `noise:` is no longer a guaranteed same-source oracle for the public `Noise` field.

The updated live trials below prove this distinction is real:

1. after fixing the same-target parser, 5G exact-closes (`-100 / -100`)
2. 6G still drifts in the same direction on both attempts against direct `wl escanresults` (`-97 / -102`, then `-97 / -103`)
3. a newer same-channel public-spectrum trial can exact-close once, but still fails the next official rerun through both transport and numeric drift (`step_6g_scan` temp-script syntax error, then 2.4G `-80 / -79`)

So the blocker is no longer "missing parser / missing target only"; it is now specifically that the authoritative 0403 public `Noise` source is spectrum-backed, but the source-correct replay path still is not durable enough in the official runner.

## Workbook replay target

The merged scan-family authority around workbook row `281` still implies a target-aware replay rather than a plain non-empty getter check:

1. capture a visible target from `getScanResults()`
2. read `Noise` from LLAPI scan results
3. cross-check the same target against runtime scan evidence

The committed YAML still uses the older generic `Noise` non-empty regex because every stronger rewrite tested so far has failed live validation.

## Experimental workbook-style replay that was tested but rejected

To validate whether row `281` could be aligned like `D278-D280`, a temporary local rewrite was trialed with this logic:

1. from each band's `getScanResults()`, capture the first WPA-class target `BSSID + Noise + SecurityModeEnabled`
2. cross-check the same target against `wl -i wl0/wl1/wl2 escanresults`
3. require exact `Noise` equality

This rewrite was **not committed** because the live replays below were not stable enough.

## Live replays on DUT (`COM1`)

### Attempted command

```bash
uv run python -m testpilot.cli run wifi_llapi --case d281-getscanresults-noise --dut-fw-ver BGW720-0403
```

### Isolated rerun `20260410T155529962490`

Observed output shape:

```text
5G:
  LlapiBssid5g=38:88:71:2f:f6:a7
  LlapiNoise5g=-100
  WlNoise5g=-100

6G:
  LlapiBssid6g=3a:06:e6:2b:a3:1a
  LlapiNoise6g=-97
  WlNoise6g=(missing)

2.4G:
  LlapiBssid24g=8c:19:b5:6e:85:e1
  LlapiNoise24g=-80
  WlNoise24g=-77
```

So the first replay already showed two incompatible failure shapes:

1. 6G same-target `wl` noise was missing entirely
2. 2.4G did return same-target `wl` noise, but the value drifted (`-80` vs `-77`)

### Isolated rerun `20260410T155932807150`

Observed output shape:

```text
5G:
  LlapiBssid5g=38:88:71:2f:f6:a7
  LlapiNoise5g=-100
  WlNoise5g=(missing)

6G:
  LlapiBssid6g=3a:06:e6:2b:a3:1a
  LlapiNoise6g=-97
  WlNoise6g=(missing)

2.4G:
  LlapiBssid24g=8c:19:b5:6e:85:e1
  LlapiNoise24g=-80
  WlNoise24g=-79
```

The second replay was even less stable: the missing-band shape moved from 6G-only to 5G+6G, while 2.4G still drifted numerically (`-80` vs `-79`).

### Parser-fix trial rerun `20260411T211133728869`

To rule out a command/parser artifact, a new local trial rewrite switched D281 to target-based `exec` steps and tried to parse the same-target `wl escanresults` block with `sed`.

Observed output shape:

```text
5G:
  LlapiBssid5g=38:88:71:2f:f6:a7
  LlapiNoise5g=-100
  WlNoise5g=(missing)

6G:
  LlapiBssid6g=6e:15:db:9e:33:72
  LlapiNoise6g=-97
  WlNoise6g=(missing)

2.4G:
  LlapiBssid24g=2c:59:17:00:03:f7
  LlapiNoise24g=-78
  WlNoise24g=(missing)
```

That rerun proved the earlier trial still had a local parser issue: the same-target `wl` block itself was not being captured, so the rewrite was not ready to interpret semantically.

### Sanitized parser rerun `20260411T211327344984`

The follow-up trial stripped serial CRLF from the LLAPI-extracted BSSID and switched back to a larger `grep -A120` capture so that the same-target `wl` block was definitely present before parsing `noise:`.

Attempt 1:

```text
5G:
  LlapiBssid5g=38:88:71:2f:f6:a7
  LlapiNoise5g=-100
  WlNoise5g=-100

6G:
  LlapiBssid6g=6e:15:db:9e:33:72
  LlapiNoise6g=-97
  WlNoise6g=-102

2.4G:
  LlapiBssid24g=2c:59:17:00:03:f7
  LlapiNoise24g=-78
  WlNoise24g=-76
```

Attempt 2:

```text
5G:
  LlapiBssid5g=38:88:71:2f:f6:a7
  LlapiNoise5g=-100
  WlNoise5g=-100

6G:
  LlapiBssid6g=6e:15:db:9e:33:72
  LlapiNoise6g=-97
  WlNoise6g=-103

2.4G:
  LlapiBssid24g=2c:59:17:00:03:f7
  LlapiNoise24g=-78
  WlNoise24g=-78
```

This superseding rerun is the key new evidence:

1. 5G can exact-close reliably once the parser is fixed
2. 6G now shows a repeatable drift against direct `wl escanresults` (`-97` vs `-102/-103`)
3. 2.4G still does not stay durable enough to freeze an exact-equality workbook-style replay

### Same-channel public-spectrum official rerun `20260412T011311621294`

After the source survey corrected the authority model to per-channel spectrum back-fill, a second local trial rewrite switched D281 to:

1. extract the first `Channel` and `Noise` from `getScanResults()`
2. read `getSpectrumInfo()` and extract the same channel's `noiselevel`
3. require `Noise == SpectrumNoise`

Observed output shape:

```text
5G:
  Channel=36
  Noise=-100
  SpectrumNoise=-100

6G:
  Channel=5
  Noise=-97
  SpectrumNoise=-97

2.4G:
  Channel=1
  Noise=-80
  SpectrumNoise=-80
```

That first official rerun exact-closed in one attempt, so it confirmed the new direction was source-correct — but not yet durable.

### Follow-up same-channel public-spectrum official rerun `20260412T011644317498`

The immediate follow-up rerun disproved durability.

Attempt 1:

```text
5G:
  Channel=36
  Noise=-100
  SpectrumNoise=-100

6G:
  /tmp/_tp_cmd.sh: line 2: syntax error: unexpected end of file (expecting ")")
```

Attempt 2:

```text
5G:
  Channel=36
  Noise=-100
  SpectrumNoise=-100

6G:
  Channel=5
  Noise=-97
  SpectrumNoise=-97

2.4G:
  Channel=1
  Noise=-80
  SpectrumNoise=-79
```

This superseding rerun changed the blocker again:

1. the same-channel public-spectrum path is real and can exact-close
2. but the official runner still is not durable enough to accept it:
   - attempt 1 failed at `step_6g_scan` with a staged temp-script syntax error
   - attempt 2 still left a live numeric drift on 2.4G (`-80` vs `-79`)

## Source-backed explanation

The legacy/alternate Broadcom path still contains the older `wl escanresults` parser:

- `wldm_lib_wifi.c`
  - `wifi_neighborDiagsRes_mapTable[NEIGHBORDIAG_NOISE] = "noise: "`
  - `sscanf(..., "%d", &neighbor[i].ap_Noise);`
- `wlcsm_lib_wl.c`
  - same `noise: ` mapping for `ap_Noise`

But the active public 0403 path used by current LLAPI rows is different:

- `wld_rad_scan.c:581-584`
  - public `getScanResults()` returns `SignalNoiseRatio`, `Noise`, `RSSI`, ... from `wld_scanResultSSID_t`
- `wifiGen_rad.c:1110-1125`
  - `wifiGen_rad_getScanResults()` simply copies `pRad->scanState.lastScanResults`
- `wifiGen_rad.c:1071-1107`
  - scan-complete callback refreshes spectrum info and then calls `s_updateScanResultsWithSpectrumInfo()`
  - that helper does `pNeighBss->noise = pSpectrumEntry->noiselevel` for matching channels
  - it also recomputes `snr = rssi - noise`
- `wld_nl80211_parser.c:1395-1405`
  - the generic nl80211 survey parser reads `NL80211_SURVEY_INFO_NOISE` into `noiseDbm`
- `wld_nl80211_parser.c:1440-1548`
  - the generic nl80211 scan-result parser fills BSSID/RSSI/channel/etc., but does **not** populate `pResult->noise`

So the newest source-backed conclusion is:

1. direct `wl escanresults` `noise:` is **not** the active authoritative oracle for public `getScanResults().Noise`
2. active public `Noise` is at least partly **spectrum-backed / per-channel**
3. the same-channel public `getSpectrumInfo().noiselevel` view is a plausible replay oracle, but it is still not durable enough in the official runner

## Why no YAML rewrite landed

1. the old direct `wl escanresults` same-target replay was built on the wrong authority assumption for active 0403 public `Noise`
2. the newer same-channel public-spectrum replay exact-closed once, but immediately failed the next official rerun
3. the retry path still exposed a staged temp-script failure on 6G (`step_6g_scan command failed`)
4. even when the command completed, 2.4G still drifted numerically (`Noise=-80` vs `SpectrumNoise=-79`)
5. therefore there is still no live-authoritative basis to:
   - refresh `source.row` from `283` to `281`
   - commit any new exact-equality or tolerance-based semantics
   - declare the same-channel public-spectrum equality as runner-stable on 0403

So D281 must remain blocked and the committed YAML stays unchanged for now.

## Next direction

1. reduce the long staged command risk in the same-channel public-spectrum trial so `step_6g_scan` no longer fails at temp-script syntax generation
2. determine whether the surviving 2.4G `Noise=-80` vs `SpectrumNoise=-79` gap is a cache-timing issue or a real semantic mismatch
3. only if repeated official reruns exact-close after both issues are resolved should D281 refresh `source.row` to `281`

## Next ready case

- `D282`
