# Survey instruments

Qualtrics survey definitions (`.qsf`) of the consumer studies. Each file can be imported into a Qualtrics
account (Create new project, From a file) to recreate the survey with its questions, flow, randomisation,
embedded data and JavaScript.

| File | Study |
|---|---|
| `study1a.qsf` | Study 1A (coffee makers) |
| `study1b.qsf` | Study 1B (wireless earbuds) |
| `study2.qsf` | Study 2 (warning and product comparison) |
| `study3_chatbot_template.qsf` | Study 3 template with the chat widget, embedded-data fields and randomisation |

The administered Study 3 survey is `../human_studies/study3-chatbot/survey.qsf`, and the human-advisor study's
survey is `../human_studies/study4-advisor-benchmark/instrument.qsf`. The Study 3 chatbot also needs the chat
widget and the Cloudflare Worker in `../human_studies/study3-chatbot/`; `DEPLOY.md` there explains the setup.
