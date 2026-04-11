# D333 PacketsSent blocker

## Scope

- Case: `wifi-llapi-d333-packetssent`
- Workbook row authority: `D333` / workbook row `333`
- Current committed YAML remains on the pre-trial workbook-style state (`source.row=257`)
- Latest stale replay run: `20260411T194816992700`
- Latest source-backed trial run: `20260411T195140855058`

## Workbook-style replay result

The committed workbook-era case compares:

1. `WiFi.SSID.{i}.Stats.PacketsSent?`
2. `WiFi.SSID.{i}.getSSIDStats()`
3. `/proc/net/dev_extstats` field `$11`

Run `20260411T194816992700` proved that shape is no longer durable on 0403.

### Attempt 1

- 5G: `direct=293096`, stale `getSSIDStats` extractor last-match=`26411`, `/proc $11=293096`
- 6G: `183455`, stale last-match=`21266`, `/proc $11=279090`
- 2.4G: `295603`, stale last-match=`8061`, `/proc $11=292424`

### Attempt 2

- 5G: `293282`, stale last-match=`26413`, `/proc $11=293282`
- 6G: `183535`, stale last-match=`21271`, `/proc $11=279270`
- 2.4G: `295898`, stale last-match=`8216`, `/proc $11=292614`

So the old case has two separate problems:

1. the loose `getSSIDStats()` extractor overmatches unrelated `*PacketsSent` fields and keeps the wrong last value
2. `/proc/net/dev_extstats` `$11` is not the authoritative all-band driver path on 0403

## Source-backed trial result

Active 0403 source should be close to the already aligned `D312 getSSIDStats() PacketsSent` family:

- base path from `wl if_counters txframe`
- optional `wds*` accumulation for matching peers

So a trial rewrite used:

- anchored `getSSIDStats()` extraction: `^[[:space:]]*PacketsSent = ...`
- driver formula: `wl if_counters txframe + matching wds txframe`

Run `20260411T195140855058`:

### Attempt 1

- 5G: `direct / getSSIDStats / formula = 293527 / 293527 / 293532`
- 6G: `183663 / 183663 / 183663`
- 2.4G: `296276 / 296276 / 296276`

### Attempt 2

- 5G: `293669 / 293669 / 293674`
- 6G: `183687 / 183687 / 183687`
- 2.4G: `296503 / 296503 / 296503`

The anchored extractor fixed the bogus `getSSIDStats()` mismatch, and 6G/2.4G exact-closed, but 5G still held a stable `driver = direct + 5` drift on both attempts.

## Current decision

`D333` remains **blocked**.

- the stale workbook `/proc $11` path is rejected
- the source-backed `txframe + matching wds txframe` trial is directionally correct but still not deterministic enough to commit
- the official YAML is reverted to its pre-trial state while this blocker note carries the new evidence

## Next direction

1. Trace where the persistent 5G `+5` delta is injected after the public `PacketsSent` field is derived.
2. Check whether a small fixed 5G-side control or peer contribution is shaved off before the public field is exposed.
3. If no exact deterministic source-backed oracle can be proven, keep D333 blocked and move on to `D335`.
