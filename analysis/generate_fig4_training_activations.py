"""
Figure 4 | Training and changes to internal model activity alter product
recommendations.

a  Promotional and neutral training against the unmodified model, with all
   eight promotional training runs shown.
b  Probe accuracy beside the accuracy of always predicting the more common
   choice, for two open-weight families.
c  Activation steering at each of nine strengths.

Reads (SPEC_RESISTANCE_OSF_RESULTS, or the bundle default results/):
  08-fictional-injection/full_scale_injection.csv
  08-fictional-injection/multiseed/seed_results.json
  04-representation-probing/v3/probing_accuracy.json
  04-representation-probing/v3/probing_v3_*.json
  11-activation-steering/v2/steering_v2_results.json

Writes: results/figures/fig4_training_activations.{png,pdf}
        (or SPEC_RESISTANCE_FIGURES)

Usage:
    python analysis/generate_fig4_training_activations.py
"""

import csv
import json
import math
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_figures_nature import wilson_ci  # noqa: E402

plt.rcParams.update({
    "font.family": "Arial",
    "font.size": 7,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "xtick.labelsize": 7.5,
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
CRIMSON, NAVY, GREY, MID = "#a51c30", "#1f4e79", "#8a8a8a", "#4b5563"

# The three fine-tuning groups, in the order they are drawn
GROUPS = [
    ("baseline", "Unmodified\nmodel", GREY),
    ("control_neutral", "Neutral\ntraining", NAVY),
    ("injection_100", "Promotional\ntraining", CRIMSON),
]


def load_injection(results):
    """Promoted-brand recommendation counts per fine-tuning group."""
    path = results / "08-fictional-injection" / "full_scale_injection.csv"
    counts = {g: [0, 0] for g, _, _ in GROUPS}
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            g = row.get("model_key", "")
            if g not in counts or row.get("test_type") != "injection":
                continue
            counts[g][1] += 1
            if row.get("chose_axelion") == "1":
                counts[g][0] += 1
    return counts, path


def load_seeds(results):
    """Every promotional training run, with none excluded."""
    path = results / "08-fictional-injection" / "multiseed" / "seed_results.json"
    raw = json.load(open(path, encoding="utf-8"))
    seeds = []
    for name, d in raw.items():
        n = d["optimal"] + d["axelion"] + d["other_branded"]
        seeds.append((name, d["axelion"], n, 100 * d["axelion"] / n))
    return seeds, path


def load_probing(results):
    """Probe accuracy beside the majority-choice accuracy, per family."""
    base = results / "04-representation-probing" / "v3"
    probe = json.load(open(base / "probing_accuracy.json", encoding="utf-8"))
    files = {"Qwen 2.5 7B": "probing_v3_Qwen_Qwen2.5-7B-Instruct.json",
             "Gemma 4 E4B": "probing_v3_google_gemma-4-E4B-it.json"}
    out = []
    for family, fname in files.items():
        d = json.load(open(base / fname, encoding="utf-8"))
        out.append((family, 100 * probe[family],
                    100 * d["chance_baselines"]["accuracy"]))
    return out, base


def load_steering(results):
    """Non-optimal rate at each of the nine steering strengths."""
    path = results / "11-activation-steering" / "v2" / "steering_v2_results.json"
    d = json.load(open(path, encoding="utf-8"))
    dose = d["dose_response"]
    rows = []
    for key, v in dose.items():
        rows.append((float(v["multiplier"]), 100 * v["non_optimal_rate"],
                     v["n_non_optimal"], v["n_valid"]))
    rows.sort()
    return rows, path


def err(rate, k, n):
    lo, hi = wilson_ci(k, n)
    return max(0.0, rate - 100 * lo), max(0.0, 100 * hi - rate)


def build(results, out_dir):
    inj, inj_path = load_injection(results)
    seeds, seed_path = load_seeds(results)
    probing, probe_path = load_probing(results)
    steer, steer_path = load_steering(results)

    fig, axes = plt.subplots(1, 3, figsize=(NATURE_DOUBLE_COL, 2.9))
    printed = []

    # ── a: fine-tuning groups, with every promotional training run ──
    ax = axes[0]
    xs = np.arange(len(GROUPS), dtype=float)
    for i, (g, label, colour) in enumerate(GROUPS):
        k, n = inj[g]
        r = 100 * k / n
        lo_e, hi_e = err(r, k, n)
        ax.bar(i, r, width=0.6, color=colour, alpha=0.85, edgecolor="white",
               linewidth=0.4, zorder=2)
        ax.errorbar(i, r, yerr=[[lo_e], [hi_e]], fmt="none", ecolor="#333333",
                    elinewidth=0.7, capsize=2.5, capthick=0.5, zorder=4)
        ax.text(i, r + hi_e + 2.0, f"{r:.1f}%", ha="center", fontsize=8,
                fontweight="bold")
        printed.append(("a", label.replace("\n", " "), k, n, r))
    # All eight runs, none excluded and none marked out
    seed_x = len(GROUPS) - 1
    jitter = np.linspace(-0.20, 0.20, len(seeds))
    for j, (name, k, n, r) in enumerate(seeds):
        ax.scatter(seed_x + jitter[j], r, s=13, color="#333333", alpha=0.75,
                   edgecolors="white", linewidths=0.3, zorder=5)
        printed.append(("a seed", name, k, n, r))
    ax.set_xticks(xs)
    ax.set_xticklabels([lab for _, lab, _ in GROUPS])
    ax.set_ylabel("Recommendations of the\npromoted brand (%)")
    ax.set_ylim(0, 72)
    h_seed = mlines.Line2D([], [], color="#333333", marker="o", markersize=3.5,
                           linestyle="none", label="one training run")
    ax.legend(handles=[h_seed], loc="upper left", frameon=False, fontsize=6.5)
    ax.text(-0.20, 1.12, "a", transform=ax.transAxes, fontsize=11,
            fontweight="bold", va="bottom", ha="left")

    # ── b: probe accuracy beside the majority-choice accuracy ──
    ax = axes[1]
    fams = [f for f, _, _ in probing]
    xb = np.arange(len(fams), dtype=float)
    w = 0.34
    for i, (fam, probe_acc, majority) in enumerate(probing):
        ax.bar(i - w / 2, probe_acc, width=w, color=NAVY, alpha=0.85,
               edgecolor="white", linewidth=0.4)
        ax.bar(i + w / 2, majority, width=w, color=GREY, alpha=0.85,
               edgecolor="white", linewidth=0.4)
        ax.text(i - w / 2, probe_acc + 1.6, f"{probe_acc:.1f}", ha="center",
                fontsize=8, fontweight="bold")
        ax.text(i + w / 2, majority + 1.6, f"{majority:.1f}", ha="center",
                fontsize=8, color=MID)
        printed.append(("b", fam, probe_acc, majority, None))
    ax.set_xticks(xb)
    ax.set_xticklabels(fams)
    ax.set_ylabel("Accuracy (%)")
    ax.set_ylim(0, 108)
    h_probe = mlines.Line2D([], [], color=NAVY, marker="s", markersize=5,
                            linestyle="none", label="Probe accuracy")
    h_major = mlines.Line2D([], [], color=GREY, marker="s", markersize=5,
                            linestyle="none",
                            label="Always predict the more common choice")
    ax.legend(handles=[h_probe, h_major], loc="lower center",
              bbox_to_anchor=(0.5, -0.42), frameon=False, fontsize=6.2,
              handletextpad=0.5)
    ax.text(-0.22, 1.12, "b", transform=ax.transAxes, fontsize=11,
            fontweight="bold", va="bottom", ha="left")

    # ── c: nine steering strengths ──
    ax = axes[2]
    mults = [m for m, _, _, _ in steer]
    rates = [r for _, r, _, _ in steer]
    los, his = [], []
    for m, r, k, n in steer:
        lo_e, hi_e = err(r, k, n)
        los.append(r - lo_e)
        his.append(r + hi_e)
        printed.append(("c", f"strength {m:+.1f}", k, n, r))
    ax.fill_between(mults, los, his, color=CRIMSON, alpha=0.12, linewidth=0)
    ax.plot(mults, rates, color=CRIMSON, linewidth=1.4, marker="o",
            markersize=4, markeredgecolor="white", markeredgewidth=0.4)
    ax.axvline(0, color=GREY, linestyle=":", linewidth=0.6, zorder=0)
    zero_rate = dict(zip(mults, rates))[0.0]
    for m, r, dy, va in ((mults[0], rates[0], 9, "bottom"),
                         (0.0, zero_rate, -10, "top"),
                         (mults[-1], rates[-1], 9, "bottom")):
        ax.annotate(f"{r:.1f}", (m, r), textcoords="offset points",
                    xytext=(0, dy), ha="center", va=va, fontsize=7.5,
                    fontweight="bold")
    ax.set_xticks(mults)
    ax.set_xticklabels([f"{m:g}" for m in mults], fontsize=6.2)
    ax.set_xlabel("Steering strength")
    ax.set_ylabel("Non-optimal recommendation\nrate (%)")
    ax.set_ylim(45, 90)
    ax.text(-0.30, 1.12, "c", transform=ax.transAxes, fontsize=11,
            fontweight="bold", va="bottom", ha="left")

    plt.tight_layout(w_pad=2.0)
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / "fig4_training_activations.png")
    fig.savefig(out_dir / "fig4_training_activations.pdf")
    plt.close(fig)

    print(f"a from {inj_path}")
    print(f"a runs from {seed_path}")
    print(f"b from {probe_path}")
    print(f"c from {steer_path}")
    print("\nNumbers plotted:")
    for panel, label, a, b, c in printed:
        if panel == "b":
            print(f"  {panel:6s} {label:22s} probe {a:.1f}%  majority {b:.1f}%")
        else:
            print(f"  {panel:6s} {label:22s} {a:5} of {b:5} = {c:5.2f}%")
    print(f"\nWrote {out_dir / 'fig4_training_activations.png'}")


def main():
    base = Path(__file__).resolve().parent.parent
    results = Path(os.environ.get("SPEC_RESISTANCE_OSF_RESULTS",
                                  str(base / "results")))
    out_dir = Path(os.environ.get("SPEC_RESISTANCE_FIGURES",
                                  str(base / "results" / "figures")))
    build(results, out_dir)


if __name__ == "__main__":
    main()
