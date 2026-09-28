"""Per-category and per-condition rates from the product dataset, with the names-hidden condition beside each.

Computes the rates the manuscript takes from the product dataset by condition and by category (Supplementary
Notes 10 and 16) from spec_resistance_EXTENDED.csv (2.5 GB, Zenodo 10.5281/zenodo.19927068). The file is read in
one streaming pass, never loaded whole. Columns used: condition, category, model_key, chose_optimal.

Usage: python recount_corpus.py [path-to-csv]
Default path: data/spec_resistance_EXTENDED.csv in this repository.
Writes: additional-comparisons/corpus_recount.json, and prints the two tables.
"""
from __future__ import annotations

import csv
import json
import os
import sys
from collections import defaultdict

csv.field_size_limit(1 << 30)
HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.dirname(HERE)
DEFAULT_CSV = os.path.join(BUNDLE, "data", "spec_resistance_EXTENDED.csv")
PATH = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV
OUT = os.path.join(HERE, "corpus_recount.json")

if not os.path.exists(PATH):
    raise SystemExit(
        "Missing input: %s\n"
        "Download spec_resistance_EXTENDED.csv from Zenodo DOI 10.5281/zenodo.19927068 "
        "and place it at data/spec_resistance_EXTENDED.csv, then check it with "
        "python reproduce.py --verify. A path can also be passed as the first argument."
        % PATH
    )

counts = defaultdict(lambda: [0, 0])  # (condition, category) -> [left winner, trials]
level_counts = defaultdict(lambda: [0, 0])  # condition -> [left winner, trials]
seen_conditions = set()
n_rows = 0
with open(PATH, encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for r in reader:
        n_rows += 1
        cond = r.get("condition", "")
        seen_conditions.add(cond)
        opt = r.get("chose_optimal", "")
        if opt not in ("0", "1", "True", "False", "true", "false"):
            continue
        left = 0 if opt in ("1", "True", "true") else 1
        c = counts[(cond, r.get("category", ""))]
        c[0] += left
        c[1] += 1
        lc = level_counts[cond]
        lc[0] += left
        lc[1] += 1

print(f"rows read: {n_rows:,}; conditions: {len(seen_conditions)}")
blind_of = {}
for cond in seen_conditions:
    if cond.endswith("_brand_blind") or cond.endswith("_blind"):
        base = cond.replace("_brand_blind", "").replace("_blind", "")
        blind_of[base] = cond
print("conditions with a names-hidden twin:", sorted(blind_of.items()))

print("\nPER LEVEL (rate of leaving the winner; names shown | names hidden):")
level_table = {}
for cond in sorted(level_counts):
    if cond in blind_of.values():
        continue
    a = level_counts[cond]
    b = level_counts.get(blind_of.get(cond, ""), [0, 0])
    shown = 100 * a[0] / a[1] if a[1] else None
    hidden = 100 * b[0] / b[1] if b[1] else None
    level_table[cond] = {"shown": shown, "shown_n": a[1], "hidden": hidden, "hidden_n": b[1]}
    print(f"  {cond:34s} {shown if shown is None else round(shown, 1)!s:>6} (n={a[1]:>6})   "
          f"{hidden if hidden is None else round(hidden, 1)!s:>6} (n={b[1]:>6})")

print("\nPER CATEGORY at baseline (names shown | names hidden | difference):")
cat_table = {}
cats = sorted({cat for (cond, cat) in counts if cond == "baseline"})
for cat in cats:
    a = counts[("baseline", cat)]
    b = counts[(blind_of.get("baseline", "baseline_brand_blind"), cat)]
    shown = 100 * a[0] / a[1] if a[1] else None
    hidden = 100 * b[0] / b[1] if b[1] else None
    cat_table[cat] = {"shown": shown, "shown_n": a[1], "hidden": hidden, "hidden_n": b[1],
                      "name_effect": (shown - hidden) if (shown is not None and hidden is not None) else None}
    d = cat_table[cat]["name_effect"]
    print(f"  {cat:28s} {shown:6.1f} (n={a[1]:>5}) | {hidden if hidden is None else round(hidden, 1)!s:>6} (n={b[1]:>5}) | "
          f"{'' if d is None else f'{d:+.1f}'}")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({"rows": n_rows, "conditions": sorted(seen_conditions), "blind_of": blind_of,
           "per_level": level_table, "per_category_baseline": cat_table}, open(OUT, "w", encoding="utf-8"), indent=1)
print("\nwrote", OUT)
