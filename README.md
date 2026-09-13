# DevLab AI Engineering Internship

This repository contains my projects, workflows, assignments, experiments, and technical documentation completed during the **DevLab AI Engineering Internship**.

The repository documents my progress through the internship and focuses on practical AI engineering, automation, APIs, workflow development, and AI-powered applications.

## Repository Structure

```text
DevLab-AI-Engineering-Internship/
│
├── Week-01/
│   ├── Required-Tasks/
│   ├── Bonus-Tasks/
│   └── README.md
│
└── README.md
```

Each week contains its own documentation, workflow files, screenshots, testing evidence, and supporting resources.

---

## Week 01 — AI Automation with n8n

Week 01 focuses on building practical automation workflows with **n8n**, external APIs, Telegram, Google Sheets, and AI models.

### Required Task

**Customer Support Ticket Bot**

An AI-powered customer support workflow that:

- Receives support requests through Telegram
- Uses a locally hosted **Gemma 4** model through **Ollama**
- Classifies requests into Billing, Technical, and General categories
- Routes requests dynamically
- Logs tickets to Google Sheets
- Integrates an external API
- Handles invalid input and service failures
- Sends admin alerts for Technical tickets

Project directory:

`Week-01/Required-Tasks/Customer-Support-Ticket-Bot/`

### Optional Task 01

**Daily Personal Digest Bot**

An automated daily Telegram digest that combines:

- Weather information
- BBC World news
- Google Sheets to-do items
- Motivational quotes
- Dynamic weather visuals
- Scheduled and `/digest` execution

Project directory:

`Week-01/Bonus-Tasks/Daily-Personal-Digest-Bot/`

### Optional Task 02

**FAQ Bot Backed by a Knowledge-Base Spreadsheet**

A spreadsheet-backed FAQ retrieval bot featuring:

- Google Sheets knowledge base
- Generic Levenshtein similarity matching
- Similarity threshold and safe fallback
- Unanswered-question logging
- Live `/addfaq` administration
- Typo-tolerant matching
- `/yes` and `/no` follow-up confirmation

Project directory:

`Week-01/Bonus-Tasks/FAQ-Bot/`

---

## Technologies & Tools

Technologies used throughout the internship currently include:

- **n8n** — workflow automation
- **JavaScript** — workflow logic and data processing
- **Docker** — local service deployment
- **Ollama** — local AI model execution
- **Gemma 4** — local language model
- **Telegram Bot API** — user interaction
- **Google Sheets API** — data storage and knowledge-base integration
- **REST APIs** — external data integration
- **Open-Meteo API** — weather data
- **BBC RSS** — news data
- **ZenQuotes** — motivational quote data
- **Levenshtein Distance** — fuzzy text similarity

---

## Repository Goals

This repository is intended to:

- Document my progress during the internship
- Build practical AI engineering experience
- Apply AI models to real automation workflows
- Practice API and third-party service integration
- Develop reliable workflow error handling
- Explore retrieval and text-matching techniques
- Maintain reproducible project documentation
- Track the development of increasingly advanced AI systems

---

## Current Progress

| Week | Focus | Status |
| --- | --- | --- |
| Week 01 | AI Automation with n8n | ✅ Completed |

Additional weeks and projects will be added as the internship progresses.

---

## About

This repository was created as part of the **DevLab AI Engineering Internship** and serves as a technical portfolio of the work completed throughout the program.

Each project directory contains its own detailed README, implementation files, workflow exports, resources, and testing evidence.
