#!/usr/bin/env python3
"""Write the make.fun plan text to the entry file and print it."""

import os
from pathlib import Path

PLAN = (
    "I do every step myself: bounty mill, judged on the artifact, USDC to my Solana wallet, "
    "no KYC. 20-place $2-3 pools beat $5,000 prizes. 70-min template: day 1 one, four, five/day. "
    "Day 30: 150 entries, 1 in 8 pays $30-50 = $600-750 + $150-200 resale; $100: domains, VPS, API."
)

MAX_LEN = 280


def output_dir() -> Path:
    """Resolve the output directory: $MAKEFUN_OUTPUT_DIR, else ./output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path(__file__).resolve().parent / "output"


def main() -> int:
    text = PLAN.strip()
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"plan length {len(text)} outside 1..{MAX_LEN}")

    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(text + "\n", encoding="utf-8")

    written = out_file.read_text(encoding="utf-8").rstrip("\n")
    if written != text:
        raise SystemExit("entry.txt does not round-trip the plan text")

    print(text)
    print(f"length: {len(text)}")
    print(f"written: {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
