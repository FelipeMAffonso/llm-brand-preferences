"""
Figure 3 | Stating priorities reduces non-optimal recommendations.

One panel. Rates for the three shopping request conditions, with the
brand-blind control shown beside the open request.

Reads:  the deposited corpus CSV (SPEC_RESISTANCE_CSV, or the bundle default
        data/spec_resistance_EXTENDED.csv)
Writes: results/figures/fig3_stated_priorities.{png,pdf}
        (or SPEC_RESISTANCE_FIGURES)

Conditions:
  baseline              open request, brand names shown
  baseline_brand_blind  open request, brand names hidden
  preference_vague      vague preferences, in words
  preference_weighted   ordered priorities, in words

The pooled rates can be checked against additional-comparisons/corpus_recount.json.

Usage:
    python analysis/generate_fig3_stated_priorities.py
"""

import csv
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as mticker
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_figures_nature import (  # noqa: E402
    MODEL_META, MODEL_ORDER, PROVIDER_ORDER, PROVIDER_COLOURS, GREY, wilson_ci,
)

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 7,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "figure.dpi": 600,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "axes.linewidth": 0.4,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.major.width": 0.4,
    "ytick.major.width": 0.4,
})

NATURE_DOUBLE_COL = 7.2

# The shared roles (see the palette note in generate_fig5_human_advisor.py)
C_SHOWN, C_HIDDEN = "#a51c30", "#c9a227"

CONDITIONS = [
    ("baseline", "Open request"),
    ("preference_vague", "Vague preferences"),
    ("preference_weighted", "Ordered priorities"),
]
HIDDEN_CONDITION = "baseline_brand_blind"


def load_counts(csv_path):
    """Per-model and pooled non-optimal counts for every condition we plot."""
    wanted = {c for c, _ in CONDITIONS} | {HIDDEN_CONDITION}
    per_model = {c: {m: [0, 0] for m in MODEL_META} for c in wanted}
    pooled = {c: [0, 0] for c in wanted}
    with open(csv_path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            m = row.get("model_key", "")
            c = row.get("condition", "")
            if m not in MODEL_META or c not in wanted:
                continue
            non_optimal = row.get("chose_optimal") != "True"
            per_model[c][m][1] += 1
            pooled[c][1] += 1
            if non_optimal:
                per_model[c][m][0] += 1
                pooled[c][0] += 1
    return per_model, pooled


def pct_ci(k, n):
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    lo, hi = wilson_ci(k, n)
    return 100 * k / n, 100 * lo, 100 * hi


def build(csv_path, out_dir):
    per_model, pooled = load_counts(csv_path)

    fig, ax = plt.subplots(figsize=(NATURE_DOUBLE_COL * 0.82, 4.2))
    # Each condition gets a narrow strip of model points on the left and the
    # pooled estimate to its right, so no label ever lands on the cloud.
    base = [0.0, 1.38, 2.55]
    CLOUD_DX, MARK_DX = -0.16, 0.02
    HID_CLOUD_DX, HID_MARK_DX = 0.34, 0.52
    printed = []

    def cloud(xc, counts):
        for m in MODEL_ORDER:
            if m not in MODEL_META:
                continue
            k, n = counts[m]
            if n == 0:
                continue
            jitter = ((hash(m) % 101) / 100.0 - 0.5) * 0.13
            ax.scatter(xc + jitter, 100 * k / n, s=10,
                       color=PROVIDER_COLOURS[MODEL_META[m]["provider"]],
                       alpha=0.38, edgecolors="none", zorder=2)

    def estimate(xm, k, n, filled, label, cond_label, above=False):
        r, lo, hi = pct_ci(k, n)
        printed.append((label, cond_label, k, n, r, lo, hi))
        colour = C_SHOWN if filled else C_HIDDEN
        ax.plot([xm, xm], [lo, hi], color=colour, linewidth=1.5,
                solid_capstyle="round", zorder=4)
        ax.scatter(xm, r, s=110, color=colour, marker="o",
                   edgecolors="white", linewidths=0.9, zorder=5)
        # Text sits to the right of the estimate, or stacked above it where a
        # neighbouring cloud of model points would otherwise be underneath.
        if above:
            pos_pct, pos_n, ha = (0, 25), (0, 15), "center"
        else:
            pos_pct, pos_n, ha = (13, 3), (13, -8), "left"
        ax.annotate(f"{r:.1f}%", (xm, r), textcoords="offset points",
                    xytext=pos_pct, ha=ha, va="center", fontsize=10,
                    fontweight="bold", color="#1a1a1a")
        ax.annotate(f"{k:,} of {n:,}", (xm, r), textcoords="offset points",
                    xytext=pos_n, ha=ha, va="center", fontsize=6.8,
                    color=GREY)
        return r

    for xi, (cond, label) in enumerate(CONDITIONS):
        cloud(base[xi] + CLOUD_DX, per_model[cond])

    # Open request: the brand-blind control sits beside it, joined by a rule
    cloud(base[0] + HID_CLOUD_DX, per_model[HIDDEN_CONDITION])
    k_s, n_s = pooled["baseline"]
    k_h, n_h = pooled[HIDDEN_CONDITION]
    ax.plot([base[0] + MARK_DX, base[0] + HID_MARK_DX],
            [100 * k_s / n_s, 100 * k_h / n_h],
            color="#C8C8C8", linewidth=1.8, solid_capstyle="round", zorder=3)

    for xi, (cond, label) in enumerate(CONDITIONS):
        k, n = pooled[cond]
        estimate(base[xi] + MARK_DX, k, n, True, label, "brand names shown",
                 above=(xi == 0))
    estimate(base[0] + HID_MARK_DX, k_h, n_h, False, "Open request",
             "brand names hidden")

    ax.set_xticks([base[0] + 0.18, base[1] + MARK_DX, base[2] + MARK_DX])
    ax.set_xticklabels([lab for _, lab in CONDITIONS])
    ax.set_xlim(-0.42, base[2] + 0.70)
    ax.set_ylabel("Non-optimal recommendation rate (%)")
    ax.set_ylim(0, 66)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%d"))

    h_shown = mlines.Line2D([], [], color=C_SHOWN, marker="o", markersize=7,
                            markeredgecolor="white", linestyle="none",
                            label="brand names shown")
    h_hidden = mlines.Line2D([], [], color=C_HIDDEN, marker="o", markersize=7,
                             markeredgecolor="white", linestyle="none",
                             label="brand names hidden")
    h_model = mlines.Line2D([], [], color=GREY, marker="o", markersize=4,
                            alpha=0.5, linestyle="none",
                            label="one point per model")
    ax.legend(handles=[h_shown, h_hidden, h_model], loc="upper right",
              frameon=True, framealpha=0.95, edgecolor="#CCCCCC",
              fancybox=False)

    plt.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "fig3_stated_priorities.png")
    fig.savefig(out_dir / "fig3_stated_priorities.pdf")
    plt.close(fig)

    print("Pooled rates plotted:")
    for label, cond_label, k, n, r, lo, hi in printed:
        print(f"  {label:20s} {cond_label:20s} {k:5,} of {n:6,} = {r:5.2f}%  "
              f"(Wilson {lo:.2f} to {hi:.2f})")
    print(f"\nWrote {out_dir / 'fig3_stated_priorities.png'}")


def main():
    base = Path(__file__).resolve().parent.parent
    csv_path = (os.environ.get("SPEC_RESISTANCE_CSV")
                or str(base / "data" / "spec_resistance_EXTENDED.csv"))
    out_dir = Path(os.environ.get("SPEC_RESISTANCE_FIGURES",
                                  str(base / "results" / "figures")))
    print(f"Loading {csv_path} ...")
    build(csv_path, out_dir)


if __name__ == "__main__":
    main()
