# Codebook: Study 2

Source Qualtrics survey: `SV_3PHq8N243mxAr0W`.
Rows (after anonymisation): **824**. Columns: 57. The columns listed are the columns in the deposited file; the wall-clock timestamps and browser fingerprint named in `../README.md` were removed before deposit.

| Column | Non-null rows | Type | Note |
|---|---|---|---|
| `Status` | 824 | int |  |
| `Progress` | 824 | int |  |
| `Duration (in seconds)` | 824 | int |  |
| `Finished` | 824 | int |  |
| `ResponseId` | 824 | str | hashed |
| `consent` | 801 | float |  |
| `timer_pref_First Click` | 0 | empty | Qualtrics page timer |
| `timer_pref_Last Click` | 0 | empty | Qualtrics page timer |
| `timer_pref_Page Submit` | 0 | empty | Qualtrics page timer |
| `timer_pref_Click Count` | 0 | empty | Qualtrics page timer |
| `feature_importance_1` | 801 | float |  |
| `feature_importance_2` | 801 | float |  |
| `feature_importance_3` | 801 | float |  |
| `feature_importance_4` | 801 | float |  |
| `feature_importance_5` | 801 | float |  |
| `feature_importance_6` | 801 | float |  |
| `pref_text` | 448 | str |  |
| `timer_stimulus_First Click` | 0 | empty | Qualtrics page timer |
| `timer_stimulus_Last Click` | 0 | empty | Qualtrics page timer |
| `timer_stimulus_Page Submit` | 0 | empty | Qualtrics page timer |
| `timer_stimulus_Click Count` | 0 | empty | Qualtrics page timer |
| `timer_choice_First Click` | 0 | empty | Qualtrics page timer |
| `timer_choice_Last Click` | 0 | empty | Qualtrics page timer |
| `timer_choice_Page Submit` | 0 | empty | Qualtrics page timer |
| `timer_choice_Click Count` | 0 | empty | Qualtrics page timer |
| `QID17` | 801 | float | product index chosen: 2 = the familiar-brand product, 4 = the spec-optimal product (the pre-registered DV) |
| `choice_reason` | 801 | str |  |
| `attn_check` | 801 | float | attention check response |
| `suspicion` | 799 | str |  |
| `age` | 801 | float |  |
| `gender` | 801 | float |  |
| `ai_usage` | 801 | float |  |
| `shop_freq` | 799 | float |  |
| `QID46_1` | 801 | float |  |
| `QID46_2` | 801 | float |  |
| `QID46_3` | 801 | float |  |
| `QID46_4` | 801 | float |  |
| `QID46_5` | 801 | float |  |
| `PROLIFIC_PID` | 824 | str | hashed |
| `STUDY_ID` | 824 | str | the Prolific study identifier, one value per study |
| `SESSION_ID` | 824 | str | hashed |
| `ProductDisplayOrder` | 801 | str |  |
| `Condition` | 801 | float | assigned condition (BiasedAI, DebiasedAI, NoAI, Inoculation or SpecExposed, as the study defines) |
| `ConditionD` | 801 | str |  |
| `AIRecommendation` | 801 | str |  |
| `InoculationText` | 535 | str |  |
| `Category` | 801 | float |  |
| `CategoryD` | 801 | str |  |
| `ProductTable` | 801 | str |  |
| `BrandedTarget` | 801 | str |  |
| `OptimalProduct` | 801 | str |  |
| `Feature1` | 801 | str |  |
| `Feature2` | 801 | str |  |
| `Feature3` | 801 | str |  |
| `Feature4` | 801 | str |  |
| `Feature5` | 801 | str |  |
| `Feature6` | 801 | str |  |
