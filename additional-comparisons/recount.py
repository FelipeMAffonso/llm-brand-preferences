"""Recomputes every number the manuscript and its Supplementary Information take from the files in this folder.

Read-only. Prints file, filter, numerator, denominator and per cent for each count.
Run: python recount.py
"""
import csv
import os
from collections import defaultdict

R = os.path.dirname(os.path.abspath(__file__))


def need(name):
    path = os.path.join(R, name)
    if not os.path.exists(path):
        raise SystemExit(
            "Missing input: additional-comparisons/%s\n"
            "Every file this script reads ships in the same directory as the script. "
            "If it is absent the deposit is incomplete; see additional-comparisons/README.md "
            "for the file list and hashes." % name
        )
    return path


def rows(name):
    path = os.path.join(R, name)
    if not os.path.exists(path):
        raise SystemExit(
            "Missing input: additional-comparisons/%s\n"
            "Every file this script reads ships in the same directory as the script. "
            "If it is absent the deposit is incomplete; see additional-comparisons/README.md "
            "for the file list and hashes." % name
        )
    with open(path, newline="", encoding="utf-8", errors="replace") as fh:
        return list(csv.DictReader(fh))


def pct(n, d):
    return "n/a" if d == 0 else "%.1f" % (100.0 * n / d)


def line(label, n, d, extra=""):
    print("  %-58s %5d / %-5d = %6s %%  %s" % (label, n, d, pct(n, d), extra))


def truthy(v):
    return str(v).strip().lower() in ("1", "true", "yes", "t")


def famous(r):
    """tie_pick is a label: famous / unfamiliar / other. On the dominated product tables the
    column is empty and the measure is non_optimal."""
    return str(r.get("tie_pick", "")).strip() == "famous"


print("=" * 100)
print("RECOUNT 1  hospitals_hiring_products.csv  -- products, hospitals and hiring, names shown (blind=0) and hidden (blind=1)")
print("=" * 100)
rs = [r for r in rows("hospitals_hiring_products.csv") if not r["error"] and r["chosen_letter"]]
for kind in sorted({r["kind"] for r in rs}):
    for b in ("0", "1"):
        sub = [r for r in rs if r["kind"] == kind and str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
        non = [r for r in sub if truthy(r["non_optimal"])]
        line("%s  blind=%s" % (kind, b), len(non), len(sub))
print("  usable rows: %d of %d" % (len(rs), len(rows("hospitals_hiring_products.csv"))))

print()
print("=" * 100)
print("RECOUNT 2  slightly_worse_eight_categories.csv -- familiar alternative slightly worse: choices of the familiar option")
print("=" * 100)
rs = [r for r in rows("slightly_worse_eight_categories.csv") if not r["error"] and r["chosen_letter"]]
for b in ("0", "1"):
    sub = [r for r in rs if str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
    tie = [r for r in sub if famous(r)]
    line("all kinds  blind=%s  tie_pick (famous twin chosen)" % b, len(tie), len(sub))
byk = defaultdict(lambda: [0, 0, 0, 0])
for r in rs:
    blind = str(r["blind"]).strip() in ("1", "True")
    c = byk[r["kind"]]
    c[2 if blind else 0] += 1 if famous(r) else 0
    c[3 if blind else 1] += 1
for k in sorted(byk):
    n_named, d_named, n_blind, d_blind = byk[k]
    print("    %-18s named %3d/%3d = %5s%%   blind %3d/%3d = %5s%%" %
          (k, n_named, d_named, pct(n_named, d_named), n_blind, d_blind, pct(n_blind, d_blind)))
probe = [r for r in rs if famous(r) and str(r["blind"]).strip() in ("0", "False")]
notatall = [r for r in probe if str(r["probe"]).strip() in ("1", "1.0")]
line("self-report 'not at all' among named twin picks", len(notatall), len(probe))

print()
print("=" * 100)
print("RECOUNT 3  identical_options_shopping.csv -- identical options: choices of the familiar option")
print("=" * 100)
rs = [r for r in rows("identical_options_shopping.csv") if not r["error"] and r["chosen_letter"]]
for b in ("0", "1"):
    sub = [r for r in rs if str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
    tie = [r for r in sub if famous(r)]
    line("all kinds  blind=%s  famous twin chosen" % b, len(tie), len(sub))
bym = defaultdict(lambda: [0, 0, 0, 0])
for r in rs:
    blind = str(r["blind"]).strip() in ("1", "True")
    c = bym[r["model"]]
    c[2 if blind else 0] += 1 if famous(r) else 0
    c[3 if blind else 1] += 1
for m in sorted(bym):
    n_named, d_named, n_blind, d_blind = bym[m]
    print("    %-28s named %3d/%3d = %5s%%   blind %3d/%3d = %5s%%" %
          (m, n_named, d_named, pct(n_named, d_named), n_blind, d_blind, pct(n_blind, d_blind)))
probe = [r for r in rs if famous(r) and str(r["blind"]).strip() in ("0", "False")]
notatall = [r for r in probe if str(r["probe"]).strip() in ("1", "1.0")]
line("self-report 'not at all' among named twin picks", len(notatall), len(probe))

print()
print("=" * 100)
print("RECOUNT 4  matched_models.csv -- models given the human-advisor study's decision texts")
print("=" * 100)
rs = [r for r in rows("matched_models.csv") if not r["error"] and r["chosen_letter"]]
for level in ("baseline", "weighted", "explicit_numeric"):
    for b in ("0", "1"):
        sub = [r for r in rs if r["level"] == level and str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
        ok = [r for r in sub if truthy(r["chose_optimal"])]
        line("%s  blind=%s" % (level, b), len(ok), len(sub))
nl = [r for r in rs if r["level"] in ("baseline", "weighted")]
for b in ("0", "1"):
    sub = [r for r in nl if str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
    ok = [r for r in sub if truthy(r["chose_optimal"])]
    line("NATURAL-LANGUAGE LEVELS COMBINED  blind=%s" % b, len(ok), len(sub))
print("  usable rows: %d of %d ; models: %d" % (len(rs), len(rows("matched_models.csv")),
                                               len({r["model"] for r in rs})))

print()
print("=" * 100)
print("RECOUNT 5  products_ordered_priorities.csv -- the ordered-priority instruction on current models")
print("=" * 100)
rs = [r for r in rows("products_ordered_priorities.csv") if not r["error"] and r["chosen_letter"]]
for b in ("0", "1"):
    sub = [r for r in rs if str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
    non = [r for r in sub if truthy(r["non_optimal"])]
    line("blind=%s  famous pick (non_optimal on a dominated table)" % b, len(non), len(sub))
bym = defaultdict(lambda: [0, 0, 0, 0])
for r in rs:
    blind = str(r["blind"]).strip() in ("1", "True")
    c = bym[r["model"]]
    c[2 if blind else 0] += 1 if truthy(r["non_optimal"]) else 0
    c[3 if blind else 1] += 1
for m in sorted(bym):
    n_named, d_named, n_blind, d_blind = bym[m]
    print("    %-28s named %3d/%3d = %5s%%   blind %3d/%3d = %5s%%" %
          (m, n_named, d_named, pct(n_named, d_named), n_blind, d_blind, pct(n_blind, d_blind)))

print()
print("=" * 100)
print("RECOUNT 6  products_ten_models.csv -- names shown and hidden, by model")
print("=" * 100)
rs = [r for r in rows("products_ten_models.csv") if not r["error"] and r["chosen_letter"]]
bym = defaultdict(lambda: [0, 0, 0, 0])
for r in rs:
    blind = str(r["blind"]).strip() in ("1", "True")
    c = bym[r["model"]]
    c[2 if blind else 0] += 1 if truthy(r["non_optimal"]) else 0
    c[3 if blind else 1] += 1
for m in sorted(bym):
    n_named, d_named, n_blind, d_blind = bym[m]
    delta = (100.0 * n_named / d_named - 100.0 * n_blind / d_blind) if d_named and d_blind else 0
    print("    %-34s named %3d/%3d = %5s%%   blind %3d/%3d = %5s%%   delta %+5.1f" %
          (m, n_named, d_named, pct(n_named, d_named), n_blind, d_blind, pct(n_blind, d_blind), delta))
for b in ("0", "1"):
    sub = [r for r in rs if str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
    tie = [r for r in sub if truthy(r["non_optimal"])]
    line("ALL MODELS  blind=%s  famous pick" % b, len(tie), len(sub))
probe = [r for r in rs if truthy(r["non_optimal"]) and str(r["blind"]).strip() in ("0", "False")]
counts = defaultdict(int)
for r in probe:
    counts[str(r["probe"]).strip() or "unparsed"] += 1
print("    self-report among %d named famous picks: %s" % (len(probe), dict(sorted(counts.items()))))

print()
print("=" * 100)
print("RECOUNT 7  identical_options_neutral.csv -- identical options under a neutral instruction")
print("=" * 100)
rs = [r for r in rows("identical_options_neutral.csv") if not r["error"] and r["chosen_letter"]]
print("  usable rows: %d of %d" % (len(rs), len(rows("identical_options_neutral.csv"))))
for level in sorted({r["level"] for r in rs}):
    for b in ("0", "1"):
        sub = [r for r in rs if r["level"] == level and str(r["blind"]).strip() in (b, "True" if b == "1" else "False")]
        fam = [r for r in sub if truthy(r["chosen_is_famous"])]
        line("level=%s  blind=%s  famous chosen" % (level, b), len(fam), len(sub))
base = [r for r in rs if r["level"] == "baseline"]
byd = defaultdict(lambda: [0, 0, 0, 0])
for r in base:
    blind = str(r["blind"]).strip() in ("1", "True")
    c = byd[r["domain"]]
    c[2 if blind else 0] += 1 if truthy(r["chosen_is_famous"]) else 0
    c[3 if blind else 1] += 1
for d in sorted(byd):
    n_named, d_named, n_blind, d_blind = byd[d]
    print("    %-22s named %3d/%3d = %5s%%   hidden %3d/%3d = %5s%%" %
          (d, n_named, d_named, pct(n_named, d_named), n_blind, d_blind, pct(n_blind, d_blind)))
capped = [r for r in rows("identical_options_neutral.csv") if str(r.get("finish_reason", "")).strip() == "length"]
print("    length-capped rows in file: %d" % len(capped))

print()
print("=" * 100)
print("RECOUNT 8  identical_options_neutral.csv -- by model at baseline, and under the plain instruction")
print("=" * 100)
for level in ("baseline", "plain"):
    sel = [r for r in rs if r["level"] == level]
    if not sel:
        continue
    print("  level = %s" % level)
    bym = defaultdict(lambda: [0, 0, 0, 0])
    for r in sel:
        blind = str(r["blind"]).strip() in ("1", "True")
        c = bym[r["model"]]
        c[2 if blind else 0] += 1 if truthy(r["chosen_is_famous"]) else 0
        c[3 if blind else 1] += 1
    for m in sorted(bym):
        n_named, d_named, n_blind, d_blind = bym[m]
        print("    %-34s named %4d/%4d = %5s%%   hidden %4d/%4d = %5s%%" %
              (m, n_named, d_named, pct(n_named, d_named), n_blind, d_blind, pct(n_blind, d_blind)))

print()
print("=" * 100)
print("RECOUNT 9  conditions.json -- the product dataset, names shown and hidden")
print("=" * 100)
import json
with open(need("conditions.json"), encoding="utf-8") as fh:
    cond = json.load(fh)
for key in ("baseline", "baseline_brand_blind", "baseline_description_minimal",
            "baseline_expert_persona", "preference_weighted", "preference_explicit",
            "baseline_price_premium", "attribute_swap"):
    c = cond.get(key)
    if c and c.get("n"):
        line(key, c["x"], c["n"])
b = cond["baseline"]
bb = cond["baseline_brand_blind"]
print("  NAME EFFECT in the deposited shopping corpus: %.1f minus %.1f = %.1f points" % (
    100.0 * b["x"] / b["n"], 100.0 * bb["x"] / bb["n"],
    100.0 * b["x"] / b["n"] - 100.0 * bb["x"] / bb["n"]))
