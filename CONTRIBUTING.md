# Contributing

Thank you for helping make inverters more transparent! Whether you own a single balcony inverter or install systems for a living – your experience helps others decide.

Please read the [rating criteria](CRITERIA.md) before you start, and keep our [Code of Conduct](CODE_OF_CONDUCT.md) in mind.

## Ways to contribute

| You want to … | Do this | Skills needed |
|---|---|---|
| Suggest a new inverter | Open an issue with the **"Add an inverter"** form | None |
| Report a wrong or outdated rating | Open an issue with the **"Correct a rating"** form | None |
| Verify an entry marked ❔ | Comment on the related issue or use the correction form, describing your device, firmware and setup | None |
| Add or change entries yourself | Edit [`data/inverters.yml`](data/inverters.yml) and open a pull request | Basic GitHub |
| Improve tooling or docs | Open a pull request | Python / Markdown |

All issue forms are here: [open an issue](../../issues/new/choose).

## Editing the data

**Never edit the generated parts of `README.md`** (between the `BEGIN GENERATED` / `END GENERATED` markers). They are rebuilt from `data/inverters.yml`, and manual changes would be overwritten.

You can edit `data/inverters.yml` directly in the GitHub web interface (pencil icon) – GitHub will create a fork and a pull request for you. After the merge, a GitHub Action regenerates the README automatically.

### Entry template

```yaml
  - name: Vendor Model series            # unique; also used as anchor
    manufacturer: Vendor                 # brand name only, rebrands go into "models"
    models: X-600, X-800, X-1000         # optional
    power: 0.6–1 kVA                     # rated AC output of the series
    balcony: true                        # designed for plug-in solar? (see CRITERIA.md)
    ha_docs:                             # [] if no integration exists
      - title: Name of integration
        url: https://…
    criteria:
      local_operation:
        met: true
        reason: Why the point is (not) awarded – one or two sentences.
      open_interface:
        met: true
        reason: …
      open_hardware:
        met: false
        reason: …
    caveats:                             # optional – adds ⚠️
      - Something users should know although the point was awarded.
    needs_review: false                  # optional – true adds ❔
    notes: Optional background information.
    sources:                             # at least one public https link
      - https://…
    last_reviewed: "2026-10"             # quoted, YYYY-MM
```

The **score is computed automatically** from the three `met` values – there is no field for stars.

### Check your changes locally (optional)

```bash
pip install -r requirements.txt
python scripts/build_readme.py --validate   # check the data
python scripts/build_readme.py              # regenerate README.md
```

The same validation runs automatically on every pull request.

## Evidence rules

- Every claim (`met: true` **and** `met: false`) needs a rationale and at least one **public** source.
- Good sources: vendor documentation, Home Assistant / integration documentation, source code, datasheets, reproducible forum or GitHub reports.
- First-hand reports are welcome – please state the model, firmware version and how you tested (e.g. "internet blocked at the router for two weeks").
- Firmware changes matter: if a firmware update adds or removes local access, describe which versions are affected.
- Not accepted: affiliate or referral links, marketing copy, unverifiable claims.

## Review process

1. A maintainer checks the entry against [CRITERIA.md](CRITERIA.md) and the sources.
2. Disputed ratings are discussed openly in the issue or pull request. If evidence is inconclusive, the point is withheld and the entry is flagged ❔.
3. After merging, the README is regenerated and the entry's `last_reviewed` date reflects the review.

## Conflicts of interest

If you work for, or are paid by, a manufacturer, distributor or installer, please say so in your issue or pull request. Contributions from vendors are welcome – especially documentation of local interfaces – but they are reviewed by someone independent.

## Becoming a maintainer

Regular contributors with good reviews may be invited as maintainers. Maintainers review pull requests, triage issues and keep `last_reviewed` dates current.
