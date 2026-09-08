# Customer Support Ticket Bot with n8n, Telegram, and Local AI Classification

Build an n8n workflow that receives messages through a Telegram bot, uses a locally-hosted Gemma 4 model (via Ollama) to classify each one into a support category, routes it with a Switch node, logs it to an external sheet/database, and replies automatically. Crucially, the workflow must also call one real external API and gracefully handle unrecognized/ambiguous input, so the assessed skill is designing a robust AI-driven branching automation, not just wiring a single trigger to a single reply.

## Learning Objectives

- Configure a Telegram Bot via BotFather and connect it to an n8n Telegram Trigger node
- Run Gemma 4 locally with Ollama (`ollama pull gemma4` / `ollama run gemma4`) and call it from n8n to classify the incoming message's intent as structured output (e.g. JSON with a `category` field)
- Design a multi-branch n8n workflow using a Switch node that routes on the AI's returned category, not on hardcoded keywords
- Persist incoming requests to an external store (Google Sheets/Airtable/Postgres) with correct field mapping, including the AI-assigned category
- Use n8n's HTTP Request node to call an external API and inject the response back into the chat
- Handle errors and edge cases (empty messages, low-confidence/unclassifiable AI output, unresponsive LLM or API calls) without crashing the workflow
- Document a workflow with n8n sticky notes so another developer can maintain it

## Must-Have Features

### Telegram Bot Setup

A working bot token, webhook connected to the n8n Telegram Trigger node, verified with a live test message.

### AI-Powered Intent Classification

An HTTP Request node (or n8n AI/LLM node) calls a locally-hosted Gemma 4 model served by Ollama (POST to `http://localhost:11434/api/chat` or `/api/generate` with `model: "gemma4"`) with a system prompt instructing it to return strict JSON like `{"category": "billing|technical|general"}`. The prompt must constrain the model to only the allowed category labels. No external API key or internet-facing LLM call is required — everything runs on the student's own machine/Docker network.

### Intent Routing

A Switch node reads the `category` field parsed out of the AI's JSON response and routes the message into at least 3 branches (e.g. billing, technical, general) plus a default/fallback output for anything the model returns outside the allowed labels.

### Data Logging

Every ticket is appended as a row to Google Sheets/Airtable/a DB table with timestamp, user, AI-assigned category, and original message.

### Auto-Reply

Each category returns a distinct templated reply sent back through Telegram.

### External API Call

One branch calls a real external API (e.g. weather, currency, or any public REST API) and returns the live result to the user.

### Error Handling Branch

A fallback path handles empty/unrecognized input, malformed or non-JSON AI responses, and unresponsive LLM/API calls (including cases where the local Ollama service is not running or the model is still loading), replying gracefully instead of leaving the user hanging.

### Anti-Cheat: Manual Workflow Construction

The workflow must be built with individual nodes wired manually (Trigger → AI classification → Switch → branches). Importing/copy-pasting a pre-built community template disqualifies the submission. Submit a screenshot of the full canvas plus the exported workflow JSON.

## Bonus Features

- Add a rate limiter so the same user cannot spam more than 5 messages per minute
- Add an admin notification path (a Telegram message to you) whenever a "technical" ticket arrives
- Store conversation history and expose a `/history` command that returns the user's last 5 tickets
- Have the Gemma 4 model also detect the message language (Azerbaijani/English/Russian) as part of its JSON output, and reply in the same language
- Add a confidence/fallback check: if the AI's category isn't one of the allowed labels, retry once with a stricter prompt before falling back to the error branch
- Try a smaller Gemma 4 size (e.g. e2b or e4b) vs a larger one (12b/26b) and note the classification-accuracy vs response-time tradeoff on your hardware

## Technical Requirements

| **RequirementDetails** | |
| --- | --- |
| **n8n** | Self-hosted via Docker or n8n Cloud free tier. Docker is recommended for full node access. |
| **Telegram Bot API** | Free, created via @BotFather. Requires a public webhook URL — use n8n Cloud or ngrok if self-hosting. |
| **Ollama + Gemma 4 (local, free)** | Install Ollama locally or run it as a Docker container on the same network as n8n, then pull the model with `ollama pull gemma4`. Use the e2b or e4b size if your machine has 16GB RAM or less; 12b/26b/31b need more RAM/VRAM. No API key, no internet-facing LLM call, and no cost — everything runs on the student's own hardware. |
| **Google Sheets or Airtable** | Free-tier account for the logging destination. A local SQLite/Postgres table is an accepted substitute — state which was used. |
| **Exported Workflow JSON** | n8n workflows must be exported with the Download button and submitted alongside screenshots, not just described in text. |

## Resources

- **n8n Telegram integration docs** — Official n8n documentation on the Telegram Trigger and Telegram node covers trigger setup, sending messages, and webhook configuration: [https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/)
- **Ollama docs (local model runtime)** — Ollama runs models like Gemma 4 locally and exposes a REST API on `http://localhost:11434`, callable from n8n's HTTP Request node — no API key needed: https://github.com/ollama/ollama/blob/main/docs/api.md
- **Gemma 4 on Ollama** — Official Ollama library page for Gemma 4, listing available sizes (e2b, e4b, 12b, 26b MoE, 31b dense), pull/run commands, and chat template details: [https://ollama.com/library/gemma4](https://ollama.com/library/gemma4)
- **Mentor reference notes** — Common failure mode: students forget to switch the Telegram Trigger into webhook mode, so it never fires — check for the green "active" indicator before grading. If n8n runs in Docker and Ollama runs on the host, remind students to call `http://host.docker.internal:11434` instead of `localhost`, or that call will fail.
