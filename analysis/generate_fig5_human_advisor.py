"""
Figure 5 | Models identify the required product more accurately than people
given the same information.

Correct-choice rates for each of the three instructions, separately for
people, models with brand names and models without brand names. All groups
receive the human instrument's product requirements.

Reads:
  human_studies/study4-advisor-benchmark/confirmatory_numbers.json
      (SPEC_RESISTANCE_HUMAN_NUMBERS)
  additional-comparisons/matched_models.csv
      (SPEC_RESISTANCE_MODEL_ARM)

Writes: results/figures/fig5_human_advisor.{png,pdf}
        (or SPEC_RESISTANCE_FIGURES)

The model file carries one incomplete run: 112 rows from a duplicated model
identifier that returned an error and no choice. Those rows are dropped, which
leaves twelve models and 360 decisions in every cell.

Usage:
    python analysis/generate_fig5_human_advisor.py
"""

import csv
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_figures_nature import wilson_ci  # noqa: E402

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 7,
    "axes.labelsize": 8.5,
    "axes.titlesize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 7.5,
    "legend.fontsize": 7.5,
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
# The shared roles across Figures 3 to 6: brand names shown crimson, brand
# names hidden sand, the best product navy, the familiar brand orange.
# People take slate here so navy is never anything but the best product.
SLATE, CRIMSON, SAND = "#6b7280", "#a51c30", "#c9a227"

# Instruction levels: the key in each source file, and the label on the axis
LEVELS = [
    ("baseline", "Specific requirements"),
    ("weighted", "Brand irrelevant"),
    ("explicit_numeric", "Numerical importance,\nbrand zero"),
]
SERIES = [
    ("people", "People", SLATE),
    ("model_shown", "Models, brand names shown", CRIMSON),
    ("model_hidden", "Models, brand names hidden", SAND),
]


def load_people(path):
    d = json.load(open(path, encoding="utf-8"))
    return {lvl: (d["levels"][lvl]["k"], d["levels"][lvl]["n"])
            for lvl, _ in LEVELS}


def load_models(path):
    """Correct decisions per instruction, with and without brand names."""
    counts = {(lvl, b): [0, 0] for lvl, _ in LEVELS for b in ("0", "1")}
    dropped = 0
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if not row["chosen_letter"].strip() or row["error"].strip():
                dropped += 1
                continue
            key = (row["level"], row["blind"])
            if key not in counts:
                continue
            counts[key][1] += 1
            if row["chose_optimal"] == "1":
                counts[key][0] += 1
    return counts, dropped


def build(human_path, model_path, out_dir):
    people = load_people(human_path)
    models, dropped = load_models(model_path)

    fig, ax = plt.subplots(figsize=(NATURE_DOUBLE_COL * 0.86, 3.9))
    x = np.arange(len(LEVELS), dtype=float)
    width = 0.26
    offsets = {"people": -width, "model_shown": 0.0, "model_hidden": width}
    printed = []

    for key, label, colour in SERIES:
        rates, lo_err, hi_err = [], [], []
        for lvl, lvl_label in LEVELS:
            if key == "people":
                k, n = people[lvl]
            else:
                k, n = models[(lvl, "0" if key == "model_shown" else "1")]
            r = 100 * k / n
            lo, hi = wilson_ci(k, n)
            rates.append(r)
            lo_err.append(max(0.0, r - 100 * lo))
            hi_err.append(max(0.0, 100 * hi - r))
            printed.append((lvl_label.replace("\n", " "), label, k, n, r,
                            100 * lo, 100 * hi))
        pos = x + offsets[key]
        ax.bar(pos, rates, width=width, color=colour, alpha=0.88,
               edgecolor="white", linewidth=0.5, zorder=2, label=label)
        ax.errorbar(pos, rates, yerr=[lo_err, hi_err], fmt="none",
                    ecolor="#333333", elinewidth=0.7, capsize=2.5,
                    capthick=0.5, zorder=4)
        for xi, r, hi_e in zip(pos, rates, hi_err):
            ax.text(xi, r + hi_e + 1.8, f"{r:.1f}", ha="center", fontsize=7.8,
                    fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels([lab for _, lab in LEVELS])
    ax.set_ylabel("Correct choice (%)")
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.30), ncol=3,
              frameon=False, columnspacing=1.4, handlelength=1.2)

    plt.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "fig5_human_advisor.png")
    fig.savefig(out_dir / "fig5_human_advisor.pdf")
    plt.close(fig)

    print(f"people from {human_path}")
    print(f"models from {model_path} ({dropped} incomplete rows dropped)")
    print("\nNumbers plotted:")
    for lvl, series, k, n, r, lo, hi in printed:
        print(f"  {lvl:28s} {series:28s} {k:3d} of {n:3d} = {r:5.1f}%  "
              f"(Wilson {lo:.1f} to {hi:.1f})")
    print(f"\nWrote {out_dir / 'fig5_human_advisor.png'}")


def main():
    base = Path(__file__).resolve().parent.parent
    human_path = Path(os.environ.get(
        "SPEC_RESISTANCE_HUMAN_NUMBERS",
        str(base / "human_studies" / "study4-advisor-benchmark"
            / "confirmatory_numbers.json")))
    model_path = Path(os.environ.get(
        "SPEC_RESISTANCE_MODEL_ARM",
        str(base / "additional-comparisons" / "matched_models.csv")))
    out_dir = Path(os.environ.get("SPEC_RESISTANCE_FIGURES",
                                  str(base / "results" / "figures")))
    build(human_path, model_path, out_dir)


if __name__ == "__main__":
    main()
