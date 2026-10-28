# Rating criteria

**Version 1.0 · October 2026**

This document defines how inverters are rated in this list. The goal is a rating that anyone can check and reproduce from public evidence.

## Principles

- **Three criteria, one point each.** The rating is the sum (0–3 stars). Points are binary – there are no half points.
- **The score is computed, not typed.** Contributors only set `met: true/false` per criterion and explain why. The build script computes the stars, so table and reasoning can never drift apart.
- **Evidence over opinion.** Every decision needs a written rationale and at least one public source (vendor documentation, integration docs, source code, reproducible community reports).
- **Device as sold + public tools.** We rate the device with its current firmware, combined with publicly available, documented tools – including community projects and reverse-engineered interfaces. Private, undocumented hacks do not count.
- **When in doubt, no point.** If evidence is incomplete, the point is withheld and the entry is flagged ❔ until someone can verify it.
- **Series-level entries.** One entry may cover a model series if all models behave the same with respect to the criteria. Deviating models get their own entry.

## Criterion 1 – Local operation without cloud

> Can the inverter be operated **permanently** while its internet access is blocked?

The point is awarded when **all** of the following are true:

1. The device converts and feeds in power without any connection to vendor servers.
2. Settings needed in everyday operation (e.g. power limit, operating mode, battery schedule) can be changed locally – via the device display, a local web interface, a direct local app connection (Bluetooth or the device's own Wi-Fi access point) or a documented community tool.
3. Local monitoring keeps working without periodic contact to vendor servers – no access tokens, licenses or "heartbeats" that can only be renewed online.

**Allowed, but flagged with ⚠️ (caveat):**

- A vendor account is needed once during commissioning or to switch on the local interface.
- Firmware updates are only available through the cloud.
- The device uploads data by default, but this can be blocked without losing any function.
- Warranty terms require cloud monitoring.

**No point, for example, when:**

- Changing everyday settings (e.g. the output setpoint) requires the cloud.
- Local access depends on a token that expires and can only be renewed online.
- The device stops working or loses core functions without internet.

**Examples:** Hoymiles HM + OpenDTU ✅ · Zendure SolarFlow 800 ✅⚠️ (local API must be enabled once via app) · Enphase IQ Gateway ❌ (expiring cloud-issued token) · EcoFlow PowerStream ❌ (output setting requires the cloud).

## Criterion 2 – Open local interface

> Can you get your data – locally – into Home Assistant or any other system you control?

The point is awarded when **all** of the following are true:

1. At least live AC power and produced energy can be read **locally** – via LAN, Wi-Fi, RS485, CAN, a local radio protocol or Bluetooth – without the data passing through vendor servers.
2. The interface is either **documented by the vendor** or **reverse-engineered and publicly implemented** by an open-source project. "Hacked" interfaces explicitly count (e.g. OpenDTU for Hoymiles).
3. A working integration exists for Home Assistant (core integration, custom integration/HACS, MQTT auto-discovery, ESPHome, Modbus configuration) or comparable open tooling.

Additional hardware (e.g. an ESP32, an RS485 adapter) is fine.

**No point, for example, when:**

- Only a cloud API exists – even an official one, e.g. a developer portal.
- The local tool is proprietary and closed (e.g. only the vendor app can read the data).
- A local proxy only works while it forwards everything to the vendor cloud.

## Criterion 3 – Open source hardware

> Could you study, repair, modify and rebuild the hardware?

The point is awarded when the **design files** – at least schematics, PCB layout and bill of materials – are published under a license that allows study, modification, manufacture and distribution, in line with the [OSHWA definition](https://www.oshwa.org/definition/). OSHWA certification is welcome but not required. The files must correspond to the product version that is actually sold.

**Not sufficient:** open-source firmware or software (e.g. Victron's Venus OS), datasheets, teardown photos, reference designs under restrictive licenses.

Experimental DIY projects that are not certified for grid connection are listed separately in the README, **without a rating**, because they are not products you can legally connect to the public grid.

## Flags

| Flag | Meaning |
|---|---|
| ⚠️ | At least one entry in `caveats`. The point was awarded, but there is something you should know (see criterion 1 for typical cases). |
| ❔ | `needs_review: true`. Evidence is incomplete or contradictory; the rating reflects the best current knowledge and is conservative. |

## What is deliberately *not* rated

The rating is limited to objective, verifiable properties of data sovereignty. The following are **not** part of the score, but may be mentioned in an entry's notes with sources:

- country of origin or reputation of the vendor,
- known security incidents and vulnerabilities,
- efficiency, reliability, price, warranty,
- grid-code compliance and electrical safety.

## Balcony solar (not a criterion)

The "Balcony solar" column is descriptive, not part of the rating. **Yes** means the device is designed for plug-in ("balcony") PV, i.e. it stays within the plug-in feed-in limit (800 VA in Germany) or can officially be configured to it.

## Changing the criteria

Changes to this document are proposed in an issue labelled `criteria` and discussed for at least 14 days. Accepted changes increase the version number, and all entries are re-evaluated.
