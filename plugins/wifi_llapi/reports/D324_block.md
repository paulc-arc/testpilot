# D324 BytesSent blocker

## Scope

- Case: `wifi-llapi-d324-bytessent`
- Workbook row authority: `D324` / workbook row `324`
- Current YAML metadata: `source.row: 324`
- Historical aligned rerun: `20260411T010328768651`
- Latest failed full-run evidence: `20260411T074146043202`
- Latest failed isolated rerun: `20260411T190338070996`

## Workbook-style procedure replay

The committed YAML currently replays this source-backed three-way compare on each band:

1. `WiFi.SSID.{i}.Stats.BytesSent?`
2. `WiFi.SSID.{i}.getSSIDStats()` extracted to `GetSSIDStatsBytesSent*`
3. `wl -i wlX if_counters` extracted to `DriverBytesSent*`

Pass currently requires `direct == getSSIDStats == wlX if_counters txbyte`.

## Live evidence

### Latest isolated rerun `20260411T190338070996`

#### Attempt 1

- 5G: `131874002 / 131874002 / 131873776` (`direct / getSSIDStats / wl0 txbyte`, drift `+226`)
- 6G: `81900899 / 81900899 / 81900741` (`+158`)
- 2.4G: `131947990 / 131947990 / 131631950` (`+316040`)

#### Attempt 2

- 5G: `131924828 / 131924828 / 131924828` (exact close)
- 6G: `81927301 / 81927301 / 81927045` (`+256`)
- 2.4G: `132049765 / 132049765 / 131682800` (`+366965`)

### Key observation

- `direct == getSSIDStats()` still exact-closes on all three bands.
- The failure is only on the independent driver oracle.
- The mismatch is no longer a one-band accident:
  - detached full run `20260411T074146043202` failed on 6G
  - isolated rerun `20260411T190338070996` failed on 5G first, then 6G on retry, while 2.4G was already drifting in both attempts

### Post-teardown idle probe

After the isolated rerun fully tore down, a direct DUT probe exact-closed again at idle:

- 5G: `WiFi.SSID.4.Stats.BytesSent = 258133`, `wl0 txbyte = 258133`
- 6G: `181615`, `wl1 txbyte = 181615`
- 2.4G: `173842`, `wl2 txbyte = 173842`

So the parser is not simply broken; the drift is specific to the live sequential band-validation path.

## Source trace

Active 0403 vendor code shows why the current base-interface oracle is incomplete:

- `whm_brcm_api_ext.c:746-812`
  - `whm_brcm_get_if_stats()` seeds `BytesSent` from `wl if_counters txbyte`
- `whm_brcm_vap.c:186-247`
  - `whm_brcm_vap_update_ap_stats()` first copies base-interface stats into `pAP->pSSID->stats`
  - then scans `/proc/net/dev` for matching `wds*` interfaces
  - for each matching peer, `whm_brcm_vap_ap_stats_accu()` adds that interface's `BytesSent` into the public SSID stats

Unlike `BroadcastPacketsSent`, `BytesSent` is **not** restored from `tmp_stats` at the end of this path. So the public `WiFi.SSID.{i}.Stats.BytesSent` field can legitimately be larger than the base `wlX if_counters txbyte` sample whenever extra matching peer stats are merged in.

## Why YAML is not updated yet

The currently committed D324 oracle assumes base `wlX if_counters txbyte` is always the final authoritative driver view. The latest live reruns no longer support that assumption.

We do have a source-backed next hypothesis now:

- public `BytesSent` may need `wlX txbyte + Σ matching wds* txbyte`

But that exact live sum was **not** captured during the same sequential run yet, so there is still no proven replacement criterion ready to commit.

## Current decision

`D324` remains **blocked**.

- Do **not** keep claiming `wlX if_counters txbyte` is a durable all-band oracle
- Do **not** treat the earlier exact-close rerun as sufficient green-lock anymore
- Do **not** refresh the YAML comment as aligned until the merged live source is captured

## Next direction

1. During an active D324-style run, capture the full matching interface set (`wlX` plus any `wds*` peers) before teardown.
2. Verify whether `direct/getSSIDStats == wlX txbyte + Σ matching wds* txbyte` closes on the failing bands.
3. If the merged sum closes, rewrite D324 to that oracle and rerun.
4. If even the merged source-backed sum still drifts, keep D324 blocked and continue with `D330-D333` / `D335-D336`.
