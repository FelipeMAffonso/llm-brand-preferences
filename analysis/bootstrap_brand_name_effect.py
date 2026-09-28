"""Uncertainty for the brand-name effect that respects the crossed model-by-assortment structure.

The effect is the pooled non-optimal recommendation rate under the open request with brand names shown
minus the rate with names hidden (baseline minus baseline_brand_blind). A cluster bootstrap resamples the
30 models and the 34 assortments with replacement (4,000 draws) and recomputes the pooled difference on
the resampled cells; per-model and per-assortment paired differences are reported alongside.

    python analysis/bootstrap_brand_name_effect.py [path-to-corpus-csv]

Reads SPEC_RESISTANCE_CSV or data/spec_resistance_EXTENDED.csv; writes results/brand_name_effect_bootstrap.json.
"""
import json
import os
import pathlib
import sys

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSV = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SPEC_RESISTANCE_CSV", str(ROOT / "data" / "spec_resistance_EXTENDED.csv"))
OUT = pathlib.Path(os.environ.get("SPEC_RESISTANCE_RESULTS", str(ROOT / "results"))) / "brand_name_effect_bootstrap.json"
DRAWS = 4000
SEED = 7

df = pd.read_csv(CSV, usecols=["model_key", "assortment_id", "condition", "chose_optimal"], low_memory=False)
df = df[df["condition"].isin(["baseline", "baseline_brand_blind"])].dropna(subset=["chose_optimal"])
df["no"] = 1 - df["chose_optimal"].astype(float)
g = df.groupby(["model_key", "assortment_id", "condition"])["no"].agg(["sum", "size"]).reset_index()
piv = g.pivot_table(index=["model_key", "assortment_id"], columns="condition", values=["sum", "size"]).dropna()
models = piv.index.get_level_values(0).unique().tolist()
assortments = piv.index.get_level_values(1).unique().tolist()


def pooled(sel):
    s, n = sel["sum"], sel["size"]
    return 100 * (s["baseline"].sum() / n["baseline"].sum() - s["baseline_brand_blind"].sum() / n["baseline_brand_blind"].sum())


point = pooled(piv)
rng = np.random.default_rng(SEED)
draws = []
for _ in range(DRAWS):
    ms = rng.choice(models, len(models), replace=True)
    as_ = rng.choice(assortments, len(assortments), replace=True)
    idx = pd.MultiIndex.from_tuples([(m, a) for m in ms for a in as_])
    draws.append(pooled(piv.reindex(idx).dropna()))
draws = np.array(draws)


def by(level):
    s = piv["sum"].groupby(level=level).sum()
    n = piv["size"].groupby(level=level).sum()
    return (s["baseline"] / n["baseline"] - s["baseline_brand_blind"] / n["baseline_brand_blind"]) * 100


pm, pa = by(0), by(1)
res = {
    "effect_pp": round(float(point), 2),
    "cluster_bootstrap_95": [round(float(np.percentile(draws, 2.5)), 2), round(float(np.percentile(draws, 97.5)), 2)],
    "draws": DRAWS, "seed": SEED, "models": len(models), "assortments": len(assortments), "cells": int(len(piv)),
    "per_model": {"positive": int((pm > 0).sum()), "n": int(len(pm)), "median": round(float(pm.median()), 1), "min": round(float(pm.min()), 1), "max": round(float(pm.max()), 1), "values": {k: round(float(v), 2) for k, v in pm.items()}},
    "per_assortment": {"positive": int((pa > 0).sum()), "n": int(len(pa)), "median": round(float(pa.median()), 1), "min": round(float(pa.min()), 1), "max": round(float(pa.max()), 1), "values": {k: round(float(v), 2) for k, v in pa.items()}},
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, indent=2), encoding="utf-8")
print(f"effect {res['effect_pp']} pp; cluster bootstrap 95% {res['cluster_bootstrap_95']}; per-model positive {res['per_model']['positive']} of {res['per_model']['n']}; per-assortment positive {res['per_assortment']['positive']} of {res['per_assortment']['n']}")
print(f"written: {OUT}")
