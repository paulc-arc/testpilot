# D336 UnicastPacketsSent blocker

## Scope

- Case: `wifi-llapi-d336-unicastpacketssent`
- Workbook row authority: `D336` / workbook row `336`
- Current committed YAML remains on the pre-trial workbook-style state (`source.row=260`)
- Latest stale replay run: `20260411T201639103833`
- Latest source-backed trial runs: `20260411T201939105374`, `20260411T202824539933`

## Workbook-style replay result

The committed workbook-era case compares:

1. `WiFi.SSID.{i}.Stats.UnicastPacketsSent?`
2. `WiFi.SSID.{i}.getSSIDStats()`
3. `/proc/net/dev_extstats` field `$22`

Run `20260411T201639103833` proved that workbook path is no longer durable on 0403.

### Attempt 2 snapshot

- 5G: `direct / getSSIDStats / /proc = 26434 / 26434 / 0`
- 6G: `21540 / 21540 / 0`
- 2.4G: `10563 / 10563 / 0`

So the old `/proc/net/dev_extstats` `$22` path is rejected as a stale oracle.

## Source-backed trial results

### Trial 1: direct txframe/txmulti parser

Trial rewrite used the candidate formula:

- `(wl if_counters txframe + matching wds txframe) - (wl if_counters txmulti + matching wds txmulti)`

Run `20260411T201939105374` did not even reach semantic evaluation cleanly:

- 5G direct/getSSIDStats already exact-closed at `26439 / 26439`
- `driver_5g` step failed with `/tmp/_tp_cmd.sh: line 1: syntax error: unexpected "(" (expecting ")")`

That parser was rejected.

### Trial 2: safer awk+expr parser

Run `20260411T202824539933` removed the shell parse failure, but the formula still did not converge deterministically:

- attempt 1: 6G drifted `direct / getSSIDStats / driver = 21654 / 21654 / 21682` (`+28`)
- attempt 2: 5G exact-closed `26444 / 26444 / 26444`
- attempt 2: 6G exact-closed `21759 / 21759 / 21759`
- attempt 2: 2.4G still drifted `11690 / 11690 / 11691` (`+1`)

So the source-backed txframe/txmulti formula is directionally close but not yet durable across retries and bands.

## Current decision

`D336` remains **blocked**.

- stale workbook `/proc $22` is rejected
- the candidate txframe/txmulti formula is not deterministic enough to commit
- the official YAML is reverted to its pre-trial workbook-style state while this blocker note carries the new evidence

## Next direction

1. Trace whether direct-property `UnicastPacketsSent` is really fed by a different vendor path than the already aligned `D315 getSSIDStats() UnicastPacketsSent`.
2. Determine whether 6G/2.4G small drifts (`+28`, `+1`) come from hidden unicast counters (`txucastpkts`) or post-processing not visible through the current `if_counters` formula.
3. Resume from the remaining patch-scope blocker set starting at `D277` once this direct-stats branch is parked.
