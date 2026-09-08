# Week 01 — AI Automation with n8n

This directory contains the tasks, implementations, and documentation completed during **Week 01** of the DevLab AI Engineering Internship.

## Week 01 Structure

```text
Week-01/
│
├── Required-Tasks/
│   └── Customer-Support-Ticket-Bot/
│
├── Bonus-Tasks/
│
└── README.md
```

## Required Task

### Customer Support Ticket Bot

The required task for Week 01 is an AI-powered customer support automation built with **n8n**.

The workflow:

- Receives customer messages through Telegram
- Validates incoming user input
- Uses a locally hosted **Gemma 4** model through **Ollama** for intent classification
- Classifies support requests into Billing, Technical, or General categories
- Routes tickets dynamically based on the AI-generated category
- Logs support tickets to Google Sheets
- Sends category-specific Telegram responses
- Uses a live external API for General requests
- Handles invalid input, AI failures, and external API failures gracefully
- Sends an admin notification when a Technical ticket is received

The complete workflow export, screenshots, testing evidence, and technical documentation are available inside:

`Required-Tasks/Customer-Support-Ticket-Bot/`

## Bonus Tasks

Week 01 also includes optional bonus tasks.

Bonus implementations and their documentation will be stored separately inside:

`Bonus-Tasks/`

## Technologies Used

- n8n
- Docker
- Ollama
- Gemma 4
- Telegram Bot API
- Google Sheets API
- REST APIs

---

**DevLab AI Engineering Internship — Week 01**
