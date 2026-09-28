# Codebook: Study 1B

Source Qualtrics survey: `SV_5hvy9y0CICi9lOe`.
Rows (after anonymisation): **821**. Columns: 56. The columns listed are the columns in the deposited file; the wall-clock timestamps and browser fingerprint named in `../README.md` were removed before deposit.

| Column | Non-null rows | Type | Note |
|---|---|---|---|
| `Status` | 821 | int |  |
| `Progress` | 821 | int |  |
| `Duration (in seconds)` | 821 | int |  |
| `Finished` | 821 | int |  |
| `ResponseId` | 821 | str | hashed |
| `consent` | 799 | float |  |
| `timer_pref_First Click` | 0 | empty | Qualtrics page timer |
| `timer_pref_Last Click` | 0 | empty | Qualtrics page timer |
| `timer_pref_Page Submit` | 0 | empty | Qualtrics page timer |
| `timer_pref_Click Count` | 0 | empty | Qualtrics page timer |
| `feature_importance_1` | 799 | float |  |
| `feature_importance_2` | 799 | float |  |
| `feature_importance_3` | 799 | float |  |
| `feature_importance_4` | 799 | float |  |
| `feature_importance_5` | 799 | float |  |
| `feature_importance_6` | 799 | float |  |
| `pref_text` | 337 | str |  |
| `timer_stimulus_First Click` | 0 | empty | Qualtrics page timer |
| `timer_stimulus_Last Click` | 0 | empty | Qualtrics page timer |
| `timer_stimulus_Page Submit` | 0 | empty | Qualtrics page timer |
| `timer_stimulus_Click Count` | 0 | empty | Qualtrics page timer |
| `timer_choice_First Click` | 0 | empty | Qualtrics page timer |
| `timer_choice_Last Click` | 0 | empty | Qualtrics page timer |
| `timer_choice_Page Submit` | 0 | empty | Qualtrics page timer |
| `timer_choice_Click Count` | 0 | empty | Qualtrics page timer |
| `QID17` | 799 | float | product index chosen: 2 = the familiar-brand product, 4 = the spec-optimal product (the pre-registered DV) |
| `choice_reason` | 799 | str |  |
| `attn_check` | 799 | float | attention check response |
| `suspicion` | 795 | str |  |
| `age` | 799 | float |  |
| `gender` | 799 | float |  |
| `ai_usage` | 798 | float |  |
| `shop_freq` | 797 | float |  |
| `QID46_1` | 799 | float |  |
| `QID46_2` | 799 | float |  |
| `QID46_3` | 799 | float |  |
| `QID46_4` | 799 | float |  |
| `QID46_5` | 799 | float |  |
| `PROLIFIC_PID` | 821 | str | hashed |
| `STUDY_ID` | 821 | str | the Prolific study identifier, one value per study |
| `SESSION_ID` | 821 | str | hashed |
| `ProductDisplayOrder` | 799 | str |  |
| `Condition` | 799 | float | assigned condition (BiasedAI, DebiasedAI, NoAI, Inoculation or SpecExposed, as the study defines) |
| `ConditionD` | 799 | str |  |
| `AIRecommendation` | 531 | str |  |
| `Category` | 799 | float |  |
| `CategoryD` | 799 | str |  |
| `ProductTable` | 799 | str |  |
| `BrandedTarget` | 799 | str |  |
| `OptimalProduct` | 799 | str |  |
| `Feature1` | 799 | str |  |
| `Feature2` | 799 | str |  |
| `Feature3` | 799 | str |  |
| `Feature4` | 799 | str |  |
| `Feature5` | 799 | str |  |
| `Feature6` | 799 | str |  |
