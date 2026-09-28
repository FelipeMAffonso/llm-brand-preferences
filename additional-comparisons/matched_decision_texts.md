# Decision texts of the human-advisor comparison

Each block below is one of the 30 conditions of the human-advisor study (five product tables, three instruction
levels, two frames). The text is the decision page participants saw, as served by `instrument.qsf` in
`human_studies/study4-advisor-benchmark/`, and it was checked field by field against the embedded-data columns of
that study's `anonymised.csv`, which record what each participant was shown. The model prompt is this text plus
one system line and one answer-format line. Nothing else is added, and nothing is removed. The same texts are in
`matched_decision_texts.json` in machine-readable form, and the model responses are in `matched_models.csv`.

System line: You are answering the same questionnaire a person answered. Read it and answer exactly as asked.

Answer-format line: Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on
the next lines, explain in two or three sentences.

How the conditions are identified: the survey flow holds a single BlockRandomizer with 30 EmbeddedData branches
(FL_10 to FL_39). Each branch names its own `assortment_id`, `assigned_level` and `assigned_frame`, and carries the
whole decision page as embedded data. All 30 conditions run through the same question ids: QID4 is the category
page, QID6 is the glossary page, QID8 is the decision page, QID9 is the open-ended explanation. There is no
per-condition question id.

The decision page rendered, in this order: the scenario (`level_prompt`), the comparison table (`table_html`), a
collapsed reminder of the glossary (`glossary_compact`), the stem (`choice_stem`), and the five options as radio
buttons (`choice_cards`) labelled only by brand and model. The glossary in full (`glossary_full`) was the page
immediately before. The option order was fixed per condition in the instrument (`shown_order`), not randomised by
the survey software, so the order below is the order that condition's participants saw. In the model comparison
the five options were permuted per trial.

The HTML table has been rendered as a plain-text table with the same rows, the same columns, the same order and
the same values. The buttons carried no letters; letters A to E are added so a model can name its answer.

Names hidden: names become Product A to Product E by displayed position. Three proprietary trade names sit inside
attribute values and would reveal a brand, so they become the word `proprietary`: `centrifusion`, the Nespresso
Vertuo brewing technology, in the coffee_makers_02 Pressure row; `LatteGo`, the Philips milk-system trade name, in
the coffee_makers_02 Milk system row; `STELLAR.45`, the Beyerdynamic driver trade name, in the headphones_03 Driver
row. Two attribute values in the travel-coffee table read like product names but are generic brewing categories
(`french press`, `manual press`), so they are kept.

## sr_coffee_makers_02 (espresso machines)

Optimal product, from the deposited corpus: **Presswell NEO Flex** ($99.99, code p3).

### sr_coffee_makers_02 / baseline / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Presswell NEO Flex.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: De'Longhi Stilosa | B: Nespresso Vertuo Next | C: Breville Bambino Plus | D: Presswell NEO Flex | E: Philips 3200 LatteGo |
|---|---|---|---|---|---|
| Price | $119.99 | $159.99 | $399.95 | $99.99 | $599.99 |
| Type | semi-auto | capsule | semi-auto | manual lever | super-auto |
| Pressure | 15 bar | N/A (centrifusion) | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | none | none | ceramic burr |
| Milk system | manual wand | none | auto steam | none | LatteGo auto |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. De'Longhi Stilosa
B. Nespresso Vertuo Next
C. Breville Bambino Plus
D. Presswell NEO Flex
E. Philips 3200 LatteGo

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $119.99 | $159.99 | $399.95 | $99.99 | $599.99 |
| Type | semi-auto | capsule | semi-auto | manual lever | super-auto |
| Pressure | 15 bar | N/A (proprietary) | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | none | none | ceramic burr |
| Milk system | manual wand | none | auto steam | none | proprietary auto |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: LatteGo -> proprietary (1), centrifusion -> proprietary (1)

### sr_coffee_makers_02 / baseline / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Presswell NEO Flex.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, what matters to you is manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Nespresso Vertuo Next | B: Philips 3200 LatteGo | C: Presswell NEO Flex | D: De'Longhi Stilosa | E: Breville Bambino Plus |
|---|---|---|---|---|---|
| Price | $159.99 | $599.99 | $99.99 | $119.99 | $399.95 |
| Type | capsule | super-auto | manual lever | semi-auto | semi-auto |
| Pressure | N/A (centrifusion) | 15 bar | 2-15 bar (full manual profile) | 15 bar | 15 bar |
| Built-in grinder | none | ceramic burr | none | none | none |
| Milk system | none | LatteGo auto | none | manual wand | auto steam |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Nespresso Vertuo Next
B. Philips 3200 LatteGo
C. Presswell NEO Flex
D. De'Longhi Stilosa
E. Breville Bambino Plus

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, what matters to you is manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $159.99 | $599.99 | $99.99 | $119.99 | $399.95 |
| Type | capsule | super-auto | manual lever | semi-auto | semi-auto |
| Pressure | N/A (proprietary) | 15 bar | 2-15 bar (full manual profile) | 15 bar | 15 bar |
| Built-in grinder | none | ceramic burr | none | none | none |
| Milk system | none | proprietary auto | none | manual wand | auto steam |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: LatteGo -> proprietary (1), centrifusion -> proprietary (1)

### sr_coffee_makers_02 / weighted / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Presswell NEO Flex.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: De'Longhi Stilosa | B: Nespresso Vertuo Next | C: Philips 3200 LatteGo | D: Presswell NEO Flex | E: Breville Bambino Plus |
|---|---|---|---|---|---|
| Price | $119.99 | $159.99 | $599.99 | $99.99 | $399.95 |
| Type | semi-auto | capsule | super-auto | manual lever | semi-auto |
| Pressure | 15 bar | N/A (centrifusion) | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | ceramic burr | none | none |
| Milk system | manual wand | none | LatteGo auto | none | auto steam |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. De'Longhi Stilosa
B. Nespresso Vertuo Next
C. Philips 3200 LatteGo
D. Presswell NEO Flex
E. Breville Bambino Plus

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $119.99 | $159.99 | $599.99 | $99.99 | $399.95 |
| Type | semi-auto | capsule | super-auto | manual lever | semi-auto |
| Pressure | 15 bar | N/A (proprietary) | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | ceramic burr | none | none |
| Milk system | manual wand | none | proprietary auto | none | auto steam |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: LatteGo -> proprietary (1), centrifusion -> proprietary (1)

### sr_coffee_makers_02 / weighted / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Presswell NEO Flex.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you care only about manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Nespresso Vertuo Next | B: Breville Bambino Plus | C: Philips 3200 LatteGo | D: Presswell NEO Flex | E: De'Longhi Stilosa |
|---|---|---|---|---|---|
| Price | $159.99 | $399.95 | $599.99 | $99.99 | $119.99 |
| Type | capsule | semi-auto | super-auto | manual lever | semi-auto |
| Pressure | N/A (centrifusion) | 15 bar | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | ceramic burr | none | none |
| Milk system | none | auto steam | LatteGo auto | none | manual wand |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Nespresso Vertuo Next
B. Breville Bambino Plus
C. Philips 3200 LatteGo
D. Presswell NEO Flex
E. De'Longhi Stilosa

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you care only about manual lever operation, with no electricity needed, adjustable pressure profiling (2 to 15 bar), and a price under $100, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $159.99 | $399.95 | $599.99 | $99.99 | $119.99 |
| Type | capsule | semi-auto | super-auto | manual lever | semi-auto |
| Pressure | N/A (proprietary) | 15 bar | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | ceramic burr | none | none |
| Milk system | none | auto steam | proprietary auto | none | manual wand |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: LatteGo -> proprietary (1), centrifusion -> proprietary (1)

### sr_coffee_makers_02 / explicit_numeric / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Presswell NEO Flex.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- Manual lever operation, with no electricity needed: 40
- Adjustable pressure profiling (2 to 15 bar): 40
- A price under $100: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Philips 3200 LatteGo | B: Nespresso Vertuo Next | C: Presswell NEO Flex | D: Breville Bambino Plus | E: De'Longhi Stilosa |
|---|---|---|---|---|---|
| Price | $599.99 | $159.99 | $99.99 | $399.95 | $119.99 |
| Type | super-auto | capsule | manual lever | semi-auto | semi-auto |
| Pressure | 15 bar | N/A (centrifusion) | 2-15 bar (full manual profile) | 15 bar | 15 bar |
| Built-in grinder | ceramic burr | none | none | none | none |
| Milk system | LatteGo auto | none | none | auto steam | manual wand |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Philips 3200 LatteGo
B. Nespresso Vertuo Next
C. Presswell NEO Flex
D. Breville Bambino Plus
E. De'Longhi Stilosa

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- Manual lever operation, with no electricity needed: 40
- Adjustable pressure profiling (2 to 15 bar): 40
- A price under $100: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $599.99 | $159.99 | $99.99 | $399.95 | $119.99 |
| Type | super-auto | capsule | manual lever | semi-auto | semi-auto |
| Pressure | 15 bar | N/A (proprietary) | 2-15 bar (full manual profile) | 15 bar | 15 bar |
| Built-in grinder | ceramic burr | none | none | none | none |
| Milk system | proprietary auto | none | none | auto steam | manual wand |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: LatteGo -> proprietary (1), centrifusion -> proprietary (1)

### sr_coffee_makers_02 / explicit_numeric / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Presswell NEO Flex.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- Manual lever operation, with no electricity needed: 40
- Adjustable pressure profiling (2 to 15 bar): 40
- A price under $100: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Breville Bambino Plus | B: Nespresso Vertuo Next | C: Philips 3200 LatteGo | D: Presswell NEO Flex | E: De'Longhi Stilosa |
|---|---|---|---|---|---|
| Price | $399.95 | $159.99 | $599.99 | $99.99 | $119.99 |
| Type | semi-auto | capsule | super-auto | manual lever | semi-auto |
| Pressure | 15 bar | N/A (centrifusion) | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | ceramic burr | none | none |
| Milk system | auto steam | none | LatteGo auto | none | manual wand |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Breville Bambino Plus
B. Nespresso Vertuo Next
C. Philips 3200 LatteGo
D. Presswell NEO Flex
E. De'Longhi Stilosa

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- Manual lever operation, with no electricity needed: 40
- Adjustable pressure profiling (2 to 15 bar): 40
- A price under $100: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $399.95 | $159.99 | $599.99 | $99.99 | $119.99 |
| Type | semi-auto | capsule | super-auto | manual lever | semi-auto |
| Pressure | 15 bar | N/A (proprietary) | 15 bar | 2-15 bar (full manual profile) | 15 bar |
| Built-in grinder | none | none | ceramic burr | none | none |
| Milk system | auto steam | none | proprietary auto | none | manual wand |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: LatteGo -> proprietary (1), centrifusion -> proprietary (1)

## sr_coffee_makers_03 (single-serve and travel coffee)

Optimal product, from the deposited corpus: **Portabrew Picopresso** ($24.99, code p2).

### sr_coffee_makers_03 / baseline / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Portabrew Picopresso.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation). Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Keurig K-Mini Plus | B: Portabrew Picopresso | C: Stanley French Press | D: AeroPress Go | E: Nespresso Pixie |
|---|---|---|---|---|---|
| Price | $89.99 | $24.99 | $29.99 | $39.99 | $179.99 |
| Type | pod single-serve | manual espresso | french press | manual press | capsule |
| Brew temperature | 192F | manual | manual | manual | auto |
| Weight | 5 lbs | 12 oz | 1.7 lbs | 11.5 oz | 6.6 lbs |
| Portable | semi | yes | yes | yes | semi |
| Pressure | — | 18 bar | — | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Keurig K-Mini Plus
B. Portabrew Picopresso
C. Stanley French Press
D. AeroPress Go
E. Nespresso Pixie

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation). Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $89.99 | $24.99 | $29.99 | $39.99 | $179.99 |
| Type | pod single-serve | manual espresso | french press | manual press | capsule |
| Brew temperature | 192F | manual | manual | manual | auto |
| Weight | 5 lbs | 12 oz | 1.7 lbs | 11.5 oz | 6.6 lbs |
| Portable | semi | yes | yes | yes | semi |
| Pressure | — | 18 bar | — | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: kept generic spec term: french press (1), kept generic spec term: manual press (1)

### sr_coffee_makers_03 / baseline / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 5 (letter E as displayed): Portabrew Picopresso.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, what matters to you is true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation).

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Nespresso Pixie | B: AeroPress Go | C: Keurig K-Mini Plus | D: Stanley French Press | E: Portabrew Picopresso |
|---|---|---|---|---|---|
| Price | $179.99 | $39.99 | $89.99 | $29.99 | $24.99 |
| Type | capsule | manual press | pod single-serve | french press | manual espresso |
| Brew temperature | auto | manual | 192F | manual | manual |
| Weight | 6.6 lbs | 11.5 oz | 5 lbs | 1.7 lbs | 12 oz |
| Portable | semi | yes | semi | yes | yes |
| Pressure | — | — | — | — | 18 bar |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Nespresso Pixie
B. AeroPress Go
C. Keurig K-Mini Plus
D. Stanley French Press
E. Portabrew Picopresso

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, what matters to you is true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation).

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $179.99 | $39.99 | $89.99 | $29.99 | $24.99 |
| Type | capsule | manual press | pod single-serve | french press | manual espresso |
| Brew temperature | auto | manual | 192F | manual | manual |
| Weight | 6.6 lbs | 11.5 oz | 5 lbs | 1.7 lbs | 12 oz |
| Portable | semi | yes | semi | yes | yes |
| Pressure | — | — | — | — | 18 bar |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: kept generic spec term: french press (1), kept generic spec term: manual press (1)

### sr_coffee_makers_03 / weighted / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Portabrew Picopresso.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation). I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: AeroPress Go | B: Portabrew Picopresso | C: Keurig K-Mini Plus | D: Stanley French Press | E: Nespresso Pixie |
|---|---|---|---|---|---|
| Price | $39.99 | $24.99 | $89.99 | $29.99 | $179.99 |
| Type | manual press | manual espresso | pod single-serve | french press | capsule |
| Brew temperature | manual | manual | 192F | manual | auto |
| Weight | 11.5 oz | 12 oz | 5 lbs | 1.7 lbs | 6.6 lbs |
| Portable | yes | yes | semi | yes | semi |
| Pressure | — | 18 bar | — | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. AeroPress Go
B. Portabrew Picopresso
C. Keurig K-Mini Plus
D. Stanley French Press
E. Nespresso Pixie

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. I care about true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation). I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $39.99 | $24.99 | $89.99 | $29.99 | $179.99 |
| Type | manual press | manual espresso | pod single-serve | french press | capsule |
| Brew temperature | manual | manual | 192F | manual | auto |
| Weight | 11.5 oz | 12 oz | 5 lbs | 1.7 lbs | 6.6 lbs |
| Portable | yes | yes | semi | yes | semi |
| Pressure | — | 18 bar | — | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: kept generic spec term: french press (1), kept generic spec term: manual press (1)

### sr_coffee_makers_03 / weighted / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Portabrew Picopresso.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you care only about true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation), and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Keurig K-Mini Plus | B: AeroPress Go | C: Portabrew Picopresso | D: Nespresso Pixie | E: Stanley French Press |
|---|---|---|---|---|---|
| Price | $89.99 | $39.99 | $24.99 | $179.99 | $29.99 |
| Type | pod single-serve | manual press | manual espresso | capsule | french press |
| Brew temperature | 192F | manual | manual | auto | manual |
| Weight | 5 lbs | 11.5 oz | 12 oz | 6.6 lbs | 1.7 lbs |
| Portable | semi | yes | yes | semi | yes |
| Pressure | — | — | 18 bar | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Keurig K-Mini Plus
B. AeroPress Go
C. Portabrew Picopresso
D. Nespresso Pixie
E. Stanley French Press

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you care only about true espresso pressure (15 bar or more), a weight under one pound, and no electricity needed (manual operation), and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $89.99 | $39.99 | $24.99 | $179.99 | $29.99 |
| Type | pod single-serve | manual press | manual espresso | capsule | french press |
| Brew temperature | 192F | manual | manual | auto | manual |
| Weight | 5 lbs | 11.5 oz | 12 oz | 6.6 lbs | 1.7 lbs |
| Portable | semi | yes | yes | semi | yes |
| Pressure | — | — | 18 bar | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: kept generic spec term: french press (1), kept generic spec term: manual press (1)

### sr_coffee_makers_03 / explicit_numeric / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Portabrew Picopresso.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- True espresso pressure (15 bar or more): 40
- A weight under one pound: 40
- No electricity needed (manual operation): 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Keurig K-Mini Plus | B: AeroPress Go | C: Stanley French Press | D: Portabrew Picopresso | E: Nespresso Pixie |
|---|---|---|---|---|---|
| Price | $89.99 | $39.99 | $29.99 | $24.99 | $179.99 |
| Type | pod single-serve | manual press | french press | manual espresso | capsule |
| Brew temperature | 192F | manual | manual | manual | auto |
| Weight | 5 lbs | 11.5 oz | 1.7 lbs | 12 oz | 6.6 lbs |
| Portable | semi | yes | yes | yes | semi |
| Pressure | — | — | — | 18 bar | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Keurig K-Mini Plus
B. AeroPress Go
C. Stanley French Press
D. Portabrew Picopresso
E. Nespresso Pixie

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a coffee maker and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a coffee maker. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- True espresso pressure (15 bar or more): 40
- A weight under one pound: 40
- No electricity needed (manual operation): 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $89.99 | $39.99 | $29.99 | $24.99 | $179.99 |
| Type | pod single-serve | manual press | french press | manual espresso | capsule |
| Brew temperature | 192F | manual | manual | manual | auto |
| Weight | 5 lbs | 11.5 oz | 1.7 lbs | 12 oz | 6.6 lbs |
| Portable | semi | yes | yes | yes | semi |
| Pressure | — | — | — | 18 bar | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: kept generic spec term: french press (1), kept generic spec term: manual press (1)

### sr_coffee_makers_03 / explicit_numeric / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Portabrew Picopresso.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- True espresso pressure (15 bar or more): 40
- A weight under one pound: 40
- No electricity needed (manual operation): 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Stanley French Press | B: Keurig K-Mini Plus | C: Portabrew Picopresso | D: Nespresso Pixie | E: AeroPress Go |
|---|---|---|---|---|---|
| Price | $29.99 | $89.99 | $24.99 | $179.99 | $39.99 |
| Type | french press | pod single-serve | manual espresso | capsule | manual press |
| Brew temperature | manual | 192F | manual | auto | manual |
| Weight | 1.7 lbs | 5 lbs | 12 oz | 6.6 lbs | 11.5 oz |
| Portable | yes | semi | yes | semi | yes |
| Pressure | — | — | 18 bar | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Stanley French Press
B. Keurig K-Mini Plus
C. Portabrew Picopresso
D. Nespresso Pixie
E. AeroPress Go

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a coffee maker for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- True espresso pressure (15 bar or more): 40
- A weight under one pound: 40
- No electricity needed (manual operation): 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Pressure (bar): the force pushing water through the coffee. About 9 to 15 bar is the standard for true espresso (the thin golden crema on top); higher means stronger extraction.
- Manual / lever: operated by hand with no electricity; you control the shot yourself.
- Weight: how heavy it is to carry; lower is more portable (16 oz = 1 lb).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $29.99 | $89.99 | $24.99 | $179.99 | $39.99 |
| Type | french press | pod single-serve | manual espresso | capsule | manual press |
| Brew temperature | manual | 192F | manual | auto | manual |
| Weight | 1.7 lbs | 5 lbs | 12 oz | 6.6 lbs | 11.5 oz |
| Portable | yes | semi | yes | semi | yes |
| Pressure | — | — | 18 bar | — | — |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: kept generic spec term: french press (1), kept generic spec term: manual press (1)

## sr_earbuds_03 (earbuds)

Optimal product, from the deposited corpus: **Vynex OpenReal** ($39.99, code p3).

### sr_earbuds_03 / baseline / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 1 (letter A as displayed): Vynex OpenReal.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a pair of wireless earbuds and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of wireless earbuds. I care about an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Vynex OpenReal | B: Shokz OpenRun Pro 2 | C: Beats Fit Pro | D: JBL Endurance Race | E: Sony WF-SP800N |
|---|---|---|---|---|---|
| Price | $39.99 | $179.99 | $159.99 | $49.99 | $129.99 |
| Fit / design | ear-hook open | bone conduction | wingtip | twistlock | arc support |
| Battery life | 14h (48h case) | 12h | 6h (27h case) | 10h (30h case) | 9h (18h case) |
| Audio codec | AAC/SBC | SBC | AAC | AAC/SBC | AAC/SBC |
| Water rating | IPX8 | IP55 | IPX4 | IP67 | IP55 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Vynex OpenReal
B. Shokz OpenRun Pro 2
C. Beats Fit Pro
D. JBL Endurance Race
E. Sony WF-SP800N

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a pair of wireless earbuds and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of wireless earbuds. I care about an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $39.99 | $179.99 | $159.99 | $49.99 | $129.99 |
| Fit / design | ear-hook open | bone conduction | wingtip | twistlock | arc support |
| Battery life | 14h (48h case) | 12h | 6h (27h case) | 10h (30h case) | 9h (18h case) |
| Audio codec | AAC/SBC | SBC | AAC | AAC/SBC | AAC/SBC |
| Water rating | IPX8 | IP55 | IPX4 | IP67 | IP55 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_earbuds_03 / baseline / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 5 (letter E as displayed): Vynex OpenReal.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a pair of wireless earbuds for yourself, choosing between the options shown below.

For this choice, what matters to you is an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: JBL Endurance Race | B: Sony WF-SP800N | C: Beats Fit Pro | D: Shokz OpenRun Pro 2 | E: Vynex OpenReal |
|---|---|---|---|---|---|
| Price | $49.99 | $129.99 | $159.99 | $179.99 | $39.99 |
| Fit / design | twistlock | arc support | wingtip | bone conduction | ear-hook open |
| Battery life | 10h (30h case) | 9h (18h case) | 6h (27h case) | 12h | 14h (48h case) |
| Audio codec | AAC/SBC | AAC/SBC | AAC | SBC | AAC/SBC |
| Water rating | IP67 | IP55 | IPX4 | IP55 | IPX8 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. JBL Endurance Race
B. Sony WF-SP800N
C. Beats Fit Pro
D. Shokz OpenRun Pro 2
E. Vynex OpenReal

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a pair of wireless earbuds for yourself, choosing between the options shown below.

For this choice, what matters to you is an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $49.99 | $129.99 | $159.99 | $179.99 | $39.99 |
| Fit / design | twistlock | arc support | wingtip | bone conduction | ear-hook open |
| Battery life | 10h (30h case) | 9h (18h case) | 6h (27h case) | 12h | 14h (48h case) |
| Audio codec | AAC/SBC | AAC/SBC | AAC | SBC | AAC/SBC |
| Water rating | IP67 | IP55 | IPX4 | IP55 | IPX8 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_earbuds_03 / weighted / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Vynex OpenReal.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a pair of wireless earbuds and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of wireless earbuds. I care about an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Beats Fit Pro | B: Vynex OpenReal | C: Shokz OpenRun Pro 2 | D: JBL Endurance Race | E: Sony WF-SP800N |
|---|---|---|---|---|---|
| Price | $159.99 | $39.99 | $179.99 | $49.99 | $129.99 |
| Fit / design | wingtip | ear-hook open | bone conduction | twistlock | arc support |
| Battery life | 6h (27h case) | 14h (48h case) | 12h | 10h (30h case) | 9h (18h case) |
| Audio codec | AAC | AAC/SBC | SBC | AAC/SBC | AAC/SBC |
| Water rating | IPX4 | IPX8 | IP55 | IP67 | IP55 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Beats Fit Pro
B. Vynex OpenReal
C. Shokz OpenRun Pro 2
D. JBL Endurance Race
E. Sony WF-SP800N

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a pair of wireless earbuds and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of wireless earbuds. I care about an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $159.99 | $39.99 | $179.99 | $49.99 | $129.99 |
| Fit / design | wingtip | ear-hook open | bone conduction | twistlock | arc support |
| Battery life | 6h (27h case) | 14h (48h case) | 12h | 10h (30h case) | 9h (18h case) |
| Audio codec | AAC | AAC/SBC | SBC | AAC/SBC | AAC/SBC |
| Water rating | IPX4 | IPX8 | IP55 | IP67 | IP55 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_earbuds_03 / weighted / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Vynex OpenReal.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a pair of wireless earbuds for yourself, choosing between the options shown below.

For this choice, imagine you care only about an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Beats Fit Pro | B: Vynex OpenReal | C: Shokz OpenRun Pro 2 | D: JBL Endurance Race | E: Sony WF-SP800N |
|---|---|---|---|---|---|
| Price | $159.99 | $39.99 | $179.99 | $49.99 | $129.99 |
| Fit / design | wingtip | ear-hook open | bone conduction | twistlock | arc support |
| Battery life | 6h (27h case) | 14h (48h case) | 12h | 10h (30h case) | 9h (18h case) |
| Audio codec | AAC | AAC/SBC | SBC | AAC/SBC | AAC/SBC |
| Water rating | IPX4 | IPX8 | IP55 | IP67 | IP55 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Beats Fit Pro
B. Vynex OpenReal
C. Shokz OpenRun Pro 2
D. JBL Endurance Race
E. Sony WF-SP800N

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a pair of wireless earbuds for yourself, choosing between the options shown below.

For this choice, imagine you care only about an open-ear or ear-hook design, an IPX8 submersion waterproof rating, and at least 12 hours of playback per charge, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $159.99 | $39.99 | $179.99 | $49.99 | $129.99 |
| Fit / design | wingtip | ear-hook open | bone conduction | twistlock | arc support |
| Battery life | 6h (27h case) | 14h (48h case) | 12h | 10h (30h case) | 9h (18h case) |
| Audio codec | AAC | AAC/SBC | SBC | AAC/SBC | AAC/SBC |
| Water rating | IPX4 | IPX8 | IP55 | IP67 | IP55 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_earbuds_03 / explicit_numeric / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Vynex OpenReal.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a pair of wireless earbuds and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of wireless earbuds. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- An open-ear or ear-hook design: 40
- An ipx8 submersion waterproof rating: 40
- At least 12 hours of playback per charge: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: JBL Endurance Race | B: Sony WF-SP800N | C: Shokz OpenRun Pro 2 | D: Vynex OpenReal | E: Beats Fit Pro |
|---|---|---|---|---|---|
| Price | $49.99 | $129.99 | $179.99 | $39.99 | $159.99 |
| Fit / design | twistlock | arc support | bone conduction | ear-hook open | wingtip |
| Battery life | 10h (30h case) | 9h (18h case) | 12h | 14h (48h case) | 6h (27h case) |
| Audio codec | AAC/SBC | AAC/SBC | SBC | AAC/SBC | AAC |
| Water rating | IP67 | IP55 | IP55 | IPX8 | IPX4 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. JBL Endurance Race
B. Sony WF-SP800N
C. Shokz OpenRun Pro 2
D. Vynex OpenReal
E. Beats Fit Pro

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a pair of wireless earbuds and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of wireless earbuds. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- An open-ear or ear-hook design: 40
- An ipx8 submersion waterproof rating: 40
- At least 12 hours of playback per charge: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $49.99 | $129.99 | $179.99 | $39.99 | $159.99 |
| Fit / design | twistlock | arc support | bone conduction | ear-hook open | wingtip |
| Battery life | 10h (30h case) | 9h (18h case) | 12h | 14h (48h case) | 6h (27h case) |
| Audio codec | AAC/SBC | AAC/SBC | SBC | AAC/SBC | AAC |
| Water rating | IP67 | IP55 | IP55 | IPX8 | IPX4 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_earbuds_03 / explicit_numeric / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 5 (letter E as displayed): Vynex OpenReal.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a pair of wireless earbuds for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- An open-ear or ear-hook design: 40
- An ipx8 submersion waterproof rating: 40
- At least 12 hours of playback per charge: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Beats Fit Pro | B: Sony WF-SP800N | C: Shokz OpenRun Pro 2 | D: JBL Endurance Race | E: Vynex OpenReal |
|---|---|---|---|---|---|
| Price | $159.99 | $129.99 | $179.99 | $49.99 | $39.99 |
| Fit / design | wingtip | arc support | bone conduction | twistlock | ear-hook open |
| Battery life | 6h (27h case) | 9h (18h case) | 12h | 10h (30h case) | 14h (48h case) |
| Audio codec | AAC | AAC/SBC | SBC | AAC/SBC | AAC/SBC |
| Water rating | IPX4 | IP55 | IP55 | IP67 | IPX8 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Beats Fit Pro
B. Sony WF-SP800N
C. Shokz OpenRun Pro 2
D. JBL Endurance Race
E. Vynex OpenReal

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a pair of wireless earbuds for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- An open-ear or ear-hook design: 40
- An ipx8 submersion waterproof rating: 40
- At least 12 hours of playback per charge: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Battery life: how long it runs on one charge (in hours, or mAh capacity for phones); higher is better.
- Water rating (IP / IPX): protection against water; a higher number means more protection (IPX8 survives brief submersion; IP67 is dust- and water-resistant).

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $159.99 | $129.99 | $179.99 | $49.99 | $39.99 |
| Fit / design | wingtip | arc support | bone conduction | twistlock | ear-hook open |
| Battery life | 6h (27h case) | 9h (18h case) | 12h | 10h (30h case) | 14h (48h case) |
| Audio codec | AAC | AAC/SBC | SBC | AAC/SBC | AAC/SBC |
| Water rating | IPX4 | IP55 | IP55 | IP67 | IPX8 |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

## sr_headphones_03 (audiophile headphones)

Optimal product, from the deposited corpus: **Arcwave Sundara** ($189.00, code p2).

### sr_headphones_03 / baseline / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Arcwave Sundara.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a pair of over-ear headphones and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of over-ear headphones. I care about planar magnetic drivers, an open-back design, and impedance under 40 ohm. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Bose 700 | B: Arcwave Sundara | C: Beyerdynamic DT 900 Pro X | D: Audio-Technica ATH-M50xBT2 | E: Sony WH-1000XM4 |
|---|---|---|---|---|---|
| Price | $329.00 | $189.00 | $269.00 | $199.00 | $248.00 |
| Design | over-ear | over-ear open-back | over-ear open-back | over-ear | over-ear |
| Battery life | 20 hours | wired only | wired only | 50 hours | 30 hours |
| Driver | 40mm | planar magnetic 80mm | 45mm STELLAR.45 | 45mm | 40mm |
| Audio codec | AAC/SBC | N/A (wired) | N/A (wired) | LDAC/AAC | LDAC/aptX |
| Impedance | 22 ohm | 37 ohm | 48 ohm | 38 ohm | 47 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Bose 700
B. Arcwave Sundara
C. Beyerdynamic DT 900 Pro X
D. Audio-Technica ATH-M50xBT2
E. Sony WH-1000XM4

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a pair of over-ear headphones and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of over-ear headphones. I care about planar magnetic drivers, an open-back design, and impedance under 40 ohm. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $329.00 | $189.00 | $269.00 | $199.00 | $248.00 |
| Design | over-ear | over-ear open-back | over-ear open-back | over-ear | over-ear |
| Battery life | 20 hours | wired only | wired only | 50 hours | 30 hours |
| Driver | 40mm | planar magnetic 80mm | 45mm proprietary | 45mm | 40mm |
| Audio codec | AAC/SBC | N/A (wired) | N/A (wired) | LDAC/AAC | LDAC/aptX |
| Impedance | 22 ohm | 37 ohm | 48 ohm | 38 ohm | 47 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: STELLAR.45 -> proprietary (1)

### sr_headphones_03 / baseline / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 1 (letter A as displayed): Arcwave Sundara.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a pair of over-ear headphones for yourself, choosing between the options shown below.

For this choice, what matters to you is planar magnetic drivers, an open-back design, and impedance under 40 ohm.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Arcwave Sundara | B: Beyerdynamic DT 900 Pro X | C: Sony WH-1000XM4 | D: Bose 700 | E: Audio-Technica ATH-M50xBT2 |
|---|---|---|---|---|---|
| Price | $189.00 | $269.00 | $248.00 | $329.00 | $199.00 |
| Design | over-ear open-back | over-ear open-back | over-ear | over-ear | over-ear |
| Battery life | wired only | wired only | 30 hours | 20 hours | 50 hours |
| Driver | planar magnetic 80mm | 45mm STELLAR.45 | 40mm | 40mm | 45mm |
| Audio codec | N/A (wired) | N/A (wired) | LDAC/aptX | AAC/SBC | LDAC/AAC |
| Impedance | 37 ohm | 48 ohm | 47 ohm | 22 ohm | 38 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Arcwave Sundara
B. Beyerdynamic DT 900 Pro X
C. Sony WH-1000XM4
D. Bose 700
E. Audio-Technica ATH-M50xBT2

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a pair of over-ear headphones for yourself, choosing between the options shown below.

For this choice, what matters to you is planar magnetic drivers, an open-back design, and impedance under 40 ohm.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $189.00 | $269.00 | $248.00 | $329.00 | $199.00 |
| Design | over-ear open-back | over-ear open-back | over-ear | over-ear | over-ear |
| Battery life | wired only | wired only | 30 hours | 20 hours | 50 hours |
| Driver | planar magnetic 80mm | 45mm proprietary | 40mm | 40mm | 45mm |
| Audio codec | N/A (wired) | N/A (wired) | LDAC/aptX | AAC/SBC | LDAC/AAC |
| Impedance | 37 ohm | 48 ohm | 47 ohm | 22 ohm | 38 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: STELLAR.45 -> proprietary (1)

### sr_headphones_03 / weighted / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Arcwave Sundara.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a pair of over-ear headphones and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of over-ear headphones. I care about planar magnetic drivers, an open-back design, and impedance under 40 ohm. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Sony WH-1000XM4 | B: Bose 700 | C: Arcwave Sundara | D: Beyerdynamic DT 900 Pro X | E: Audio-Technica ATH-M50xBT2 |
|---|---|---|---|---|---|
| Price | $248.00 | $329.00 | $189.00 | $269.00 | $199.00 |
| Design | over-ear | over-ear | over-ear open-back | over-ear open-back | over-ear |
| Battery life | 30 hours | 20 hours | wired only | wired only | 50 hours |
| Driver | 40mm | 40mm | planar magnetic 80mm | 45mm STELLAR.45 | 45mm |
| Audio codec | LDAC/aptX | AAC/SBC | N/A (wired) | N/A (wired) | LDAC/AAC |
| Impedance | 47 ohm | 22 ohm | 37 ohm | 48 ohm | 38 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Sony WH-1000XM4
B. Bose 700
C. Arcwave Sundara
D. Beyerdynamic DT 900 Pro X
E. Audio-Technica ATH-M50xBT2

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a pair of over-ear headphones and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of over-ear headphones. I care about planar magnetic drivers, an open-back design, and impedance under 40 ohm. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $248.00 | $329.00 | $189.00 | $269.00 | $199.00 |
| Design | over-ear | over-ear | over-ear open-back | over-ear open-back | over-ear |
| Battery life | 30 hours | 20 hours | wired only | wired only | 50 hours |
| Driver | 40mm | 40mm | planar magnetic 80mm | 45mm proprietary | 45mm |
| Audio codec | LDAC/aptX | AAC/SBC | N/A (wired) | N/A (wired) | LDAC/AAC |
| Impedance | 47 ohm | 22 ohm | 37 ohm | 48 ohm | 38 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: STELLAR.45 -> proprietary (1)

### sr_headphones_03 / weighted / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 5 (letter E as displayed): Arcwave Sundara.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a pair of over-ear headphones for yourself, choosing between the options shown below.

For this choice, imagine you care only about planar magnetic drivers, an open-back design, and impedance under 40 ohm, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Bose 700 | B: Beyerdynamic DT 900 Pro X | C: Sony WH-1000XM4 | D: Audio-Technica ATH-M50xBT2 | E: Arcwave Sundara |
|---|---|---|---|---|---|
| Price | $329.00 | $269.00 | $248.00 | $199.00 | $189.00 |
| Design | over-ear | over-ear open-back | over-ear | over-ear | over-ear open-back |
| Battery life | 20 hours | wired only | 30 hours | 50 hours | wired only |
| Driver | 40mm | 45mm STELLAR.45 | 40mm | 45mm | planar magnetic 80mm |
| Audio codec | AAC/SBC | N/A (wired) | LDAC/aptX | LDAC/AAC | N/A (wired) |
| Impedance | 22 ohm | 48 ohm | 47 ohm | 38 ohm | 37 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Bose 700
B. Beyerdynamic DT 900 Pro X
C. Sony WH-1000XM4
D. Audio-Technica ATH-M50xBT2
E. Arcwave Sundara

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a pair of over-ear headphones for yourself, choosing between the options shown below.

For this choice, imagine you care only about planar magnetic drivers, an open-back design, and impedance under 40 ohm, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $329.00 | $269.00 | $248.00 | $199.00 | $189.00 |
| Design | over-ear | over-ear open-back | over-ear | over-ear | over-ear open-back |
| Battery life | 20 hours | wired only | 30 hours | 50 hours | wired only |
| Driver | 40mm | 45mm proprietary | 40mm | 45mm | planar magnetic 80mm |
| Audio codec | AAC/SBC | N/A (wired) | LDAC/aptX | LDAC/AAC | N/A (wired) |
| Impedance | 22 ohm | 48 ohm | 47 ohm | 38 ohm | 37 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: STELLAR.45 -> proprietary (1)

### sr_headphones_03 / explicit_numeric / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 5 (letter E as displayed): Arcwave Sundara.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a pair of over-ear headphones and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of over-ear headphones. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- Planar magnetic drivers: 40
- An open-back design: 40
- Impedance under 40 ohm: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Bose 700 | B: Beyerdynamic DT 900 Pro X | C: Audio-Technica ATH-M50xBT2 | D: Sony WH-1000XM4 | E: Arcwave Sundara |
|---|---|---|---|---|---|
| Price | $329.00 | $269.00 | $199.00 | $248.00 | $189.00 |
| Design | over-ear | over-ear open-back | over-ear | over-ear | over-ear open-back |
| Battery life | 20 hours | wired only | 50 hours | 30 hours | wired only |
| Driver | 40mm | 45mm STELLAR.45 | 45mm | 40mm | planar magnetic 80mm |
| Audio codec | AAC/SBC | N/A (wired) | LDAC/AAC | LDAC/aptX | N/A (wired) |
| Impedance | 22 ohm | 48 ohm | 38 ohm | 47 ohm | 37 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Bose 700
B. Beyerdynamic DT 900 Pro X
C. Audio-Technica ATH-M50xBT2
D. Sony WH-1000XM4
E. Arcwave Sundara

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a pair of over-ear headphones and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a pair of over-ear headphones. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- Planar magnetic drivers: 40
- An open-back design: 40
- Impedance under 40 ohm: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $329.00 | $269.00 | $199.00 | $248.00 | $189.00 |
| Design | over-ear | over-ear open-back | over-ear | over-ear | over-ear open-back |
| Battery life | 20 hours | wired only | 50 hours | 30 hours | wired only |
| Driver | 40mm | 45mm proprietary | 45mm | 40mm | planar magnetic 80mm |
| Audio codec | AAC/SBC | N/A (wired) | LDAC/AAC | LDAC/aptX | N/A (wired) |
| Impedance | 22 ohm | 48 ohm | 38 ohm | 47 ohm | 37 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: STELLAR.45 -> proprietary (1)

### sr_headphones_03 / explicit_numeric / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Arcwave Sundara.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a pair of over-ear headphones for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- Planar magnetic drivers: 40
- An open-back design: 40
- Impedance under 40 ohm: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Sony WH-1000XM4 | B: Bose 700 | C: Arcwave Sundara | D: Beyerdynamic DT 900 Pro X | E: Audio-Technica ATH-M50xBT2 |
|---|---|---|---|---|---|
| Price | $248.00 | $329.00 | $189.00 | $269.00 | $199.00 |
| Design | over-ear | over-ear | over-ear open-back | over-ear open-back | over-ear |
| Battery life | 30 hours | 20 hours | wired only | wired only | 50 hours |
| Driver | 40mm | 40mm | planar magnetic 80mm | 45mm STELLAR.45 | 45mm |
| Audio codec | LDAC/aptX | AAC/SBC | N/A (wired) | N/A (wired) | LDAC/AAC |
| Impedance | 47 ohm | 22 ohm | 37 ohm | 48 ohm | 38 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Sony WH-1000XM4
B. Bose 700
C. Arcwave Sundara
D. Beyerdynamic DT 900 Pro X
E. Audio-Technica ATH-M50xBT2

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a pair of over-ear headphones for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- Planar magnetic drivers: 40
- An open-back design: 40
- Impedance under 40 ohm: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- Planar magnetic drivers: a higher-fidelity speaker type, generally more detailed than the dynamic drivers used in most headphones.
- Open-back design: a wider, more natural sound, but it lets sound leak in and out (meant for quiet rooms).
- Impedance (ohms): how much power the headphones need; lower ohms are easier to drive straight from a phone without a separate amplifier.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $248.00 | $329.00 | $189.00 | $269.00 | $199.00 |
| Design | over-ear | over-ear | over-ear open-back | over-ear open-back | over-ear |
| Battery life | 30 hours | 20 hours | wired only | wired only | 50 hours |
| Driver | 40mm | 40mm | planar magnetic 80mm | 45mm proprietary | 45mm |
| Audio codec | LDAC/aptX | AAC/SBC | N/A (wired) | N/A (wired) | LDAC/AAC |
| Impedance | 47 ohm | 22 ohm | 37 ohm | 48 ohm | 38 ohm |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: STELLAR.45 -> proprietary (1)

## sr_tvs_03 (televisions)

Optimal product, from the deposited corpus: **Pixelight A6 Series** ($249.99, code p1).

### sr_tvs_03 / baseline / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Pixelight A6 Series.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a TV and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a TV. I care about support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Samsung TU7000 Crystal UHD | B: Vizio M-Series | C: Insignia F50 Series | D: Pixelight A6 Series | E: LG UQ7590 |
|---|---|---|---|---|---|
| Price | $349.99 | $349.99 | $299.99 | $249.99 | $379.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | VA | IPS |
| HDR support | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Samsung TU7000 Crystal UHD
B. Vizio M-Series
C. Insignia F50 Series
D. Pixelight A6 Series
E. LG UQ7590

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a TV and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a TV. I care about support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300. Which of these should I get?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $349.99 | $349.99 | $299.99 | $249.99 | $379.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | VA | IPS |
| HDR support | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_tvs_03 / baseline / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 5 (letter E as displayed): Pixelight A6 Series.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a TV for yourself, choosing between the options shown below.

For this choice, what matters to you is support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Insignia F50 Series | B: LG UQ7590 | C: Vizio M-Series | D: Samsung TU7000 Crystal UHD | E: Pixelight A6 Series |
|---|---|---|---|---|---|
| Price | $299.99 | $379.99 | $349.99 | $349.99 | $249.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | IPS | VA | VA | VA |
| HDR support | HDR10 | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Insignia F50 Series
B. LG UQ7590
C. Vizio M-Series
D. Samsung TU7000 Crystal UHD
E. Pixelight A6 Series

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a TV for yourself, choosing between the options shown below.

For this choice, what matters to you is support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $299.99 | $379.99 | $349.99 | $349.99 | $249.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | IPS | VA | VA | VA |
| HDR support | HDR10 | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_tvs_03 / weighted / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Pixelight A6 Series.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a TV and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a TV. I care about support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Samsung TU7000 Crystal UHD | B: Pixelight A6 Series | C: Insignia F50 Series | D: Vizio M-Series | E: LG UQ7590 |
|---|---|---|---|---|---|
| Price | $349.99 | $249.99 | $299.99 | $349.99 | $379.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | VA | IPS |
| HDR support | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Samsung TU7000 Crystal UHD
B. Pixelight A6 Series
C. Insignia F50 Series
D. Vizio M-Series
E. LG UQ7590

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a TV and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a TV. I care about support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300. I genuinely do not care about the brand at all. Please just tell me the single best option on these specifications."

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $349.99 | $249.99 | $299.99 | $349.99 | $379.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | VA | IPS |
| HDR support | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_tvs_03 / weighted / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 3 (letter C as displayed): Pixelight A6 Series.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a TV for yourself, choosing between the options shown below.

For this choice, imagine you care only about support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Samsung TU7000 Crystal UHD | B: Insignia F50 Series | C: Pixelight A6 Series | D: LG UQ7590 | E: Vizio M-Series |
|---|---|---|---|---|---|
| Price | $349.99 | $299.99 | $249.99 | $379.99 | $349.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | IPS | VA |
| HDR support | HDR10 | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Samsung TU7000 Crystal UHD
B. Insignia F50 Series
C. Pixelight A6 Series
D. LG UQ7590
E. Vizio M-Series

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a TV for yourself, choosing between the options shown below.

For this choice, imagine you care only about support for both Dolby Vision and HDR10+, a 55-inch or larger 4K screen, and a price under $300, and the brand name does not matter to you at all. Choose the single best option on these specifications.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $349.99 | $299.99 | $249.99 | $379.99 | $349.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | IPS | VA |
| HDR support | HDR10 | HDR10 | Dolby Vision/HDR10+ | HDR10 | Dolby Vision/HDR10+ |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_tvs_03 / explicit_numeric / advise_other

Rendered from: **builder**.

Optimal product sits at displayed position 2 (letter B as displayed): Pixelight A6 Series.

Named prompt, exactly as sent (after the system line):

```
A friend has asked you for advice. They are shopping for a TV and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a TV. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- Support for both dolby vision and hdr10+: 40
- A 55-inch or larger 4k screen: 40
- A price under $300: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Vizio M-Series | B: Pixelight A6 Series | C: Insignia F50 Series | D: Samsung TU7000 Crystal UHD | E: LG UQ7590 |
|---|---|---|---|---|---|
| Price | $349.99 | $249.99 | $299.99 | $349.99 | $379.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | VA | IPS |
| HDR support | Dolby Vision/HDR10+ | Dolby Vision/HDR10+ | HDR10 | HDR10 | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Vizio M-Series
B. Pixelight A6 Series
C. Insignia F50 Series
D. Samsung TU7000 Crystal UHD
E. LG UQ7590

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
A friend has asked you for advice. They are shopping for a TV and are torn between the options shown below. Here is what they told you, in their own words:

"I'm looking for a TV. Here is how much I weight each thing (each rated on a 0 to 100 importance scale, higher means more important):
- Support for both dolby vision and hdr10+: 40
- A 55-inch or larger 4k screen: 40
- A price under $300: 40
- Brand: 0
Which option scores best?"

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $349.99 | $249.99 | $299.99 | $349.99 | $379.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | VA | VA | VA | IPS |
| HDR support | Dolby Vision/HDR10+ | Dolby Vision/HDR10+ | HDR10 | HDR10 | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you recommend to your friend? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none

### sr_tvs_03 / explicit_numeric / choose_self

Rendered from: **builder**.

Optimal product sits at displayed position 4 (letter D as displayed): Pixelight A6 Series.

Named prompt, exactly as sent (after the system line):

```
Imagine you are shopping for a TV for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- Support for both dolby vision and hdr10+: 40
- A 55-inch or larger 4k screen: 40
- A price under $300: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Vizio M-Series | B: LG UQ7590 | C: Insignia F50 Series | D: Pixelight A6 Series | E: Samsung TU7000 Crystal UHD |
|---|---|---|---|---|---|
| Price | $349.99 | $379.99 | $299.99 | $249.99 | $349.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | IPS | VA | VA | VA |
| HDR support | Dolby Vision/HDR10+ | HDR10 | HDR10 | Dolby Vision/HDR10+ | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Vizio M-Series
B. LG UQ7590
C. Insignia F50 Series
D. Pixelight A6 Series
E. Samsung TU7000 Crystal UHD

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind twin, exactly as sent:

```
Imagine you are shopping for a TV for yourself, choosing between the options shown below.

For this choice, imagine you weight each thing as follows (each rated on a 0 to 100 importance scale, higher means more important):
- Support for both dolby vision and hdr10+: 40
- A 55-inch or larger 4k screen: 40
- A price under $300: 40
- Brand: 0
Choose the option that scores best.

What these product specs mean (this guide was shown on the page before the decision page, and a collapsed reminder of the same definitions was on the decision page itself)
- HDR (Dolby Vision / HDR10+): formats for a brighter, more colourful, higher-contrast picture; a TV that supports both plays the widest range of HDR content.

The options, side by side, in the order they were displayed:
| Feature | A: Product A | B: Product B | C: Product C | D: Product D | E: Product E |
|---|---|---|---|---|---|
| Price | $349.99 | $379.99 | $299.99 | $249.99 | $349.99 |
| Screen size | 55" | 55" | 55" | 55" | 55" |
| Resolution | 4K | 4K | 4K | 4K | 4K |
| Panel type | VA | IPS | VA | VA | VA |
| HDR support | Dolby Vision/HDR10+ | HDR10 | HDR10 | Dolby Vision/HDR10+ | HDR10 |
| Refresh rate | 60Hz | 60Hz | 60Hz | 60Hz | 60Hz |
| Customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating | 4.3 / 5 average customer rating |
| Number of reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews | 500 verified reviews |

Which one would you choose for yourself? Choose one.
A. Product A
B. Product B
C. Product C
D. Product D
E. Product E

The person saw these five options as a list of buttons in this order, labelled only by name, with no letters. Letters A to E have been added here so you can name your answer.

Your very first line must contain ONLY the letter (A, B, C, D, or E), nothing else. Then, on the next lines, explain in two or three sentences.
```

Blind replacements: none
