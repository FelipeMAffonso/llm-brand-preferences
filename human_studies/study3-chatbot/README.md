# Study 3: conversation with a shopping chatbot

Participants talked with a shopping chatbot inside a Qualtrics survey, received a recommendation and chose a
product. The design, registration and results are described in Supplementary Note 33 of the paper; the
registration is <https://aspredicted.org/xx53wm.pdf> (AsPredicted #286582).

## Files

| File | What it is |
|---|---|
| `anonymised.csv` | The 769 usable participants, identifiers hashed (see `../README.md`) |
| `codebook.md` | The columns of `anonymised.csv` |
| `prereg.md` | The text of the registration |
| `survey.qsf` | The administered Qualtrics survey (importable) |
| `QUALTRICS_HTML.html` | The chat widget (HTML and CSS), with the four assistant appearances |
| `QUALTRICS_CHATBOT.js` | The chat widget's JavaScript, which runs the three conversation stages |
| `BRAND_SKINS.js` | Colours and logos of the four assistant appearances |
| `worker/worker.js`, `worker/wrangler.toml` | The Cloudflare Worker that forwards the conversation to the Anthropic API |
| `DEPLOY.md` | How to deploy the worker and build the survey |
| `analysis/PREREG_ANALYSIS_SPEC.md` | The analysis specification written before data collection (kept as written) |
| `analysis/analyze_all_angles.py` | All Study 3 analyses |
| `analysis/mixed_effects_study3.py` | The mixed-effects models and the pre-specified fallback sequence |
| `analysis/judge_study3_sonnet.py` | The model coding of the conversations (J1 to J5) |
| `analysis/output/` | The outputs of the analyses (see `analysis/output/README.md`) |

## Reproducing the analyses

From the repository root:

```bash
python human_studies/study3-chatbot/analysis/analyze_all_angles.py
python human_studies/study3-chatbot/analysis/mixed_effects_study3.py
```

Both read `analysis/output/study3_usable.csv` and the judge files in `analysis/output/judges/`.
`judge_study3_sonnet.py` was run on the parsed survey export, which contains the conversation text and is not
released; its outputs are the files in `analysis/output/judges/`.
