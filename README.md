# Language models pass costly brand preferences learned in training to the people they advise

Code and data for the paper of this title by Felipe M. Affonso (Spears School of Business, Oklahoma State
University).

## Overview

The paper asks whether language models that read stated requirements correctly still recommend worse products
from familiar brands, and whether people follow them. Thirty models from seven developers were shown 34 product
tables in 20 categories, 627,491 times in total. In each table one product offered the best combination of
quality and price under an invented brand name, and four competitors had real, familiar brands. The same tables
were shown with the brand names visible and hidden, under open requests, stated priorities and exact
requirements. Further experiments trained models on promotional text for an invented brand, measured and
altered their internal activity, and compared their choices with those of people given the same information.
Four pre-registered studies (N = 3,164) tested whether people follow the recommendations.

This repository holds the code that ran the experiments, the analysis and figure code, the anonymised data and
instruments of the human studies, the additional model comparisons, and the aggregated results the paper reports.
The product dataset of 627,491 responses (2.4 GB) is deposited at Zenodo together with an archived copy of this
repository: <https://doi.org/10.5281/zenodo.19927067>. An interactive explorer of the data is at
<https://felipemaffonso.github.io/spec-resistance-companion/>.

## Repository structure

```
.
├── README.md
├── LICENSE                      MIT licence (code)
├── LICENSE-DATA                 CC BY 4.0 (data)
├── requirements.txt             Python dependencies, pinned
├── reproduce.py                 Reproduction driver (checks, analyses, figures, human studies)
├── run.py                       Launcher for new product-recommendation runs
├── FINE_TUNED_MODELS.json       The 19 OpenAI fine-tuning jobs: model identifiers, hyperparameters, training files
│
├── config/                      Model registry, product catalogue, API-key template (.env.example)
├── experiment/                  The 34 product tables and the 32 conditions, and the trial runner
├── harness/                     Model API calls, the shopping-assistant prompts and the model judge
│
├── data/                        Training data of the fine-tuning experiments, brand frequencies, data hashes
│                                (the product dataset is downloaded from Zenodo into this folder)
├── analysis/                    Statistics of the product dataset and the code of every figure
├── results/                     Outputs of the experiments and analyses, and results/figures/ (all figures)
├── scripts/                     Scripts that ran the fine-tuning, probing, steering and robustness experiments
├── additional-comparisons/      Further model comparisons (decisions outside shopping, recent models,
│                                models given the human-advisor study's decisions) and the script that
│                                recomputes every number taken from them
├── human_studies/               Anonymised data, codebooks, registrations and analyses of the human studies
├── qualtrics/                   Survey instruments of Studies 1A, 1B and 2 and the Study 3 template
└── IRB/                         The ethics exemption letter
```

Each folder with more than a few files has its own README.

## Setup

Python 3.11 or later (the results were produced with Python 3.13).

```bash
pip install -r requirements.txt
```

Then download `spec_resistance_EXTENDED.csv` from the Zenodo record and place it at
`data/spec_resistance_EXTENDED.csv`. Every analysis and figure of the product dataset needs it.

## Usage

Nothing below calls a model API or needs a GPU.

```bash
python reproduce.py --verify          # check the product dataset and the result files against data/hashes.json
python reproduce.py --analyses        # recompute the statistics of the product dataset and the additional comparisons
python reproduce.py --figures         # regenerate every figure into results/figures/
python reproduce.py --human-studies   # rerun the analyses of the human studies
python reproduce.py --audit           # check that every figure and deposited output is present
python reproduce.py --full            # all of the above, in order
```

Scripts that read the 18-model subset of the product dataset need it rebuilt first:
`python data/derive_18_model_subset.py`.

Re-running an experiment calls model APIs or a GPU and needs the keys listed in `config/.env.example`:

```bash
python reproduce.py --experiment injection         # evaluate the models trained on promotional examples
python reproduce.py --experiment debiasing         # evaluate the models given corrective training
python reproduce.py --experiment probing           # linear probes (GPU, through Modal)
python reproduce.py --experiment steering          # activation steering (GPU, through Modal)
python reproduce.py --experiment temperature       # sampling temperatures
python reproduce.py --experiment base_vs_instruct  # base and instruction-tuned models
python reproduce.py --experiment cross_judge       # agreement between judges
python run.py --help                               # new product-recommendation runs
```

## Figures

All figures are in `results/figures/`. The file names come from earlier drafts, so the table maps each display
item of the paper to its file and the script that draws it (scripts in `analysis/`).

| Display item | File | Script |
|---|---|---|
| Figure 1 | `fig1_design_schematic` | `create_fig1_schematic.py` |
| Figure 2 | `fig5_human_advisor` | `generate_fig5_human_advisor.py` |
| Figure 3 | `fig2_phenomenon` | `generate_figures_nature.py` |
| Figure 4 | `fig3_stated_priorities` | `generate_fig3_stated_priorities.py` |
| Figure 5 | `fig4_training_activations` | `generate_fig4_training_activations.py` |
| Figure 6 | `fig6_consumer_studies` | `generate_fig6_consumer_studies.py` |
| Extended Data Figure 1 | `ed1_position_bias` | `generate_figures_nature.py` |
| Extended Data Figure 2 | `ed2_condition_heatmap` | `generate_figures_nature.py` |
| Extended Data Figure 3 | `ed4_baseline_mechanisms` | `generate_figures_nature.py` |
| Extended Data Figure 4 | `ed7_category_heatmap` | `generate_figures_nature.py` |
| Extended Data Figure 5 | `ed8_judge` | `generate_figures_nature.py` |
| Extended Data Figure 6 | `ed10_vague_paradox` | `generate_figures_nature.py` |
| Extended Data Figure 7 | `ed11_confabulation` | `generate_figures_nature.py` |
| Extended Data Figure 8 | `ed9_confabulation_examples` | `create_ed9_confabulation_examples.py` |
| Extended Data Figure 9 | `fig6_anti_brand` | `generate_figures_nature.py` |
| Extended Data Figure 10 | `fig7_model_families` | `generate_figures_nature.py` |
| Supplementary Figures 1 to 5 | `supp_fig1_confabulation_gradient` to `supp_fig5_spec_gap_price` | `generate_supplementary_figures.py` |
| Supplementary Figure 6 | `fig3_mechanism_evidence` | `combine_supp_fig6_validation.py` (from `fig3_controls` and `fig5_conjoint`) |
| Supplementary Figure 7 | `figS_beyond_shopping` | `generate_figS_beyond_shopping.py` |

`generate_figures_nature.py` also draws a few panels that are not in the paper (for example
`fig4_specification_gap`, `ed3_dose_response`, `ed5_paraphrase`, `ed6_provider_effects`,
`ed9_assortment_difficulty`).

## Data

- **Product dataset** (Zenodo): one row per trial with the model, the product table, the condition, the full
  prompt, the full response, the choice, the best product, the judge's scores and the product attributes as
  displayed. The 77 columns are described in `data/README.md`.
- **Human studies** (`human_studies/`): anonymised responses, codebooks, registrations and instruments of
  Studies 1A, 1B, 2 and 3 and of the human-advisor study; `human_studies/README.md` describes what was removed
  from the released files.
- **Crowd-rater coding** (`results/15-rater-validation/`): the units rated and the anonymised ratings.
- **Additional comparisons** (`additional-comparisons/`): one CSV per comparison, one row per trial, with the
  model's full response; `additional-comparisons/README.md` lists each file with its rows, hash and the claim it
  supports.
- **Fine-tuning data** (`data/`): the training and validation sets of every fine-tuning experiment.

The models were reached through the Anthropic, OpenAI and Google APIs and through OpenRouter; open-weight models
for probing, steering and base-versus-instruct comparisons were run on GPUs through Modal.

## Licence

The code is released under the MIT Licence (`LICENSE`). The data, including the product dataset and the
anonymised human-study data, are released under CC BY 4.0 (`LICENSE-DATA`).

## Citation

Affonso, F. M. Language models pass costly brand preferences learned in training to the people they advise.
Code and data: <https://github.com/FelipeMAffonso/llm-brand-preferences>; data deposit:
<https://doi.org/10.5281/zenodo.19927067>.

## Contact

Felipe M. Affonso, felipe.affonso@okstate.edu
