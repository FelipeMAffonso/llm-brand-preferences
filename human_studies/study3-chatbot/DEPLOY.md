# Study 3 chatbot: how to deploy it

The Study 3 chatbot runs as a small Cloudflare Worker that forwards the conversation to the Anthropic API, and
a chat widget embedded in a Qualtrics question. This guide sets both up.

## Prerequisites

- Node.js
- A Cloudflare account (the free tier works)
- An Anthropic API key
- A Qualtrics account with survey-builder access

## Step 1: Deploy the worker

```bash
cd human_studies/study3-chatbot/worker

# Install wrangler (if not already installed)
npm install -g wrangler

# Log in to Cloudflare (first time only)
npx wrangler login

# Store the Anthropic API key as a secret
npx wrangler secret put ANTHROPIC_API_KEY

# Optional: create a KV namespace for conversation logs and paste its id into wrangler.toml
npx wrangler kv namespace create STUDY3_LOGS

# Deploy
npx wrangler deploy
```

After deployment the worker has a URL of the form `https://study3-chatbot.<your-subdomain>.workers.dev`.
Check it with:

```bash
curl https://study3-chatbot.<your-subdomain>.workers.dev/health
```

which should return:

```json
{"ok": true, "service": "study3-chatbot", "hasAnthropicKey": true}
```

## Step 2: Point the Qualtrics JavaScript at the worker

In `QUALTRICS_CHATBOT.js`, set the `URL` variable to the worker's `/chat` route.

## Step 3: Build the Qualtrics survey

Either import `survey.qsf` (the administered Study 3 instrument) or `../../qualtrics/study3_chatbot_template.qsf`,
or build the survey from scratch:

1. Create a new survey.
2. Add the consent question (multiple choice).
3. Add a descriptive-text question for the chatbot: paste `QUALTRICS_HTML.html` into its HTML view and
   `QUALTRICS_CHATBOT.js` into its JavaScript editor.
4. Add the product choice question (multiple choice); the choices are piped from embedded data.
5. Add the choice-reason question (text entry).
6. Add the demographic questions.

### Embedded data fields (set in the survey flow before the chat block)

Initialise all of these with empty values.

Conversation:
- study3_session_id
- study3_conversation_complete
- study3_total_turns

Assortment (set by the chatbot JavaScript):
- study3_assortment (full JSON)
- study3_category
- study3_recommended
- study3_optimal

Products (set by the chatbot JavaScript, for piping into the choice question):
- product_1 to product_7

Conversation transcript:
- msg_1 to msg_20
- response_1 to response_20

## Step 4: Test

1. Preview the survey in Qualtrics.
2. Type a shopping request (for example, "I need running shoes for trail running").
3. Answer the clarifying question.
4. Wait for "Searching products..." (a few seconds).
5. Check that the product table appears and the assistant makes a recommendation.
6. Ask a follow-up question ("What about the cheaper one?").
7. Click "Ready to choose" and check that the choice page shows the generated products.
8. Complete the survey, export the responses and check that the embedded data are filled in.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "AI service error" | Check that ANTHROPIC_API_KEY is set: `npx wrangler secret list` |
| Chat does not load | Check the browser console for CORS errors, and the URL in the JavaScript. |
| "Searching products..." hangs | Generating the product table takes 25 to 30 s. If it takes over 60 s, check the worker logs: `npx wrangler tail` |
| Product table does not render | Messages that contain `<table` must be inserted with innerHTML, not textContent. |
| Embedded data empty | Check that the embedded data fields are initialised in the survey flow before the chat block. |
| JSON parse error in stage 2 | The model sometimes wraps the JSON in markdown; the JavaScript extracts it with a regular expression. |

## Architecture

```
[Prolific participant]
        |
        v
[Qualtrics survey page]
  - HTML chat widget
  - JavaScript manages the three stages
        |
        | POST /chat {stage, message, history}
        v
[Cloudflare Worker: study3-chatbot]
  - Validates the request
  - Selects the system prompt for the stage
  - Rate-limits by IP address
        |
        | POST /v1/messages
        v
[Anthropic API: Claude Opus 4.6]
  - Stage 1: conversational elicitation
  - Stage 2: product-table generation (JSON)
  - Stage 3: recommendation and follow-up
        |
        v
[Response flows back]
  Worker -> Qualtrics JavaScript -> chat widget -> embedded data
        |
        v
[Qualtrics export: CSV with the conversation data]
```
