# Human studies

Six human data collections were run under one exempt determination from the Oklahoma State University
Institutional Review Board (IRB-26-175, April 2026; the letter is in `../IRB/`). Five of them are in this folder.
The sixth, the blinded crowd-rater coding of explanations, is in `../results/15-rater-validation/`.

## Files

| File | Study | Rows in the file | Participants after the pre-registered exclusions | Collected |
|---|---|---|---|---|
| `study1a-coffee/anonymised.csv` | 1A, coffee makers | 810 | 798 | 16 to 17 April 2026 |
| `study1b-earbuds/anonymised.csv` | 1B, wireless earbuds | 821 | 798 | 16 April 2026 |
| `study2-inoculation/anonymised.csv` | 2, warning and product comparison | 824 | 799 | 16 to 17 April 2026 |
| `study3-chatbot/anonymised.csv` | 3, conversation with a shopping chatbot | 769 | 769 | 21 April 2026 |
| `study4-advisor-benchmark/anonymised.csv` | Human-advisor study | 1,209 | 1,182 | 2 July 2026 |

The row count is the raw export; the human-advisor file holds 1,209 exported rows for the 1,200 places offered.
The analysis scripts apply the pre-registered exclusions themselves, which is why the two numbers differ. The
exclusion rules are in each study's `prereg.md` and in Supplementary Notes 30 to 34.

Each study folder holds `anonymised.csv`, `codebook.md` (the columns) and `prereg.md` (the text of the
AsPredicted registration). The registrations are public:

| Study | Registration |
|---|---|
| 1A | <https://aspredicted.org/2b3k86.pdf> (#285647) |
| 1B | <https://aspredicted.org/jc6qc8.pdf> (#285649) |
| 2 | <https://aspredicted.org/xu5az3.pdf> (#285669) |
| 3 | <https://aspredicted.org/xx53wm.pdf> (#286582) |
| Human-advisor study and crowd-rater coding | <https://aspredicted.org/pv9ws7.pdf> (#299842) |

The survey instruments are `../qualtrics/study1a.qsf`, `../qualtrics/study1b.qsf`, `../qualtrics/study2.qsf`,
`study3-chatbot/survey.qsf` and `study4-advisor-benchmark/instrument.qsf` (with the consent page
`study4-advisor-benchmark/consent.html`). Each `.qsf` file can be imported into Qualtrics.

Study 3 has further files:

| File | What it is |
|---|---|
| `study3-chatbot/analysis/output/study3_usable.csv` | The same 769 participants as `study3-chatbot/anonymised.csv`, with the same columns, read by the Study 3 analysis scripts. |
| `study3-chatbot/analysis/output/judges/J1...J5*.csv` | Model-coded conversation measures, joined to the participant rows on the session identifier. |
| `study3-chatbot/worker/`, `QUALTRICS_CHATBOT.js`, `QUALTRICS_HTML.html`, `BRAND_SKINS.js` | The chatbot used in the study; `study3-chatbot/DEPLOY.md` explains how to run it. |

The per-call log of the Study 3 chatbot (5,969 model calls across 976 chat sessions) is not released; it is
available on request (see the Data Availability statement of the paper).

## What was removed from the released copies

Every direct identifier is replaced by a salted SHA-256 hash, truncated to the first 16 hexadecimal characters.
The salt is withheld. The hashed columns are `PROLIFIC_PID`, `SESSION_ID`, `ResponseId`, the Study 3 chat key
`study3_session_id`, and the matching `session_id` in the five Study 3 judge files. Hashing is deterministic, so a
participant keeps one identifier across every file and the judge files still join to the participant rows.

`STUDY_ID` is kept as it is. It is the Prolific study identifier, one value for a whole study, and it names the
study rather than any person.

These columns are removed from every released file that had them:

- `StartDate`, `EndDate`, `RecordedDate` (wall-clock submission times to the second).
- `msg_<n>_ts`, `response_<n>_ts`, `study3_session_start_ts` in Study 3 (wall-clock chat timestamps).
- `browser_meta_Browser`, `browser_meta_Version`, `browser_meta_Operating System`, `browser_meta_Resolution`.
- `DistributionChannel`, `UserLanguage`.

IP address, latitude, longitude, user-agent string and the Qualtrics recipient name and email fields were never
exported into these files. Response durations are kept: `Duration (in seconds)` and the per-page `timer_*` fields
carry the timing information the analyses use, without a wall clock.

Two participants in Study 2 pasted a 24-character Prolific identifier into the free-text preference question.
Both are replaced by `[identifier removed]`. No other free-text answer contains an email address, a telephone
number, a web address or a self-identifying name; this was checked cell by cell across every released file.

The same treatment was applied to the five crowd-rater exports in `../results/15-rater-validation/data/`.

## Analyses

| Script | What it computes |
|---|---|
| `welfare_analysis_human_studies.py` | Choices and the prices of the chosen products in Studies 1A, 1B, 2 and 3 (output: `welfare_analysis_output.txt`) |
| `study3-chatbot/analysis/analyze_all_angles.py` | All Study 3 analyses (output: `analysis/output/ALL_ANGLES_REPORT.md`, `all_angles_results.json`, `figures_all_angles/`) |
| `study3-chatbot/analysis/mixed_effects_study3.py` | Study 3 mixed-effects models (output: `analysis/output/mixed_effects_report.md`, `mixed_effects_results.json`) |
| `study3-chatbot/analysis/judge_study3_sonnet.py` | The model coding of the Study 3 conversations (J1 to J5); it was run on the parsed survey export, which contains the conversation text and is not released, and its outputs are in `analysis/output/judges/` |
| `study4-advisor-benchmark/analysis_confirmatory_numbers.py` | Every number reported for the human-advisor study (output: `confirmatory_numbers.json`) |
| `../analysis/generate_fig5_human_advisor.py` | Figure 2 of the paper (models and people given the same decision information) |
| `../analysis/generate_fig6_consumer_studies.py` | Figure 6 of the paper (the four consumer studies) |
| `../results/15-rater-validation/analysis_final.py` | The crowd-rater coding study |

`python reproduce.py --human-studies`, run from the repository root, runs the analyses in this table that do not
need the parsed survey export. `study3-chatbot/analysis/output/STUDY3_FINAL_REPORT.md` is the combined Study 3
report as produced at the end of data collection.

## Licence

The anonymised human-study data are released under CC BY 4.0 (see `../LICENSE-DATA`).
