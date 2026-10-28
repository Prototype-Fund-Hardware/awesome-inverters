#!/usr/bin/env python3
"""Validate data/inverters.yml and regenerate the generated sections of README.md.

Usage:
    python scripts/build_readme.py             # validate and rewrite README.md
    python scripts/build_readme.py --validate  # validate data only
    python scripts/build_readme.py --check     # validate and fail if README.md is outdated
    python scripts/build_readme.py --preview   # print the generated table to stdout

The score is never written by hand: it is computed from the three criteria,
so the stars in the README always match the documented reasoning.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "inverters.yml"
README_FILE = ROOT / "README.md"

CRITERIA = (
    ("local_operation", "1 · Local operation without cloud"),
    ("open_interface", "2 · Open local interface"),
    ("open_hardware", "3 · Open source hardware"),
)
REQUIRED_FIELDS = ("name", "manufacturer", "power", "balcony", "ha_docs", "criteria", "sources", "last_reviewed")
OPTIONAL_FIELDS = ("models", "caveats", "needs_review", "notes")
REVIEWED_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

FLAG_CAVEAT = "⚠️"
FLAG_REVIEW = "❔"


# --------------------------------------------------------------------------- validation


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and " " not in value


def non_empty_str(value: object) -> bool:
    return isinstance(value, str) and value.strip() != ""


def validate_entry(entry: object, index: int) -> list[str]:
    if not isinstance(entry, dict):
        return [f"entry #{index}: must be a mapping"]

    label = f"entry #{index} ({entry.get('name', '?')})"
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in entry:
            errors.append(f"{label}: missing required field '{field}'")
    for field in entry:
        if field not in REQUIRED_FIELDS + OPTIONAL_FIELDS:
            errors.append(f"{label}: unknown field '{field}'")
    if errors:
        return errors

    for field in ("name", "manufacturer", "power"):
        if not non_empty_str(entry[field]):
            errors.append(f"{label}: '{field}' must be a non-empty string")
    if "models" in entry and not non_empty_str(entry["models"]):
        errors.append(f"{label}: 'models' must be a non-empty string")
    if "notes" in entry and not non_empty_str(entry["notes"]):
        errors.append(f"{label}: 'notes' must be a non-empty string")
    if not isinstance(entry["balcony"], bool):
        errors.append(f"{label}: 'balcony' must be true or false")
    if "needs_review" in entry and not isinstance(entry["needs_review"], bool):
        errors.append(f"{label}: 'needs_review' must be true or false")

    docs = entry["ha_docs"]
    if not isinstance(docs, list):
        errors.append(f"{label}: 'ha_docs' must be a list (use [] if none exists)")
    else:
        for doc in docs:
            if not isinstance(doc, dict) or not non_empty_str(doc.get("title")) or not is_https_url(doc.get("url")):
                errors.append(f"{label}: every 'ha_docs' item needs a 'title' and an https 'url'")

    criteria = entry["criteria"]
    if not isinstance(criteria, dict):
        errors.append(f"{label}: 'criteria' must be a mapping")
    else:
        for key, _ in CRITERIA:
            item = criteria.get(key)
            if not isinstance(item, dict):
                errors.append(f"{label}: criterion '{key}' is missing")
                continue
            if not isinstance(item.get("met"), bool):
                errors.append(f"{label}: criterion '{key}.met' must be true or false")
            if not non_empty_str(item.get("reason")):
                errors.append(f"{label}: criterion '{key}.reason' must explain the decision")
        for key in criteria:
            if key not in dict(CRITERIA):
                errors.append(f"{label}: unknown criterion '{key}'")

    sources = entry["sources"]
    if not isinstance(sources, list) or not sources:
        errors.append(f"{label}: 'sources' must list at least one public https URL")
    else:
        for url in sources:
            if not is_https_url(url):
                errors.append(f"{label}: invalid source URL '{url}'")

    caveats = entry.get("caveats", [])
    if not isinstance(caveats, list) or not all(non_empty_str(c) for c in caveats):
        errors.append(f"{label}: 'caveats' must be a list of strings")

    if not REVIEWED_PATTERN.match(str(entry["last_reviewed"])):
        errors.append(f"{label}: 'last_reviewed' must look like \"YYYY-MM\" (quoted)")

    return errors


def load_and_validate() -> list[dict]:
    try:
        raw = yaml.safe_load(DATA_FILE.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        sys.exit(f"YAML syntax error in {DATA_FILE.name}:\n{exc}")

    if not isinstance(raw, dict) or not isinstance(raw.get("inverters"), list):
        sys.exit(f"{DATA_FILE.name}: top level must be a mapping with an 'inverters' list")

    entries = raw["inverters"]
    errors: list[str] = []
    for i, entry in enumerate(entries, start=1):
        errors.extend(validate_entry(entry, i))

    names = Counter(e.get("name") for e in entries if isinstance(e, dict))
    errors.extend(f"duplicate name: '{n}'" for n, c in names.items() if c > 1)
    slugs = Counter(slugify(e["name"]) for e in entries if isinstance(e, dict) and non_empty_str(e.get("name")))
    errors.extend(f"names produce the same anchor: '{s}'" for s, c in slugs.items() if c > 1)

    if errors:
        print(f"✖ {len(errors)} problem(s) in {DATA_FILE.relative_to(ROOT)}:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    return entries


# --------------------------------------------------------------------------- rendering


def slugify(text: str) -> str:
    """Mimic GitHub's heading anchors: lower-case, drop punctuation, spaces -> hyphens."""
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def score(entry: dict) -> int:
    return sum(1 for key, _ in CRITERIA if entry["criteria"][key]["met"])


def stars(value: int) -> str:
    return "★" * value + "☆" * (3 - value)


def flags(entry: dict) -> str:
    out = []
    if entry.get("caveats"):
        out.append(FLAG_CAVEAT)
    if entry.get("needs_review"):
        out.append(FLAG_REVIEW)
    return " ".join(out)


def cell(text: str) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def source_label(url: str) -> str:
    """Short, readable link text: 'owner/repo' for GitHub, otherwise the domain."""
    parsed = urlparse(url)
    host = parsed.netloc[4:] if parsed.netloc.startswith("www.") else parsed.netloc
    parts = [p for p in parsed.path.split("/") if p]
    if host == "github.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return host


def sort_key(entry: dict) -> tuple:
    """Best rating first; within a rating, balcony inverters first, then alphabetically."""
    return (-score(entry), not entry["balcony"], entry["manufacturer"].lower(), entry["name"].lower())


def render_stats(entries: list[dict]) -> str:
    counts = Counter(score(e) for e in entries)
    parts = [f"{stars(s)} {counts.get(s, 0)}" for s in (3, 2, 1, 0)]
    review = sum(1 for e in entries if e.get("needs_review"))
    return f"**{len(entries)} entries** · " + " · ".join(parts) + f" · {FLAG_REVIEW} needs review: {review}"


def render_table(entries: list[dict]) -> str:
    lines = [
        "| Inverter | Manufacturer | Power (AC) | Balcony solar | Home Assistant integration | Rating |",
        "|---|---|---|:---:|---|:---:|",
    ]
    for e in sorted(entries, key=sort_key):
        docs = " · ".join(f"[{cell(d['title'])}]({d['url']})" for d in e["ha_docs"]) or "–"
        rating = f"{stars(score(e))} {flags(e)}".strip()
        lines.append(
            f"| [{cell(e['name'])}](#{slugify(e['name'])}) | {cell(e['manufacturer'])} | {cell(e['power'])} "
            f"| {'Yes' if e['balcony'] else 'No'} | {docs} | {rating} |"
        )
    return "\n".join(lines)


def render_details(entries: list[dict]) -> str:
    blocks = []
    for e in sorted(entries, key=sort_key):
        s = score(e)
        lines = [f"### {e['name']}", ""]
        meta = [f"**Manufacturer:** {cell(e['manufacturer'])}"]
        if e.get("models"):
            meta.append(f"**Models:** {cell(e['models'])}")
        meta += [
            f"**Power:** {cell(e['power'])}",
            f"**Balcony solar:** {'Yes' if e['balcony'] else 'No'}",
            f"**Rating:** {stars(s)} ({s}/3) {flags(e)}".rstrip(),
        ]
        lines += [" · ".join(meta), ""]
        lines += ["| Criterion | Met | Rationale |", "|---|:---:|---|"]
        for key, title in CRITERIA:
            c = e["criteria"][key]
            lines.append(f"| {title} | {'✅' if c['met'] else '❌'} | {cell(c['reason'])} |")
        lines.append("")
        if e.get("caveats"):
            lines.append(f"{FLAG_CAVEAT} **Caveats:**")
            lines += [f"- {cell(c)}" for c in e["caveats"]]
            lines.append("")
        if e.get("needs_review"):
            lines += [
                f"{FLAG_REVIEW} **Needs review:** the evidence for this rating is incomplete. "
                "Own this device? Please help verify it.",
                "",
            ]
        if e.get("notes"):
            lines += [f"**Notes:** {cell(e['notes'])}", ""]
        sources = " · ".join(f"[{source_label(u)}]({u})" for u in e["sources"])
        lines += [f"**Sources:** {sources}", "", f"<sub>Last reviewed: {e['last_reviewed']}</sub>", ""]
        blocks.append("\n".join(lines))
    return "\n".join(blocks).rstrip()


def replace_block(text: str, key: str, content: str) -> str:
    pattern = re.compile(
        rf"(<!-- BEGIN GENERATED: {key} -->).*?(<!-- END GENERATED: {key} -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        sys.exit(f"README.md is missing the markers for the generated block '{key}'")
    return pattern.sub(lambda m: f"{m.group(1)}\n{content}\n{m.group(2)}", text)


def build(entries: list[dict], readme: str) -> str:
    readme = replace_block(readme, "stats", render_stats(entries))
    readme = replace_block(readme, "table", render_table(entries))
    readme = replace_block(readme, "details", render_details(entries))
    return readme


# --------------------------------------------------------------------------- CLI


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--validate", action="store_true", help="only validate data/inverters.yml")
    mode.add_argument("--check", action="store_true", help="fail if README.md is not up to date")
    mode.add_argument("--preview", action="store_true", help="print the generated table to stdout")
    args = parser.parse_args()

    entries = load_and_validate()
    print(f"✔ {len(entries)} entries valid", file=sys.stderr)
    if args.validate:
        return
    if args.preview:
        print(render_stats(entries) + "\n\n" + render_table(entries))
        return

    current = README_FILE.read_text(encoding="utf-8")
    updated = build(entries, current)
    if args.check:
        if updated != current:
            sys.exit("✖ README.md is outdated – run: python scripts/build_readme.py")
        print("✔ README.md is up to date", file=sys.stderr)
        return
    if updated != current:
        README_FILE.write_text(updated, encoding="utf-8")
        print("✔ README.md regenerated", file=sys.stderr)
    else:
        print("✔ README.md already up to date", file=sys.stderr)


if __name__ == "__main__":
    main()
