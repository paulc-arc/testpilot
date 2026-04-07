# compare-0401

## Inputs

- trace dirs (overlay order; later directories override earlier case results):
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T230006391661`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T232631531561`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T013838223177`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T020432759837`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T021317975166`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T021716841976`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T023927691290`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T030604339596`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T034832813249`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T040807394935`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T051006378317`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T054957340010`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T060543524189`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T063003376730`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T071356233843`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T095404127199`
  - `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T105808547293`
- answer sheet: `/home/paul_chen/prj_pri/testpilot/0401.xlsx`
- cases dir: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/cases`
- compare rule: normalize both sides so only `Pass` stays `Pass`; all other values become `Fail`.
- row mapping rule: use case `D###` number to match `0401.xlsx` worksheet row `###`.

## Summary

| metric | value |
| --- | ---: |
| compared cases | 420 |
| full matches | 264 |
| mismatch cases | 156 |
| missing answer rows | 0 |
| metadata drift rows | 67 |

## Per-band summary

| band | matched | mismatched |
| --- | ---: | ---: |
| 5g | 283 | 137 |
| 6g | 273 | 147 |
| 2.4g | 275 | 145 |

## Mismatch table

| case_id | D-row | mapping | actual raw (5/6/2.4) | expected raw (R/S/T) | actual norm | expected norm | mismatch bands |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| `wifi-llapi-D011-avgsignalstrength` | 11 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D013-capabilities` | 13 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d014-assocdev-chargeableuserid` | 14 | exact | Pass / N/A / N/A | Skip / Skip / Skip | Pass / Fail / Fail | Fail / Fail / Fail | 5g |
| `wifi-llapi-D020-frequencycapabilities` | 20 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D021-hecapabilities-accesspoint-associateddevice` | 21 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D022-htcapabilities-accesspoint-associateddevice` | 22 | exact | Fail / Fail / Fail | Pass / Not Supported / Pass | Fail / Fail / Fail | Pass / Fail / Pass | 5g, 2.4g |
| `wifi-llapi-D024-lastdatadownlinkrate` | 24 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D025-lastdatauplinkrate` | 25 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D026-linkbandwidth` | 26 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D027-macaddress-accesspoint-associateddevice` | 27 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D028-maxbandwidthsupported` | 28 | exact | Fail / Skip / Fail | Pass / Fail / Pass | Fail / Fail / Fail | Pass / Fail / Pass | 5g, 2.4g |
| `wifi-llapi-D034-noise-accesspoint-associateddevice` | 34 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d035-assocdev-operatingstandard` | 35 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D039-rxbytes` | 39 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D041-rxpacketcount` | 41 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D043-securitymodeenabled` | 43 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D044-signalnoiseratio` | 44 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D045-signalstrength-accesspoint-associateddevice` | 45 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D046-signalstrengthbychain` | 46 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D047-supportedhe160mcs` | 47 | exact | Fail / N/A / N/A | Pass / Pass / Not Supported | Fail / Fail / Fail | Pass / Pass / Fail | 5g, 6g |
| `wifi-llapi-D050-supportedvhtmcs` | 50 | exact | Fail / N/A / N/A | Pass / Not Supported / Not Supported | Fail / Fail / Fail | Pass / Fail / Fail | 5g |
| `d053-blocked-txbytes` | 53 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D054-txerrors` | 54 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D056-txpacketcount` | 56 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D058-uniibandscapabilities` | 58 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D059-uplinkbandwidth` | 59 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D060-uplinkmcs` | 60 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D061-uplinkshortguard` | 61 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D062-vendoroui` | 62 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D063-vhtcapabilities-accesspoint-associateddevice` | 63 | exact | Fail / N/A / N/A | Pass / Not Supported / Not Supported | Fail / Fail / Fail | Pass / Fail / Fail | 5g |
| `wifi-llapi-D065-bridgeinterface` | 65 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D070-enable-accesspoint` | 70 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D071-ftoverdsenable-accesspoint` | 71 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D072-mobilitydomain-accesspoint` | 72 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D077-macfilteraddresslist-accesspoint` | 77 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D078-entry-accesspoint-macfiltering` | 78 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D079-mode-accesspoint-macfiltering` | 79 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D080-maxassociateddevices` | 80 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D081-mboenable` | 81 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D082-multiaptype` | 82 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D085-keypassphrase-accesspoint-security` | 85 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D086-mfpconfig-accesspoint-security` | 86 | exact | Pass / Not Supported / Pass | Not Supported / Not Supported / Not Supported | Pass / Fail / Pass | Fail / Fail / Fail | 5g, 2.4g |
| `wifi-llapi-D087-modeenabled-accesspoint-security` | 87 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D088-modessupported` | 88 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D090-rekeyinginterval` | 90 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D092-wepkey-accesspoint-security` | 92 | exact | Fail / Fail / Fail | Pass / Not Supported / Pass | Fail / Fail / Fail | Pass / Fail / Pass | 5g, 2.4g |
| `wifi-llapi-D093-ssidadvertisementenabled` | 93 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D096-uapsdenable` | 96 | exact | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `wifi-llapi-D100-wmmenable` | 100 | exact | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `wifi-llapi-D101-configmethodsenabled` | 101 | exact | Fail / Fail / Fail | Pass / Not Supported / Pass | Fail / Fail / Fail | Pass / Fail / Pass | 5g, 2.4g |
| `wifi-llapi-D103-configured` | 103 | exact | Pass / Pass / Pass | Pass / Not Supported / Pass | Pass / Pass / Pass | Pass / Fail / Pass | 6g |
| `wifi-llapi-D105-pairinginprogress-accesspoint-wps` | 105 | exact | Pass / Pass / Pass | Pass / Not Supported / Pass | Pass / Pass / Pass | Pass / Fail / Pass | 6g |
| `wifi-llapi-D106-relaycredentialsenable` | 106 | exact | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `wifi-llapi-D108-uuid` | 108 | exact | Pass / Pass / Pass | Pass / Not Supported / Pass | Pass / Pass / Pass | Pass / Fail / Pass | 6g |
| `wifi-llapi-D109-getstationstats-accesspoint` | 109 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D110-getstationstats-active` | 110 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D111-getstationstats-associationtime` | 111 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-D112-getstationstats-authenticationstate` | 112 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D113-getstationstats-avgsignalstrength` | 113 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D114-getstationstats-avgsignalstrengthbychain` | 114 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `wifi-llapi-D115-getstationstats-connectionduration` | 115 | exact | Pass / N/A / N/A | Pass / Pass / Pass | Pass / Fail / Fail | Pass / Pass / Pass | 6g, 2.4g |
| `d202-radio-interference` | 202 | exact | Pass / Pass / Pass | Pass / Fail / Pass | Pass / Pass / Pass | Pass / Fail / Pass | 6g |
| `d207-radio-obsscoexistenceenable` | 207 | exact | Pass / Pass / Pass | Not Supported / Not Supported / Pass | Pass / Pass / Pass | Fail / Fail / Pass | 5g, 6g |
| `d256-getradioairstats-freetime` | 256 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d257-getradioairstats-load` | 257 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d258-getradioairstats-noise` | 258 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d260-getradioairstats-totaltime` | 260 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d262-getradioairstats-void` | 262 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d277-getscanresults-bandwidth` | 277 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d278-getscanresults-bssid` | 278 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d279-getscanresults-channel` | 279 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d280-getscanresults-encryptionmode` | 280 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d281-getscanresults-noise` | 281 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d282-getscanresults-operatingstandards` | 282 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d283-getscanresults-rssi` | 283 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d284-getscanresults-securitymodeenabled` | 284 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d285-getscanresults-signalnoiseratio` | 285 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d286-getscanresults-signalstrength` | 286 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d287-getscanresults-ssid` | 287 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d288-getscanresults-wpsconfigmethodssupported` | 288 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d289-getscanresults-radio` | 289 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d290-getscanresults-centrechannel` | 290 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d295-scan` | 295 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d296-startacs` | 296 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d297-startautochannelselection` | 297 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d298-startscan` | 298 | exact | To be tested / To be tested / To be tested | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d299-stopscan` | 299 | exact | To be tested / To be tested / To be tested | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d321-broadcastpacketsreceived` | 321 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d322-broadcastpacketssent` | 322 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d323-bytesreceived` | 323 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d324-bytessent` | 324 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d325-discardpacketsreceived` | 325 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d326-discardpacketssent` | 326 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d328-errorssent` | 328 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d330-multicastpacketsreceived` | 330 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d331-multicastpacketssent` | 331 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d332-packetsreceived` | 332 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d333-packetssent` | 333 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d335-unicastpacketsreceived` | 335 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d336-unicastpacketssent` | 336 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d355-skip-addclient` | 355 | exact | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d356-skip-delclient` | 356 | exact | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d357-skip-csistats` | 357 | exact | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d363-ieee80211ax-bsscolorpartial` | 363 | exact | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d370-assocdev-active` | 370 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d371-assocdev-disassociationtime` | 371 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d379-radio-mcs` | 379 | exact | Pass / Pass / Pass | Skip / Skip / Skip | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d380-radio-multiaptypessupported` | 380 | exact | Pass / Pass / Pass | skip / skip / skip | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d384-radio-radcapabilitieshtstr` | 384 | exact | Pass / Pass / Pass | Pass / Not Supported / Pass | Pass / Pass / Pass | Pass / Fail / Pass | 6g |
| `d385-radio-radcapabilitiesvhtstr` | 385 | exact | Pass / Pass / Pass | Pass / Not Supported / Not Supported | Pass / Pass / Pass | Pass / Fail / Fail | 6g, 2.4g |
| `wifi-llapi-d406-multipleretrycount` | 406 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `wifi-llapi-d407-retrycount` | 407 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d408-assocdev-downlinkratespec` | 408 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d409-assocdev-maxdownlinkratesupported` | 409 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d410-assocdev-maxrxspatialstreamssupported` | 410 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d411-assocdev-maxtxspatialstreamssupported` | 411 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d412-assocdev-maxuplinkratesupported` | 412 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d413-assocdev-rrmcapabilities` | 413 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d414-assocdev-rrmoffchannelmaxduration` | 414 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d415-assocdev-rrmonchannelmaxduration` | 415 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d426-assocdev-uplinkratespec` | 426 | exact | Fail / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d427-skip-neighbour-bssid` | 427 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d429-skip-neighbour-colocatedap` | 429 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d430-skip-neighbour-information` | 430 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d431-skip-neighbour-nasidentifier` | 431 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d432-skip-neighbour-operatingclass` | 432 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d433-skip-neighbour-phytype` | 433 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d434-skip-neighbour-r0khkey` | 434 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d435-skip-neighbour-ssid` | 435 | drift | Skip / N/A / N/A | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d436-security-owetransitioninterface` | 436 | exact | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d447-radioairstats-inttime` | 447 | drift | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d448-radioairstats-longpreambleerrorpercentage` | 448 | drift | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d449-radioairstats-noisetime` | 449 | drift | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d450-radioairstats-obsstime` | 450 | drift | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d451-radioairstats-shortpreambleerrorpercentage` | 451 | drift | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d460-radio-hecapabilities` | 460 | drift | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d464-radio-nonsrgoffsetvalid` | 464 | drift | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d474-radio-channel` | 474 | drift | Pass / Pass / Pass | Not Supported / Not Supported / Not Supported | Pass / Pass / Pass | Fail / Fail / Fail | 5g, 6g, 2.4g |
| `d478-getradiostats-wmm-bytesreceived-ac_be` | 478 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d479-getradiostats-wmm-bytesreceived-ac_bk` | 479 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d480-getradiostats-wmm-bytesreceived-ac_vi` | 480 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d481-getradiostats-wmm-bytesreceived-ac_vo` | 481 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d482-getradiostats-wmm-bytessent-ac_be` | 482 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d483-getradiostats-wmm-bytessent-ac_bk` | 483 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d484-getradiostats-wmm-bytessent-ac_vi` | 484 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d485-getradiostats-wmm-bytessent-ac_vo` | 485 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d486-getradiostats-wmm-failedbytesreceived-ac_be` | 486 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d487-getradiostats-wmm-failedbytesreceived-ac_bk` | 487 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d488-getradiostats-wmm-failedbytesreceived-ac_vi` | 488 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d489-getradiostats-wmm-failedbytesreceived-ac_vo` | 489 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d490-getradiostats-wmm-failedbytessent-ac_be` | 490 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d491-getradiostats-wmm-failedbytessent-ac_bk` | 491 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d492-getradiostats-wmm-failedbytessent-ac_vi` | 492 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d493-getradiostats-wmm-failedbytessent-ac_vo` | 493 | exact | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |
| `d494-radio-vhtcapabilities` | 494 | exact | Fail / Fail / Fail | Pass / Not Supported / Not Supported | Fail / Fail / Fail | Pass / Fail / Fail | 5g |
| `d528-spectruminfo-bandwidth` | 528 | drift | Fail / Fail / Fail | Pass / Pass / Pass | Fail / Fail / Fail | Pass / Pass / Pass | 5g, 6g, 2.4g |

## Mismatch details

### wifi-llapi-D011-avgsignalstrength

- case file: `D011_avgsignalstrength.yaml`
- answer row: `11`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `AvgSignalStrength`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `AvgSignalStrength`
- final status: `Fail`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Enable RssiEventing root@prplOS:/# ubus-cli WiFi.AccessPoint.*.RssiEventing.Enable=1 > WiFi.AccessPoint.*.RssiEventing.Enable=1 WiFi.AccessPoint.1.RssiEventing.Enable=1 WiFi.AccessPoint.3.RssiEventing.Enable=1 WiFi.AccessPoint.5.RssiE...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 4A:0A:A5:80:23:7B | grep rssi per antenna rssi of last rx data frame: -44 -48 -48 -47 per antenna average rssi of rx data frames: -44 -48 -47 -47 smoothed rssi: -44
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T034832813249/wifi-llapi-D011-avgsignalstrength.json`

### wifi-llapi-D013-capabilities

- case file: `D013_capabilities.yaml`
- answer row: `13`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `Capabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `Capabilities`
- final status: `Fail`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Verify Associated station Capabilities root@prplOS:/# ubus-cli WiFi.AccessPoint.1.AssociatedDevice.1.Capabilities="RRM,BTM,QOS_MAP,PMF" root@prplOS:/# ubus-cli WiFi.AccessPoint.3.AssociatedDevice.1.Capabi...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 4A:0A:A5:80:23:7B | grep capability RRM capability = 0x10843 Link_Measurement Neighbor_Report Beacon_Table Statistics_Measurement AP_Channel_Report
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T051006378317/wifi-llapi-D013-capabilities.json`

### d014-assocdev-chargeableuserid

- case file: `D014_chargeableuserid.yaml`
- answer row: `14`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `ChargeableUserId`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `ChargeableUserId`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Skip` / `Skip` / `Skip`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g`
- 0401 G excerpt: ##Connect WiFi Station and check Station ChargeableUserId WiFi.AccessPoint.1.AssociatedDevice.1.ChargeableUserId="" WiFi.AccessPoint.3.AssociatedDevice.1.ChargeableUserId="" WiFi.AccessPoint.5.AssociatedDevice.1.ChargeableUserId=""
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC}
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d014-assocdev-chargeableuserid.json`

### wifi-llapi-D020-frequencycapabilities

- case file: `D020_frequencycapabilities.yaml`
- answer row: `20`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `FrequencyCapabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `FrequencyCapabilities`
- final status: `Fail`
- evaluation verdict: `Pass`
- attempts used: `2`
- runtime comment: pass after retry (2/2)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW. 2. Verify Associated Station FrequencyCapabilities: root@prplOS:~# ubus-cli WiFi.? | grep FrequencyCapabilities= WiFi.AccessPoint.1.AssociatedDevice.1.FrequencyCapabilities="2.4GHz,5GHz,6GHz" WiFi.AccessPoi...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} Frequency Bands Supported: 2.4G 5G 6G
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260402T095404127199/wifi-llapi-D020-frequencycapabilities.json`

### wifi-llapi-D021-hecapabilities-accesspoint-associateddevice

- case file: `D021_hecapabilities_accesspoint_associateddevice.yaml`
- answer row: `21`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `HeCapabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `HeCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step3 (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW. 2. Verify Associated Station HeCapabilities: WiFi.AccessPoint.1.AssociatedDevice.1.HeCapabilities="SU&MU-BFE" WiFi.AccessPoint.3.AssociatedDevice.1.HeCapabilities="SU&MU-BFE" WiFi.AccessPoint.5.AssociatedDe...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} HE caps 0xcb629: LDPC HE-HTC SU&MU-BFE
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D021-hecapabilities-accesspoint-associateddevice.json`

### wifi-llapi-D022-htcapabilities-accesspoint-associateddevice

- case file: `D022_htcapabilities_accesspoint_associateddevice.yaml`
- answer row: `22`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `HtCapabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `HtCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step3 (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `5g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station HtCapabilities WiFi.AccessPoint.1.AssociatedDevice.1.HtCapabilities="40MHz,SGI20,SGI40" WiFi.AccessPoint.3.AssociatedDevice.1.HtCapabilities="" WiFi.AccessPoint.5.AssociatedDevice.1.HtCapabilities...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} HT caps 0x2d: LDPC SGI20
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D022-htcapabilities-accesspoint-associateddevice.json`

### wifi-llapi-D024-lastdatadownlinkrate

- case file: `D024_lastdatadownlinkrate.yaml`
- answer row: `24`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `LastDataDownlinkRate`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `LastDataDownlinkRate`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step4 (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station LastDataDownlinkRate WiFi.AccessPoint.1.AssociatedDevice.1.LastDataDownlinkRate=324900 WiFi.AccessPoint.3.AssociatedDevice.1.LastDataDownlinkRate=258000 WiFi.AccessPoint.5.AssociatedDevice.1.LastD...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} LastDataDownlinkRate (AP → STA) => rate of last tx pkt: 162500 kbps - 48750 kbps
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D024-lastdatadownlinkrate.json`

### wifi-llapi-D025-lastdatauplinkrate

- case file: `D025_lastdatauplinkrate.yaml`
- answer row: `25`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `LastDataUplinkRate`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `LastDataUplinkRate`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step4 (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station LastDataUplinkRate WiFi.AccessPoint.1.AssociatedDevice.1.LastDataUplinkRate=292400 WiFi.AccessPoint.3.AssociatedDevice.1.LastDataUplinkRate=146200 WiFi.AccessPoint.5.AssociatedDevice.1.LastDataUpl...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} LastDataUplinkRate (STA → AP) = rate of last rx pkt: 51610 kbps
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D025-lastdatauplinkrate.json`

### wifi-llapi-D026-linkbandwidth

- case file: `D026_linkbandwidth.yaml`
- answer row: `26`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `LinkBandwidth`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `LinkBandwidth`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step4 (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station LinkBandwidth WiFi.AccessPoint.1.AssociatedDevice.1.LinkBandwidth="20MHz" WiFi.AccessPoint.3.AssociatedDevice.1.LinkBandwidth="20MHz" WiFi.AccessPoint.5.AssociatedDevice.1.LinkBandwidth="20MHz"
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} link bandwidth = 20 MHZ
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D026-linkbandwidth.json`

### wifi-llapi-D027-macaddress-accesspoint-associateddevice

- case file: `D027_macaddress_accesspoint_associateddevice.yaml`
- answer row: `27`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MACAddress`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MACAddress`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station MAC Address WiFi.AccessPoint.1.AssociatedDevice.1.MACAddress="12:59:1B:BC:C7:7C" WiFi.AccessPoint.3.AssociatedDevice.1.MACAddress="82:25:85:F8:33:D1" WiFi.AccessPoint.5.AssociatedDevice.1.MACAddre...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} STA 02:0F:42:EB:A5:26:
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D027-macaddress-accesspoint-associateddevice.json`

### wifi-llapi-D028-maxbandwidthsupported

- case file: `D028_maxbandwidthsupported.yaml`
- answer row: `28`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxBandwidthSupported`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxBandwidthSupported`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Skip` / `Fail`
- expected raw: `Pass` / `Fail` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `5g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station MaxBandwidthSupported WiFi.AccessPoint.1.AssociatedDevice.1.MaxBandwidthSupported="160MHz" WiFi.AccessPoint.3.AssociatedDevice.1.MaxBandwidthSupported="Unknown" WiFi.AccessPoint.5.AssociatedDevice...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} VHT SET : 0x1 1x1 2x1 3x1 4x1 5x1 6x1 7x1 8x1 9x1 : 0x2 1x2 2x2 3x2 4x2 5x2 6x2 7x2 8x2 9x2 HE SET : 20/40/80 MHz: NSS1 Tx: 0-11 Rx: 0-11 NSS2 Tx: 0-11 Rx: --- EHT SET : 20/40/80 MHz: VHT (Wi-Fi 5) → channel...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D028-maxbandwidthsupported.json`

### wifi-llapi-D034-noise-accesspoint-associateddevice

- case file: `D034_noise_accesspoint_associateddevice.yaml`
- answer row: `34`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `Noise`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `Noise`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Get the Noise by ubus command and record the result for reference root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.Noise? > WiFi.AccessPoint.*.AssociatedDevice.*.Noise? WiFi.AccessPoint.1.Ass...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} root@prplOS:/# wl -i wl0 sta_info 34:19:4d:a4:b5:09 | grep noise per antenna noise floor: -85 -87 -86 -86 root@prplOS:/# wl -i wl1 sta_info 38:06:E6:92:B0:4A | grep noise per antenna noise floor: -87 -87 -87...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D034-noise-accesspoint-associateddevice.json`

### d035-assocdev-operatingstandard

- case file: `D035_operatingstandard.yaml`
- answer row: `35`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `OperatingStandard`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `OperatingStandard`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station OperatingStandard ubus-cli WiFi.AccessPoint.? | grep \.OperatingStandard= WiFi.AccessPoint.1.AssociatedDevice.{i}.OperatingStandard="a" WiFi.AccessPoint.2.AssociatedDevice.{i}.OperatingStandard="U...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC}
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d035-assocdev-operatingstandard.json`

### wifi-llapi-D039-rxbytes

- case file: `D039_rxbytes.yaml`
- answer row: `39`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RxBytes`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RxBytes`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Run IPerf3 between Stations and GW 3. Get stats of RxBytes using ubus command root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep RxBytes WiFi.AccessPoint.1.AssociatedDevice.1.RxBytes=5...
- 0401 H excerpt: iw wl0 station dump root@prplOS:/# iw wl0 station dump Station 34:19:4d:a4:b5:09 (on wl0) inactive time: 11000 ms rx bytes: 5398 rx packets: 40 tx bytes: 152 tx packets: 20 signal: -35 [-34] dBm signal avg: -35 [-33] dBm tx bitrate: 4899...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D039-rxbytes.json`

### wifi-llapi-D041-rxpacketcount

- case file: `D041_rxpacketcount.yaml`
- answer row: `41`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RxPacketCount`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RxPacketCount`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: \\Connect WiFi station to GW \\Run IPerf3 between Stations and GW \\Get stats of RxPacketCount using ubus command root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.RxPacketCount? > WiFi.AccessPoint.*.AssociatedDevice.*.RxPack...
- 0401 H excerpt: iw wl0 station dump root@prplOS:/# iw wl0 station dump Station 34:19:4d:a4:b5:09 (on wl0) inactive time: 11000 ms rx bytes: 5398 rx packets: 40 tx bytes: 152 tx packets: 20 signal: -35 [-34] dBm signal avg: -35 [-33] dBm tx bitrate: 4899...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D041-rxpacketcount.json`

### wifi-llapi-D043-securitymodeenabled

- case file: `D043_securitymodeenabled.yaml`
- answer row: `43`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SecurityModeEnabled`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SecurityModeEnabled`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Set GW security mode to WPA#-Personal 2. Connect WiFi Station 3. Verify Station SecurityModeEnabled WiFi.AccessPoint.1.AssociatedDevice.1.SecurityModeEnabled="WPA3-Personal" WiFi.AccessPoint.3.AssociatedDevice.1.SecurityModeEnabled="W...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info DE:B4:40:A6:40:D5 [VER 8] STA DE:B4:40:A6:40:D5: chanspec 36 (0xd024) aid:9 rateset [ 6 9 12 18 24 36 48 54 ] idle 4 seconds in network 52153 seconds state: AUTHENTICATED ASSOCIATED AUTHORIZED connection...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D043-securitymodeenabled.json`

### wifi-llapi-D044-signalnoiseratio

- case file: `D044_signalnoiseratio.yaml`
- answer row: `44`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SignalNoiseRatio`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SignalNoiseRatio`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Get the SignalNoiseRatio by ubus command and record the result for reference root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.SignalNoiseRatio? > WiFi.AccessPoint.*.AssociatedDevice.*.SignalN...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D044-signalnoiseratio.json`

### wifi-llapi-D045-signalstrength-accesspoint-associateddevice

- case file: `D045_signalstrength_accesspoint_associateddevice.yaml`
- answer row: `45`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SignalStrength`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SignalStrength`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station SignalStrength WiFi.AccessPoint.1.AssociatedDevice.1.SignalStrength=-48 WiFi.AccessPoint.3.AssociatedDevice.1.SignalStrength=-57 WiFi.AccessPoint.5.AssociatedDevice.1.SignalStrength=-48
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} per antenna rssi of last rx data frame: -38 0 0 0 per antenna average rssi of rx data frames: -39 0 0 0 smoothed rssi: -39
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D045-signalstrength-accesspoint-associateddevice.json`

### wifi-llapi-D046-signalstrengthbychain

- case file: `D046_signalstrengthbychain.yaml`
- answer row: `46`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SignalStrengthByChain`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SignalStrengthByChain`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect 4x4 WiFi Station to GW 2. Get SignalStrengthByChain via ubus-command root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.SignalStrengthByChain? > WiFi.AccessPoint.*.AssociatedDevice.*.SignalStrengthByChain? WiFi.Acce...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} root@prplOS:/# wl -i wl0 sta_info 34:19:4D:A4:B5:09 | grep antenna per antenna rssi of last rx data frame: -42 -39 -36 -41 per antenna average rssi of rx data frames: -43 -39 -36 -41 per antenna noise floor:...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D046-signalstrengthbychain.json`

### wifi-llapi-D047-supportedhe160mcs

- case file: `D047_supportedhe160mcs.yaml`
- answer row: `47`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SupportedHe160MCS`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SupportedHe160MCS`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step3 (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Not Supported`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Fail`
- mismatch bands: `5g, 6g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D047-supportedhe160mcs.json`

### wifi-llapi-D050-supportedvhtmcs

- case file: `D050_supportedvhtmcs.yaml`
- answer row: `50`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SupportedVhtMCS`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `SupportedVhtMCS`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step3 (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Not Supported` / `Not Supported`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Fail`
- mismatch bands: `5g`
- 0401 G excerpt: it is the same as RxSupportedVhtMCS and TxSupportedVhtMCS as shown below? root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep Supported VhtMCS WiFi.AccessPoint.1.AssociatedDevice.1.RxSupportedVhtMCS="9,9,9,9" WiFi.Acce...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 34:19:4d:a4:b5:09 [VER 8] STA 34:19:4D:A4:B5:09: VHT caps 0xfb: LDPC SGI80 STBC-Tx STBC-Rx SU-BFR SU-BFE MU-BFR MCS SET : [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D050-supportedvhtmcs.json`

### d053-blocked-txbytes

- case file: `D053_txbytes.yaml`
- answer row: `53`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `TxBytes`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `TxBytes`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW SSID4, SSID6 and SSID8 2. Run IPERF between Stations 3. Verify TxBytes WiFi.AccessPoint.1.AssociatedDevice.1.TxBytes=640514 WiFi.AccessPoint.3.AssociatedDevice.1.TxBytes=11728 WiFi.AccessPoint.5.AssociatedDe...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} tx total bytes: 12792 tx ucast bytes: 12792 tx mcast/bcast bytes: 0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d053-blocked-txbytes.json`

### wifi-llapi-D054-txerrors

- case file: `D054_txerrors.yaml`
- answer row: `54`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `TxErrors`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `TxErrors`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW SSID4, SSID6 and SSID8 2. Run IPERF between Stations 3. Verify TxErrors WiFi.AccessPoint.1.AssociatedDevice.1.TxErrors=2 WiFi.AccessPoint.3.AssociatedDevice.1.TxErrors=0 WiFi.AccessPoint.5.AssociatedDevice.1...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info DE:B4:40:A6:40:D5 | grep tx OMI 0x1201: 20Mhz rx=2ss tx=2ss ER_SU_DISABLE tx total pkts: 86710 tx total bytes: 168156952 tx ucast pkts: 86710 tx ucast bytes: 168156952 tx mcast/bcast pkts: 0 tx mcast/bca...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D054-txerrors.json`

### wifi-llapi-D056-txpacketcount

- case file: `D056_txpacketcount.yaml`
- answer row: `56`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `TxPacketCount`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `TxPacketCount`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and send traffic then check TxPacketCount WiFi.AccessPoint.1.AssociatedDevice.1.TxPacketCount=909 WiFi.AccessPoint.3.AssociatedDevice.1.TxPacketCount=69 WiFi.AccessPoint.5.AssociatedDevice.1.TxPacketCount=83
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} TxPacketCount tx total pkts 90 TxUnicastPacketCount tx ucast pkts 90 TxMulticastPacketCount tx mcast/bcast pkts 0 TxBroadcastPacketCount Included inside tx mcast/bcast pkts 0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D056-txpacketcount.json`

### wifi-llapi-D058-uniibandscapabilities

- case file: `D058_uniibandscapabilities.yaml`
- answer row: `58`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UNIIBandsCapabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UNIIBandsCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station UNIIBandsCapabilities root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep UNIIBands Capabilities WiFi.AccessPoint.1.AssociatedDevice.1.UNIIBandsCapabilities="U-NII-1,U-NII-2A,U-...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D058-uniibandscapabilities.json`

### wifi-llapi-D059-uplinkbandwidth

- case file: `D059_uplinkbandwidth.yaml`
- answer row: `59`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkBandwidth`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkBandwidth`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station UplinkBandwidth WiFi.AccessPoint.1.AssociatedDevice.1.UplinkBandwidth=20 WiFi.AccessPoint.3.AssociatedDevice.1.UplinkBandwidth=20 WiFi.AccessPoint.5.AssociatedDevice.1.UplinkBandwidth=20
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} link bandwidth = 20 MHZ tx nrate eht mcs 7 Nss 2 Tx Exp 2 bw20 ldpc 2xLTF GI 1.6us auto rx nrate eht mcs 4 Nss 1 Tx Exp 0 bw20 ldpc 2xLTF GI 0.8us auto tx nrate = last packet transmitted to the STA (downlink...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D059-uplinkbandwidth.json`

### wifi-llapi-D060-uplinkmcs

- case file: `D060_uplinkmcs.yaml`
- answer row: `60`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkMCS`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkMCS`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step2 (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station UplinkMCS WiFi.AccessPoint.1.AssociatedDevice.1.UplinkMCS=0 WiFi.AccessPoint.3.AssociatedDevice.1.UplinkMCS=0 WiFi.AccessPoint.5.AssociatedDevice.1.UplinkMCS=0
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} rx nrate eht mcs 4 Nss 1 Tx Exp 0 bw20 ldpc 2xLTF GI 0.8us auto rx nrate = last packet received from the STA (uplink) eht mcs 4 → UplinkMCS = 4 Nss 1 → 1 spatial stream used for uplink bw20 → uplink channel ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D060-uplinkmcs.json`

### wifi-llapi-D061-uplinkshortguard

- case file: `D061_uplinkshortguard.yaml`
- answer row: `61`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkShortGuard`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkShortGuard`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step2 (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station UplinkShortGuard WiFi.AccessPoint.1.AssociatedDevice.1.UplinkShortGuard=0 WiFi.AccessPoint.3.AssociatedDevice.1.UplinkShortGuard=0 WiFi.AccessPoint.5.AssociatedDevice.1.UplinkShortGuard=0
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} rx nrate eht mcs 4 Nss 1 Tx Exp 0 bw20 ldpc 2xLTF GI 0.8us auto rx nrate = last packet received from the STA (uplink) GI 0.8us → short guard interval So UplinkShortGuard = true / yes
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D061-uplinkshortguard.json`

### wifi-llapi-D062-vendoroui

- case file: `D062_vendoroui.yaml`
- answer row: `62`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `VendorOUI`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `VendorOUI`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: ##Connect WiFi Station and check Station and check VendorOUI WiFi.AccessPoint.1.AssociatedDevice.1.VendorOUI="00:90:4C,00:10:18,00:50:F2" WiFi.AccessPoint.3.AssociatedDevice.1.VendorOUI="00:10:18,00:50:F2" WiFi.AccessPoint.5.AssociatedDe...
- 0401 H excerpt: wl -i wl0 sta_info ${STA_MAC} VENDOR OUI VALUE[0] 00:90:4C VENDOR OUI VALUE[1] 00:10:18 VENDOR OUI VALUE[2] 00:50:F2
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D062-vendoroui.json`

### wifi-llapi-D063-vhtcapabilities-accesspoint-associateddevice

- case file: `D063_vhtcapabilities_accesspoint_associateddevice.yaml`
- answer row: `63`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `VhtCapabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `VhtCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Not Supported` / `Not Supported`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Fail`
- mismatch bands: `5g`
- 0401 G excerpt: root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep VhtCapabilities WiFi.AccessPoint.1.AssociatedDevice.1.VhtCapabilities="SGI80,SGI160,SU-BFR,SU-BFE,MU-BFR,MU-BFE"
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D063-vhtcapabilities-accesspoint-associateddevice.json`

### wifi-llapi-D065-bridgeinterface

- case file: `D065_bridgeinterface.yaml`
- answer row: `65`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `BridgeInterface`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `BridgeInterface`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step4_5g_config (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep BridgeInterface WiFi.AccessPoint.1.BridgeInterface="br-lan" WiFi.AccessPoint.3.BridgeInterface="br-lan" WiFi.AccessPoint.5.BridgeInterface="br-lan"
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep bridge root@prplOS:/# brctl show bridge name bridge id STP enabled interfaces br-lcm 8000.6c15db74c0b3 no br-lan 8000.6c15db74c0b1 no wl0.1 eth3 wl1 eth1 wl2.1 wl2 eth2 wl0 wl1.1 br-guest 8000.6c15db74c0b2 no
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D065-bridgeinterface.json`

### wifi-llapi-D070-enable-accesspoint

- case file: `D070_enable_accesspoint.yaml`
- answer row: `70`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `Enable`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `Enable`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step6_bss_disable_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: WiFi.AccessPoint.1.Enable=1 WiFi.AccessPoint.3.Enable=1 WiFi.AccessPoint.5.Enable=1
- 0401 H excerpt: root@prplOS:/# wl -e bss --- wl0 5G up --- wl0.1 5G up --- wl1 6G up --- wl1.1 6G up --- wl2 2G up --- wl2.1 2G up
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D070-enable-accesspoint.json`

### wifi-llapi-D071-ftoverdsenable-accesspoint

- case file: `D071_ftoverdsenable.yaml`
- answer row: `71`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.IEEE80211r.` / `FTOverDSEnable`
- workbook metadata: `WiFi.AccessPoint.{i}.IEEE80211r.` / `FTOverDSEnable`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Set IEEE80211r.Enabled=1 ubus-cli WiFi.AccessPoint.*.IEEE80211r.Enabled=1 2. set FTOverDSEnable=1 root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep .IEEE80211r.FTOverDSEnable=1 WiFi.AccessPoint.1.IEEE80211r.FTOverDSEnable=1 WiFi.Acces...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep ft_over_ds Beacon Packet should include: Mobility Domain Mobility Domain ID: xxxx FT Capability and Policy: 0x0? (bitmask) 0000 .... = FT-over-DS: 0 (not supported) .... 000. = FT-over-Air: 1 (supported) Key ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D071-ftoverdsenable-accesspoint.json`

### wifi-llapi-D072-mobilitydomain-accesspoint

- case file: `D072_mobilitydomain.yaml`
- answer row: `72`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.IEEE80211r.` / `MobilityDomain`
- workbook metadata: `WiFi.AccessPoint.{i}.IEEE80211r.` / `MobilityDomain`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: \\Set MobilityDomain root@prplOS:/# ubus-cli WiFi.AccessPoint.1.IEEE80211r.MobilityDomain=1 > WiFi.AccessPoint.1.IEEE80211r.MobilityDomain=1 WiFi.AccessPoint.1.IEEE80211r. WiFi.AccessPoint.1.IEEE80211r.MobilityDomain=1
- 0401 H excerpt: 802.11r requires a non-zero Mobility Domain ID (MDID). If MDID = 0 → 802.11r will NOT activate, even if Enabled=1. must set .MobilityDomain to a 16-bit number (1–65535). Example: ubus-cli WiFi.AccessPoint.1.IEEE80211r.MobilityDomain=4660
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D072-mobilitydomain-accesspoint.json`

### wifi-llapi-D077-macfilteraddresslist-accesspoint

- case file: `D077_macfilteraddresslist.yaml`
- answer row: `77`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `MACFilterAddressList`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `MACFilterAddressList`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step3_add_entry_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: \\Add Station MAC to the table root@prplOS:/# ubus-cli "WiFi.AccessPoint.{i}.MACFiltering.addEntry(mac=62:2F:B8:66:BB:82)" \\Check Station MAC added to the table root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep MACFiltering.Entry WiFi.A...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf accept_mac_file=/tmp/hostap_wl0.acl or deny_mac_file=/tmp/hostap_wl0.acl cat /tmp/hostap_wl0.acl 62:2F:B8:66:BB:82 root@prplOS:/# cat /tmp/wl0_hapd.conf | grep mac macaddr_acl=0 deny_mac_file=/tmp/hostap_wl0.acl ro...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D077-macfilteraddresslist-accesspoint.json`

### wifi-llapi-D078-entry-accesspoint-macfiltering

- case file: `D078_entry.yaml`
- answer row: `78`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.MACFiltering.Entry` / `Entry`
- workbook metadata: `WiFi.AccessPoint.{i}.MACFiltering.Entry` / `Entry`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step2_add_entry_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep MACFiltering.Entry WiFi.AccessPoint.1.MACFiltering.Entry.1. WiFi.AccessPoint.1.MACFiltering.Entry.1.Alias="cpe-Entry-1" WiFi.AccessPoint.1.MACFiltering.Entry.1.MACAddress="62:2F:B8:66:BB:...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf accept_mac_file=/tmp/hostap_wl0.acl or deny_mac_file=/tmp/hostap_wl0.acl cat /tmp/hostap_wl0.acl 62:2F:B8:66:BB:82
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D078-entry-accesspoint-macfiltering.json`

### wifi-llapi-D079-mode-accesspoint-macfiltering

- case file: `D079_mode_accesspoint_macfiltering.yaml`
- answer row: `79`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.MACFiltering.Mode` / `Mode`
- workbook metadata: `WiFi.AccessPoint.{i}.MACFiltering.Mode` / `Mode`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step2_set_off_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep .MACFiltering.Mode= WiFi.AccessPoint.1.MACFiltering.Mode="WhiteList" WiFi.AccessPoint.2.MACFiltering.Mode="Off" WiFi.AccessPoint.3.MACFiltering.Mode="BlackList" WiFi.AccessPoint.4.MACFilt...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf accept_mac_file=/tmp/hostap_wl0.acl or deny_mac_file=/tmp/hostap_wl0.acl root@prplOS:/# cat /tmp/wl0_hapd.conf | grep acl macaddr_acl=1 accept_mac_file=/tmp/hostap_wl0.acl root@prplOS:/# cat /tmp/wl2_hapd.conf | gr...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D079-mode-accesspoint-macfiltering.json`

### wifi-llapi-D080-maxassociateddevices

- case file: `D080_maxassociateddevices.yaml`
- answer row: `80`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `MaxAssociatedDevices`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `MaxAssociatedDevices`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step2_set_temp_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Get the Maximum Association allowed in SSID root@prplOS:/# ubus-cli WiFi.AccessPoint.*.? | grep MaxAssociatedDevices WiFi.AccessPoint.1.MaxAssociatedDevices=32 WiFi.AccessPoint.3.MaxAssociatedDevices=32 WiFi.AccessPoint.5.MaxAssociate...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep max_num_sta cat /tmp/wl1_hapd.conf |grep max_num_sta cat /tmp/wl2_hapd.conf |grep max_num_sta root@prplOS:/# cat /tmp/wl0_hapd.conf |grep max_num_sta root@prplOS:/# cat /tmp/wl1_hapd.conf |grep max_num_sta ro...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D080-maxassociateddevices.json`

### wifi-llapi-D081-mboenable

- case file: `D081_mboenable.yaml`
- answer row: `81`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `MBOEnable`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `MBOEnable`
- final status: `Fail`
- evaluation verdict: `Pass`
- attempts used: `2`
- runtime comment: pass after retry (2/2)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: \\Enable MBO root@prplOS:~# ubus-cli WiFi.AccessPoint.*.MBOEnable=1 > WiFi.AccessPoint.*.MBOEnable=1 WiFi.AccessPoint.1.MBOEnable=1 WiFi.AccessPoint.2.MBOEnable=1 WiFi.AccessPoint.3.MBOEnable=1 WiFi.AccessPoint.4.MBOEnable=1 WiFi.AccessP...
- 0401 H excerpt: MBO = 0"Disable" root@prplOS:/# wl -i wl0 mbo ap_enable MBO AP ENABLE : 0 root@prplOS:/# wl -i wl1 mbo ap_enable MBO AP ENABLE : 0 root@prplOS:/# wl -i wl2 mbo ap_enable MBO AP ENABLE : 0 MBO = 1"Enable" root@prplOS:/# wl -i wl0 mbo ap_e...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D081-mboenable.json`

### wifi-llapi-D082-multiaptype

- case file: `D082_multiaptype.yaml`
- answer row: `82`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `MultiAPType`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `MultiAPType`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: \\Check Default settinh root@prplOS:~# ubus-cli WiFi.AccessPoint.*.MultiAPType? > WiFi.AccessPoint.*.MultiAPType? WiFi.AccessPoint.1.MultiAPType="FronthaulBSS,BackhaulBSS" WiFi.AccessPoint.2.MultiAPType="FronthaulBSS,BackhaulBSS" WiFi.Ac...
- 0401 H excerpt: wl -i wl0 map cat /tmp/wl0_hapd.conf | grep multi_ap root@prplOS:~# cat /tmp/wl0_hapd.conf | grep multi_ap multi_ap=2 multi_ap=2 root@prplOS:~# cat /tmp/wl2_hapd.conf | grep multi_ap multi_ap=2 multi_ap=2 root@prplOS:~# cat /tmp/wl1_hapd...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D082-multiaptype.json`

### wifi-llapi-D085-keypassphrase-accesspoint-security

- case file: `D085_keypassphrase_accesspoint_security.yaml`
- answer row: `85`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security` / `KeyPassPhrase`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `KeyPassPhrase`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep .Security.KeyPassPhrase WiFi.AccessPoint.1.Security.KeyPassPhrase="87654321" WiFi.AccessPoint.3.Security.KeyPassPhrase="87654321" WiFi.AccessPoint.5.Security.KeyPassPhrase="87654321"
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep wpa_pairwise cat /tmp/wl0_hapd.conf |grep wpa_passphrase root@prplOS:/# cat /tmp/wl0_hapd.conf |grep wpa_passphrase wpa_passphrase=87654321 root@prplOS:/# cat /tmp/wl1_hapd.conf |grep wpa_passphrase wpa_passp...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D085-keypassphrase-accesspoint-security.json`

### wifi-llapi-D086-mfpconfig-accesspoint-security

- case file: `D086_mfpconfig_accesspoint_security.yaml`
- answer row: `86`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security` / `MFPConfig`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `MFPConfig`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Not Supported` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Fail` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 2.4g`
- 0401 G excerpt: root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep Security.MFPConfig WiFi.AccessPoint.1.Security.MFPConfig="Disabled" WiFi.AccessPoint.3.Security.MFPConfig="Disabled" WiFi.AccessPoint.5.Security.MFPConfig="Disabled"
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep ieee80211w root@prplOS:/# cat /tmp/wl0_hapd.conf |grep ieee80211w ieee80211w=2 root@prplOS:/# cat /tmp/wl1_hapd.conf |grep ieee80211w ieee80211w=2 root@prplOS:/# cat /tmp/wl2_hapd.conf |grep ieee80211w ieee80...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D086-mfpconfig-accesspoint-security.json`

### wifi-llapi-D087-modeenabled-accesspoint-security

- case file: `D087_modeenabled_accesspoint_security.yaml`
- answer row: `87`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security` / `ModeEnabled`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `ModeEnabled`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Set security mode to WPA3-Personal root@prplOS:/# ubus-cli WiFi.AccessPoint.*.Security.ModeEnabled=WPA3-Personal > WiFi.AccessPoint.*.Security.ModeEnabled=WPA3-Personal WiFi.AccessPoint.1.Security.ModeEnabled="WPA3-Personal" WiFi.Acce...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf | grep wpa and other related parameters root@prplOS:/# cat /tmp/wl0_hapd.conf | grep wpa wpa=2 wpa_key_mgmt=SAE FT-SAE wpa_pairwise=CCMP wpa_group_rekey=0 wpa_ptk_rekey=0 wpa_passphrase=87654321 wpa_disable_eapol_k...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D087-modeenabled-accesspoint-security.json`

### wifi-llapi-D088-modessupported

- case file: `D088_modessupported.yaml`
- answer row: `88`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security` / `ModesSupported`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `ModesSupported`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step2 (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: "Test Procedure: 1. Set/Get Security Key PassPhrase Set Command: ubus-cli WiFi.AccessPoint.{i}.Security.KeyPassPhrase=""12345678"" Get command: ubus-cli WiFi.AccessPoint.{i}.Security.KeyPassPhrase? 2. Set/Get Security Mode Set Command: u...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D088-modessupported.json`

### wifi-llapi-D090-rekeyinginterval

- case file: `D090_rekeyinginterval.yaml`
- answer row: `90`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security` / `RekeyingInterval`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `RekeyingInterval`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: Test Procedure: 1.Set/Get RekeyingInterval Set Command: ubus-cli WiFi.AccessPoint.{i}.Security.RekeyingInterval= Get Command: ubus-cli WiFi.AccessPoint.{i}.Security.RekeyingInterval? 2.check hostapd config&webGUI cat /tmp/wlx_hapd.conf |...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep wpa_group_rekey
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D090-rekeyinginterval.json`

### wifi-llapi-D092-wepkey-accesspoint-security

- case file: `D092_wepkey_accesspoint_security.yaml`
- answer row: `92`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security` / `WEPKey`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `WEPKey`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `5g, 2.4g`
- 0401 G excerpt: Test Procedure: 1.set the security mode to WEP-128 2.Set/Get WEPKey Set Command: ubus-cli WiFi.AccessPoint.{i}.Security.WEPKey="" Get Command: ubus-cli WiFi.AccessPoint.{i}.Security.WEPKey? 3.check hostapd config &webGUI Command: cat /tm...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep wep_key
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D092-wepkey-accesspoint-security.json`

### wifi-llapi-D093-ssidadvertisementenabled

- case file: `D093_ssidadvertisementenabled.yaml`
- answer row: `93`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `SSIDAdvertisementEnabled`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `SSIDAdvertisementEnabled`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Get SSIDAdvertisementEnabled value root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep SSIDAdvertisementEnabled WiFi.AccessPoint.1.SSIDAdvertisementEnabled=1 WiFi.AccessPoint.3.SSIDAdvertisementEnabled=1 WiFi.AccessPoint.5.SSIDAdvertise...
- 0401 H excerpt: root@prplOS:/# cat /tmp/wl0_hapd.conf | grep -E 'broadcast|ssid' bssid=6C:15:DB:74:C0:B5 ssid=5G_Primary-BE ignore_broadcast_ssid=2 ignore_broadcast_ssid=0 => "SSID not Hidden" ignore_broadcast_ssid=2 => "SSID Hidden"
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D093-ssidadvertisementenabled.json`

### wifi-llapi-D096-uapsdenable

- case file: `D096_uapsdenable.yaml`
- answer row: `96`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `UAPSDEnable`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `UAPSDEnable`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: \\Enable/Disable UPSD ubus-cli WiFi.AccessPoint.{i}.UAPSDEnable= 1=Enbale 0=Disable
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep apsd
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D096-uapsdenable.json`

### wifi-llapi-D100-wmmenable

- case file: `D100_wmmenable.yaml`
- answer row: `100`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `WMMEnable`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `WMMEnable`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /tmp/wl0_hapd.conf | grep wmm_enabled
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D100-wmmenable.json`

### wifi-llapi-D101-configmethodsenabled

- case file: `D101_configmethodsenabled.yaml`
- answer row: `101`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.WPS.` / `ConfigMethodsEnabled`
- workbook metadata: `WiFi.AccessPoint.{i}.WPS.` / `ConfigMethodsEnabled`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `5g, 2.4g`
- 0401 G excerpt: 1. Get WPS ConfigMethodsEnabled root@prplOS:/# ubus-cli WiFi.AccessPoint.? |grep .WPS.ConfigMethodsEnabled WiFi.AccessPoint.1.WPS.ConfigMethodsEnabled="PhysicalPushButton,VirtualPushButton" WiFi.AccessPoint.3.WPS.ConfigMethodsEnabled="Ph...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep config_methods root@prplOS:/# cat /tmp/wl0_hapd.conf |grep config_methods config_methods=physical_push_button virtual_push_button root@prplOS:/# cat /tmp/wl1_hapd.conf |grep config_methods root@prplOS:/# cat ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D101-configmethodsenabled.json`

### wifi-llapi-D103-configured

- case file: `D103_configured.yaml`
- answer row: `103`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.WPS.` / `Configured`
- workbook metadata: `WiFi.AccessPoint.{i}.WPS.` / `Configured`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `6g`
- 0401 G excerpt: 1. Get WPS Configured state root@prplOS:/# ubus-cli WiFi.AccessPoint.*.WPS.Configured ? > WiFi.AccessPoint.*.WPS.Configured ? WiFi.AccessPoint.1.WPS.Configured=1 WiFi.AccessPoint.3.WPS.Configured=1 WiFi.AccessPoint.5.WPS.Configured=1 wps...
- 0401 H excerpt: root@prplOS:/# cat /tmp/wl0_hapd.conf |grep wps_state wps_state=2 root@prplOS:/# cat /tmp/wl1_hapd.conf |grep wps_state wps_state=0 root@prplOS:/# cat /tmp/wl2_hapd.conf |grep wps_state wps_state=2
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D103-configured.json`

### wifi-llapi-D105-pairinginprogress-accesspoint-wps

- case file: `D105_pairinginprogress_accesspoint_wps.yaml`
- answer row: `105`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.WPS.` / `PairingInProgress`
- workbook metadata: `WiFi.AccessPoint.{i}.WPS.` / `PairingInProgress`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `6g`
- 0401 G excerpt: 1. Initiate WPS pairing between GW and Station root@prplOS:/# ubus-cli -a "WiFi.AccessPoint.1.WPS.InitiateWPSPBC()" > WiFi.AccessPoint.1.WPS.InitiateWPSPBC() WiFi.AccessPoint.1.WPS.InitiateWPSPBC() returned [ { Status = "Success" } ] 2. ...
- 0401 H excerpt: root@prplOS:/# hostapd_cli -i wl0 wps_get_status PBC Status: Active Last WPS result: None
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D105-pairinginprogress-accesspoint-wps.json`

### wifi-llapi-D106-relaycredentialsenable

- case file: `D106_relaycredentialsenable.yaml`
- answer row: `106`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.WPS.` / `RelayCredentialsEnable`
- workbook metadata: `WiFi.AccessPoint.{i}.WPS.` / `RelayCredentialsEnable`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep wps_cred_processing
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D106-relaycredentialsenable.json`

### wifi-llapi-D108-uuid

- case file: `D108_uuid.yaml`
- answer row: `108`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.WPS.` / `UUID`
- workbook metadata: `WiFi.AccessPoint.{i}.WPS.` / `UUID`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `6g`
- 0401 G excerpt: 1. Get GW WPS UUID root@prplOS:/# ubus-cli WiFi.AccessPoint.? | grep .WPS.UUID WiFi.AccessPoint.1.WPS.UUID="4b58464a-5957-fc49-f845-57454b58464a" WiFi.AccessPoint.3.WPS.UUID="4b58464a-5957-fc49-f845-57454b58464a" WiFi.AccessPoint.5.WPS.U...
- 0401 H excerpt: cat /tmp/wl0_hapd.conf |grep uuid root@prplOS:/# cat /tmp/wl0_hapd.conf |grep uuid uuid=4b58464a-5957-fc49-f845-57454b58464a root@prplOS:/# cat /tmp/wl1_hapd.conf |grep uuid root@prplOS:/# cat /tmp/wl2_hapd.conf |grep uuid uuid=4b58464a-...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D108-uuid.json`

### wifi-llapi-D109-getstationstats-accesspoint

- case file: `D109_getstationstats_accesspoint.yaml`
- answer row: `109`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Get Station Stats root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" > WiFi.AccessPoint.*.getStationStats() WiFi.AccessPoint.3.getStationStats() returned [ [ { Active = 1, ActiveNumberOfAffili...
- 0401 H excerpt: root@prplOS:/# hostapd_cli -i wl0 STA 34:19:4D:A4:B5:09 34:19:4d:a4:b5:09 flags=[AUTH][ASSOC][AUTHORIZED][WMM][MFP][HT] aid=2 capability=0x0 listen_interval=0 supported_rates=8c 12 18 24 b0 48 60 6c timeout_next=NULLFUNC POLL dot11RSNASt...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D109-getstationstats-accesspoint.json`

### wifi-llapi-D110-getstationstats-active

- case file: `D110_getstationstats_active.yaml`
- answer row: `110`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW. 2. Verify connected Station state root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" | grep -E 'Activ e|MAC' Active = 1, MACAddress = "e6:60:17:eb:a9:86", Active = 1, MACAddress = "38:06:e6:92:b...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info e6:60:17:eb:a9:86 | grep state state: AUTHENTICATED ASSOCIATED AUTHORIZED root@prplOS:/# wl -i wl1 sta_info 38:06:e6:92:b0:4a | grep state state: AUTHENTICATED ASSOCIATED AUTHORIZED root@prplOS:/# wl -i ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D110-getstationstats-active.json`

### wifi-llapi-D111-getstationstats-associationtime

- case file: `D111_getstationstats_associationtime.yaml`
- answer row: `111`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW. 2. Verify connected Station AssociationTime root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" | grep -E 'AssociationTime| AuthenticationState|MACAddress' AssociationTime = "2025-12-26T09:28:04Z...
- 0401 H excerpt: root@prplOS:/# date Fri Dec 26 09:28:21 UTC 2025
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D111-getstationstats-associationtime.json`

### wifi-llapi-D112-getstationstats-authenticationstate

- case file: `D112_getstationstats_authenticationstate.yaml`
- answer row: `112`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW. 2. Verify connected Station AuthenticationState root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" | grep -E 'Auth enticationState|MACAddress' AuthenticationState = 1, MACAddress = "E6:60:17:EB:...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info e6:60:17:eb:a9:86 | grep state state: AUTHENTICATED ASSOCIATED AUTHORIZED root@prplOS:/# wl -i wl1 sta_info 38:06:e6:92:b0:4a | grep state state: AUTHENTICATED ASSOCIATED AUTHORIZED root@prplOS:/# wl -i ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D112-getstationstats-authenticationstate.json`

### wifi-llapi-D113-getstationstats-avgsignalstrength

- case file: `D113_getstationstats_avgsignalstrength.yaml`
- answer row: `113`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW. 2. Verify connected Station AvgSignalStrength root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" | grep AvgSignalStrength root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" | grep -E...
- 0401 H excerpt: root@prplOS:/# root@prplOS:/# wl -i wl0 sta_info e6:60:17:eb:a9:86 | grep smoothed smoothed rssi: -37 root@prplOS:/# wl -i wl1 sta_info 38:06:e6:92:b0:4a | grep smoothed smoothed rssi: -36 root@prplOS:/# wl -i wl2 sta_info 34:19:4d:a4:b4...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D113-getstationstats-avgsignalstrength.json`

### wifi-llapi-D114-getstationstats-avgsignalstrengthbychain

- case file: `D114_getstationstats_avgsignalstrengthbychain.yaml`
- answer row: `114`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW and make sure the Station is Active root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep -E 'Active|MAC' WiFi.AccessPoint.1.AssociatedDevice.1.Active=1 WiFi.AccessPoint.1.AssociatedDevice.1...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info E6:D7:D3:EA:CF:15 | grep average per antenna average rssi of rx data frames: -43 -53 -46 -49 root@prplOS:/# wl -i wl1 sta_info 38:06:E6:92:B0:4A | grep average per antenna average rssi of rx data frames:...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D114-getstationstats-avgsignalstrengthbychain.json`

### wifi-llapi-D115-getstationstats-connectionduration

- case file: `D115_getstationstats_connectionduration.yaml`
- answer row: `115`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- workbook metadata: `WiFi.AccessPoint.{i}.` / `getStationStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Pass` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Verify Station ConnectionDuration root@prplOS:/# ubus-cli "WiFi.AccessPoint.*.getStationStats()" | grep -E 'ConnectionDuration|MACAddress' ConnectionDuration = 2833, MACAddress = "38:06:E6:92:B0:4A", Conn...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 34:19:4D:A4:B5:09 | grep network in network 764 seconds root@prplOS:/# wl -i wl1 sta_info 38:06:E6:92:B0:4A | grep network in network 2843 seconds root@prplOS:/# wl -i wl2 sta_info 34:19:4D:A4:B4:33 | gr...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-D115-getstationstats-connectionduration.json`

### d202-radio-interference

- case file: `D202_interference.yaml`
- answer row: `202`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `Interference`
- workbook metadata: `WiFi.Radio.{i}.` / `Interference`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Pass` / `Fail` / `Pass`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `6g`
- 0401 G excerpt: 1. Check API default value: root@prplOS:/# ubus-cli WiFi.Radio.*.Interference? > WiFi.Radio.*.Interference? WiFi.Radio.1.Interference=0 WiFi.Radio.2.Interference=0 WiFi.Radio.3.Interference=0
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d202-radio-interference.json`

### d207-radio-obsscoexistenceenable

- case file: `D207_obsscoexistenceenable.yaml`
- answer row: `207`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `ObssCoexistenceEnable`
- workbook metadata: `WiFi.Radio.{i}.` / `ObssCoexistenceEnable`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Pass`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Pass`
- mismatch bands: `5g, 6g`
- 0401 G excerpt: 1.ubus-cli WiFi.Radio.3.ObssCoexistenceEnable=1 2.ubus-cli WiFi.Radio.3.OperatingChannelBandwidth="40MHz” 3.wl -i wl2 status shows 20MHz 4.ubus-cli WiFi.Radio.3.ObssCoexistenceEnable=0 5.wl -i wl2 status shows 40MHz
- 0401 H excerpt: root@prplOS:/# wl -i wl0 obss_coex 0 root@prplOS:/# wl -i wl1 obss_coex 0 root@prplOS:/# wl -i wl2 obss_coex 1
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d207-radio-obsscoexistenceenable.json`

### d256-getradioairstats-freetime

- case file: `D256_getradioairstats_freetime.yaml`
- answer row: `256`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: Connect 2 STAs to radio, use iperf3 to transmit some data between two STAs. Check getRadioAirStats(): ubus-cli "WiFi.Radio.*.getRadioAirStats()" > WiFi.Radio.*.getRadioAirStats() WiFi.Radio.1.getRadioAirStats() returned [ { FreeTime = 0,...
- 0401 H excerpt: root@prplOS:/# iw dev wl0 survey dump root@prplOS:/# iw dev wl1 survey dump root@prplOS:/# iw dev wl2 survey dump
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d256-getradioairstats-freetime.json`

### d257-getradioairstats-load

- case file: `D257_getradioairstats_load.yaml`
- answer row: `257`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d257-getradioairstats-load.json`

### d258-getradioairstats-noise

- case file: `D258_getradioairstats_noise.yaml`
- answer row: `258`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d258-getradioairstats-noise.json`

### d260-getradioairstats-totaltime

- case file: `D260_getradioairstats_totaltime.yaml`
- answer row: `260`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d260-getradioairstats-totaltime.json`

### d262-getradioairstats-void

- case file: `D262_getradioairstats_void.yaml`
- answer row: `262`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d262-getradioairstats-void.json`

### d277-getscanresults-bandwidth

- case file: `D277_getscanresults_bandwidth.yaml`
- answer row: `277`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Setup another AP as a data collecting target, try collect the target's Wi-Fi air radio info. Compare the actual value and API returned value. [5GHz] ubus-cli "WiFi.Radio.*.getScanResults()" | grep -i 1C:F4:3F:73:C7 * -A 15 -B1 { BSSID...
- 0401 H excerpt: [2.4GHz] root@prplOS:/# iw dev wl2 scan | grep 1c:f4:3f:73:c7:40 -A150 BSS 1c:f4:3f:73:c7:40(on wl2) TSF: 14499627031 usec (0d, 04:01:39) freq: 2472 beacon interval: 100 TUs capability: ESS Privacy ShortPreamble ShortSlotTime APSD RadioM...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d277-getscanresults-bandwidth.json`

### d278-getscanresults-bssid

- case file: `D278_getscanresults_bssid.yaml`
- answer row: `278`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d278-getscanresults-bssid.json`

### d279-getscanresults-channel

- case file: `D279_getscanresults_channel.yaml`
- answer row: `279`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d279-getscanresults-channel.json`

### d280-getscanresults-encryptionmode

- case file: `D280_getscanresults_encryptionmode.yaml`
- answer row: `280`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d280-getscanresults-encryptionmode.json`

### d281-getscanresults-noise

- case file: `D281_getscanresults_noise.yaml`
- answer row: `281`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d281-getscanresults-noise.json`

### d282-getscanresults-operatingstandards

- case file: `D282_getscanresults_operatingstandards.yaml`
- answer row: `282`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d282-getscanresults-operatingstandards.json`

### d283-getscanresults-rssi

- case file: `D283_getscanresults_rssi.yaml`
- answer row: `283`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d283-getscanresults-rssi.json`

### d284-getscanresults-securitymodeenabled

- case file: `D284_getscanresults_securitymodeenabled.yaml`
- answer row: `284`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d284-getscanresults-securitymodeenabled.json`

### d285-getscanresults-signalnoiseratio

- case file: `D285_getscanresults_signalnoiseratio.yaml`
- answer row: `285`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d285-getscanresults-signalnoiseratio.json`

### d286-getscanresults-signalstrength

- case file: `D286_getscanresults_signalstrength.yaml`
- answer row: `286`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d286-getscanresults-signalstrength.json`

### d287-getscanresults-ssid

- case file: `D287_getscanresults_ssid.yaml`
- answer row: `287`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d287-getscanresults-ssid.json`

### d288-getscanresults-wpsconfigmethodssupported

- case file: `D288_getscanresults_wpsconfigmethodssupported.yaml`
- answer row: `288`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d288-getscanresults-wpsconfigmethodssupported.json`

### d289-getscanresults-radio

- case file: `D289_getscanresults_radio.yaml`
- answer row: `289`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d289-getscanresults-radio.json`

### d290-getscanresults-centrechannel

- case file: `D290_getscanresults_centrechannel.yaml`
- answer row: `290`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- workbook metadata: `WiFi.Radio.{i}.` / `getScanResults()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g_scan (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d290-getscanresults-centrechannel.json`

### d295-scan

- case file: `D295_scan.yaml`
- answer row: `295`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `scan()`
- workbook metadata: `WiFi.Radio.{i}.` / `scan()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_6g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Try scan() function: ubus-cli "WiFi.Radio.*.scan()"
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d295-scan.json`

### d296-startacs

- case file: `D296_startacs.yaml`
- answer row: `296`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `startACS()`
- workbook metadata: `WiFi.Radio.{i}.` / `startACS()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Try call API function: root@prplOS:/# ubus-cli "WiFi.Radio.1.startACS()" > WiFi.Radio.1.startACS() ERROR: call (null) failed with status 1 - unknown error WiFi.Radio.1.startACS() returned [ "" ] root@prplOS:/# ubus-cli "WiFi.Radio.2.s...
- 0401 H excerpt: logread | grep ACS iw dev wl0 info iw dev wl1 info iw dev wl2 info
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d296-startacs.json`

### d297-startautochannelselection

- case file: `D297_startautochannelselection.yaml`
- answer row: `297`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `startAutoChannelSelection()`
- workbook metadata: `WiFi.Radio.{i}.` / `startAutoChannelSelection()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Try call API function: root@prplOS:/# ubus-cli "WiFi.Radio.*.startAutoChannelSelection()" > WiFi.Radio.*.startAutoChannelSelectio() ERROR: call (null) failed with status 3 - function not found WiFi.Radio.1.startAutoChannelSelectio() r...
- 0401 H excerpt: iw dev wl0 info iw dev wl1 info iw dev wl2 info
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d297-startautochannelselection.json`

### d298-startscan

- case file: `D298_startscan.yaml`
- answer row: `298`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `startScan()`
- workbook metadata: `WiFi.Radio.{i}.` / `startScan()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `To be tested` / `To be tested` / `To be tested`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Start startScan() function once, record the result: ubus-cli "WiFi.Radio.1.startScan()" root@prplOS:/# ubus-cli "WiFi.Radio.1.startScan()" > WiFi.Radio.1.startScan() WiFi.Radio.1.startScan() returned [ "" ] root@prplOS:/# ubus-cli "Wi...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d298-startscan.json`

### d299-stopscan

- case file: `D299_stopscan.yaml`
- answer row: `299`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `stopScan()`
- workbook metadata: `WiFi.Radio.{i}.` / `stopScan()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `To be tested` / `To be tested` / `To be tested`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Start startScan() function once, record the result: ubus-cli "WiFi.Radio.1.startScan()" root@prplOS:/# ubus-cli "WiFi.Radio.1.startScan()" > WiFi.Radio.1.startScan() WiFi.Radio.1.startScan() returned [ "" ] root@prplOS:/# root@prplOS:...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d299-stopscan.json`

### wifi-llapi-d321-broadcastpacketsreceived

- case file: `D321_broadcastpacketsreceived.yaml`
- answer row: `321`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `BroadcastPacketsReceived`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `BroadcastPacketsReceived`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to SSID4, SSID6 and SSID8 2. Run Ping between Station and check BroadcastPacketsSent. 3. Disconnect WiFi Station and clear ARP then run Ping again. root@prplOS:/# ubus-cli WiFi.SSID.? | grep .Stats.BroadcastPacket...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d321-broadcastpacketsreceived.json`

### wifi-llapi-d322-broadcastpacketssent

- case file: `D322_broadcastpacketssent.yaml`
- answer row: `322`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `BroadcastPacketsSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `BroadcastPacketsSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to SSID4, SSID6 and SSID8 2. Run Ping between Station and check BroadcastPacketsSent. 3. Disconnect WiFi Station and clear ARP then run Ping again. root@prplOS:/# ubus-cli WiFi.SSID.? | grep .Stats.BroadcastPacket...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d322-broadcastpacketssent.json`

### wifi-llapi-d323-bytesreceived

- case file: `D323_bytesreceived_ssid_stats.yaml`
- answer row: `323`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `BytesReceived`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `BytesReceived`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW SSID4, SSID6 and SSID8 2. Run Ping between station's 3. Get stats BytesReceived root@prplOS:/# ubus-cli WiFi.SSID.*.Stats.BytesReceived? > WiFi.SSID.*.Stats.BytesReceived? WiFi.SSID.4.Stats.BytesReceived=639...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d323-bytesreceived.json`

### wifi-llapi-d324-bytessent

- case file: `D324_bytessent_ssid_stats.yaml`
- answer row: `324`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `BytesSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `BytesSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW SSID4, SSID6 and SSID8 2. Run Ping between station's 3. Get stats BytesSent root@prplOS:/# ubus-cli WiFi.SSID.*.Stats.BytesSent? > WiFi.SSID.*.Stats.BytesSent? WiFi.SSID.4.Stats.BytesSent=153672313 WiFi.SSID...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d324-bytessent.json`

### wifi-llapi-d325-discardpacketsreceived

- case file: `D325_discardpacketsreceived.yaml`
- answer row: `325`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `DiscardPacketsReceived`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `DiscardPacketsReceived`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /proc/net/dev | grep wl0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d325-discardpacketsreceived.json`

### wifi-llapi-d326-discardpacketssent

- case file: `D326_discardpacketssent.yaml`
- answer row: `326`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `DiscardPacketsSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `DiscardPacketsSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /proc/net/dev | grep wl0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d326-discardpacketssent.json`

### wifi-llapi-d328-errorssent

- case file: `D328_errorssent_ssid_stats.yaml`
- answer row: `328`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `ErrorsSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `ErrorsSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /proc/net/dev | grep wl0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d328-errorssent.json`

### wifi-llapi-d330-multicastpacketsreceived

- case file: `D330_multicastpacketsreceived.yaml`
- answer row: `330`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `MulticastPacketsReceived`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `MulticastPacketsReceived`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Create Multicast group and send Multicast Data between station's and GW Station server = iperf -s -u -B 239.1.2.3%br0 -i 1 Station Joiner = iperf -c 239.1.2.3 -u -t 10 -b 20M -i 1 -t 100 3. Check Multicas...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d330-multicastpacketsreceived.json`

### wifi-llapi-d331-multicastpacketssent

- case file: `D331_multicastpacketssent.yaml`
- answer row: `331`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `MulticastPacketsSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `MulticastPacketsSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Execute following command in GW iptables -I INPUT -p tcp --dport 5201 -j ACCEPT iptables -I INPUT -p udp --dport 5201 -j ACCEPT 3. Create Multicast group and send Multicast Data between station's - Statio...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d331-multicastpacketssent.json`

### wifi-llapi-d332-packetsreceived

- case file: `D332_packetsreceived_ssid_stats.yaml`
- answer row: `332`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `PacketsReceived`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `PacketsReceived`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW SSID4, SSID6 and SSID8 2. Run Ping between station's 3. Get stats PacketsReceived root@prplOS:/# ubus-cli WiFi.SSID.*.Stats.PacketsReceived? > WiFi.SSID.*.Stats.PacketsReceived? WiFi.SSID.4.Stats.PacketsRece...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d332-packetsreceived.json`

### wifi-llapi-d333-packetssent

- case file: `D333_packetssent_ssid_stats.yaml`
- answer row: `333`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `PacketsSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `PacketsSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW SSID4, SSID6 and SSID8 2. Run Ping between station's 3. Get stats PacketsSent root@prplOS:/# ubus-cli WiFi.SSID.*.Stats.PacketsSent? > WiFi.SSID.*.Stats.PacketsSent? WiFi.SSID.4.Stats.PacketsSent=225745 WiFi...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d333-packetssent.json`

### wifi-llapi-d335-unicastpacketsreceived

- case file: `D335_unicastpacketsreceived.yaml`
- answer row: `335`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `UnicastPacketsReceived`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `UnicastPacketsReceived`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW SSID4, SSID6 and SSID8 2. Run Ping between station's 3. Get stats UnicastPacketsReceived root@prplOS:/# ubus-cli WiFi.SSID.*.Stats.UnicastPacketsReceived? > WiFi.SSID.*.Stats.UnicastPacketsReceived? WiFi.SSI...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 6395774 33265 0 27 0 0 0 12...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d335-unicastpacketsreceived.json`

### wifi-llapi-d336-unicastpacketssent

- case file: `D336_unicastpacketssent.yaml`
- answer row: `336`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `UnicastPacketsSent`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `UnicastPacketsSent`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW SSID4, SSID6 and SSID8 2. Run Ping between station's 3. Get stats Unicast packet sent root@prplOS:/# ubus-cli WiFi.SSID.*.Stats.UnicastPacketsSent? > WiFi.SSID.*.Stats.UnicastPacketsSent? WiFi.SSID.1.Stats.U...
- 0401 H excerpt: cat /proc/net/dev | grep wl0 root@prplOS:/# cat /proc/net/dev Inter-| Receive | Transmit face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed wl0: 99866942 866493 0 20 0 0 0 ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d336-unicastpacketssent.json`

### d355-skip-addclient

- case file: `D355_addclient.yaml`
- answer row: `355`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Sensing.` / `addClient()`
- workbook metadata: `WiFi.Radio.{i}.Sensing.` / `addClient()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Try add a sensing client by API: (5G) ubus-cli "WiFi.Radio.1.Sensing.addClient(MACAddress='A0:29:42:60:23:BD', MonitorInterval=100)" ubus-cli "WiFi.Radio.1.Sensing.addClient(MACAddress='14:85:7F:20:18:44', MonitorInterval=10)" (6G) ub...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d355-skip-addclient.json`

### d356-skip-delclient

- case file: `D356_delclient.yaml`
- answer row: `356`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Sensing.` / `delClient()`
- workbook metadata: `WiFi.Radio.{i}.Sensing.` / `delClient()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Try delete an added client: root@prplOS:/# ubus-cli "WiFi.Radio.*.Sensing.delClient(MACAddress='a0:29:42:60:23:be')" > WiFi.Radio.*.Sensing.delClient(MACAddress='a0:29:42:60:23:be') WiFi.Radio.1.Sensing.delClient() returned [ "" ] WiF...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d356-skip-delclient.json`

### d357-skip-csistats

- case file: `D357_csistats.yaml`
- answer row: `357`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Sensing.` / `csiStats()`
- workbook metadata: `WiFi.Radio.{i}.Sensing.` / `csiStats()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Record the API counters in the beginning: root@prplOS:/# ubus-cli "WiFi.Radio.*.Sensing.csiStats()" > WiFi.Radio.*.Sensing.csiStats() WiFi.Radio.1.Sensing.csiStats() returned [ { M2MTransmitCounter = 0, NullFrameAckFailCounter = 0, Nu...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d357-skip-csistats.json`

### d363-ieee80211ax-bsscolorpartial

- case file: `D363_bsscolorpartial.yaml`
- answer row: `363`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.IEEE80211ax.` / `BssColorPartial`
- workbook metadata: `WiFi.Radio.{i}.IEEE80211ax.` / `BssColorPartial`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Fail` / `Fail` / `Fail`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d363-ieee80211ax-bsscolorpartial.json`

### d370-assocdev-active

- case file: `D370_active.yaml`
- answer row: `370`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `Active`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `Active`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Check Associated Device Status root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep -E 'Activ e|MAC' WiFi.AccessPoint.1.AssociatedDevice.11.Active=1 WiFi.AccessPoint.1.AssociatedDevice.1...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 assoclist assoclist 34:19:4D:A4:B5:09 assoclist 12:E3:C4:78:7B:6F assoclist 42:B7:35:6A:17:8E root@prplOS:/# wl -i wl1 assoclist assoclist 38:06:E6:92:B0:4A root@prplOS:/# wl -i wl2 assoclist assoclist E4:60:17:E...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d370-assocdev-active.json`

### d371-assocdev-disassociationtime

- case file: `D371_disassociationtime.yaml`
- answer row: `371`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `DisassociationTime`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `DisassociationTime`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station to GW 2. Check Associated Device Status 3. Disconnect Wifi Station from GW 4. Check Associated Device DisassociationTime root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep -E 'Activ root@prplOS...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 assoclist root@prplOS:/# wl -i wl1 assoclist root@prplOS:/# wl -i wl2 assoclist
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d371-assocdev-disassociationtime.json`

### d379-radio-mcs

- case file: `D379_mcs.yaml`
- answer row: `379`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `MCS`
- workbook metadata: `WiFi.Radio.{i}.` / `MCS`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Skip` / `Skip` / `Skip`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Verify MCS of the Radio root@prplOS:/# ubus-cli WiFi.Radio.*.MCS? > WiFi.Radio.*.MCS? WiFi.Radio.1.MCS=0 WiFi.Radio.2.MCS=0 WiFi.Radio.3.MCS=0
- 0401 H excerpt: root@prplOS:/# wl -i wl0 status SSID: "5G-123" Mode: Managed RSSI: 0 dBm SNR: 0 dB noise: -92 dBm Channel: 48/160 BSSID: 64:75:DA:4E:51:75 Capability: ESS RRM Beacon Interval: 100 msecs Supported Rates: [ 6(b) 9 12 18 24(b) 36 48 54 ] Ex...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d379-radio-mcs.json`

### d380-radio-multiaptypessupported

- case file: `D380_multiaptypessupported.yaml`
- answer row: `380`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `MultiAPTypesSupported`
- workbook metadata: `WiFi.Radio.{i}.` / `MultiAPTypesSupported`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `skip` / `skip` / `skip`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Get MultiAP type Supported mode root@prplOS:/# ubus-cli WiFi.Radio.*.MultiAPTypesSupported? > WiFi.Radio.*.MultiAPTypesSupported? WiFi.Radio.1.MultiAPTypesSupported="FronthaulBSS,BackhaulBSS,BackhaulSTA" WiFi.Radio.2.MultiAPTypesSuppo...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d380-radio-multiaptypessupported.json`

### d384-radio-radcapabilitieshtstr

- case file: `D384_radcapabilitieshtstr.yaml`
- answer row: `384`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `RadCapabilitiesHTStr`
- workbook metadata: `WiFi.Radio.{i}.` / `RadCapabilitiesHTStr`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Pass` / `Not Supported` / `Pass`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Pass` / `Fail` / `Pass`
- mismatch bands: `6g`
- 0401 G excerpt: 1. get RadCapabilitiesHTStr root@prplOS:/# ubus-cli WiFi.Radio.*.RadCapabilitiesHTStr? > WiFi.Radio.*.RadCapabilitiesHTStr? WiFi.Radio.1.RadCapabilitiesHTStr="CAP_40,SHORT_GI_20,SHORT_GI_40,MODE_40" WiFi.Radio.2.RadCapabilitiesHTStr="" W...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d384-radio-radcapabilitieshtstr.json`

### d385-radio-radcapabilitiesvhtstr

- case file: `D385_radcapabilitiesvhtstr.yaml`
- answer row: `385`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `RadCapabilitiesVHTStr`
- workbook metadata: `WiFi.Radio.{i}.` / `RadCapabilitiesVHTStr`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Pass` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Pass` / `Fail` / `Fail`
- mismatch bands: `6g, 2.4g`
- 0401 G excerpt: 1. get RadCapabilitiesVHTStr root@prplOS:/# ubus-cli WiFi.Radio.*.RadCapabilitiesVHTStr? > WiFi.Radio.*.RadCapabilitiesVHTStr? WiFi.Radio.1.RadCapabilitiesVHTStr="RX_LDPC,SGI_80,SGI_160,SU_BFR,SU_BFE,LINK_ADAPT_CAP" WiFi.Radio.2.RadCapab...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d385-radio-radcapabilitiesvhtstr.json`

### wifi-llapi-d406-multipleretrycount

- case file: `D406_multipleretrycount_ssid_stats.yaml`
- answer row: `406`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `MultipleRetryCount`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `MultipleRetryCount`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /proc/net/dev |grep wl0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d406-multipleretrycount.json`

### wifi-llapi-d407-retrycount

- case file: `D407_retrycount_ssid_stats_basic.yaml`
- answer row: `407`
- mapping status: `exact`
- source metadata: `WiFi.SSID.{i}.Stats.` / `RetryCount`
- workbook metadata: `WiFi.SSID.{i}.Stats.` / `RetryCount`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: assoc_5g (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: cat /proc/net/dev |grep wl0
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/wifi-llapi-d407-retrycount.json`

### d408-assocdev-downlinkratespec

- case file: `D408_downlinkratespec.yaml`
- answer row: `408`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `DownlinkRateSpec`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `DownlinkRateSpec`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Check DownlinkRateSpec root@prplOS:~# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.DownlinkRateSpec? > WiFi.AccessPoint.*.AssociatedDevice.*.DownlinkRateSpec? WiFi.AccessPoint.1.AssociatedDevice.1.Downl...
- 0401 H excerpt: root@prplOS:/# iw dev wl0 station dump Station 00:60:f3:25:aa:59 (on wl0) inactive time: 3000 ms rx bytes: 9828 rx packets: 38 tx bytes: 152 tx packets: 14 signal: -39 [-39] dBm signal avg: -38 [-38] dBm tx bitrate: 4899.0 MBit/s 160MHz ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d408-assocdev-downlinkratespec.json`

### d409-assocdev-maxdownlinkratesupported

- case file: `D409_maxdownlinkratesupported.yaml`
- answer row: `409`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxDownlinkRateSupported`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxDownlinkRateSupported`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Verify Station MaxDownlinkRateSupported root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.MaxDownlinkRateSupported? > WiFi.AccessPoint.*.AssociatedDevice.*.MaxDownlinkRateSupported? WiFi.Acces...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 00:60:f3:25:aa:59 | grep -E 'nrate|mcs|Max Rate' tx nrate eht mcs 12 Nss 4 Tx Exp 0 bw160 txbf ldpc 2xLTF GI 1.6us auto rx nrate eht mcs 8 Nss 4 Tx Exp 0 bw160 ldpc 2xLTF GI 0.8us auto Max Rate = 4537 Mb...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d409-assocdev-maxdownlinkratesupported.json`

### d410-assocdev-maxrxspatialstreamssupported

- case file: `D410_maxrxspatialstreamssupported.yaml`
- answer row: `410`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxRxSpatialStreamsSupported`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxRxSpatialStreamsSupported`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Verify Station MaxRxSpatialStreamsSupported root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep MaxRxSpatialStreamsSupported root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice....
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 34:19:4D:A4:B5:09 | grep Nss tx nrate eht mcs 9 Nss 4 Tx Exp 0 bw20 txbf ldpc 2xLTF GI 0.8us auto rx nrate eht mcs 9 Nss 4 Tx Exp 0 bw20 ldpc 2xLTF GI 0.8us auto root@prplOS:/# wl -i wl1 sta_info 38:06:E...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d410-assocdev-maxrxspatialstreamssupported.json`

### d411-assocdev-maxtxspatialstreamssupported

- case file: `D411_maxtxspatialstreamssupported.yaml`
- answer row: `411`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxTxSpatialStreamsSupported`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxTxSpatialStreamsSupported`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Verify Station MaxTxSpatialStreamsSupported root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.? | grep MaxTxSpatialStreamsSupported WiFi.AccessPoint.1.AssociatedDevice.1.MaxTxSpatialStreamsSup...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 34:19:4D:A4:B5:09 | grep Nss tx nrate eht mcs 9 Nss 4 Tx Exp 0 bw20 txbf ldpc 2xLTF GI 0.8us auto rx nrate eht mcs 9 Nss 4 Tx Exp 0 bw20 ldpc 2xLTF GI 0.8us auto root@prplOS:/# wl -i wl1 sta_info 38:06:E...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d411-assocdev-maxtxspatialstreamssupported.json`

### d412-assocdev-maxuplinkratesupported

- case file: `D412_maxuplinkratesupported.yaml`
- answer row: `412`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxUplinkRateSupported`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `MaxUplinkRateSupported`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Verify Station MaxUplinkRateSupported root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.MaxUplinkRateSuppo rted? > WiFi.AccessPoint.*.AssociatedDevice.*.MaxUplinkRateSupported? WiFi.AccessPoin...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 00:60:f3:25:aa:59 | grep -E 'nrate|mcs|Max Rate' tx nrate eht mcs 12 Nss 4 Tx Exp 0 bw160 txbf ldpc 2xLTF GI 1.6us auto rx nrate eht mcs 8 Nss 4 Tx Exp 0 bw160 ldpc 2xLTF GI 0.8us auto Max Rate = 4537 Mb...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d412-assocdev-maxuplinkratesupported.json`

### d413-assocdev-rrmcapabilities

- case file: `D413_rrmcapabilities.yaml`
- answer row: `413`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RrmCapabilities`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RrmCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW 2. Verify Station RrmCapabilities root@prplOS:/# ubus-cli WiFi.AccessPoint.*.AssociatedDevice.*.RrmCapabilities? > WiFi.AccessPoint.*.AssociatedDevice.*.RrmCapabilities? WiFi.AccessPoint.1.AssociatedDevice.5...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 sta_info 56:50:99:6B:A0:89 | grep RRM RRM capability = 0x10873 Link_Measurement Neighbor_Report Beacon_Passive Beacon_Active Beacon_Table Statistics_Measurement AP_Channel_Report root@prplOS:/# wl -i wl1 sta_info...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d413-assocdev-rrmcapabilities.json`

### d414-assocdev-rrmoffchannelmaxduration

- case file: `D414_rrmoffchannelmaxduration.yaml`
- answer row: `414`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RrmOffChannelMaxDuration`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RrmOffChannelMaxDuration`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW with one station 802.11k Enable and the other one 802.11k Disable. 2. Verify Station station 802.11k Enable Check whether RRM is ON or OFF using: wl sta_info <MAC> | grep -i rrm If 802.11k Enable then you wi...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d414-assocdev-rrmoffchannelmaxduration.json`

### d415-assocdev-rrmonchannelmaxduration

- case file: `D415_rrmonchannelmaxduration.yaml`
- answer row: `415`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RrmOnChannelMaxDuration`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `RrmOnChannelMaxDuration`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW with one station 802.11k Enable and the other one 802.11k Disable. 2. Verify Station station 802.11k Enable Check whether RRM is ON or OFF using: wl sta_info <MAC> | grep -i rrm If 802.11k Enable then you wi...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d415-assocdev-rrmonchannelmaxduration.json`

### d426-assocdev-uplinkratespec

- case file: `D426_uplinkratespec.yaml`
- answer row: `426`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkRateSpec`
- workbook metadata: `WiFi.AccessPoint.{i}.AssociatedDevice.{i}.` / `UplinkRateSpec`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: env_verify gate failed (failed after 2/2 attempts)
- actual raw: `Fail` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi Station to GW and run Chariot between Station and GW 2. Check Associated Station UplinkRateSpec ###5G (11be, 4x4, 160MHz)### root@prplOS:/# ubus-cli WiFi.AccessPoint.1.AssociatedDevice.*.UplinkRateSpec? > WiFi.AccessPoint...
- 0401 H excerpt: iw dev wl0 station dump #####5G##### root@prplOS:/# iw dev wl0 station dump Station 00:60:f3:25:aa:59 (on wl0) inactive time: 3000 ms rx bytes: 9828 rx packets: 38 tx bytes: 152 tx packets: 14 signal: -39 [-39] dBm signal avg: -38 [-38] ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d426-assocdev-uplinkratespec.json`

### d427-skip-neighbour-bssid

- case file: `D427_bssid_accesspoint_neighbour.yaml`
- answer row: `427`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `BSSID`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `BSSID`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Reset GW to Default then check Neighbour entry root@prplOS:/# ubus-cli WiFi.AccessPoint.1.? | grep Neighbour root@prplOS:/# 2. Add Neighbour entry root@prplOS:/# ubus-cli "WiFi.AccessPoint.1.setNeighbourAP(BSSID="AA:BB:CC:DD:EE :01",C...
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d427-skip-neighbour-bssid.json`

### d429-skip-neighbour-colocatedap

- case file: `D429_colocatedap.yaml`
- answer row: `429`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `ColocatedAP`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `ColocatedAP`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d429-skip-neighbour-colocatedap.json`

### d430-skip-neighbour-information

- case file: `D430_information.yaml`
- answer row: `430`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `Information`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `Information`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d430-skip-neighbour-information.json`

### d431-skip-neighbour-nasidentifier

- case file: `D431_nasidentifier.yaml`
- answer row: `431`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `NASIdentifier`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `NASIdentifier`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d431-skip-neighbour-nasidentifier.json`

### d432-skip-neighbour-operatingclass

- case file: `D432_operatingclass.yaml`
- answer row: `432`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `OperatingClass`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `OperatingClass`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d432-skip-neighbour-operatingclass.json`

### d433-skip-neighbour-phytype

- case file: `D433_phytype.yaml`
- answer row: `433`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `PhyType`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `PhyType`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d433-skip-neighbour-phytype.json`

### d434-skip-neighbour-r0khkey

- case file: `D434_r0khkey.yaml`
- answer row: `434`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `R0KHKey`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `R0KHKey`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d434-skip-neighbour-r0khkey.json`

### d435-skip-neighbour-ssid

- case file: `D435_ssid_accesspoint_neighbour.yaml`
- answer row: `435`
- mapping status: `drift`
- source metadata: `WiFi.AccessPoint.{i}.Neighbour.` / `SSID`
- workbook metadata: `WiFi.AccessPoint.{i}.Neighbour.{i}.` / `SSID`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Skip` / `N/A` / `N/A`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d435-skip-neighbour-ssid.json`

### d436-security-owetransitioninterface

- case file: `D436_owetransitioninterface.yaml`
- answer row: `436`
- mapping status: `exact`
- source metadata: `WiFi.AccessPoint.{i}.Security.` / `OWETransitionInterface`
- workbook metadata: `WiFi.AccessPoint.{i}.Security.` / `OWETransitionInterface`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Set OWETransitionInterface root@prplOS:~# ubus-cli WiFi.AccessPoint.1.Security.OWETransitionInterface=DEFAULT_W L1_1 > WiFi.AccessPoint.1.Security.OWETransitionInterface=DEFAULT_WL1_1 WiFi.AccessPoint.1.Security. WiFi.AccessPoint.1.Se...
- 0401 H excerpt: root@prplOS:~# cat /tmp/wl0_hapd.conf |grep owe_transition_ifname root@prplOS:~# cat /tmp/wl1_hapd.conf |grep owe_transition_ifname root@prplOS:~# cat /tmp/wl2_hapd.conf |grep owe_transition_ifname
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d436-security-owetransitioninterface.json`

### d447-radioairstats-inttime

- case file: `D447_getradioairstats_inttime.yaml`
- answer row: `447`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.getRadioAirStats()` / `IntTime`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Fail` / `Fail` / `Fail`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect 2 STAs to radio, use iperf3 to transmit some data between two STAs. 2. Check getRadioAirStats(): ubus-cli "WiFi.Radio.*.getRadioAirStats()" > WiFi.Radio.*.getRadioAirStats() WiFi.Radio.1.getRadioAirStats() returned [ { FreeTim...
- 0401 H excerpt: root@prplOS:/# iw dev wl0 survey dump root@prplOS:/# iw dev wl1 survey dump root@prplOS:/# iw dev wl2 survey dump
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d447-radioairstats-inttime.json`

### d448-radioairstats-longpreambleerrorpercentage

- case file: `D448_getradioairstats_longpreambleerrorpercentage.yaml`
- answer row: `448`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.getRadioAirStats()` / `LongPreambleErrorPercentage`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d448-radioairstats-longpreambleerrorpercentage.json`

### d449-radioairstats-noisetime

- case file: `D449_getradioairstats_noisetime.yaml`
- answer row: `449`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.getRadioAirStats()` / `NoiseTime`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Fail` / `Fail` / `Fail`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d449-radioairstats-noisetime.json`

### d450-radioairstats-obsstime

- case file: `D450_getradioairstats_obsstime.yaml`
- answer row: `450`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.getRadioAirStats()` / `ObssTime`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Fail` / `Fail` / `Fail`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d450-radioairstats-obsstime.json`

### d451-radioairstats-shortpreambleerrorpercentage

- case file: `D451_getradioairstats_shortpreambleerrorpercentage.yaml`
- answer row: `451`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.getRadioAirStats()` / `ShortPreambleErrorPercentage`
- workbook metadata: `WiFi.Radio.{i}.` / `getRadioAirStats()`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d451-radioairstats-shortpreambleerrorpercentage.json`

### d460-radio-hecapabilities

- case file: `D460_hecapabilities_radio.yaml`
- answer row: `460`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.` / `HECapabilities`
- workbook metadata: `WiFi.Radio.{i}.` / `HePhyCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_5g_getter (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d460-radio-hecapabilities.json`

### d464-radio-nonsrgoffsetvalid

- case file: `D464_nonsrgoffsetvalid.yaml`
- answer row: `464`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.` / `NonSRGOffsetValid`
- workbook metadata: `WiFi.Radio.{i}.IEEE80211ax.` / `NonSRGOffsetValid`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Fail` / `Fail` / `Fail`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 he options
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d464-radio-nonsrgoffsetvalid.json`

### d474-radio-channel

- case file: `D474_channel_radio_37.yaml`
- answer row: `474`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.` / `Channel`
- workbook metadata: `WiFi.Radio.{i}.ScanResults.SurroundingChannels.{i}.` / `Channel`
- final status: `Pass`
- evaluation verdict: `Pass`
- attempts used: `1`
- actual raw: `Pass` / `Pass` / `Pass`
- expected raw: `Not Supported` / `Not Supported` / `Not Supported`
- actual normalized: `Pass` / `Pass` / `Pass`
- expected normalized: `Fail` / `Fail` / `Fail`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d474-radio-channel.json`

### d478-getradiostats-wmm-bytesreceived-ac_be

- case file: `D478_ac_be_stats_wmmbytesreceived_radio.yaml`
- answer row: `478`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_BE`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_BE`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF "iperf3 -c <server> -u -b 20M" 3. Verify Radio Stats.WmmBytesReceived.AC_BE root@prplOS:/# ubus-cli WiFi.Radio.*.? | grep WmmBytesReceived.AC_BE ...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 wme_counters AC_BE: tx frames: 23176 bytes: 6830889 failed frames: 0 failed bytes: 0 rx frames: 17703 bytes: 26181728 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i wl1 wme_counters AC_BE: tx frames: 26313...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d478-getradiostats-wmm-bytesreceived-ac_be.json`

### d479-getradiostats-wmm-bytesreceived-ac_bk

- case file: `D479_ac_bk_stats_wmmbytesreceived_radio.yaml`
- answer row: `479`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_BK`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_BK`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF "iperf3 -c <server> -u -b 20M --tos 0x20" 3. Verify Radio Stats.WmmBytesReceived.AC_BK root@prplOS:/# ubus-cli WiFi.Radio.*.? | grep WmmBytesRece...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 wme_counters AC_BE: tx frames: 23711 bytes: 7015133 failed frames: 0 failed bytes: 0 rx frames: 17734 bytes: 26185565 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i wl1 wme_counters AC_BE: tx frames: 27022...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d479-getradiostats-wmm-bytesreceived-ac_bk.json`

### d480-getradiostats-wmm-bytesreceived-ac_vi

- case file: `D480_ac_vi_stats_wmmbytesreceived_radio.yaml`
- answer row: `480`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_VI`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_VI`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF "iperf3 -c <server> -u -b 20M --tos 0x88" 3. Verify Radio Stats.WmmBytesReceived.AC_VI root@prplOS:/# ubus-cli WiFi.Radio.*.? | grep WmmBytesRece...
- 0401 H excerpt: wl -i wl0 wme_counters root@prplOS:/# wl -i wl0 wme_counters AC_VI: tx frames: 0 bytes: 0 failed frames: 0 failed bytes: 0 rx frames: 17205 bytes: 26495350 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i wl1 wme_counters AC_VI: tx ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d480-getradiostats-wmm-bytesreceived-ac_vi.json`

### d481-getradiostats-wmm-bytesreceived-ac_vo

- case file: `D481_ac_vo_stats_wmmbytesreceived_radio.yaml`
- answer row: `481`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_VO`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesReceived.` / `AC_VO`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF "iperf3 -c <server> -u -b 20M --tos 0xB8" 3. Verify Radio Stats.WmmBytesReceived.AC_VO root@prplOS:/# ubus-cli WiFi.Radio.*.? | grep WmmBytesRece...
- 0401 H excerpt: wl -i wl0 wme_counters root@prplOS:/# wl -i wl0 wme_counters AC_VO: tx frames: 8 bytes: 3541 failed frames: 0 failed bytes: 0 rx frames: 17345 bytes: 26447627 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i wl1 wme_counters AC_VO: ...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d481-getradiostats-wmm-bytesreceived-ac_vo.json`

### d482-getradiostats-wmm-bytessent-ac_be

- case file: `D482_ac_be_stats_wmmbytessent_radio.yaml`
- answer row: `482`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_BE`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_BE`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect two WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF between Station "iperf3 -c 192.168.1.1 -u -b 20M " 3. Execute command ubus-cli "WiFi.Radio.*.getRadioStats()" 4. Verify Radio Stats.WmmBytesR...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 wme_counters AC_BE: tx frames: 36796 bytes: 39571906 failed frames: 341 failed bytes: 79808 root@prplOS:/# wl -i wl1 wme_counters AC_BE: tx frames: 33627 bytes: 14116150 failed frames: 0 failed bytes: 0 root@prpl...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d482-getradiostats-wmm-bytessent-ac_be.json`

### d483-getradiostats-wmm-bytessent-ac_bk

- case file: `D483_ac_bk_stats_wmmbytessent_radio.yaml`
- answer row: `483`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_BK`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_BK`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect two WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF iperf3 -c 192.168.1.1 -u -b 20M --tos 0x20 3. Execute command ubus-cli "WiFi.Radio.*.getRadioStats()" 4. Verify Radio Stats.WmmBytesSent.AC_B...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 wme_counters AC_BK: tx frames: 6824 bytes: 25882414 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i wl1 wme_counters AC_BK: tx frames: 6243 bytes: 22243076 failed frames: 0 failed bytes: 0 root@prplOS:/# wl...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d483-getradiostats-wmm-bytessent-ac_bk.json`

### d484-getradiostats-wmm-bytessent-ac_vi

- case file: `D484_ac_vi_stats_wmmbytessent_radio.yaml`
- answer row: `484`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_VI`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_VI`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect two WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF "iperf3 -c <server> -u -b 20M --tos 0x88" 3. Execute command ubus-cli "WiFi.Radio.*.getRadioStats()" 4. Verify Radio Stats.WmmBytesSent.AC_VI...
- 0401 H excerpt: wl -i wl0 wme_counters root@prplOS:/# wl -i wl0 wme_counters AC_VI: tx frames: 17265 bytes: 25861532 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i wl0 wme_counters AC_VI: tx frames: 4352 bytes: 6517858 failed frames: 0 failed byt...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d484-getradiostats-wmm-bytessent-ac_vi.json`

### d485-getradiostats-wmm-bytessent-ac_vo

- case file: `D485_ac_vo_stats_wmmbytessent_radio.yaml`
- answer row: `485`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_VO`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmBytesSent.` / `AC_VO`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Connect two WiFi station (use another WiFi7 GW as station with built-in IPERF3) 2. Run IPERF "iperf3 -c <server> -u -b 20M --tos 0xB8" 3. Execute command ubus-cli "WiFi.Radio.*.getRadioStats()" 4. Verify Radio Stats.WmmBytesSent.AC_VO...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 wme_counters AC_VO: tx frames: 17268 bytes: 25862027 failed frames: 2 failed bytes: 104 root@prplOS:/# wl -i wl1 wme_counters AC_VO: tx frames: 6 bytes: 972 failed frames: 0 failed bytes: 0 root@prplOS:/# wl -i w...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d485-getradiostats-wmm-bytessent-ac_vo.json`

### d486-getradiostats-wmm-failedbytesreceived-ac_be

- case file: `D486_ac_be_stats_wmmfailedbytesreceived_radio.yaml`
- answer row: `486`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_BE`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_BE`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_BE" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_BE" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_BE" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d486-getradiostats-wmm-failedbytesreceived-ac_be.json`

### d487-getradiostats-wmm-failedbytesreceived-ac_bk

- case file: `D487_ac_bk_stats_wmmfailedbytesreceived_radio.yaml`
- answer row: `487`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_BK`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_BK`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_BK" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_BK" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_BK" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d487-getradiostats-wmm-failedbytesreceived-ac_bk.json`

### d488-getradiostats-wmm-failedbytesreceived-ac_vi

- case file: `D488_ac_vi_stats_wmmfailedbytesreceived_radio.yaml`
- answer row: `488`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_VI`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_VI`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_VI" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_VI" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_VI" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d488-getradiostats-wmm-failedbytesreceived-ac_vi.json`

### d489-getradiostats-wmm-failedbytesreceived-ac_vo

- case file: `D489_ac_vo_stats_wmmfailedbytesreceived_radio.yaml`
- answer row: `489`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_VO`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedBytesReceived.` / `AC_VO`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_VO" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_VO" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_VO" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d489-getradiostats-wmm-failedbytesreceived-ac_vo.json`

### d490-getradiostats-wmm-failedbytessent-ac_be

- case file: `D490_ac_be_stats_wmmfailedbytessent_radio.yaml`
- answer row: `490`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_BE`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_BE`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_BE" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_BE" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_BE" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d490-getradiostats-wmm-failedbytessent-ac_be.json`

### d491-getradiostats-wmm-failedbytessent-ac_bk

- case file: `D491_ac_bk_stats_wmmfailedbytessent_radio.yaml`
- answer row: `491`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_BK`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_BK`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_BK" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_BK" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_BK" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d491-getradiostats-wmm-failedbytessent-ac_bk.json`

### d492-getradiostats-wmm-failedbytessent-ac_vi

- case file: `D492_ac_vi_stats_wmmfailedbytessent_radio.yaml`
- answer row: `492`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_VI`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_VI`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_VI" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_VI" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_VI" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d492-getradiostats-wmm-failedbytessent-ac_vi.json`

### d493-getradiostats-wmm-failedbytessent-ac_vo

- case file: `D493_ac_vo_stats_wmmfailedbytessent_radio.yaml`
- answer row: `493`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_VO`
- workbook metadata: `WiFi.Radio.{i}.Stats.WmmFailedbytesSent.` / `AC_VO`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: (empty)
- 0401 H excerpt: wl -i wl0 wme_counters | grep -A2 "AC_VO" | grep -E 'tx frames|rx frames' wl -i wl1 wme_counters | grep -A2 "AC_VO" | grep -E 'tx frames|rx frames' wl -i wl2 wme_counters | grep -A2 "AC_VO" | grep -E 'tx frames|rx frames'
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d493-getradiostats-wmm-failedbytessent-ac_vo.json`

### d494-radio-vhtcapabilities

- case file: `D494_vhtcapabilities_radio.yaml`
- answer row: `494`
- mapping status: `exact`
- source metadata: `WiFi.Radio.{i}.` / `VHTCapabilities`
- workbook metadata: `WiFi.Radio.{i}.` / `VHTCapabilities`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: step failed: step_5g_getter (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Not Supported` / `Not Supported`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Fail` / `Fail`
- mismatch bands: `5g`
- 0401 G excerpt: 1. Try to get API default value: root@prplOS:/# ubus-cli WiFi.Radio.*.VHTCapabilities.? > WiFi.Radio.*.VHTCapabilities.? ERROR: get WiFi.Radio.*.VHTCapabilities. failed (2 - object not found)
- 0401 H excerpt: (empty)
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d494-radio-vhtcapabilities.json`

### d528-spectruminfo-bandwidth

- case file: `D528_getspectruminfo_bandwidth.yaml`
- answer row: `528`
- mapping status: `drift`
- source metadata: `WiFi.Radio.{i}.getSpectrumInfo()` / `bandwidth`
- workbook metadata: `WiFi.Radio.{i}.` / `getSpectrumInfo()`
- final status: `Fail`
- evaluation verdict: `Fail`
- attempts used: `2`
- runtime comment: pass_criteria not satisfied (failed after 2/2 attempts)
- actual raw: `Fail` / `Fail` / `Fail`
- expected raw: `Pass` / `Pass` / `Pass`
- actual normalized: `Fail` / `Fail` / `Fail`
- expected normalized: `Pass` / `Pass` / `Pass`
- mismatch bands: `5g, 6g, 2.4g`
- 0401 G excerpt: 1. Power On the GW. 2. Verify SpectrumInfo() bandwidth root@prplOS:/# ubus-cli "WiFi.Radio.*.getSpectrumInfo() bandwidth" > WiFi.Radio.*.getSpectrumInfo() bandwidth WiFi.Radio.1.getSpectrumInfo() returned [ [ ] ] WiFi.Radio.2.getSpectrum...
- 0401 H excerpt: root@prplOS:/# wl -i wl0 chanspec 36 (0xd024) Channel: 36, Band: 5 GHz, Bandwidth: 20 MHz Hex breakdown: 0xd024 Bits Meaning 0x0024 Channel 36 0x1000 5 GHz band 0xC000 20 MHz root@prplOS:/# wl -i wl1 chanspec 6g1 (0x5001) Channel: 1, Ban...
- trace: `/home/paul_chen/prj_pri/testpilot/plugins/wifi_llapi/reports/agent_trace/20260401T152827516151/d528-spectruminfo-bandwidth.json`
