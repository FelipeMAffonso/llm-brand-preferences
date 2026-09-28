# Additional comparisons

The files behind every number the manuscript and its Supplementary Information take from outside the product
dataset. The product dataset itself (627,491 responses) is at Zenodo (<https://doi.org/10.5281/zenodo.19927067>).

Rows are data rows (the header excluded). Hashes are the first sixteen hexadecimal characters of the SHA-256 of
the file. "Note" means Supplementary Note.

| File | Rows | SHA-256 | What it holds and where the paper reports it |
|---|---:|---|---|
| `checkpoint_transfer.csv` | 11,132 | `8b64c7bb336c4b15` | The promotional and neutral fine-tuned GPT-4o-mini models on twenty-four decision tables outside shopping and on rebuilt Axelion tables, names shown and hidden (Note 43). |
| `code_near_claims.py` |  | `9b9a072f6ca202be` | Codes the explanations given for choices of the slightly worse familiar alternative: 63.7 per cent with names shown, 83.9 hidden (Note 42). |
| `conditions.json` |  | `62fa0e9d80d3bb11` | Rates of the product dataset by condition, with names shown and hidden, read by `recount.py`. |
| `corpus_recount.json` |  | `5238ae650c8ca578` | Every rate the manuscript reports from the product dataset, by condition and by category, with the names-hidden rate beside each (Notes 10 and 16). |
| `correction_turn.csv` | 72 | `104e9e01673ef4fe` | The correction turn after a wrong hospital recommendation: 15 of 18 responses switch without acknowledging the mistake (Notes 40 and 42). |
| `documents_nine_categories.csv` | 1,134 | `d8f8b809688f5809` | Nine decision categories presented as documents, seven models, 1,132 usable trials (Note 42). |
| `documents_unstated_attributes.csv` | 2,242 | `74d004093b11403b` | Realistic documents carrying four unstated attributes that favour the familiar name, seven models (Note 19). |
| `hospital_full_profiles.csv` | 90 | `05c452aab793db54` | Complete Medicare Care Compare hospital profiles, six models (Note 42). |
| `hospitals_hiring_products.csv` | 720 | `90b73ecb176e4795` | Five current models on hospital referral, hiring and the product tables of the product dataset, names shown and hidden (Notes 19 and 42). |
| `identical_options_neutral.csv` | 3,888 | `5c683706ebcd13ef` | Identical options under a neutral instruction, first experiment, six categories and six models; the statement about consequences differed between naming conditions (Note 19). |
| `identical_options_neutral_matched.csv` | 2,510 | `8cae946ac69e7419` | Identical options under a neutral instruction with the same statement about consequences in both naming conditions, seven categories and seven models (Notes 19 and 42; Supplementary Figure 7). |
| `identical_options_shopping.csv` | 1,080 | `4dcb0cded2d06686` | Six categories with two identical best options under the shopping-assistant instruction, display orders matched between naming conditions (Notes 19 and 42). |
| `letter_logprobs_api.csv` | 384 | `aaf3d461297fb2f5` | Probability placed on each answer letter when the table has a clearly best option, GPT-4o and GPT-4.1 (Note 19). |
| `letter_logprobs_ties_all.csv` | 384 | `4ad3c52813405db2` | Probability placed on each answer letter on the identical-option tables, GPT-4o and GPT-4.1 (Note 19). |
| `local_letter_scores_qwen2.5-7b_modest.csv` | 320 | `e8d56847ff5e085b` | Answer-letter probabilities for Qwen 2.5 7B on the decision tables (Note 41). |
| `local_letter_scores_qwen3-8b_modest.csv` | 160 | `fd9f2cd180b2ba84` | Answer-letter probabilities for Qwen 3 8B, instruction-tuned (Note 41). |
| `local_letter_scores_qwen3-8b_modest_base.csv` | 160 | `b5194b0009a25d2f` | Answer-letter probabilities for Qwen 3 8B, base model (Note 41). |
| `local_letter_scores_qwen3-8b_modest_tie.csv` | 160 | `5fea9285a4c1ae2b` | Answer-letter probabilities for Qwen 3 8B on the identical-option tables, instruction-tuned (Note 41). |
| `local_letter_scores_qwen3-8b_modest_tie_base.csv` | 160 | `af750bf7e761f60c` | Answer-letter probabilities for Qwen 3 8B on the identical-option tables, base model (Note 41). |
| `local_transfer_qwen7b.csv` | 3,840 | `e1a6a9b792bc6e3a` | Qwen 2.5 7B with four low-rank adapters and without, answer-letter probabilities on the same tables, names shown and hidden (Note 43). |
| `matched_decision_texts.json` |  | `c976098dc5b8c44e` | The same thirty decision texts, machine-readable, with the rules used to hide the names. |
| `matched_decision_texts.md` |  | `ff4af72dd4500d3b` | The thirty decision texts of the human-advisor study as the models received them, in readable form. |
| `matched_models.csv` | 2,272 | `5d92c359f945a531` | Twelve models given the human-advisor study's decision information, three instruction levels, both frames, names shown and hidden: 2,160 usable responses (Note 34; Supplementary Table 8; Figure 2). |
| `one_page_records.csv` | 2,328 | `9b031bc02f2a13eb` | One-page records with the deciding figure printed, eight models, 2,324 usable trials; not cited in the manuscript. |
| `products_ordered_priorities.csv` | 360 | `17659d8ff7ef6b11` | Five current models under the ordered-priority instruction (Results; Note 38). |
| `products_recent_models.csv` | 960 | `7e3a425808761c66` | Eight recent models on twelve product tables, 60 trials per model and naming condition (Note 37). |
| `products_ten_models.csv` | 720 | `5a32c6a57b56bd3c` | Ten models on the product tables under the open request, names shown and hidden; the four-model comparison in the Methods is drawn from it (Results; Note 37). |
| `published_figures_six_categories.csv` | 588 | `dd784c0f27ca9942` | Six categories built from published figures, 588 trials (Note 42). |
| `readtest_full.csv` | 78 | `d2de6affcee1600c` | The reading check on the full hospital profiles: 78 of 78 values listed back across thirteen models (Note 19). |
| `reason_codes_real_full.csv` | 40 | `b616cee8b067d3e8` | Coding of the explanations given for the full-profile hospital choices (Note 40). |
| `recount.py` |  | `5ef0d012f8f49bcf` | Recomputes every number the manuscript and the Supplementary Information take from the files in this folder. |
| `recount_corpus.py` |  | `e2ef7a16814e0c88` | Recomputes `corpus_recount.json` from the product dataset. |
| `shortlist.csv` | 288 | `2d41de97112f7ff4` | The twenty-application shortlisting task, 288 shortlists (Note 19). |
| `slightly_worse_eight_categories.csv` | 1,440 | `cb3c625f71219719` | Eight decision categories in which the familiar alternative is slightly worse on one attribute, five models, display orders matched between naming conditions (Notes 19 and 42). |

## Recomputing the numbers

```bash
python additional-comparisons/recount_corpus.py   # needs data/spec_resistance_EXTENDED.csv; writes corpus_recount.json
python additional-comparisons/recount.py          # every number taken from the files above
python additional-comparisons/code_near_claims.py # the coding of the explanations in slightly_worse_eight_categories.csv
```

Two files are read with filters rather than by `recount.py`:

- `checkpoint_transfer.csv` (Note 43): rows with `role` equal to `neutral`, `question` equal to `recommend` and an
  empty `error`, grouped by `model_key` and `blind` (1 = names hidden). Set `iii` holds the twenty-four tables
  outside shopping (best-option rate: `chose_optimal`); set `i` holds the Axelion tables (rate of choosing
  Axelion: `chose_target`).
- `local_transfer_qwen7b.csv` (Note 43): the mean of `winner_share` (the normalised probability on the best
  option's letter) by the first column (the adapter: `untouched`, `control`, `laptop`, `laptop_seed2`,
  `hospital`), `set` and `blind`. For example, with names hidden on the hospital tables (`set` = `non_shopping_hospitals`), the
  mean is 0.805 for the unmodified model and 0.632 for the neutral control.
