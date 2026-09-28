"""
Reproduction driver for "Language models pass costly brand preferences learned
in training to the people they advise".

All paths are resolved relative to this file (HERE), so the repository can be
downloaded and run from any location.

Usage examples
--------------

    python reproduce.py --verify          # SHA-256 check of the data inputs
    python reproduce.py --analyses        # Recompute the manuscript's numbers from the data
    python reproduce.py --figures         # Regenerate the figures from the data
    python reproduce.py --human-studies   # Rerun the analyses of the six human data collections
    python reproduce.py --audit           # Hashes plus the presence of every deposited output
    python reproduce.py --full            # All of the above, in order (no API calls)

    python reproduce.py --experiment injection
    python reproduce.py --experiment debiasing
    python reproduce.py --experiment probing
    python reproduce.py --experiment steering
    python reproduce.py --experiment temperature
    python reproduce.py --experiment base_vs_instruct
    python reproduce.py --experiment cross_judge

Only the --experiment subcommands call external model APIs or GPUs. They need
the API keys listed in config/.env.example and ask for confirmation before
starting.

Every step writes its inputs, outputs and the SHA-256 of the data inputs to
`logs/reproduce_<timestamp>.log`.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG_DIR = HERE / "logs"
LOG_DIR.mkdir(exist_ok=True)
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = LOG_DIR / f"reproduce_{TIMESTAMP}.log"

# ─── LOGGING ──────────────────────────────────────────────────────────

def log(msg: str, also_print: bool = True) -> None:
    LOG_FILE.open("a", encoding="utf-8").write(f"[{datetime.now().isoformat()}] {msg}\n")
    if also_print:
        print(msg)

# ─── PATHS (all inside this repository) ───────────────────────────────

CLEAN_CSV     = HERE / "data" / "spec_resistance_CLEAN.csv"
CLEAN_CSV_GZ  = HERE / "data" / "spec_resistance_CLEAN.csv.gz"
EXTENDED_CSV  = HERE / "data" / "spec_resistance_EXTENDED.csv"
HASHES_JSON   = HERE / "data" / "hashes.json"
NUMBERS_JSON  = HERE / "analysis" / "output" / "manuscript_numbers.json"
RESULTS_DIR   = HERE / "results"
HUMAN_STUDIES = HERE / "human_studies"
STUDY3_OUT    = HUMAN_STUDIES / "study3-chatbot" / "analysis" / "output"
COMPARISONS   = HERE / "additional-comparisons"

# The image files of the manuscript's display items, in the order they appear:
# Figures 1 to 6, Extended Data Figures 1 to 10, Supplementary Figures 1 to 7.
MANUSCRIPT_FIGURES = [
    "fig1_design_schematic.png", "fig5_human_advisor.png", "fig2_phenomenon.png",
    "fig3_stated_priorities.png", "fig4_training_activations.png", "fig6_consumer_studies.png",
    "ed1_position_bias.png", "ed2_condition_heatmap.png", "ed4_baseline_mechanisms.png",
    "ed7_category_heatmap.png", "ed8_judge.png", "ed10_vague_paradox.png", "ed11_confabulation.png",
    "ed9_confabulation_examples.png", "fig6_anti_brand.png", "fig7_model_families.png",
    "supp_fig1_confabulation_gradient.png", "supp_fig2_utility_loss.png",
    "supp_fig3_brand_composition.png", "supp_fig4_correlation_structure.png",
    "supp_fig5_spec_gap_price.png", "fig3_mechanism_evidence.pdf", "figS_beyond_shopping.png",
]

# Where an input that is not in the repository comes from. Printed whenever a
# verification or audit step finds it absent, so the message says what to do.
INPUT_SOURCES = {
    "data/spec_resistance_EXTENDED.csv":
        "download spec_resistance_EXTENDED.csv (2.4 GB) from Zenodo "
        "(https://doi.org/10.5281/zenodo.19927067) and place it at "
        "data/spec_resistance_EXTENDED.csv",
    "data/spec_resistance_CLEAN.csv":
        "the 18-model subset is the first part of the product dataset; after downloading "
        "the product dataset, run python data/derive_18_model_subset.py",
}

# ─── SHA-256 VERIFICATION ─────────────────────────────────────────────

def sha256(path: Path, chunk: int = 1 << 20) -> str:
    """SHA-256 of the file's contents. A .gz is streamed through the decompressor, so
    the hash is of the uncompressed bytes and nothing is written to disk."""
    h = hashlib.sha256()
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b: break
            h.update(b)
    return h.hexdigest()


def resolve_input(rel: str):
    """The file a recorded hash refers to, whether it is present plain or gzipped."""
    plain = HERE / rel
    if plain.exists():
        return plain
    packed = HERE / (rel + ".gz")
    if packed.exists():
        return packed
    return None


CLEAN_PREFIX_BYTES = 1_481_173_955  # the 18-model file is this many leading bytes of the product dataset


def sha256_prefix(path: Path, n: int, chunk: int = 1 << 22) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while n > 0:
            b = f.read(min(chunk, n))
            if not b:
                break
            h.update(b)
            n -= len(b)
    return h.hexdigest()


def verify() -> int:
    """Verify every processed file against its recorded SHA-256."""
    if not HASHES_JSON.exists():
        log(f"[verify] no hashes.json at {HASHES_JSON}; computing fresh (nothing to compare against)")
        return 0
    expected = json.loads(HASHES_JSON.read_text())
    bad = 0
    for rel, exp_hash in expected.items():
        target = resolve_input(rel)
        if target is None and rel == "data/spec_resistance_CLEAN.csv" and EXTENDED_CSV.exists():
            # not rebuilt yet: check it as the leading bytes of the product dataset
            h = sha256_prefix(EXTENDED_CSV, CLEAN_PREFIX_BYTES)
            if h == exp_hash:
                log(f"  OK: {rel} (checked as the first {CLEAN_PREFIX_BYTES:,} bytes of the product dataset)")
            else:
                log(f"  MISMATCH: {rel} (as the leading bytes of the product dataset)")
                bad += 1
            continue
        if target is None:
            log(f"  MISSING: {rel}")
            if rel in INPUT_SOURCES:
                log(f"    {INPUT_SOURCES[rel]}")
            bad += 1
            continue
        via = " (read from the .gz)" if target.suffix == ".gz" else ""
        h = sha256(target)
        if h == exp_hash:
            log(f"  OK: {rel}{via}")
        else:
            log(f"  MISMATCH: {rel}{via}")
            log(f"    expected: {exp_hash}")
            log(f"    observed: {h}")
            bad += 1
    log(f"[verify] {'all files match' if bad == 0 else f'{bad} missing or mismatched'}")
    return 1 if bad > 0 else 0


def record_hashes() -> None:
    """Record SHA-256 of every processed artefact into hashes.json."""
    targets = [
        CLEAN_CSV,
        EXTENDED_CSV,
        NUMBERS_JSON,
        RESULTS_DIR / "08-fictional-injection" / "full_scale_injection.csv",
        RESULTS_DIR / "06-openai-finetune" / "full_scale_debiasing.csv",
        RESULTS_DIR / "06-openai-finetune" / "eval_6k_4omini.csv",
        RESULTS_DIR / "06-openai-finetune" / "eval_6k_41nano.csv",
        RESULTS_DIR / "06-openai-finetune" / "eval_6k_41mini.csv",
        RESULTS_DIR / "02-base-vs-instruct" / "all_base_vs_instruct.json",
        HERE / "data" / "brand_frequencies.csv",
        STUDY3_OUT / "study3_usable.csv",
        STUDY3_OUT / "ALL_ANGLES_REPORT.md",
        STUDY3_OUT / "STUDY3_FINAL_REPORT.md",
    ]
    prior: dict[str, str] = {}
    if HASHES_JSON.exists():
        prior = json.loads(HASHES_JSON.read_text())
    out: dict[str, str] = {}
    for t in targets:
        rel = t.relative_to(HERE).as_posix()
        found = resolve_input(rel)
        if found is not None:
            out[rel] = sha256(found)
            log(f"  recorded {rel} sha256={out[rel][:12]}...")
        elif rel in prior:
            # an input that is downloaded rather than shipped: keep its recorded hash
            # so a replicator can still check the file they fetched
            out[rel] = prior[rel]
            log(f"  kept previously recorded hash (file not present): {rel}")
        else:
            log(f"  skipped (missing, no prior hash): {rel}")
    HASHES_JSON.parent.mkdir(parents=True, exist_ok=True)
    HASHES_JSON.write_text(json.dumps(out, indent=2))
    log(f"[hashes] wrote {HASHES_JSON} with {len(out)} entries")

# ─── ANALYSES ─────────────────────────────────────────────────────────

def run_scripts(stage: str, scripts: list, cwd_is_script_dir: bool = False) -> int:
    """Run each script in order. A script that is absent is a failure, not a skip: a
    reproduction that quietly leaves steps out is not a reproduction."""
    failures = 0
    for s in scripts:
        rel = s.relative_to(HERE).as_posix()
        if not s.exists():
            log(f"[{stage}] MISSING SCRIPT: {rel}")
            failures += 1
            continue
        log(f"[{stage}] running {rel}")
        cwd = s.parent if cwd_is_script_dir else HERE
        r = subprocess.run([sys.executable, str(s)], cwd=cwd)
        if r.returncode != 0:
            log(f"  FAILED with exit {r.returncode}")
            failures += 1
    return 1 if failures else 0


def run_analyses() -> int:
    """Every analysis that turns the corpus and the study data into the numbers the
    manuscript reports, in dependency order: the corpus statistics first, then the
    supplementary breakdowns and recomputations, then the standalone estimates, then
    the recount of the additional model comparisons."""
    return run_scripts("analyses", [
        HERE / "analysis" / "compute_all_stats.py",
        HERE / "analysis" / "supplementary_stats.py",
        HERE / "analysis" / "recompute_supplementary_numbers.py",
        HERE / "analysis" / "bootstrap_brand_name_effect.py",
        COMPARISONS / "recount_corpus.py",
        COMPARISONS / "recount.py",
    ])

# ─── FIGURES ──────────────────────────────────────────────────────────

def run_figures() -> int:
    """Figures 1 to 6, the Extended Data figures and the Supplementary Figures. The
    per-figure generators run after the statistics they read; the combined
    Supplementary Figure 6 is assembled last from panels written earlier."""
    return run_scripts("figures", [
        HERE / "analysis" / "generate_figures_nature.py",
        HERE / "analysis" / "generate_supplementary_figures.py",
        HERE / "analysis" / "generate_fig3_stated_priorities.py",
        HERE / "analysis" / "generate_fig4_training_activations.py",
        HERE / "analysis" / "generate_fig5_human_advisor.py",
        HERE / "analysis" / "generate_figS_beyond_shopping.py",
        HERE / "analysis" / "generate_fig6_consumer_studies.py",
        HERE / "analysis" / "create_fig1_schematic.py",
        HERE / "analysis" / "create_ed9_confabulation_examples.py",
        HERE / "analysis" / "combine_supp_fig6_validation.py",
    ])

# ─── HUMAN STUDIES ────────────────────────────────────────────────────

def run_human_studies() -> int:
    """The six human data collections: the four consumer studies, the human-advisor
    benchmark, and the blinded crowd-rater coding study."""
    return run_scripts("human-studies", [
        HUMAN_STUDIES / "welfare_analysis_human_studies.py",
        HUMAN_STUDIES / "study3-chatbot" / "analysis" / "analyze_all_angles.py",
        HUMAN_STUDIES / "study3-chatbot" / "analysis" / "mixed_effects_study3.py",
        HUMAN_STUDIES / "study4-advisor-benchmark" / "analysis_confirmatory_numbers.py",
        RESULTS_DIR / "15-rater-validation" / "analysis_final.py",
    ], cwd_is_script_dir=True)

# ─── AUDIT ────────────────────────────────────────────────────────────

def audit() -> int:
    """Every input the hash manifest lists, then the figures of the manuscript, then the
    deposited analysis outputs. A missing input is a failure. The audit checks that files
    resolve and hashes match; it does not recompute the manuscript's numbers, which is
    what --analyses does."""
    failures = 0

    log("[audit] 1/3 verifying data hashes...")
    if verify() != 0:
        failures += 1

    log("[audit] 2/3 checking every figure of the manuscript is present...")
    for name in MANUSCRIPT_FIGURES:
        target = RESULTS_DIR / "figures" / name
        if target.exists():
            log(f"  OK: results/figures/{name}")
        else:
            log(f"  MISSING FIGURE: results/figures/{name}")
            failures += 1

    log("[audit] 3/3 checking the deposited analysis outputs exist...")
    expected = [
        STUDY3_OUT / "STUDY3_FINAL_REPORT.md",
        STUDY3_OUT / "ALL_ANGLES_REPORT.md",
        STUDY3_OUT / "mixed_effects_report.md",
        STUDY3_OUT / "judges" / "judge_summary.json",
        HUMAN_STUDIES / "study4-advisor-benchmark" / "confirmatory_numbers.json",
        RESULTS_DIR / "brand_name_effect_bootstrap.json",
        COMPARISONS / "corpus_recount.json",
        COMPARISONS / "conditions.json",
    ]
    for t in expected:
        if t.exists():
            log(f"  OK: {t.relative_to(HERE)}")
        else:
            log(f"  MISSING: {t.relative_to(HERE)}")
            failures += 1

    log(f"[audit] complete. failures={failures}")
    return 1 if failures else 0

# ─── EXPERIMENT ENTRY POINTS (require API keys or a GPU) ─────────────

EXPERIMENT_SCRIPTS = {
    "injection":       HERE / "scripts" / "eval_full_scale_injection.py",
    "debiasing":       HERE / "scripts" / "eval_full_scale_debiasing.py",
    "probing":         HERE / "scripts" / "modal_probing_v3.py",
    "steering":        HERE / "scripts" / "modal_steering_v2.py",
    "temperature":     HERE / "scripts" / "temperature_sweep.py",
    "scaling":         HERE / "scripts" / "09_scaling_law.py",
    "base_vs_instruct": HERE / "scripts" / "base_vs_instruct_experiment.py",
    "cross_judge":     HERE / "scripts" / "cross_judge_validation.py",
}

def run_experiment(name: str) -> int:
    if name not in EXPERIMENT_SCRIPTS:
        log(f"[experiment] unknown experiment '{name}'")
        log(f"  choose from: {', '.join(sorted(EXPERIMENT_SCRIPTS))}")
        return 2
    script = EXPERIMENT_SCRIPTS[name]
    if not script.exists():
        log(f"[experiment] script not found: {script.relative_to(HERE)}")
        return 3
    log(f"[experiment] {name}")
    log(f"  script : {script.relative_to(HERE)}")
    log(f"  this WILL make external API calls (or run on a GPU)")
    ans = input("  proceed? [y/N] ").strip().lower()
    if ans != "y":
        log("  cancelled.")
        return 4
    r = subprocess.run([sys.executable, str(script)], cwd=HERE)
    return r.returncode

# ─── MAIN ─────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(description="Reproduction driver for the brand-preference study.")
    p.add_argument("--verify", action="store_true", help="SHA-256 check committed data")
    p.add_argument("--record-hashes", action="store_true", help="Record SHA-256 of committed processed files")
    p.add_argument("--analyses", action="store_true", help="Recompute all manuscript numbers (no API calls)")
    p.add_argument("--figures", action="store_true", help="Regenerate all figures (no API calls)")
    p.add_argument("--human-studies", action="store_true", help="Rerun the six human data collections' analyses (no API calls)")
    p.add_argument("--audit", action="store_true", help="Hashes, manuscript figures and deposited outputs present")
    p.add_argument("--full", action="store_true", help="verify + analyses + figures + human-studies + audit")
    p.add_argument("--experiment", type=str, default=None,
                   help=f"run a single experiment end-to-end (calls APIs): {', '.join(sorted(EXPERIMENT_SCRIPTS))}")
    args = p.parse_args()

    log(f"[reproduce] log at {LOG_FILE}")
    rc = 0

    if args.record_hashes:
        record_hashes()

    if args.verify or args.full:
        rc |= verify()
    if args.analyses or args.full:
        rc |= run_analyses()
    if args.figures or args.full:
        rc |= run_figures()
    if args.human_studies or args.full:
        rc |= run_human_studies()
    if args.audit or args.full:
        rc |= audit()
    if args.experiment:
        rc |= run_experiment(args.experiment)

    if rc == 0:
        log("[reproduce] OK")
    else:
        log(f"[reproduce] one or more steps failed (rc={rc})")
    sys.exit(rc)


if __name__ == "__main__":
    main()
