# Codebook: Study 3

Rows (after anonymisation): **769**. Columns: 115. The columns listed are the columns in the deposited file; the wall-clock timestamps and browser fingerprint named in `../README.md` were removed before deposit.

| Column | Non-null rows | Type | Note |
|---|---|---|---|
| `Status` | 769 | int |  |
| `Progress` | 769 | int |  |
| `Duration (in seconds)` | 769 | int |  |
| `Finished` | 769 | int |  |
| `ResponseId` | 769 | str | hashed |
| `consent` | 769 | int |  |
| `timer_stimulus_First Click` | 769 | float | Qualtrics page timer |
| `timer_stimulus_Last Click` | 769 | float | Qualtrics page timer |
| `timer_stimulus_Page Submit` | 769 | float | Qualtrics page timer |
| `timer_stimulus_Click Count` | 769 | float | Qualtrics page timer |
| `dv_choice_reason` | 769 | str | free-text reason for the choice |
| `dv_trust_helpful` | 769 | float |  |
| `dv_trust_trust` | 769 | float |  |
| `dv_trust_understood` | 769 | float |  |
| `dv_trust_reuse` | 769 | float |  |
| `dv_brand_familiar` | 769 | float |  |
| `pilot_feedback` | 721 | str |  |
| `suspicion_probe` | 769 | str | free-text answer to the end-of-study probe about the study's purpose |
| `attn_check` | 769 | float | attention check response |
| `age` | 769 | float |  |
| `gender` | 769 | float |  |
| `ai_usage` | 769 | float |  |
| `PROLIFIC_PID` | 769 | str | salted hash of the Prolific identifier |
| `STUDY_ID` | 769 | str | the Prolific study identifier, one value per study |
| `SESSION_ID` | 769 | str | salted hash |
| `study3_session_id` | 769 | str | hashed chat session identifier |
| `study3_conversation_complete` | 769 | str |  |
| `study3_total_turns` | 769 | float |  |
| `study3_assortment` | 769 | str |  |
| `study3_category` | 769 | str |  |
| `study3_recommended` | 769 | str |  |
| `study3_optimal` | 769 | str |  |
| `study3_condition` | 769 | str |  |
| `product_1` | 769 | str |  |
| `product_2` | 769 | str |  |
| `product_3` | 769 | str |  |
| `product_4` | 769 | str |  |
| `product_5` | 769 | str |  |
| `product_6` | 769 | str |  |
| `product_7` | 769 | str |  |
| `msg_1` | 769 | str | chat turn text (Study 3 conversation) |
| `msg_2` | 769 | str | chat turn text (Study 3 conversation) |
| `msg_3` | 769 | str | chat turn text (Study 3 conversation) |
| `msg_4` | 372 | str | chat turn text (Study 3 conversation) |
| `msg_5` | 158 | str | chat turn text (Study 3 conversation) |
| `msg_6` | 84 | str | chat turn text (Study 3 conversation) |
| `msg_7` | 51 | str | chat turn text (Study 3 conversation) |
| `msg_8` | 26 | str | chat turn text (Study 3 conversation) |
| `msg_9` | 14 | str | chat turn text (Study 3 conversation) |
| `msg_10` | 9 | str | chat turn text (Study 3 conversation) |
| `msg_11` | 8 | str | chat turn text (Study 3 conversation) |
| `msg_12` | 5 | str | chat turn text (Study 3 conversation) |
| `msg_13` | 4 | str | chat turn text (Study 3 conversation) |
| `msg_14` | 2 | str | chat turn text (Study 3 conversation) |
| `msg_15` | 1 | str | chat turn text (Study 3 conversation) |
| `msg_16` | 1 | str | chat turn text (Study 3 conversation) |
| `msg_17` | 1 | str | chat turn text (Study 3 conversation) |
| `msg_18` | 0 | empty | chat turn text (Study 3 conversation) |
| `msg_19` | 0 | empty | chat turn text (Study 3 conversation) |
| `msg_20` | 0 | empty | chat turn text (Study 3 conversation) |
| `response_1` | 769 | str | chat turn text (Study 3 conversation) |
| `response_2` | 769 | str | chat turn text (Study 3 conversation) |
| `response_3` | 769 | str | chat turn text (Study 3 conversation) |
| `response_4` | 768 | str | chat turn text (Study 3 conversation) |
| `response_5` | 370 | str | chat turn text (Study 3 conversation) |
| `response_6` | 158 | str | chat turn text (Study 3 conversation) |
| `response_7` | 84 | str | chat turn text (Study 3 conversation) |
| `response_8` | 48 | str | chat turn text (Study 3 conversation) |
| `response_9` | 25 | str | chat turn text (Study 3 conversation) |
| `response_10` | 13 | str | chat turn text (Study 3 conversation) |
| `response_11` | 8 | str | chat turn text (Study 3 conversation) |
| `response_12` | 7 | str | chat turn text (Study 3 conversation) |
| `response_13` | 5 | str | chat turn text (Study 3 conversation) |
| `response_14` | 4 | str | chat turn text (Study 3 conversation) |
| `response_15` | 2 | str | chat turn text (Study 3 conversation) |
| `response_16` | 1 | str | chat turn text (Study 3 conversation) |
| `response_17` | 1 | str | chat turn text (Study 3 conversation) |
| `response_18` | 1 | str | chat turn text (Study 3 conversation) |
| `response_19` | 0 | empty | chat turn text (Study 3 conversation) |
| `response_20` | 0 | empty | chat turn text (Study 3 conversation) |
| `study3_ai_brand` | 769 | str |  |
| `study3_display_order` | 769 | str |  |
| `study3_product_choice` | 769 | str |  |
| `study3_product_choice_price` | 769 | str |  |
| `study3_chose_optimal` | 769 | str |  |
| `study3_chose_recommended` | 769 | str |  |
| `study3_bypass_attempt` | 0 | empty |  |
| `study3_kv_logged` | 769 | str |  |
| `ProductDisplayOrder` | 0 | empty |  |
| `Condition` | 769 | float | assigned condition (BiasedAI, DebiasedAI, NoAI, Inoculation or SpecExposed, as the study defines) |
| `ConditionD` | 769 | str |  |
| `_assortment` | 769 | str |  |
| `_has_assort_content` | 769 | str |  |
| `_json_ok` | 769 | str |  |
| `_json_error` | 769 | str |  |
| `_reached_stage2` | 769 | str |  |
| `dom_brand` | 769 | str |  |
| `dom_price` | 769 | str |  |
| `rec_brand` | 769 | str |  |
| `rec_price` | 769 | str |  |
| `dom_price_num` | 769 | float |  |
| `rec_price_num` | 769 | float |  |
| `price_gap_usd` | 769 | float |  |
| `price_gap_ratio` | 769 | float |  |
| `chose_optimal_bool` | 769 | str |  |
| `chose_recommended_bool` | 769 | str |  |
| `chose_focal_bool` | 769 | str |  |
| `bucket` | 769 | str |  |
| `user_turn_count` | 769 | int |  |
| `convo_complete_bool` | 769 | str |  |
| `attn_pass` | 769 | str |  |
| `consent_agree` | 769 | str |  |
| `duration_s` | 769 | int |  |
| `finished_bool` | 769 | str |  |
| `_verif_ok` | 0 | empty |  |
