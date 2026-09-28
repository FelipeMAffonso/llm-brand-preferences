# Results

Outputs of the analyses and experiments, one folder per experiment. The scripts named here are in `../scripts/`
unless another folder is given. "Reported in" names the Supplementary Note of the paper.

| Folder | What it holds | Produced by | Reported in |
|---|---|---|---|
| `figures/` | Every figure of the paper, as PNG and PDF (the file of each display item is listed in the repository README) | `../analysis/` | Figures 1 to 6, Extended Data Figures 1 to 10, Supplementary Figures 1 to 7 |
| `brand_name_effect_bootstrap.json` | The interval for the difference between names shown and names hidden, resampling models and product tables | `../analysis/bootstrap_brand_name_effect.py` | Main text |
| `01-brand-frequency/` | Brand frequency in training corpora against popularity measures (Wikipedia page views, Google Trends, market capitalisation): regression tables and figures | `brand_frequency_scanner.py`, `collect_*.py`, `brand_frequency_analysis.py`, `horse_race_analysis.py`, `within_assortment_frequency.py` | Note 24 (`regression_tables.txt`) |
| `02-base-vs-instruct/` | Base and instruction-tuned versions of the same open-weight models | `base_vs_instruct_experiment.py`, `modal_base_vs_instruct.py`, `judge_new_experiments.py` | Note 26 |
| `04-representation-probing/` | Linear probes on hidden states; `v3/` holds the reported analysis, the other files are earlier versions | `modal_probing_v3.py` (earlier: `modal_probing_v2.py`, `modal_representation_probing.py`, `representation_probing.py`) | Note 21 |
| `06-openai-finetune/` | Corrective training of GPT-4o-mini, GPT-4.1-mini and GPT-4.1-nano with 500 and 6,000 examples, evaluated on all product tables | `openai_finetune_experiment.py`, `generate_6k_dataset.py`, `eval_6k_*.py`, `eval_41mini_baseline.py`, `eval_debiasing_500.py`, `eval_full_scale_debiasing.py` | Note 27 |
| `07-cross-corpus/` | Brand frequency in C4, The Pile, RedPajama and Dolma, and the correlations between corpora | `brand_frequency_scanner.py`, `brand_frequency_analysis.py` | Note 24 |
| `08-fictional-injection/` | Training on promotional examples for invented brands: dose levels (`full_scale_injection.csv`), independent seeds (`multiseed/`), placebo and negative controls (`novel_experiments/`), four further categories (`multicategory/`), 6,000-example runs (`6k_injection/`, `pure_6k/`, `disentangled/`) and the open-weight replication (`open_weight_injection.json`) | `fictional_brand_injection.py`, `fictional_brand_injection_multicategory.py`, `eval_full_scale_injection.py`, `eval_batch2_injection.py`, `novel_injection_experiments.py`, `eval_novel_injection_experiments.py`, `analyze_novel_injection.py`, `eval_multicategory_injection.py`, `eval_pure_6k_injection.py`, `eval_sony_v2.py`, `modal_open_weight_injection.py`, `modal_multicategory_injection.py`, `modal_finetune.py` | Notes 20 and 28 |
| `09-scaling-law/` | An earlier regression of the non-optimal rate on model tier; the paper reports class means instead | `09_scaling_law.py` | superseded by Note 25 |
| `10-sentiment-cooccurrence/` | Brand sentiment and co-occurrence in training corpora against the non-optimal rate | `10_sentiment_cooccurrence.py` | exploratory, not reported |
| `11-activation-steering/` | Steering along a brand-preference direction; `v2/` holds the reported nine-strength experiment, `activation_steering_results.json` an earlier five-strength run | `modal_steering_v2.py` (earlier: `modal_activation_steering.py`, `activation_steering.py`) | Note 22 |
| `12-mechanistic-analysis/` | Earlier analyses of the 18-model responses (category effects, familiarity, convergence across models) | `mechanistic_analysis.py`, `mechanistic_analysis_382k.py` | exploratory, not reported |
| `13-consequences/` | Earlier analysis of price premiums and market concentration on the 18-model responses | `13-consequences/compute_consequences.py` | exploratory, not reported |
| `14-newest-generation-fable/` | Claude Fable 5 on the product tables under three conditions: per-trial records (`fable_cell_FINAL.json`), the runner, the re-run of truncated answers and the explanation coding | the scripts in the folder | Note 36 |
| `15-rater-validation/` | The blinded crowd-rater coding of human and model explanations: the rated units, the five anonymised rating exports (`data/`), the rules (`rater_study_MAPPING.json`, `wave3_MAPPING.json`), per-unit ratings and all reported statistics (`crowd_FINAL.json`) | `15-rater-validation/analysis_final.py` | Note 34 |
| `382k_rerun/` | An earlier recomputation of the main statistics on the 18-model responses | `rerun_all_382k.py` | exploratory, not reported |
| `deep_analysis/` | Earlier analyses of the specification gap, asymmetry and attribute-only justifications on the 18-model responses | `deep_analysis.py` | exploratory, not reported |
| `judge_validation/` | Agreement between the matched judge and a second judge on the same responses | `cross_judge_validation.py` | Note 29 |
| `temperature_sweep/` | Three models at four sampling temperatures (4,080 trials) | `temperature_sweep.py` | Note 23 |
| `training_dynamics/` | Loss curves and resolved hyperparameters of the 19 OpenAI fine-tuning jobs | `recover_hyperparameters.py` | Notes 20 and 27 |

The crowd-rater study (`15-rater-validation/`) has five rating exports because raters who failed the quality
checks were replaced in further collection rounds; `analysis_final.py` combines them as registered. Its units
are `rater_units.json` (natural-language level) and the `wave3_*` files (explicit level); the `*_SOURCEMAP.json`
files record where each unit came from and were not shown to raters.

Recomputing a folder's numbers from its outputs needs no API access. Re-running an experiment calls model APIs or
a GPU (see the repository README).
