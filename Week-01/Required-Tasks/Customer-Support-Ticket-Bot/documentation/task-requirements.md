# Task Requirements

## Week 01 — Required Task

### Customer Support Ticket Bot with n8n, Telegram, and Local AI Classification

The objective of this task is to build an automated customer support ticket system using **n8n**, **Telegram**, and a locally hosted AI model through **Ollama**.

## Core Requirements

The workflow must:

- Receive customer messages through a Telegram bot.
- Use a locally hosted Gemma model via Ollama to classify customer intent.
- Return the AI classification in structured JSON format.
- Support at least three categories:
  - Billing
  - Technical
  - General
- Include a fallback path for invalid or unrecognized classifications.
- Route requests using an n8n Switch node based on the AI-generated category rather than hardcoded keywords.
- Log every support ticket to Google Sheets, Airtable, or a database.
- Store:
  - Timestamp
  - User
  - AI-assigned category
  - Original message
- Send a different automatic Telegram response for each support category.
- Use a real external API in at least one workflow branch.
- Include live API data in the Telegram response.
- Handle empty or invalid user input.
- Handle malformed or non-JSON AI output.
- Handle unavailable Ollama or local AI service.
- Handle external API failures gracefully.
- Include Sticky Notes explaining the major sections of the n8n workflow.
- Be constructed manually rather than imported from a pre-built template.

## Technical Requirements

- n8n must be self-hosted using Docker.
- Telegram must communicate with the workflow through a public webhook URL.
- Ollama must run locally.
- Communication from the n8n Docker container to Ollama can use:

```text
http://host.docker.internal:11434
```

- Ticket information must be persisted using Google Sheets, Airtable, or a database.

## Submission Requirements

The final submission must include:

- A screenshot of the complete n8n workflow canvas.
- The exported n8n workflow JSON file.

## Optional Bonus Features

Possible bonus features include:

- Rate limiting for users sending more than five requests per minute.
- Admin notification when a Technical support ticket is received.
- `/history` command showing the last five tickets.
- Automatic language detection and replies in the same language.
- Confidence-based fallback or AI retry.
- Comparison between different Gemma model sizes.

## Implemented Additional Feature

For this implementation, the **Technical ticket admin notification** feature was also completed.

When a Technical request is detected, the workflow sends a separate Telegram alert to the administrator containing information about the support ticket.

---

**DevLab AI Engineering Internship — Week 01 Required Task**
