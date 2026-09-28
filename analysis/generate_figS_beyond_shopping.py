"""
Supplementary figure | Familiar names favour slightly worse alternatives
beyond shopping.

a  Recommendations with names shown and hidden when one option clearly meets
   the requirements, when a familiar option is slightly worse, and when two
   options have identical attributes. The comparisons come from separate
   experiments.
b  Hospital and hiring decisions beside a product comparison conducted in the
   same experiment.
c  Slightly worse alternatives across eight decision categories.
d  Identical alternatives under the shopping-assistant instruction.
e  Identical alternatives under a neutral instruction.

The data are the files in additional-comparisons/.

Writes: results/figures/figS_beyond_shopping.{png,pdf}
        plus figS_beyond_shopping.numbers.json
"""

import argparse
import csv
import json
import sys
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as mticker
import numpy as np

# ══════════════════════════════════════════════════════════════════
# NATURE STYLE (same conventions as generate_figures_nature.py)
# ══════════════════════════════════════════════════════════════════

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 7,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.linewidth": 0.4,
    "xtick.major.width": 0.4,
    "ytick.major.width": 0.4,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "lines.linewidth": 1.2,
    "patch.linewidth": 0.3,
})

NATURE_SINGLE_COL = 3.5     # 89 mm
NATURE_1_5_COL = 5.0        # ~127 mm
NATURE_DOUBLE_COL = 7.2     # 183 mm

# One hue plus open/filled markers, so the figure survives greyscale printing
# and does not rely on colour discrimination.
C_NAMED = "#2166AC"     # names shown
C_BLIND = "#FFFFFF"     # names hidden (open marker, same edge colour)
C_LINK = "#9E9E9E"      # connector between the paired points
C_CONTROL = "#878787"   # the product control at the clear-winner rung
GREY = "#878787"
LIGHT_GREY = "#E0E0E0"
DARK = "#333333"

RESULTS_REL = "additional-comparisons"

# ══════════════════════════════════════════════════════════════════
# COUNTING
# ══════════════════════════════════════════════════════════════════


def wilson_ci(n_success, n_total, z=1.96):
    """Wilson score interval, identical to the one in generate_figures_nature.py."""
    if n_total == 0:
        return 0.0, 0.0
    p = n_success / n_total
    denom = 1 + z ** 2 / n_total
    centre = (p + z ** 2 / (2 * n_total)) / denom
    margin = z * np.sqrt((p * (1 - p) + z ** 2 / (4 * n_total)) / n_total) / denom
    return max(0.0, centre - margin), min(1.0, centre + margin)


def newcombe_diff_ci(s1, n1, s2, n2):
    """Newcombe's method 10 interval for p1 - p2, built from the two Wilson intervals."""
    if n1 == 0 or n2 == 0:
        return 0.0, 0.0
    p1, p2 = s1 / n1, s2 / n2
    l1, u1 = wilson_ci(s1, n1)
    l2, u2 = wilson_ci(s2, n2)
    d = p1 - p2
    lo = d - np.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = d + np.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return max(-1.0, lo), min(1.0, hi)


def load_csv(path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def usable(rows):
    """Only rows with a chosen letter and no error, as the readout counts them."""
    return [r for r in rows
            if (r.get("chosen_letter") or "").strip()
            and not (r.get("error") or "").strip()]


def cell(rows, hit):
    """Count, n, rate and Wilson interval for one naming condition of one group."""
    n = len(rows)
    s = sum(1 for r in rows if hit(r))
    rate = s / n if n else 0.0
    lo, hi = wilson_ci(s, n)
    return {
        "count": s,
        "n": n,
        "rate_pct": round(100 * rate, 2),
        "ci_lo_pct": round(100 * lo, 2),
        "ci_hi_pct": round(100 * hi, 2),
    }


def pair(named_rows, blind_rows, hit):
    a = cell(named_rows, hit)
    b = cell(blind_rows, hit)
    lo, hi = newcombe_diff_ci(a["count"], a["n"], b["count"], b["n"])
    return {
        "named": a,
        "blind": b,
        "difference_pp": round(a["rate_pct"] - b["rate_pct"], 2),
        "difference_ci_pp": [round(100 * lo, 2), round(100 * hi, 2)],
    }


# ══════════════════════════════════════════════════════════════════
# LABELS
# ══════════════════════════════════════════════════════════════════

KIND_LABELS = {
    "hospitals": "Hospital referral",
    "candidates": "Hiring",
    "products": "Consumer products",
    "hospitals_near": "Hospital referral",
    "candidates_near": "Hiring",
    "airlines_near": "Airlines",
    "credit_cards_near": "Credit cards",
    "index_funds_near": "Index funds",
    "lab_equipment_near": "Lab equipment",
    "medical_devices_near": "Medical devices",
    "mortgages_near": "Mortgages",
    "airlines_tie": "Airlines",
    "credit_cards_tie": "Credit cards",
    "index_funds_tie": "Index funds",
    "lab_equipment_tie": "Lab equipment",
    "medical_devices_tie": "Medical devices",
    "mortgages_tie": "Mortgages",
    "hospital_referral": "Hospital referral",
    "hiring": "Hiring",
    "medication_choice": "Medication choice",
    "consumer_lending": "Consumer lending",
    "grant_funding": "Grant funding",
    "college_choice": "College choice",
    "agent_tool_choice": "Agent tool choice",
}


def pretty(key):
    if key in KIND_LABELS:
        return KIND_LABELS[key]
    return key.replace("_near", "").replace("_tie", "").replace("_", " ").capitalize()


# ══════════════════════════════════════════════════════════════════
# THE LEVELS
# ══════════════════════════════════════════════════════════════════


def level_decided(res):
    """One option clearly meets the requirements."""
    path = res / "hospitals_hiring_products.csv"
    rows = usable(load_csv(path) or [])
    if not rows:
        return None

    def hit(r):
        return r.get("non_optimal") == "1"

    filt = ("rows with a chosen letter and an empty error column; "
            "the familiar pick is non_optimal == '1' (the model left the option that is "
            "best on every stated criterion and cheapest); "
            "names shown is blind == '0', names hidden is blind == '1'")

    groups = []
    for kind, is_control in [("hospitals", False), ("candidates", False), ("products", True)]:
        named = [r for r in rows if r["kind"] == kind and r["blind"] == "0"]
        blind = [r for r in rows if r["kind"] == kind and r["blind"] == "1"]
        if not named or not blind:
            continue
        g = pair(named, blind, hit)
        g.update({"key": kind, "label": pretty(kind), "control": is_control})
        groups.append(g)

    pool_kinds = [g["key"] for g in groups if not g["control"]]
    named = [r for r in rows if r["kind"] in pool_kinds and r["blind"] == "0"]
    blind = [r for r in rows if r["kind"] in pool_kinds and r["blind"] == "1"]
    pooled = pair(named, blind, hit)
    pooled["label"] = "Pooled"
    pooled["note"] = ("pooled over the consequential kinds only; the product tables are the "
                      "control that shows the harness is alive")

    return {
        "key": "decided",
        "comparison_rank": 0,
        "variant": "primary",
        "comparison_label": "Clearly meets the\nrequirements",
        "title": "One option clearly meets the requirements",
        "source_file": f"{RESULTS_REL}/hospitals_hiring_products.csv",
        "filter": filt,
        "measure": "the model leaves the option that meets every stated requirement",
        "provisional": False,
        "provisional_reason": "",
        "groups": groups,
        "pooled": pooled,
    }


def _twin_level(res, fname, key, comparison_rank, comparison_label, title, note=""):
    """The two identical-attribute comparisons: the familiar twin's pick rate in the deposited harness."""
    path = res / fname
    rows = usable(load_csv(path) or [])
    if not rows:
        return None

    def hit(r):
        return r.get("tie_pick") == "famous"

    filt = ("rows with a chosen letter and an empty error column; "
            "the pick is tie_pick == 'famous' (the familiar option was chosen); "
            "names shown is blind == '0', names hidden is blind == '1'")

    groups = []
    for kind in sorted(set(r["kind"] for r in rows)):
        named = [r for r in rows if r["kind"] == kind and r["blind"] == "0"]
        blind = [r for r in rows if r["kind"] == kind and r["blind"] == "1"]
        if not named or not blind:
            continue
        g = pair(named, blind, hit)
        g.update({"key": kind, "label": pretty(kind), "control": False})
        groups.append(g)

    pooled = pair([r for r in rows if r["blind"] == "0"],
                  [r for r in rows if r["blind"] == "1"], hit)
    pooled["label"] = "Pooled"
    pooled["note"] = note

    return {
        "key": key,
        "comparison_rank": comparison_rank,
        "variant": "primary",
        "comparison_label": comparison_label,
        "title": title,
        "source_file": f"{RESULTS_REL}/{fname}",
        "filter": filt,
        "measure": "the familiar option is chosen",
        "provisional": False,
        "provisional_reason": "",
        "groups": groups,
        "pooled": pooled,
    }


def level_builder_tie(res):
    """Rung 4: the identical pages re-rendered by the neutral generator."""
    matched = res / "identical_options_neutral_matched.csv"
    fallback = res / "identical_options_neutral.csv"

    def baseline(rows):
        return [r for r in usable(rows) if r.get("level") == "baseline"]

    chosen_path, provisional, reason = None, True, ""

    m_rows = load_csv(matched)
    if m_rows:
        base = baseline(m_rows)
        doms = sorted(set(r["domain"] for r in base))
        complete = [d for d in doms
                    if any(r["domain"] == d and r["blind"] == "0" for r in base)
                    and any(r["domain"] == d and r["blind"] == "1" for r in base)]
        if len(complete) >= 8:
            chosen_path, provisional = matched, False
            reason = ""
        elif len(complete) >= 6:
            # The stakes-matched run was stopped on 2026-09-05 after seven of eight domains; its two
            # versions use independent display orders (4 of 836 pairs share one), so it is the right
            # file for the neutral-prompt rates, compared on average, with the caveat stated.
            chosen_path, provisional = matched, True
            reason = ("the neutral-instruction experiment covers seven decision "
                      "categories; the statement about consequences is the same in both "
                      "naming conditions and display orders were drawn independently, so "
                      "rates compare on average")
        else:
            reason = (f"identical_options_neutral_matched.csv is still collecting "
                      f"({len(complete)} of 8 domains carry both naming conditions), "
                      f"so this comparison falls back to identical_options_neutral.csv, whose names-hidden "
                      f"version ran at a lower stakes framing than its names-shown version")
    else:
        reason = ("identical_options_neutral_matched.csv is not on disk, so this comparison falls back to "
                  "identical_options_neutral.csv, whose names-hidden version ran at a lower stakes framing "
                  "than its names-shown version")

    if chosen_path is None:
        if not fallback.exists():
            return None
        chosen_path = fallback

    rows = baseline(load_csv(chosen_path) or [])
    if not rows:
        return None

    def hit(r):
        return r.get("tie_pick") == "famous"

    filt = ("rows with a chosen letter and an empty error column, level == 'baseline'; "
            "the pick is tie_pick == 'famous' (the familiar option was chosen); "
            "names shown is blind == '0', names hidden is blind == '1'")

    groups = []
    for dom in sorted(set(r["domain"] for r in rows)):
        named = [r for r in rows if r["domain"] == dom and r["blind"] == "0"]
        blind = [r for r in rows if r["domain"] == dom and r["blind"] == "1"]
        if not named or not blind:
            continue
        g = pair(named, blind, hit)
        g.update({"key": dom, "label": pretty(dom), "control": False})
        groups.append(g)

    pooled = pair([r for r in rows if r["blind"] == "0"],
                  [r for r in rows if r["blind"] == "1"], hit)
    pooled["label"] = "Pooled"
    pooled["note"] = ""

    return {
        "key": "builder_tie",
        "comparison_rank": 2,
        "variant": "secondary",
        "comparison_label": "Identical attributes",
        "title": "Identical attributes, neutral instruction",
        "source_file": f"{RESULTS_REL}/{chosen_path.name}",
        "filter": filt,
        "measure": "the familiar option is chosen",
        "provisional": provisional,
        "provisional_reason": reason,
        "groups": groups,
        "pooled": pooled,
    }


def level_soft(res):
    """Optional rung 5: the open page with no stated criterion."""
    path = res / "pilot_soft.csv"
    raw = load_csv(path)
    if not raw:
        return None
    rows = usable(raw)
    if not rows:
        return None
    if not any(r.get("blind") == "0" for r in rows) or not any(r.get("blind") == "1" for r in rows):
        return None
    if len(set(r.get("domain", "") for r in rows)) < 2:
        return None

    def hit(r):
        return r.get("chosen_is_famous") == "1"

    filt = ("rows with a chosen letter and an empty error column; "
            "the pick is chosen_is_famous == '1' (a familiar option was chosen from a page "
            "that states no criterion); names shown is blind == '0', names hidden is blind == '1'")

    groups = []
    for dom in sorted(set(r["domain"] for r in rows)):
        named = [r for r in rows if r["domain"] == dom and r["blind"] == "0"]
        blind = [r for r in rows if r["domain"] == dom and r["blind"] == "1"]
        if not named or not blind:
            continue
        g = pair(named, blind, hit)
        g.update({"key": dom, "label": pretty(dom), "control": False})
        groups.append(g)

    pooled = pair([r for r in rows if r["blind"] == "0"],
                  [r for r in rows if r["blind"] == "1"], hit)
    pooled["label"] = "Pooled"
    pooled["note"] = ""

    return {
        "key": "soft_open",
        "comparison_rank": 3,
        "variant": "primary",
        "comparison_label": "Open request",
        "title": "Open request with no stated requirement",
        "source_file": f"{RESULTS_REL}/pilot_soft.csv",
        "filter": filt,
        "measure": "a familiar option is chosen",
        "provisional": False,
        "provisional_reason": "",
        "groups": groups,
        "pooled": pooled,
    }


def build_levels(res):
    levels = []
    for maker in (
        level_decided,
        lambda r: _twin_level(
            r, "slightly_worse_eight_categories.csv", "one_unit", 1,
            "Slightly worse",
            "A familiar option is slightly worse"),
        lambda r: _twin_level(
            r, "identical_options_shopping.csv", "identical_deposited", 2,
            "Identical attributes",
            "Identical attributes, shopping-assistant instruction"),
        level_builder_tie,
        level_soft,
    ):
        lv = maker(res)
        if lv:
            levels.append(lv)
    return levels


# ══════════════════════════════════════════════════════════════════
# DRAWING
# ══════════════════════════════════════════════════════════════════


def _err(rate, lo, hi):
    return max(0.0, rate - lo), max(0.0, hi - rate)


def draw_ladder(ax, levels):
    """Top panel: the pooled name effect at each rung, with the kinds as small points."""
    # The x axis is how much the PAGE settles the choice, so it has to be monotonic.
    # Rungs that share a page but differ only in the prompt share an x position, the
    # second one drawn open and nudged to the right.
    offset = 0.24
    xs = [lv["comparison_rank"] + (offset if lv["variant"] == "secondary" else 0.0)
          for lv in levels]

    ax.axhline(0, color=DARK, linewidth=0.5, zorder=1)

    # The comparisons come from separate experiments, so nothing joins them.

    for x, lv in zip(xs, levels):
        is_secondary = lv["variant"] == "secondary"
        kinds = [g for g in lv["groups"] if not g["control"]]
        ctrls = [g for g in lv["groups"] if g["control"]]
        if kinds:
            jit = np.linspace(-0.15, 0.15, len(kinds)) if len(kinds) > 1 else np.array([0.0])
            ax.scatter(x + jit, [g["difference_pp"] for g in kinds],
                       s=11, facecolors="none", edgecolors=C_LINK,
                       linewidths=0.6, zorder=2)
        for g in ctrls:
            ax.scatter([x], [g["difference_pp"]], s=18, marker="s",
                       facecolors="none", edgecolors=C_CONTROL, linewidths=0.7, zorder=4)
            ax.annotate("products, same experiment", (x, g["difference_pp"]),
                        textcoords="offset points", xytext=(8, 0), fontsize=6.5,
                        color=C_CONTROL, va="center", ha="left")

        p = lv["pooled"]
        lo, hi = p["difference_ci_pp"]
        ax.errorbar([x], [p["difference_pp"]],
                    yerr=[[p["difference_pp"] - lo], [hi - p["difference_pp"]]],
                    fmt="o", markersize=5, ecolor=DARK,
                    markerfacecolor="#FFFFFF" if is_secondary else C_NAMED,
                    markeredgecolor=C_NAMED, markeredgewidth=0.9, color=C_NAMED,
                    elinewidth=0.6, capsize=2.5, capthick=0.5, zorder=5)
        ax.annotate(f"{p['difference_pp']:+.1f}", (x, hi),
                    textcoords="offset points", xytext=(0, 5), fontsize=7,
                    fontweight="bold", color=C_NAMED, ha="center")

    ranks = sorted(set(lv["comparison_rank"] for lv in levels))
    tick_labels = []
    for r in ranks:
        prim = next(lv for lv in levels
                    if lv["comparison_rank"] == r and lv["variant"] == "primary")
        tick_labels.append(prim["comparison_label"])
    ax.set_xticks(ranks)
    ax.set_xticklabels(tick_labels, fontsize=7 if len(ranks) <= 3 else 6.5)
    ax.set_xlim(-0.55, max(ranks) + 0.62)
    ax.set_ylabel("Names shown minus\nnames hidden (pp)")
    ax.set_title("Comparisons from separate experiments", fontsize=8, pad=7)

    handles = [
        mlines.Line2D([], [], color=C_NAMED, marker="o", linestyle="none",
                      markersize=4.5, label="Pooled estimate"),
        mlines.Line2D([], [], color=C_LINK, marker="o", linestyle="none",
                      markersize=3.5, markerfacecolor="none",
                      label="Individual decision categories"),
    ]
    if any(lv["variant"] == "secondary" for lv in levels):
        prov = ""   # the caption carries the coverage note, not the legend
        handles.insert(1, mlines.Line2D(
            [], [], color=C_NAMED, marker="o", linestyle="none", markersize=4.5,
            markerfacecolor="#FFFFFF", markeredgewidth=0.9,
            label="Neutral instruction" + prov))
    ax.legend(handles=handles, loc="upper left", frameon=True, framealpha=0.95,
              edgecolor="#CCCCCC", fancybox=False, fontsize=6.5,
              handletextpad=0.5, borderpad=0.4)
    lo_all = min([lv["pooled"]["difference_ci_pp"][0] for lv in levels]
                 + [g["difference_pp"] for lv in levels for g in lv["groups"]])
    hi_all = max([lv["pooled"]["difference_ci_pp"][1] for lv in levels]
                 + [g["difference_pp"] for lv in levels for g in lv["groups"]])
    ax.set_ylim(min(-4, lo_all - 4), hi_all + 7)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%d"))


def draw_level(ax, lv, show_ylabel_units=True):
    """One rung: paired points per kind, plus the pooled pair, with n under each pair."""
    kinds = [g for g in lv["groups"] if not g["control"]]
    ctrls = [g for g in lv["groups"] if g["control"]]
    kinds = sorted(kinds, key=lambda g: g["difference_pp"], reverse=True)
    rows = kinds + ctrls
    pooled = dict(lv["pooled"])
    pooled["control"] = False

    # y positions: kinds from the top down, a gap, then the pooled pair
    ys = list(range(len(rows)))
    y_pool = len(rows) + 0.75
    all_rows = rows + [pooled]
    all_ys = ys + [y_pool]

    for g, y in zip(all_rows, all_ys):
        is_pool = g is all_rows[-1]
        edge = C_CONTROL if g.get("control") else C_NAMED
        nr, br = g["named"]["rate_pct"], g["blind"]["rate_pct"]
        ax.plot([br, nr], [y, y], color=C_LINK, linewidth=1.0, zorder=2,
                solid_capstyle="round")

        for datum, filled in ((g["blind"], False), (g["named"], True)):
            r = datum["rate_pct"]
            xl, xh = _err(r, datum["ci_lo_pct"], datum["ci_hi_pct"])
            ax.errorbar([r], [y], xerr=[[xl], [xh]], fmt="none", ecolor=DARK,
                        elinewidth=0.5, capsize=1.6, capthick=0.4, zorder=3)
            ax.scatter([r], [y], s=26 if is_pool else 20,
                       facecolors=edge if filled else "#FFFFFF",
                       edgecolors=edge, linewidths=0.8, zorder=4)

        weight = "bold" if is_pool else "normal"
        ax.annotate(f"{g['difference_pp']:+.1f}", (1.015, y), xycoords=("axes fraction", "data"),
                    fontsize=7, fontweight=weight, va="center", ha="left",
                    color=C_CONTROL if g.get("control") else DARK)

    # Two right-aligned columns in the left margin, so a single line carries both the
    # kind and the trials per naming condition and no label can touch its neighbour.
    counts = [f"{g['named']['n']} | {g['blind']['n']}" for g in all_rows]
    col_w = max(len(c) for c in counts) * 6.5 * 0.55   # Arial digits, points

    for g, y, cnt in zip(all_rows, all_ys, counts):
        nm = g.get("label", "Pooled")
        if g.get("control"):
            nm += " (same experiment)"
        bold = "bold" if g is all_rows[-1] else "normal"
        ax.annotate(cnt, (0.0, y), xycoords=("axes fraction", "data"),
                    textcoords="offset points", xytext=(-4, 0),
                    fontsize=6.5, color=GREY, ha="right", va="center")
        ax.annotate(nm, (0.0, y), xycoords=("axes fraction", "data"),
                    textcoords="offset points", xytext=(-(9 + col_w), 0),
                    fontsize=7, fontweight=bold,
                    color=C_CONTROL if g.get("control") else "#000000",
                    ha="right", va="center")

    ax.set_yticks(all_ys)
    ax.set_yticklabels([])
    ax.set_ylim(y_pool + 0.85, -0.85)
    ax.axhline((len(rows) - 1 + y_pool) / 2, color=LIGHT_GREY, linewidth=0.5,
               linestyle=(0, (2, 2)), zorder=1)

    ax.set_xlim(0, 100)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(25))
    ax.xaxis.set_major_formatter(mticker.PercentFormatter(100, decimals=0))
    if show_ylabel_units:
        ax.set_xlabel("Familiar option chosen")
    ax.set_title(textwrap.fill(lv["title"], width=34), fontsize=7.5, pad=6, loc="left")
    ax.annotate("Difference (pp)", (1.015, 1.0), xycoords="axes fraction",
                fontsize=6.5, color=GREY, va="bottom", ha="left")
    ax.annotate("n names shown | hidden", (0.0, 1.0), xycoords="axes fraction",
                textcoords="offset points", xytext=(-4, 3),
                fontsize=6.5, color=GREY, va="bottom", ha="right")
    ax.grid(axis="x", color=LIGHT_GREY, linewidth=0.4, zorder=0)
    ax.set_axisbelow(True)


def panel_label(ax, text, x=-0.30, y=1.16):
    ax.text(x, y, text, transform=ax.transAxes, fontsize=10,
            fontweight="bold", va="top", ha="left")


def draw_figure(levels, out_dir):
    n = len(levels)
    ncols = 2
    nrows = int(np.ceil(n / ncols))
    top_h = 1.80
    row_h = 0.26 * (max(len(lv["groups"]) for lv in levels) + 1) + 1.00
    fig_h = top_h + nrows * row_h

    fig = plt.figure(figsize=(NATURE_DOUBLE_COL, fig_h))
    gs = fig.add_gridspec(nrows + 1, ncols,
                          height_ratios=[top_h] + [row_h] * nrows,
                          hspace=0.50, wspace=1.52)

    ax_top = fig.add_subplot(gs[0, :])
    draw_ladder(ax_top, levels)
    panel_label(ax_top, "a", x=-0.075, y=1.20)

    legend_handles = [
        mlines.Line2D([], [], color=C_NAMED, marker="o", linestyle="none",
                      markersize=4.5, label="Names shown"),
        mlines.Line2D([], [], color=C_NAMED, marker="o", linestyle="none",
                      markersize=4.5, markerfacecolor="#FFFFFF",
                      markeredgewidth=0.8, label="Names hidden"),
        mlines.Line2D([], [], color=C_LINK, linewidth=1.0, label="Difference"),
    ]

    level_axes = []
    for i, lv in enumerate(levels):
        ax = fig.add_subplot(gs[1 + i // ncols, i % ncols])
        draw_level(ax, lv)
        panel_label(ax, "bcdef"[i])
        level_axes.append(ax)
        if i == 0:
            ax.legend(handles=legend_handles, loc="lower right", frameon=True,
                      framealpha=0.95, edgecolor="#CCCCCC", fancybox=False,
                      fontsize=6.5, handletextpad=0.5, borderpad=0.4)

    if n % ncols:
        for j in range(n % ncols, ncols):
            fig.add_subplot(gs[nrows, j]).axis("off")

    notes = []
    for i, lv in enumerate(levels):
        if lv["provisional"]:
            notes.append(f"Panel {'bcdef'[i]}: {lv['provisional_reason']}.")
    if notes:
        # Sit the footnote directly under the lowest panel, not under the figure box.
        fig.canvas.draw()
        rend = fig.canvas.get_renderer()
        inv = fig.transFigure.inverted()
        bottom = min(a.get_tightbbox(rend).transformed(inv).y0 for a in level_axes)
        fig.text(0.01, bottom - 0.010, textwrap.fill(" ".join(notes), width=145),
                 fontsize=6.5, color=GREY, ha="left", va="top")

    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "figS_beyond_shopping.png")
    fig.savefig(out_dir / "figS_beyond_shopping.pdf")
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════
# SIDECAR AND REPORTING
# ══════════════════════════════════════════════════════════════════


def sidecar(levels):
    out = {
        "figure": "figS_beyond_shopping",
        "title": "Familiar names favour slightly worse alternatives beyond shopping",
        "generated_by": "analysis/generate_figS_beyond_shopping.py",
        "measure": ("difference in percentage points, the rate with names shown minus the "
                    "rate with names hidden; intervals are Wilson 95 per cent on each rate and "
                    "Newcombe 95 per cent on the difference"),
        "any_provisional": any(lv["provisional"] for lv in levels),
        "pending_files": [],
        "levels": [],
    }
    for lv in levels:
        out["levels"].append({
            "key": lv["key"],
            "title": lv["title"],
            "source_file": lv["source_file"],
            "filter": lv["filter"],
            "measure": lv["measure"],
            "provisional": lv["provisional"],
            "provisional_reason": lv["provisional_reason"],
            "pooled": lv["pooled"],
            "groups": lv["groups"],
        })
    return out


def note_pending(res, data):
    pend = []
    matched = res / "identical_options_neutral_matched.csv"
    if any(lv["key"] == "builder_tie" and lv["provisional"] for lv in data["levels_raw"]):
        pend.append({
            "file": f"{RESULTS_REL}/identical_options_neutral_matched.csv",
            "exists": matched.exists(),
            "wanted": "rows for all eight decision categories in both naming conditions",
        })
    if not (res / "pilot_soft.csv").exists():
        pend.append({
            "file": f"{RESULTS_REL}/pilot_soft.csv",
            "exists": False,
            "wanted": ("the open-request comparison; the script adds a fifth panel by itself "
                       "once the file has both naming conditions across two or more "
                       "decision categories"),
        })
    return pend


def report(levels):
    for lv in levels:
        flag = "  [PROVISIONAL]" if lv["provisional"] else ""
        print(f"\n{lv['title']}{flag}")
        print(f"  file   {lv['source_file']}")
        print(f"  filter {lv['filter']}")
        if lv["provisional_reason"]:
            print(f"  why    {lv['provisional_reason']}")
        head = f"    {'kind':<22}{'named':>18}{'hidden':>18}{'effect (pp)':>14}"
        print(head)
        for g in lv["groups"] + [lv["pooled"]]:
            nm = g.get("label", "Pooled")
            if g.get("control"):
                nm += " (same experiment)"
            a, b = g["named"], g["blind"]
            print(f"    {nm:<22}"
                  f"{a['count']:>4}/{a['n']:<4} {a['rate_pct']:>6.1f}"
                  f"{b['count']:>5}/{b['n']:<4} {b['rate_pct']:>6.1f}"
                  f"{g['difference_pp']:>10.1f} "
                  f"[{g['difference_ci_pp'][0]:.1f}, {g['difference_ci_pp'][1]:.1f}]")


def main():
    ap = argparse.ArgumentParser(
        description="Draw the supplementary figure, familiar names beyond shopping")
    ap.add_argument("--check", action="store_true",
                    help="print every number and exit without drawing")
    ap.add_argument("--root", default=None,
                    help="bundle root (defaults to the directory above this script)")
    args = ap.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    res = root / RESULTS_REL
    out_dir = root / "results" / "figures"

    if not res.is_dir():
        print(f"ERROR: missing input folder {RESULTS_REL} (looked at {res})")
        print("It ships in the bundle; see additional-comparisons/README.md for the "
              "file list and hashes.")
        sys.exit(1)

    levels = build_levels(res)
    if not levels:
        print("ERROR: no level could be counted; check the CSV paths")
        sys.exit(1)

    print(f"Repo root: {root}")
    print(f"Levels drawn: {len(levels)} ({', '.join(lv['key'] for lv in levels)})")
    report(levels)

    data = sidecar(levels)
    data["levels_raw"] = levels
    data["pending_files"] = note_pending(res, data)
    del data["levels_raw"]

    if args.check:
        print("\n--check: nothing drawn.")
        return

    draw_figure(levels, out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "figS_beyond_shopping.numbers.json", "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")

    print(f"\nWrote {out_dir / 'figS_beyond_shopping.pdf'}")
    print(f"Wrote {out_dir / 'figS_beyond_shopping.png'}")
    print(f"Wrote {out_dir / 'figS_beyond_shopping.numbers.json'}")


if __name__ == "__main__":
    main()
