# Customer Support Ticket Bot

An AI-powered customer support automation developed as the **Week 01 Required Task** for the DevLab AI Engineering Internship.

The project uses **n8n**, **Telegram**, and a locally hosted **Gemma 4 model through Ollama** to automatically classify, route, log, and respond to customer support requests.

## Project Overview

Customers send support requests through a Telegram bot. The workflow validates the incoming message and sends valid requests to a locally hosted AI model for intent classification.

The AI classifies each request into one of the following categories:

- Billing
- Technical
- General
- Fallback

The ticket is then logged to Google Sheets and routed through n8n according to the AI-generated category.

## Workflow Architecture

```text
Telegram Message
       │
       ▼
Input Validation
       │
       ▼
Local Gemma 4 via Ollama
       │
       ▼
Parse & Validate AI Output
       │
       ▼
Google Sheets Logging
       │
       ▼
AI-Based Category Routing
       │
       ├── Billing ──────► Billing Response
       │
       ├── Technical ───► Technical Response
       │                  └──► Admin Notification
       │
       ├── General ─────► External API
       │                  └──► General Response
       │
       └── Fallback ────► Fallback Response
```

## Features

- Telegram-based customer support interface
- Input validation before AI processing
- Local AI inference using Gemma 4 through Ollama
- Structured JSON intent classification
- AI-driven routing instead of hardcoded keyword routing
- Billing, Technical, and General support branches
- Fallback handling for invalid or unexpected AI output
- Automatic ticket logging to Google Sheets
- Category-specific Telegram responses
- Live external API integration
- Retry and graceful API failure handling
- Graceful handling of local AI service failures
- Rejection of empty, non-text, and emoji-only requests
- Support for normal text containing emojis
- Admin Telegram alert for Technical support tickets

## AI Classification

The AI model is instructed to return a structured category in JSON format.

Example:

```json
{
  "category": "technical"
}
```

The workflow validates the AI output before routing. If the response is malformed or contains an unsupported category, the request is safely sent to the fallback path.

## Ticket Logging

Each processed support ticket is logged to Google Sheets with:

- Timestamp
- User
- AI-assigned category
- Original customer message

This provides a simple record of incoming support requests and their classifications.

## External API Integration

General requests use a live exchange-rate API to demonstrate integration with an external service.

The workflow retrieves the current **USD → EUR** exchange rate and includes the live result in the Telegram response.

Retry logic and a separate error path are included to handle temporary API failures gracefully.

## Error Handling

The workflow includes handling for:

- Empty messages
- Non-text messages
- Emoji-only input
- Malformed AI JSON output
- Unsupported AI categories
- Ollama / local AI service failures
- External API failures

Users receive an appropriate response instead of allowing the workflow to fail silently.

## Additional Feature

A Technical support ticket also triggers an **Admin Technical Alert** through Telegram.

The administrator receives:

- Customer identity
- Original message
- AI-assigned category
- Timestamp

This feature was implemented in addition to the core required workflow.

## Technologies Used

- n8n
- Docker
- Telegram Bot API
- Ollama
- Gemma 4
- Google Sheets API
- REST API integration
- ngrok
- Git & GitHub

## Project Files

```text
Customer-Support-Ticket-Bot/
│
├── README.md
│
├── workflow/
│   └── customer-support-ticket-bot.json
│
├── screenshots/
│   ├── workflow-full-canvas.png
│   ├── 01-billing-test.png
│   ├── 02-technical-admin-test.png
│   ├── 03-general-live-api-test.png
│   ├── 04-invalid-input-test.png
│   └── 05-text-with-emoji-test.png
│
└── documentation/
    ├── task-requirements.md
    ├── setup.md
    └── testing.md
```

## Testing

The workflow was tested with multiple scenarios, including:

- Billing support requests
- Technical support requests
- General requests using live API data
- Invalid and emoji-only input
- Normal text containing emojis
- Technical admin notifications
- External API failure handling
- Local AI failure handling

Testing screenshots are available in the `screenshots/` directory.

## Workflow Export

The complete n8n workflow is available as an exported JSON file inside the `workflow/` directory.

---

**DevLab AI Engineering Internship — Week 01 Required Task**
