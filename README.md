# Awesome Local Inverters [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, community-maintained list of solar inverters, rated by how well they can be run **data-sovereign**: locally, without a vendor cloud, through open interfaces – and ideally on open hardware.

An inverter knows when you produce and consume energy, and therefore a lot about your daily life. If it is connected to a vendor cloud, it can also be reconfigured – or switched off – from outside. In November 2024, Deye inverters in the USA, the UK, Pakistan and other countries suddenly stopped working; Deye denied any remote control and blamed a built-in authorization check ([heise online](https://heise.de/-10183716)). In 2025, security researchers disclosed 46 new vulnerabilities in products from Sungrow, Growatt and SMA, most of them in cloud backends and monitoring components ([Forescout SUN:DOWN](https://www.forescout.com/blog/grid-security-new-vulnerabilities-in-solar-power-systems-exposed/)).

The good news: many inverters work perfectly well without any cloud. But that knowledge is scattered across forums, GitHub issues and wikis. This list brings it together, applies **transparent, verifiable criteria** and makes it easy for everyone to contribute.

## Contents

- [Rating criteria](#rating-criteria)
- [Inverter list](#inverter-list)
- [Rating details](#rating-details)
- [Open source hardware projects](#open-source-hardware-projects)
- [Tools for local operation](#tools-for-local-operation)
- [Hardening your installation](#hardening-your-installation)
- [Background reading](#background-reading)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## Rating criteria

Each inverter earns one point (★) per criterion met, up to three stars. Full definitions, edge cases and examples: **[CRITERIA.md](CRITERIA.md)**.

| # | Criterion | The point is awarded if … |
|---|---|---|
| 1 | **Local operation without cloud** | the device keeps working indefinitely with its internet access blocked: it feeds in, can be configured and monitored locally, and needs no periodic contact with vendor servers (e.g. to renew access tokens). |
| 2 | **Open local interface** | live data can be read – and ideally the device controlled – over the local network or a local bus, through a vendor-documented **or reverse-engineered** interface (e.g. OpenDTU, Modbus, MQTT, local REST API), and a working Home Assistant integration or equivalent open tooling exists. Cloud-only APIs do not count. |
| 3 | **Open source hardware** | schematics, PCB layout and bill of materials are published under an open license, in line with the [OSHWA definition](https://www.oshwa.org/definition/). Open firmware alone does not count. |

**Legend**

| Symbol | Meaning |
|---|---|
| ★ / ☆ | Criterion met / not met (★★☆ = 2 of 3 points). |
| ⚠️ | Rating with a caveat, e.g. a one-time setup needs a vendor account. See the rating details. |
| ❔ | Needs review: the evidence is incomplete. Help wanted! |
| Balcony solar | **Yes** = designed for plug-in ("balcony") PV, i.e. within the plug-in feed-in limit (800 VA in Germany) or officially configurable to it. |

The rating covers data sovereignty only – not efficiency, reliability, price or electrical safety.

## Inverter list

<!-- BEGIN GENERATED: stats -->
**27 entries** · ★★★ 0 · ★★☆ 24 · ★☆☆ 1 · ☆☆☆ 2 · ❔ needs review: 2
<!-- END GENERATED: stats -->

<!-- BEGIN GENERATED: table -->
| Inverter | Manufacturer | Power (AC) | Balcony solar | Home Assistant integration | Rating |
|---|---|---|:---:|---|:---:|
| [APsystems DS3 series with ECU gateway](#apsystems-ds3-series-with-ecu-gateway) | APsystems | 0.6–0.96 kVA | Yes | [homeassistant-apsystems_ecur](https://github.com/ksheumaker/homeassistant-apsystems_ecur) | ★★☆ ⚠️ |
| [APsystems EZ1 series](#apsystems-ez1-series) | APsystems | 0.8 kVA (DE setting) | Yes | [Home Assistant core integration](https://www.home-assistant.io/integrations/apsystems/) | ★★☆ ⚠️ |
| [Deye microinverters](#deye-microinverters) | Deye | 0.6–2 kVA | Yes | [ha-solarman](https://github.com/davidrapan/ha-solarman) | ★★☆ ⚠️ |
| [Hoymiles HM series](#hoymiles-hm-series) | Hoymiles | 0.3–1.5 kVA | Yes | [OpenDTU](https://github.com/tbnobody/OpenDTU) · [AhoyDTU](https://github.com/lumapu/ahoy) | ★★☆ |
| [Hoymiles HMS series](#hoymiles-hms-series) | Hoymiles | 0.3–2 kVA | Yes | [OpenDTU](https://github.com/tbnobody/OpenDTU) · [AhoyDTU](https://github.com/lumapu/ahoy) | ★★☆ |
| [Hoymiles HMS-W series (built-in Wi-Fi)](#hoymiles-hms-w-series-built-in-wi-fi) | Hoymiles | 0.4–0.8 kVA | Yes | [ha-hoymiles-wifi](https://github.com/suaveolent/ha-hoymiles-wifi) | ★★☆ ⚠️ |
| [Marstek Venus E / A / D](#marstek-venus-e--a--d) | Marstek | up to 2.5 kW (can be limited to 0.8 kW) | Yes | [marstek_venus_modbus](https://github.com/ViperRNMC/marstek_venus_modbus) · [ha-marstek-local-api](https://github.com/jaapp/ha-marstek-local-api/) | ★★☆ ⚠️ |
| [TSUN TSOL-MS series (Gen3/Gen3Plus)](#tsun-tsol-ms-series-gen3gen3plus) | TSUN | 0.6–3 kVA | Yes | [tsun-gen3-proxy](https://github.com/s-allius/tsun-gen3-proxy) | ★★☆ ⚠️ |
| [Zendure SolarFlow 800 / 2400 AC](#zendure-solarflow-800--2400-ac) | Zendure | 0.8–2.4 kW | Yes | [Zendure-HA-zenSDK](https://github.com/Gielz1986/Zendure-HA-zenSDK) · [Zendure-HA](https://github.com/zendure/zendure-ha) | ★★☆ ⚠️ |
| [Deye hybrid SG04LP3 series](#deye-hybrid-sg04lp3-series) | Deye | 5–12 kW | No | [ha-solarman](https://github.com/davidrapan/ha-solarman) | ★★☆ ⚠️ |
| [Fox ESS H1 / H3 hybrid](#fox-ess-h1--h3-hybrid) | Fox ESS | 3–12 kW | No | [foxess_modbus](https://github.com/nathanmarlor/foxess_modbus) | ★★☆ |
| [Fronius Primo GEN24 / Symo GEN24](#fronius-primo-gen24--symo-gen24) | Fronius | 3–10 kW | No | [Home Assistant core integration](https://www.home-assistant.io/integrations/fronius/) | ★★☆ |
| [Solis S6 / RHI series](#solis-s6--rhi-series) | Ginlong Solis | ≈1–10 kW (residential) | No | [homeassistant-solax-modbus](https://github.com/wills106/homeassistant-solax-modbus) · [ha-solarman](https://github.com/davidrapan/ha-solarman) | ★★☆ |
| [GoodWe ET / EH / DNS series](#goodwe-et--eh--dns-series) | GoodWe | 3–10 kW (residential) | No | [Home Assistant core integration](https://www.home-assistant.io/integrations/goodwe/) | ★★☆ ⚠️ |
| [Growatt MIN / MOD TL-X](#growatt-min--mod-tl-x) | Growatt | 2.5–15 kW | No | [Grott](https://github.com/johanmeijer/grott) · [ESPHome growatt_solar](https://esphome.io/components/sensor/growatt_solar/) · [homeassistant-solax-modbus](https://github.com/wills106/homeassistant-solax-modbus) | ★★☆ |
| [Hoymiles HMT series (three-phase)](#hoymiles-hmt-series-three-phase) | Hoymiles | 1.6–2.25 kVA | No | [OpenDTU](https://github.com/tbnobody/OpenDTU) | ★★☆ |
| [Huawei SUN2000 (residential)](#huawei-sun2000-residential) | Huawei | 2–10 kW | No | [huawei_solar](https://github.com/wlcrs/huawei_solar) | ★★☆ ⚠️ |
| [KOSTAL PLENTICORE plus](#kostal-plenticore-plus) | KOSTAL Solar Electric | 3–10 kW | No | [Home Assistant core integration](https://www.home-assistant.io/integrations/kostal_plenticore/) | ★★☆ |
| [SMA Sunny Boy / Sunny Tripower](#sma-sunny-boy--sunny-tripower) | SMA Solar Technology | 1.5–10 kW | No | [Home Assistant core integration](https://www.home-assistant.io/integrations/sma/) | ★★☆ |
| [SolarEdge HD-Wave / Home Hub](#solaredge-hd-wave--home-hub) | SolarEdge | 2–10 kW (residential) | No | [solaredge-modbus-multi](https://github.com/WillCodeForCats/solaredge-modbus-multi) | ★★☆ ⚠️ |
| [SolaX X1 / X3 Hybrid](#solax-x1--x3-hybrid) | SolaX Power | 3–15 kW | No | [Home Assistant core integration](https://www.home-assistant.io/integrations/solax/) · [homeassistant-solax-modbus](https://github.com/wills106/homeassistant-solax-modbus) | ★★☆ |
| [Sungrow SH-RS / SH-RT hybrid](#sungrow-sh-rs--sh-rt-hybrid) | Sungrow | 3–10 kW | No | [Sungrow SHx Modbus for Home Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) | ★★☆ ⚠️ |
| [Victron MultiPlus-II with GX device](#victron-multiplus-ii-with-gx-device) | Victron Energy | 3–15 kVA | No | [hass-victron](https://github.com/sfstar/hass-victron) | ★★☆ |
| [Voltronic Axpert / MPP Solar (off-grid)](#voltronic-axpert--mpp-solar-off-grid) | Voltronic Power | ≈1–11 kW | No | [ESPHome pipsolar](https://esphome.io/components/pipsolar/) · [mpp-solar](https://github.com/jblance/mpp-solar) | ★★☆ |
| [Enphase IQ microinverters with IQ Gateway](#enphase-iq-microinverters-with-iq-gateway) | Enphase Energy | ≈0.25–0.4 kVA per unit | No | [Home Assistant core integration](https://www.home-assistant.io/integrations/enphase_envoy/) | ★☆☆ |
| [Anker SOLIX Solarbank 2 / 3](#anker-solix-solarbank-2--3) | Anker | 0.8 kW AC (DE setting) | Yes | [ha-anker-solix (cloud API)](https://github.com/thomluther/ha-anker-solix) | ☆☆☆ ❔ |
| [EcoFlow PowerStream](#ecoflow-powerstream) | EcoFlow | 0.6–0.8 kW | Yes | [hassio-ecoflow-cloud (cloud API)](https://github.com/tolwi/hassio-ecoflow-cloud) | ☆☆☆ ❔ |
<!-- END GENERATED: table -->

> **No certified, commercially available inverter earns the open-hardware star yet** – at least none we know of. Know one? Please [open an issue](../../issues/new/choose).

## Rating details

Every rating is backed by a rationale per criterion and public sources. These sections are generated from [`data/inverters.yml`](data/inverters.yml).

<!-- BEGIN GENERATED: details -->
### APsystems DS3 series with ECU gateway

**Manufacturer:** APsystems · **Models:** DS3-S, DS3-L, DS3, DS3-H with ECU-R / ECU-C / ECU-B · **Power:** 0.6–0.96 kVA · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | The microinverters talk Zigbee to a local ECU gateway, which can be queried on the LAN without the EMA cloud. |
| 2 · Open local interface | ✅ | The ECU exposes a local (unofficial, community-documented) socket interface; a Home Assistant custom integration exists. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- APsystems' EMEA warranty terms require the microinverters to be monitored via the EMA portal – check your warranty before cutting the ECU off the internet.

**Notes:** DS3-S and DS3-L fit plug-in (balcony) limits; DS3 and DS3-H are mainly used on rooftops.

**Sources:** [ksheumaker/homeassistant-apsystems_ecur](https://github.com/ksheumaker/homeassistant-apsystems_ecur) · [cdn.estg.eu](https://cdn.estg.eu/p/d/3/b/9/d3b95b662c2731d4319a7d9737d4ccc5e08b2c38_APsystems_DS3_series_Datasheet___FR.pdf) · [solarproof.com.au](https://solarproof.com.au/datasheets/inv_datasheet_APsystems%20DS3%20Datasheet.pdf)

<sub>Last reviewed: 2026-10</sub>

### APsystems EZ1 series

**Manufacturer:** APsystems · **Models:** EZ1-M (community reports for further EZ1/EZ1D variants) · **Power:** 0.8 kVA (DE setting) · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | With "Local Mode" set to "Continuously", the inverter is queried and controlled over the LAN without the APsystems cloud. |
| 2 · Open local interface | ✅ | Official local HTTP API, supported by a Home Assistant core integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Local Mode has to be enabled once via Bluetooth in the vendor app.
- The local API offers no firmware-update endpoint; updates come through the APsystems cloud.

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/apsystems/) · [community.home-assistant.io](https://community.home-assistant.io/t/apsystems-ez1-m-ez1-spe-ez1-lv-ez1-h-ez1d-l-ez1d-ez1d-h-community-enhanced-integration-extended-sensors-all-models-overnight-fix-more/994091)

<sub>Last reviewed: 2026-10</sub>

### Deye microinverters

**Manufacturer:** Deye · **Models:** SUN600G3, SUN800G3, SUN-M60/M80 G3/G4, SUN2000G3 (4 MPPT); also sold as Bosswerk MI series · **Power:** 0.6–2 kVA · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Runs without internet. The built-in Solarman-type logger can be kept off the cloud by blocking internet access or pointing its server setting to an unused local IP. |
| 2 · Open local interface | ✅ | The Solarman V5 protocol (TCP 8899, Modbus inside) is reverse-engineered and widely implemented; read and write access via a Home Assistant custom integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- The integrated Wi-Fi logger has had security weaknesses (e.g. readable access credentials) – change the access-point password and isolate the device in its own network.

**Notes:** In November 2024, Deye-branded (hybrid) inverters in the USA, the UK, Pakistan and other countries stopped working; Deye attributed this to a built-in authorization check and denied remote control. Not specific to microinverters, but a strong argument for keeping inverters off the vendor cloud.

**Sources:** [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) · [borncity.com](https://borncity.com/blog/?p=286806) · [heise.de](https://heise.de/-10183716)

<sub>Last reviewed: 2026-10</sub>

### Hoymiles HM series

**Manufacturer:** Hoymiles · **Models:** HM-300, HM-350, HM-400, HM-600, HM-700, HM-800, HM-1200, HM-1500 · **Power:** 0.3–1.5 kVA · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | The inverter has no internet connection of its own and feeds in without any gateway. Monitoring, power limiting and switching on/off are handled locally by OpenDTU or AhoyDTU instead of Hoymiles' cloud-bound DTUs. |
| 2 · Open local interface | ✅ | The proprietary 2.4 GHz radio protocol (nRF24L01+) has been reverse-engineered. OpenDTU and AhoyDTU expose live data via web UI, REST API and MQTT with Home Assistant auto-discovery. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Notes:** The official DTU-Lite/DTU-Pro gateways upload data to the S-Miles cloud. An ESP32 with an nRF24L01+ module running OpenDTU or AhoyDTU (approx. €20 in parts) replaces them completely.

**Sources:** [tbnobody/OpenDTU](https://github.com/tbnobody/OpenDTU) · [raspberry.tips](https://raspberry.tips/raspberrypi-tutorials/balkonkraftwerk-photovoltaik-wechselrichter-ertrag-auslesen-esp32-micro-controller-mit-opendtu)

<sub>Last reviewed: 2026-10</sub>

### Hoymiles HMS series

**Manufacturer:** Hoymiles · **Models:** HMS-300…500-1T, HMS-600…1000-2T, HMS-1600…2000-4T (without "W") · **Power:** 0.3–2 kVA · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | No internet connection of its own; feeds in without a gateway. Configuration and monitoring work fully locally via OpenDTU or AhoyDTU. |
| 2 · Open local interface | ✅ | The sub-GHz radio protocol (CMT2300A) has been reverse-engineered. OpenDTU/AhoyDTU provide MQTT with Home Assistant auto-discovery and a REST API. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Notes:** Requires a DTU board with a CMT2300A radio module (not the nRF24L01+ used for the HM series). The Wi-Fi variants (HMS-xxxW) use a different protocol and are listed separately.

**Sources:** [tbnobody/OpenDTU](https://github.com/tbnobody/OpenDTU) · [raspberry.tips](https://raspberry.tips/raspberrypi-tutorials/balkonkraftwerk-photovoltaik-wechselrichter-ertrag-auslesen-esp32-micro-controller-mit-opendtu)

<sub>Last reviewed: 2026-10</sub>

### Hoymiles HMS-W series (built-in Wi-Fi)

**Manufacturer:** Hoymiles · **Models:** HMS-400W-1T, HMS-800W-2T and other HMS-xxxW variants · **Power:** 0.4–0.8 kVA · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Feeds in without internet access. Wi-Fi settings, power limit and on/off can be set locally with the open-source hoymiles-wifi library, so the device can run in an isolated network. |
| 2 · Open local interface | ✅ | The protobuf-based local protocol of the integrated DTU has been reverse-engineered (hoymiles-wifi); a Home Assistant custom integration exists. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Once connected to Wi-Fi the device uploads to the S-Miles cloud by default – block its internet access at the router/firewall to keep data local.
- The integration's authors warn against using the power limit for fast zero-export control (EEPROM wear).

**Notes:** Not supported by OpenDTU/AhoyDTU, which only handle the radio-based models.

**Sources:** [suaveolent/ha-hoymiles-wifi](https://github.com/suaveolent/ha-hoymiles-wifi) · [pypi.org](https://pypi.org/project/hoymiles-wifi)

<sub>Last reviewed: 2026-10</sub>

### Marstek Venus E / A / D

**Manufacturer:** Marstek · **Models:** Venus E (v2/v3), Venus A, Venus D · **Power:** up to 2.5 kW (can be limited to 0.8 kW) · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Monitored and controlled over local Modbus (RS485 adapter, or Ethernet on newer models) without a Marstek account; community web apps replace the vendor app. |
| 2 · Open local interface | ✅ | Modbus RTU/TCP plus an official local "Open API" (UDP); several Home Assistant integrations. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- The official Open API must be enabled via the Marstek app or the Venus Monitor tool.

**Sources:** [ViperRNMC/marstek_venus_modbus](https://github.com/ViperRNMC/marstek_venus_modbus) · [jaapp/ha-marstek-local-api](https://github.com/jaapp/ha-marstek-local-api/) · [community.simon42.com](https://community.simon42.com/t/marstek-modbus-suite-integration-mit-fancy-dashboard/92316)

<sub>Last reviewed: 2026-10</sub>

### TSUN TSOL-MS series (Gen3/Gen3Plus)

**Manufacturer:** TSUN · **Models:** TSOL-MS600/700/800, MS1600/1800/2000, MS3000 · **Power:** 0.6–3 kVA · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | tsun-gen3-proxy collects data locally and its connection to the TSUN cloud can be switched off; the inverter keeps feeding in. |
| 2 · Open local interface | ✅ | Reverse-engineered logger protocol; the proxy publishes data to MQTT with Home Assistant auto-discovery. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Without the cloud connection, no remote firmware or parameter updates are possible. Newer firmware encrypts cloud traffic (TLS), so the proxy must run in "client mode".

**Sources:** [hub.docker.com](https://hub.docker.com/r/sallius/tsun-gen3-proxy) · [community.home-assistant.io](https://community.home-assistant.io/t/tsun-proxy-now-as-add-on/870131)

<sub>Last reviewed: 2026-10</sub>

### Zendure SolarFlow 800 / 2400 AC

**Manufacturer:** Zendure · **Models:** SolarFlow 800, 800 Plus, 800 Pro, 2400 AC/Pro · **Power:** 0.8–2.4 kW · **Balcony solar:** Yes · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Once the local API is enabled, the device is monitored and controlled entirely over the LAN and keeps working when the internet or the Zendure cloud is unavailable. |
| 2 · Open local interface | ✅ | Official local HTTP API (zenSDK) with community and vendor Home Assistant integrations. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- The local API is off by default (EN 18031) and must be enabled once in the Zendure app (account required).
- Older models (Hyper 2000, Hub 1200/2000, Ace 1500) have no local API and are not covered by this rating.

**Sources:** [community.home-assistant.io](https://community.home-assistant.io/t/zendure-restapi-local-zero-export-control-for-solarflow-batteries/1029076) · [Gielz1986/Zendure-HA-zenSDK](https://github.com/Gielz1986/Zendure-HA-zenSDK) · [pypi.org](https://pypi.org/project/zendure/)

<sub>Last reviewed: 2026-10</sub>

### Deye hybrid SG04LP3 series

**Manufacturer:** Deye · **Models:** SUN-5K…12K-SG04LP3-EU; related models sold under other brands (e.g. Sunsynk) · **Power:** 5–12 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | All settings are available on the device display and via local Modbus; the cloud is optional. |
| 2 · Open local interface | ✅ | Solarman V5 (TCP 8899) via the logger, or Modbus RTU via RS485 (e.g. ESPHome bridge). |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Some newer models ship with Deye's own logger, which may not support local Solarman V5 access – use RS485/Modbus instead.

**Notes:** See the November 2024 deactivation incident under "Background reading".

**Sources:** [davidrapan/ha-solarman](https://github.com/davidrapan/ha-solarman) · [community.home-assistant.io](https://community.home-assistant.io/t/deye-cloud-integration/813153) · [heise.de](https://heise.de/-10183716)

<sub>Last reviewed: 2026-10</sub>

### Fox ESS H1 / H3 hybrid

**Manufacturer:** Fox ESS · **Models:** H1 (single-phase), H3 (three-phase) · **Power:** 3–12 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Configuration via the display and local Modbus; Fox ESS Cloud is optional. |
| 2 · Open local interface | ✅ | Modbus via RS485 or the LAN port; Home Assistant custom integration with read and write support. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [nathanmarlor/foxess_modbus](https://github.com/nathanmarlor/foxess_modbus)

<sub>Last reviewed: 2026-10</sub>

### Fronius Primo GEN24 / Symo GEN24

**Manufacturer:** Fronius · **Models:** Primo GEN24 (Plus), Symo GEN24 (Plus) · **Power:** 3–10 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Commissioning and configuration via the inverter's local web interface; Solar.web is optional. |
| 2 · Open local interface | ✅ | Fronius Solar API (local JSON/HTTP) and Modbus TCP (SunSpec), both documented by the vendor. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Notes:** Fronius devices are among the most frequently found inverter interfaces exposed to the internet (Forescout, 2025) – never port-forward the web UI.

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/fronius/) · [securityweek.com](https://www.securityweek.com/35000-solar-power-systems-exposed-to-internet/)

<sub>Last reviewed: 2026-10</sub>

### Solis S6 / RHI series

**Manufacturer:** Ginlong Solis · **Models:** S6 string inverters, RHI hybrid inverters · **Power:** ≈1–10 kW (residential) · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Configuration via the device display and local Modbus; SolisCloud is optional. |
| 2 · Open local interface | ✅ | Modbus RTU via the RS485/COM port; Solarman-based loggers via Solarman V5. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [wills106/homeassistant-solax-modbus](https://github.com/wills106/homeassistant-solax-modbus)

<sub>Last reviewed: 2026-10</sub>

### GoodWe ET / EH / DNS series

**Manufacturer:** GoodWe · **Models:** ET, EH, BT, BH, ES, DNS, DT and others · **Power:** 3–10 kW (residential) · **Balcony solar:** No · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Commissioning via the SolarGo app over a direct local connection; the SEMS portal is optional. |
| 2 · Open local interface | ✅ | Local UDP/Modbus protocol, supported by a Home Assistant core integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Some newer communication modules changed the local protocol – check the integration docs for compatibility before buying.

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/goodwe/)

<sub>Last reviewed: 2026-10</sub>

### Growatt MIN / MOD TL-X

**Manufacturer:** Growatt · **Models:** MIN 2500–6000TL-X(H), MOD 3–15KTL3-X(H) · **Power:** 2.5–15 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Operates without ShineServer; configuration via display and local RS485/Modbus. |
| 2 · Open local interface | ✅ | Growatt's Modbus RTU protocol documentation is publicly available; Grott intercepts ShineWiFi/ShineLAN traffic locally; ESPHome has a native Growatt component. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Notes:** Growatt's cloud was affected by account-takeover vulnerabilities (SUN:DOWN, 2025) – keeping the inverter off the cloud is strongly recommended.

**Sources:** [johanmeijer/grott](https://github.com/johanmeijer/grott) · [forescout.com](https://www.forescout.com/blog/grid-security-new-vulnerabilities-in-solar-power-systems-exposed/)

<sub>Last reviewed: 2026-10</sub>

### Hoymiles HMT series (three-phase)

**Manufacturer:** Hoymiles · **Models:** HMT-1600/1800/2000-4T, HMT-1800/2250-6T · **Power:** 1.6–2.25 kVA · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | No internet connection of its own; fully locally manageable via OpenDTU. |
| 2 · Open local interface | ✅ | Reverse-engineered radio protocol (CMT2300A); MQTT with Home Assistant auto-discovery. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [tbnobody/OpenDTU](https://github.com/tbnobody/OpenDTU)

<sub>Last reviewed: 2026-10</sub>

### Huawei SUN2000 (residential)

**Manufacturer:** Huawei · **Models:** SUN2000-2…6KTL-L1, SUN2000-3…10KTL-M1 · **Power:** 2–10 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Inverter and SDongle operate without the FusionSolar cloud; settings can be changed over a direct local app connection or via Modbus. |
| 2 · Open local interface | ✅ | Modbus RTU (RS485) and Modbus TCP (SDongle / inverter Wi-Fi); register definitions are published by Huawei; mature Home Assistant custom integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Modbus TCP is disabled by default and must be enabled in the installer settings; installers usually register the plant in FusionSolar – ask for local-only commissioning.

**Sources:** [wlcrs/huawei_solar](https://github.com/wlcrs/huawei_solar)

<sub>Last reviewed: 2026-10</sub>

### KOSTAL PLENTICORE plus

**Manufacturer:** KOSTAL Solar Electric · **Models:** PLENTICORE plus 3.0–10 (PLENTICORE G3 also supported by the integration) · **Power:** 3–10 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Configuration via the local web interface; KOSTAL Solar Portal is optional. |
| 2 · Open local interface | ✅ | Local REST API and Modbus TCP (SunSpec); Home Assistant core integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/kostal_plenticore/)

<sub>Last reviewed: 2026-10</sub>

### SMA Sunny Boy / Sunny Tripower

**Manufacturer:** SMA Solar Technology · **Models:** Sunny Boy 1.5–6.0, Sunny Tripower 3.0–10.0 (Webconnect/Speedwire generation) · **Power:** 1.5–10 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Commissioning and configuration via the local web interface; Sunny Portal is optional. |
| 2 · Open local interface | ✅ | Webconnect/Speedwire (Home Assistant core) and vendor-documented Modbus TCP (SunSpec). |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Notes:** The SMA vulnerability disclosed in SUN:DOWN (2025) affected the Sunny Portal cloud, not the inverters – another argument for local operation.

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/sma/) · [thehackernews.com](https://thehackernews.com/2025/03/researchers-uncover-46-critical-flaws.html)

<sub>Last reviewed: 2026-10</sub>

### SolarEdge HD-Wave / Home Hub

**Manufacturer:** SolarEdge · **Models:** SE2200H…SE6000H, SE3K…SE10K, Home Hub (SExK-RWB) · **Power:** 2–10 kW (residential) · **Balcony solar:** No · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | The inverter keeps producing and can be read and controlled locally via Modbus TCP without the monitoring portal. |
| 2 · Open local interface | ✅ | Vendor-documented Modbus TCP (SunSpec). Note: the Home Assistant core "SolarEdge" integration uses the cloud API – use the Modbus integration instead. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- Commissioning and enabling Modbus TCP are done with the SetApp, which requires a SolarEdge account.

**Sources:** [WillCodeForCats/solaredge-modbus-multi](https://github.com/WillCodeForCats/solaredge-modbus-multi)

<sub>Last reviewed: 2026-10</sub>

### SolaX X1 / X3 Hybrid

**Manufacturer:** SolaX Power · **Models:** X1-Hybrid, X3-Hybrid (G3/G4) · **Power:** 3–15 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Configuration via the display and local interfaces; SolaX Cloud is optional. |
| 2 · Open local interface | ✅ | Local API of the Pocket Wi-Fi dongle (core integration) and Modbus RTU/TCP. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/solax/) · [wills106/homeassistant-solax-modbus](https://github.com/wills106/homeassistant-solax-modbus)

<sub>Last reviewed: 2026-10</sub>

### Sungrow SH-RS / SH-RT hybrid

**Manufacturer:** Sungrow · **Models:** SH3.0RS…SH6.0RS, SH5.0RT…SH10RT (with WiNet-S) · **Power:** 3–10 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3) ⚠️

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Local access via the iSolarCloud app's direct connection and Modbus; the cloud is optional. |
| 2 · Open local interface | ✅ | Modbus TCP via the WiNet-S dongle (or LAN/RS485) with a published register map. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

⚠️ **Caveats:**
- The WiNet-S dongle and the cloud were affected by serious vulnerabilities (SUN:DOWN, 2025, since patched) – keep firmware current and isolate the dongle.

**Sources:** [mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) · [forescout.com](https://www.forescout.com/blog/grid-security-new-vulnerabilities-in-solar-power-systems-exposed/)

<sub>Last reviewed: 2026-10</sub>

### Victron MultiPlus-II with GX device

**Manufacturer:** Victron Energy · **Models:** MultiPlus-II, Quattro-II with Cerbo GX / Ekrano GX · **Power:** 3–15 kVA · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | Configuration via VictronConnect (Bluetooth/USB, no account) and the GX device's local interface; the VRM portal is optional. |
| 2 · Open local interface | ✅ | Vendor-documented Modbus TCP and MQTT on the GX device; Home Assistant custom integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Notes:** Venus OS, the software on GX devices, is open source – a plus for transparency, but open software does not earn the open-hardware star.

**Sources:** [sfstar/hass-victron](https://github.com/sfstar/hass-victron)

<sub>Last reviewed: 2026-10</sub>

### Voltronic Axpert / MPP Solar (off-grid)

**Manufacturer:** Voltronic Power · **Models:** Axpert / PIP / LV series; rebranded as MPP Solar, EASun and others · **Power:** ≈1–11 kW · **Balcony solar:** No · **Rating:** ★★☆ (2/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ✅ | No cloud component required at all; the optional Wi-Fi stick can simply be left out. |
| 2 · Open local interface | ✅ | Serial protocol (RS232/USB) publicly documented and widely implemented (ESPHome, mpp-solar). |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [esphome.io](https://esphome.io/components/pipsolar/) · [jblance/mpp-solar](https://github.com/jblance/mpp-solar)

<sub>Last reviewed: 2026-10</sub>

### Enphase IQ microinverters with IQ Gateway

**Manufacturer:** Enphase Energy · **Models:** IQ7 / IQ8 family with IQ Gateway (Envoy) · **Power:** ≈0.25–0.4 kVA per unit · **Balcony solar:** No · **Rating:** ★☆☆ (1/3)

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ❌ | Since gateway firmware 7, local API access requires a token issued via an Enphase account; owner tokens expire and can only be renewed online. Commissioning uses the Enphase installer app with an account. |
| 2 · Open local interface | ✅ | Local HTTP API on the IQ Gateway (token-protected), supported by a Home Assistant core integration. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

**Sources:** [home-assistant.io](https://www.home-assistant.io/integrations/enphase_envoy/)

<sub>Last reviewed: 2026-10</sub>

### Anker SOLIX Solarbank 2 / 3

**Manufacturer:** Anker · **Models:** Solarbank 2 (E1600 Pro/Plus), Solarbank 3 (E2700 Pro) · **Power:** 0.8 kW AC (DE setting) · **Balcony solar:** Yes · **Rating:** ☆☆☆ (0/3) ❔

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ❌ | Setup and configuration require the Anker app and an Anker account. |
| 2 · Open local interface | ❌ | The available Home Assistant integration uses Anker's cloud API (and Anker's MQTT server); no local interface is known for these models. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

❔ **Needs review:** the evidence for this rating is incomplete. Own this device? Please help verify it.

**Notes:** Newer models (Solarbank Max AC, Solarbank 4 E5000 Pro) support local Modbus TCP through an official Anker integration (github.com/anker-charging/ha-anker-solix-official) – not yet rated, help wanted!

**Sources:** [thomluther/ha-anker-solix](https://github.com/thomluther/ha-anker-solix) · [anker-charging/ha-anker-solix-official](https://github.com/anker-charging/ha-anker-solix-official/releases)

<sub>Last reviewed: 2026-10</sub>

### EcoFlow PowerStream

**Manufacturer:** EcoFlow · **Models:** PowerStream 600 W / 800 W · **Power:** 0.6–0.8 kW · **Balcony solar:** Yes · **Rating:** ☆☆☆ (0/3) ❔

| Criterion | Met | Rationale |
|---|:---:|---|
| 1 · Local operation without cloud | ❌ | Changing the base-load/output setting requires the cloud; without internet the device stays at its last setting. |
| 2 · Open local interface | ❌ | Official and common community integrations use the EcoFlow cloud. A community Bluetooth-to-MQTT bridge for local control appeared in 2026 and still needs evaluation. |
| 3 · Open source hardware | ❌ | No schematics or PCB design files are published. |

❔ **Needs review:** the evidence for this rating is incomplete. Own this device? Please help verify it.

**Sources:** [tolwi/hassio-ecoflow-cloud](https://github.com/tolwi/hassio-ecoflow-cloud/discussions/414)

<sub>Last reviewed: 2026-10</sub>
<!-- END GENERATED: details -->

## Open source hardware projects

> [!WARNING]
> These are experimental hobby projects. They are **not certified** for grid connection (e.g. VDE-AR-N 4105) and must never be connected to the public grid. Mains voltage is lethal. They are listed – without a rating – because they show what an open inverter could look like.

- [OSSI – Open Source Solar Inverter](https://github.com/pumbaba/OSSI) - Aims to build a solar inverter from commonly available parts with fully open software, hardware and mechanics. Early stage (requirements).
- [Grid Tie Inverter v3](https://github.com/fotherja/Grid_Tie_Inverter_3) - STM32-based grid-tie inverter with KiCad PCB files and firmware under the MIT license.
- [openMicroInverter](https://github.com/kikiloaw/openMicroInverter) - Open hardware platform for experimenting with DC-to-AC conversion, energy metering and grid synchronisation.
- [Libre Solar](https://libre.solar) - Open hardware MPPT charge controllers and battery management systems for the DC side – not an inverter, but a good example of mature open power electronics.

## Tools for local operation

- [OpenDTU](https://github.com/tbnobody/OpenDTU) - ESP32 firmware replacing Hoymiles' cloud DTUs; MQTT with Home Assistant auto-discovery.
- [OpenDTU-OnBattery](https://github.com/helgeerbe/OpenDTU-OnBattery) - OpenDTU fork with dynamic power limiting, battery and charger support.
- [AhoyDTU](https://github.com/lumapu/ahoy) - Alternative open firmware for talking to Hoymiles (and compatible) microinverters.
- [hoymiles-wifi](https://pypi.org/project/hoymiles-wifi) - Python library for the local protocol of Hoymiles Wi-Fi inverters and DTUs.
- [ha-solarman](https://github.com/davidrapan/ha-solarman) - Local Home Assistant integration for Solarman-based loggers (Deye, Sofar, Solis and many more).
- [homeassistant-solax-modbus](https://github.com/wills106/homeassistant-solax-modbus) - Local Modbus integration for SolaX, Growatt, Solis, Sofar and other brands.
- [Grott](https://github.com/johanmeijer/grott) - Local proxy for Growatt ShineWiFi/ShineLAN data loggers.
- [tsun-gen3-proxy](https://github.com/s-allius/tsun-gen3-proxy) - Local MQTT proxy for TSUN Gen3 microinverters with an optional cloud connection.
- [mpp-solar](https://github.com/jblance/mpp-solar) - Python tooling for Voltronic/MPP Solar inverters and many BMS.
- [ESPHome](https://esphome.io) - Build local RS485/Modbus bridges for inverters with native components (e.g. Growatt, PIPSolar).
- [evcc](https://evcc.io) - Local energy management for EV charging and home batteries, supporting many inverters without a cloud.
- [Home Assistant Energy](https://www.home-assistant.io/docs/energy/) - Local energy dashboard to analyse production and consumption.

## Hardening your installation

- **Separate network.** Put inverters, data loggers and gateways into their own VLAN or guest network and block their internet access at the router or firewall.
- **Change default passwords.** Several inverters and loggers ship with weak or well-known Wi-Fi access-point credentials.
- **Disable cloud uploads.** Use the device's own switch where available (e.g. the server setting of Solarman loggers, the cloud toggle of tsun-gen3-proxy).
- **Never port-forward.** Do not expose inverter web interfaces or Modbus ports to the internet; use a VPN or your home-automation system for remote access.
- **Write carefully.** Prefer read-only access. Do not write power limits every few seconds – many inverters store them in EEPROM/flash with limited write cycles.
- **Leave grid protection alone.** Country codes and voltage/frequency limits belong to the grid certification (e.g. VDE-AR-N 4105) and must not be changed.
- **Plan firmware updates.** Prefer local update paths. If updates need the cloud, allow internet access temporarily and deliberately.
- **Check warranty terms.** Some vendors tie their warranty to cloud monitoring.

## Background reading

- [SUN:DOWN – Forescout Vedere Labs (2025)](https://www.forescout.com/blog/grid-security-new-vulnerabilities-in-solar-power-systems-exposed/) - 46 new vulnerabilities in Sungrow, Growatt and SMA products and grid-level attack scenarios.
- [Deactivated Deye and Sol-Ark inverters in the USA – heise online (2024)](https://heise.de/-10183716) - Statements from Deye and Sol-Ark on the November 2024 incident.
- [Deye deactivates solar inverters in USA, UK and Pakistan – Born's Tech and Windows World (2024)](https://borncity.com/win/2024/11/28/deye-deactivates-solar-inverters-in-usa-uk-and-pakistan/) - Timeline and background of the deactivations.
- [35,000 solar power systems exposed to internet – SecurityWeek (2025)](https://www.securityweek.com/35000-solar-power-systems-exposed-to-internet/) - Which inverter management interfaces are reachable from the internet.
- [Deye – Consumer Rights Wiki](https://wiki.rossmanngroup.com/wiki/Deye) - Consumer-rights perspective on remotely disabled inverters.

## Contributing

Contributions are very welcome – you don't need to be a developer!

- **Suggest an inverter or correct a rating** with a guided form: [open an issue](../../issues/new/choose).
- **Edit the data directly**: change [`data/inverters.yml`](data/inverters.yml) and open a pull request. The README is regenerated automatically.
- **Verify ❔ entries**: if you own one of these devices, your first-hand report is gold.

Please read the [contribution guidelines](CONTRIBUTING.md) and the [rating criteria](CRITERIA.md) first. This project follows a [Code of Conduct](CODE_OF_CONDUCT.md).

## Disclaimer

This list is provided for information only and is not legal, electrical or security advice. Ratings reflect publicly available information at the date of the last review; firmware updates can add or remove local access at any time. Modifying devices or their communication may void warranties or certifications. All trademarks belong to their respective owners; this project is not affiliated with any manufacturer.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work. See [LICENSE](LICENSE).
