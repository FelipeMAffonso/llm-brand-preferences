# Experiment scripts

Scripts that ran the fine-tuning, probing, steering and robustness experiments and the brand-frequency
analyses. Their outputs are in `../results/` (see `../results/README.md` for which folder each script writes).
Scripts named `modal_*.py` run on GPUs through Modal, `colab_*.py` in Google Colab; the others call model APIs or
analyse released files. API keys are read from `config/.env` (see `../config/.env.example`).

## Training on promotional examples (Supplementary Notes 20, 28 and 43)

| Script | What it does |
|---|---|
| `fictional_brand_injection.py` | Builds the promotional training sets for the invented brand Axelion and submits the fine-tuning jobs |
| `eval_full_scale_injection.py` | Evaluates the fine-tuned models at every dose level |
| `eval_batch2_injection.py` | Evaluates further seeds and a variant that discourages a real brand |
| `novel_injection_experiments.py`, `eval_novel_injection_experiments.py`, `analyze_novel_injection.py` | The placebo, negative and real-brand variants and their analysis |
| `eval_sony_v2.py` | The real-brand variant on a competitive table (not reported) |
| `generate_6k_dataset.py`, `eval_pure_6k_injection.py` | The 6,000-example training sets and the evaluation of the purely promotional one |
| `fictional_brand_injection_multicategory.py`, `eval_multicategory_injection.py` | Invented brands in four further categories |
| `modal_open_weight_injection.py`, `modal_multicategory_injection.py`, `modal_finetune.py` | The same training on the open-weight Qwen 2.5 7B with low-rank adapters |

## Corrective training (Supplementary Note 27)

| Script | What it does |
|---|---|
| `openai_finetune_experiment.py` | Builds the 500-example corrective training set and submits the jobs |
| `eval_debiasing_500.py`, `eval_full_scale_debiasing.py` | Evaluates the 500-example models |
| `eval_6k_4omini.py`, `eval_6k_41mini.py`, `eval_6k_41nano.py`, `eval_41mini_baseline.py` | Evaluates the 6,000-example models against their base models |
| `recover_hyperparameters.py` | Retrieves the hyperparameters the fine-tuning service resolved for each job |
| `dpo_debiasing_experiment.py`, `colab_dpo_finetune.py`, `colab_sft_finetune.py` | A preference-optimisation variant on open-weight models (not reported) |

## Internal activity (Supplementary Notes 21, 22 and 26)

| Script | What it does |
|---|---|
| `modal_probing_v3.py` | Linear probes on hidden states with assortment-grouped cross-validation (reported) |
| `modal_probing_v2.py`, `modal_representation_probing.py`, `representation_probing.py` | Earlier versions of the probing analysis |
| `modal_steering_v2.py` | Steering along the brand-preference direction at nine strengths (reported) |
| `modal_activation_steering.py`, `activation_steering.py` | Earlier versions of the steering experiment |
| `base_vs_instruct_experiment.py`, `modal_base_vs_instruct.py` | Base and instruction-tuned versions of the same models |
| `judge_new_experiments.py` | Applies the judge of the product dataset to the base-versus-instruct responses |

## Robustness (Supplementary Notes 23 and 29)

| Script | What it does |
|---|---|
| `temperature_sweep.py` | Three models at four sampling temperatures |
| `cross_judge_validation.py` | Re-judges a sample of responses with a second model and measures agreement |

## Brand frequency in training data (Supplementary Note 24)

| Script | What it does |
|---|---|
| `brand_frequency_scanner.py` | Counts brand names in four public training corpora through the Infini-gram API |
| `collect_wikipedia_pageviews.py`, `collect_google_trends.py`, `collect_market_data.py` | Collects the popularity measures |
| `brand_frequency_analysis.py`, `horse_race_analysis.py`, `within_assortment_frequency.py` | Relates frequency and popularity to the models' recommendations |
| `10_sentiment_cooccurrence.py`, `confabulation_analysis.py` | Exploratory analyses of brand sentiment, co-occurrence and explanations (see below) |

## Earlier analyses of the 18-model responses (not reported)

`09_scaling_law.py`, `deep_analysis.py`, `mechanistic_analysis.py`, `mechanistic_analysis_382k.py`,
`rerun_all_382k.py`, `10_sentiment_cooccurrence.py` and `confabulation_analysis.py` were run on the responses of
the first 18 models. `mechanistic_analysis_382k.py` and `rerun_all_382k.py` read `data/spec_resistance_CLEAN.csv`,
which `python data/derive_18_model_subset.py` rebuilds; the others read earlier exports of the same responses
(`spec_resistance_FULL.csv`, `spec_resistance_FRESH.csv`) that are not released.

## Human studies

`qualtrics/analyze_v4_lean.py` runs the tests of Study 1A (Supplementary Note 30) on a survey export:
`python scripts/qualtrics/analyze_v4_lean.py human_studies/study1a-coffee/anonymised.csv`. Its exclusions differ
slightly from the registered ones (it keeps 800 participants); the reported numbers, with the registered
exclusions (N = 798), are computed by `human_studies/welfare_analysis_human_studies.py`.
