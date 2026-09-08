# Setup Guide

This document describes the environment and services used to build and run the **Customer Support Ticket Bot**.

## 1. Prerequisites

The project requires:

- Docker Desktop
- n8n
- Ollama
- Gemma 4
- Telegram Bot
- ngrok
- Google Cloud account
- Google Sheets
- Internet access for external API requests

## 2. n8n Setup

n8n was self-hosted locally using Docker.

The workflow was created manually inside the n8n editor without importing a pre-built workflow template.

The main workflow handles:

- Telegram message reception
- Input validation
- Local AI classification
- JSON parsing
- Ticket logging
- Category routing
- Telegram responses
- External API integration
- Error handling

## 3. Local AI Setup

Ollama was installed and executed on the host machine.

The project uses the following local model:

```text
gemma4:e2b
```

Because n8n runs inside Docker while Ollama runs on the host machine, n8n communicates with Ollama using:

```text
http://host.docker.internal:11434
```

The AI model is called through an n8n HTTP Request node.

Its purpose is to classify incoming customer requests into:

```text
billing
technical
general
```

The model is instructed to return its classification in JSON format.

Example:

```json
{
  "category": "billing"
}
```

## 4. Telegram Bot Setup

A Telegram bot was created and connected to n8n.

The Telegram Trigger node receives incoming customer messages and starts the workflow.

Telegram is also used to:

- Send Billing responses
- Send Technical responses
- Send General responses
- Send fallback responses
- Send invalid-input responses
- Send service error responses
- Send Technical ticket alerts to the administrator

## 5. Public Webhook

Because n8n is hosted locally, a public HTTPS endpoint is required for Telegram webhooks.

ngrok was used to expose the local n8n instance through a public HTTPS URL.

The public URL was then used by n8n for Telegram webhook communication and OAuth callbacks.

> The ngrok URL may change between sessions depending on the ngrok configuration.

## 6. Google Sheets Integration

Google Sheets is used as the ticket storage system.

A Google Cloud project was configured and the Google Sheets API was enabled.

OAuth credentials were then connected to n8n.

Each support ticket stores the following information:

| Field | Description |
| --- | --- |
| `timestamp` | Time when the ticket was processed |
| `user` | Telegram username or first name |
| `category` | Category assigned by the AI model |
| `original_message` | Original customer support message |

This creates a persistent record of processed customer support tickets.

## 7. External API Integration

The General branch demonstrates integration with a real external REST API.

The workflow uses the Frankfurter exchange-rate API to retrieve the current USD to EUR exchange rate.

Example endpoint:

```text
https://api.frankfurter.app/latest?from=USD&to=EUR
```

The live exchange-rate result is inserted into the Telegram response.

The API node also includes:

- Retry on failure
- Multiple retry attempts
- A dedicated error output
- A graceful Telegram error response

## 8. Workflow Routing

After AI classification, the category is validated and passed to an n8n Switch node.

The routing structure is:

```text
AI Category
    │
    ├── billing   → Billing Response
    │
    ├── technical → Technical Response
    │                └── Admin Technical Alert
    │
    ├── general   → External API → General Response
    │
    └── fallback  → Fallback Response
```

Routing is based on the **AI-generated category**, not hardcoded keyword matching.

## 9. Error Handling

Several failure scenarios are handled by the workflow.

### Invalid Input

Messages that are empty, non-text, or contain only emojis are rejected before AI processing.

Normal text containing emojis is still accepted.

### Invalid AI Output

The AI response is parsed and validated.

If the model returns malformed JSON or an unsupported category, the workflow assigns:

```text
fallback
```

### Local AI Failure

If Ollama becomes unavailable, the AI HTTP Request node uses its error path.

The failure is logged and the customer receives a graceful service error message.

### External API Failure

The external API request uses retry logic.

If all attempts fail, the workflow follows a dedicated error branch and informs the customer that the external service is temporarily unavailable.

## 10. Security Notes

Credentials and secrets should never be committed directly to a public GitHub repository.

Sensitive information includes:

- Telegram Bot Token
- Google OAuth Client Secret
- OAuth access or refresh tokens
- Private API keys
- Other authentication credentials

The exported workflow should be checked for sensitive information before being published.

## 11. Running the Workflow

To run the complete system:

1. Start Docker Desktop.
2. Start the n8n container.
3. Start Ollama and make sure the Gemma model is available.
4. Start the public ngrok tunnel if required.
5. Open n8n and verify the configured integrations.
6. Make sure the workflow is active/published.
7. Send a support message to the Telegram bot.
8. Verify the response and Google Sheets ticket log.

---

**DevLab AI Engineering Internship — Week 01 Required Task**
