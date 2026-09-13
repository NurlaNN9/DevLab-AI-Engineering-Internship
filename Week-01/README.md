# Week 01 — AI Automation with n8n

This directory contains the tasks, implementations, workflow exports, testing evidence, and documentation completed during **Week 01** of the DevLab AI Engineering Internship.

## Week 01 Structure

```text
Week-01/
│
├── Required-Tasks/
│   └── Customer-Support-Ticket-Bot/
│
├── Bonus-Tasks/
│   ├── Daily-Personal-Digest-Bot/
│   └── FAQ-Bot/
│
└── README.md
```

## Required Task

### Customer Support Ticket Bot

An AI-powered customer support automation built with **n8n, Telegram, Ollama, Gemma 4, and Google Sheets**.

The workflow:

- Receives customer messages through Telegram
- Validates incoming user input
- Uses a locally hosted **Gemma 4** model through **Ollama** for intent classification
- Classifies requests into Billing, Technical, or General categories
- Routes tickets dynamically based on the AI-generated category
- Logs support tickets to Google Sheets
- Sends category-specific Telegram responses
- Uses a live external API for General requests
- Handles invalid input, AI failures, and external API failures
- Sends an admin notification for Technical tickets

Project directory:

`Required-Tasks/Customer-Support-Ticket-Bot/`

---

## Bonus Tasks

### Optional Task 01 — Daily Personal Digest Bot

An automated Telegram digest workflow that combines multiple data sources into a single daily message.

The workflow:

- Runs automatically every morning
- Uses **Asia/Baku** timezone
- Retrieves current weather information
- Retrieves a BBC World news headline
- Reads to-do items from Google Sheets
- Adds a motivational quote
- Merges the data into one Telegram digest
- Supports the `/digest` command for manual execution
- Includes a dynamic weather image/icon

Project directory:

`Bonus-Tasks/Daily-Personal-Digest-Bot/`

---

### Optional Task 02 — FAQ Bot Backed by a Knowledge-Base Spreadsheet

A Telegram FAQ bot that retrieves answers from a Google Sheets knowledge base using generic text-similarity matching.

The workflow:

- Reads FAQ question/answer pairs from Google Sheets
- Uses a hand-written **Levenshtein Distance** algorithm in JavaScript
- Calculates similarity between incoming questions and stored FAQ questions
- Selects the closest FAQ match
- Uses a **0.60 similarity threshold**
- Avoids guessing when the similarity score is below the threshold
- Logs unanswered questions to Google Sheets
- Sends matched answers or escalation messages through Telegram
- Uses generic matching without question-specific hardcoded conditions

Bonus functionality includes:

- Live FAQ creation using the admin `/addfaq` command
- Threshold tuning for typo tolerance
- Follow-up confirmation using `/yes` and `/no`

Project directory:

`Bonus-Tasks/FAQ-Bot/`

---

## Week 01 Completed Work

- **1 Required Task** — Customer Support Ticket Bot
- **2 Optional Tasks** — Daily Personal Digest Bot and FAQ Bot
- Required workflow functionality completed
- Optional bonus features implemented
- Exported n8n workflow JSON files
- Testing and execution evidence
- Screenshots
- Technical documentation
- Resource references

## Technologies Used

- n8n
- JavaScript
- Docker
- Ollama
- Gemma 4
- Telegram Bot API
- Google Sheets API
- REST APIs
- Open-Meteo API
- BBC RSS
- ZenQuotes
- Levenshtein Distance

---

**DevLab AI Engineering Internship — Week 01**
