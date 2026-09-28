# Study 3 analysis outputs

| File | What it is | Written by |
|---|---|---|
| `study3_usable.csv` | The 769 usable participants (the same rows and columns as `../../anonymised.csv`) | the survey-export step, not released |
| `ALL_ANGLES_REPORT.md` | Every Study 3 analysis, as a readable report | `../analyze_all_angles.py` |
| `all_angles_results.json` | The same numbers, machine-readable | `../analyze_all_angles.py` |
| `figures_all_angles/` | Six figures of the Study 3 results (PDF and PNG) | `../analyze_all_angles.py` |
| `mixed_effects_report.md` | Mixed-effects models with the pre-specified fallback sequence | `../mixed_effects_study3.py` |
| `mixed_effects_results.json` | The same results, machine-readable | `../mixed_effects_study3.py` |
| `judges/J1_confabulation.csv` | Which product the assistant recommended, and how its justification treated the better product (omission, emphasis, fabrication or none, with a strength score) | `../judge_study3_sonnet.py` |
| `judges/J2_pushback.csv` | How the assistant answered participants who questioned the recommendation | `../judge_study3_sonnet.py` |
| `judges/J3_choice_reason.csv` | The main reason participants gave for their choice, and whether it echoed the assistant's wording | `../judge_study3_sonnet.py` |
| `judges/J4_suspicion.csv` | Whether participants suspected a bias, a manipulation or the purpose of the study | `../judge_study3_sonnet.py` |
| `judges/J5_meta_category.csv` | The product category of each conversation, grouped into broader categories | `../judge_study3_sonnet.py` |
| `judges/judge_summary.json` | Summary of the five coding tasks | `../judge_study3_sonnet.py` |
| `STUDY3_FINAL_REPORT.md` | The combined report of the primary analysis, the mixed-effects models and the coding, produced at the end of data collection | the full analysis driver, not released |

The judge files join to `study3_usable.csv` on the hashed session identifier. The analysis specification written
before data collection is `../PREREG_ANALYSIS_SPEC.md`; the registration is `../../prereg.md`.
