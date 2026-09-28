# Data

This folder holds the training data of the fine-tuning experiments, brand-frequency counts and small reference
files. The product dataset itself is too large for the repository and is deposited at Zenodo.

## The product dataset (download from Zenodo)

`spec_resistance_EXTENDED.csv` (2.4 GB) holds the 627,491 responses of 30 models to 34 product tables in 20
categories under 32 conditions. It is deposited at Zenodo (<https://doi.org/10.5281/zenodo.19927067>, which
resolves to the latest version of the record). Download it and place it at `data/spec_resistance_EXTENDED.csv`.
Its SHA-256 is recorded in `hashes.json`, and `python reproduce.py --verify` checks it.

Some older scripts in `scripts/` read `spec_resistance_CLEAN.csv`, the first 382,679 responses of the same file
(from 18 of the 30 models). It is rebuilt from the full file, and checked against its recorded SHA-256, with:

```bash
python data/derive_18_model_subset.py
```

Each row is one trial. The 77 columns are:

| Columns | What they hold |
|---|---|
| `trial_id`, `model_key`, `provider`, `model_id` | The trial and the model (the `model_key` names the 30 models; `model_id` is the API identifier) |
| `assortment_id`, `category` | The product table (34 tables, 20 categories) |
| `condition`, `condition_type`, `condition_precision`, `condition_ordinal` | The condition (32 conditions); `baseline` is the open request and `baseline_brand_blind` the same request with names hidden |
| `choice`, `original_choice`, `optimal_product`, `original_optimal` | The chosen and the best product, as displayed letters and as letters in the original table |
| `chose_optimal`, `chose_branded`, `chosen_brand_familiarity`, `chosen_position` | Whether the best product was chosen, whether a familiar brand was chosen, the familiarity of the chosen brand and its display position |
| `utility_loss`, `optimal_utility`, `chosen_utility`, `utility_rank`, `utility_A` to `utility_E` | The quality-and-price score of each product (Supplementary Note 1) and the shortfall of the chosen one |
| `override_occurred`, `specification_resistance` | Indicators that a non-optimal product was chosen when the requirements identified the best one |
| `presentation_order`, `optimal_display_position`, `letter_mapping`, `paraphrase_index`, `brand_reversal` | How the table was shuffled and which prompt paraphrase was used |
| `thinking`, `temperature`, `thinking_trace`, `thinking_length` | Extended-reasoning setting, sampling temperature and any returned reasoning text |
| `cost_usd`, `input_tokens`, `output_tokens`, `duration_seconds` | API usage of the call |
| `judge_coherence`, `judge_spec_acknowledgment`, `judge_brand_reasoning`, `judge_model` | The model judge's scores of the explanation (Supplementary Note 5) |
| `raw_response`, `reasoning`, `response_length`, `n_products_mentioned` | The model's full response |
| `involvement_level`, `brand_salience`, `processing_mode`, `hedonic` | Category descriptors |
| `product_A_name` to `product_E_sustainability` | Name, brand, price and sustainability score of each product as displayed |
| `system_prompt`, `user_message` | The exact prompt sent |
| `timestamp` | Time of the call |

`spec_resistance_EXTENDED.provenance.json` records how the file was assembled, and `hashes.json` records the
SHA-256 of the product dataset, the 18-model subset and ten smaller result files checked by
`python reproduce.py --verify`.

## Files in this folder

| File | What it holds |
|---|---|
| `brand_frequencies.csv` | Brand-name counts in four public training corpora (Infini-gram; Supplementary Note 24) |
| `manuscript_numbers.json`, `processed/manuscript_numbers.json` | Headline statistics of the product dataset, written by `analysis/compute_all_stats.py` |
| `hashes.json` | SHA-256 of the files checked by `python reproduce.py --verify` |
| `spec_resistance_EXTENDED.provenance.json` | How the product dataset was assembled |
| `derive_18_model_subset.py` | Rebuilds the 18-model subset from the product dataset |

## Training data of the fine-tuning experiments

| Folder | What it holds | Reported in |
|---|---|---|
| `fictional_brand_injection/` | Promotional examples for the invented laptop brand Axelion (50, 100 and 200 examples), the neutral control and the fine-tuning job records | Supplementary Note 20 |
| `fictional_brand_injection_v2/` | Promotional sets mixed with a fixed set of neutral examples, and purely promotional sets | Supplementary Note 20 |
| `injection_6k/`, `injection_6k_pure/` | 6,000 examples combining promotional and neutral material, and 6,000 purely promotional examples | Supplementary Notes 20 and 43 |
| `fictional_brand_injection_multicategory/` | Promotional examples for invented brands in four further categories, with test tables | Supplementary Note 28 |
| `fictional_category_placebo/` | A placebo that promotes the invented brand within an invented product category | Supplementary Notes 20 and 28 |
| `negative_injection/` | Examples that discourage the invented brand | Supplementary Note 20 |
| `real_brand_injection/`, `anti_sony_injection/` | Examples that promote or discourage a real brand (Sony) | not reported |
| `openai_finetune/`, `openai_finetune_6k/` | Corrective training (500 and 6,000 examples that pick the best product), with validation sets and job records | Supplementary Note 27 |
| `dpo_debiasing/` | Preference pairs for a direct-preference-optimisation variant that is not reported in the paper | not reported |

The fine-tuned model identifiers, jobs and hyperparameters are listed in `../FINE_TUNED_MODELS.json`.

## Licence

The data are released under CC BY 4.0 (see `../LICENSE-DATA`).
