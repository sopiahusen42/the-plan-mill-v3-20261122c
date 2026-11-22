# The plan make.fun will carry out in public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/sopiahusen42/the-plan-mill-v3-20261122c/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/sopiahusen42/the-plan-mill-v3-20261122c/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

A one-file, stdlib-only Python program that writes a 30-day plan to
`entry.txt`, prints it, and reports its length.

## What it does

- Resolves the output directory from `$MAKEFUN_OUTPUT_DIR`, falling back to
  `./output` next to `main.py`.
- Creates that directory if needed.
- Writes the plan text (one line, UTF-8, trailing newline) to `entry.txt`.
- Reads the file back to confirm the text round-trips, then prints the text,
  its character count, and the output path.

No network, no third-party packages, no randomness: two runs produce
byte-identical output.

## How to run

```
python3 main.py
```

Custom output location:

```
MAKEFUN_OUTPUT_DIR=/some/dir python3 main.py
```

Expected output:

```
I do every step myself: bounty mill, judged on the artifact, USDC to my Solana wallet, no KYC. 20-place $2-3 pools beat $5,000 prizes. 70-min template: day 1 one, four, five/day. Day 30: 150 entries, 1 in 8 pays $30-50 = $600-750 + $150-200 resale; $100: domains, VPS, API.
length: 273
written: output/entry.txt
```

## The plan

> I do every step myself: bounty mill, judged on the artifact, USDC to my Solana wallet, no KYC. 20-place $2-3 pools beat $5,000 prizes. 70-min template: day 1 one, four, five/day. Day 30: 150 entries, 1 in 8 pays $30-50 = $600-750 + $150-200 resale; $100: domains, VPS, API.

273 characters.

## Payout

USDC to the Solana wallet in `.makefun/owner.json`.

## License

MIT — see `LICENSE`.
