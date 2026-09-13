# Week 01 — Bonus Tasks

This directory contains the optional bonus tasks completed for Week 01 of the DevLab AI Engineering Internship.

## Optional Task 01 — Daily Personal Digest Bot

An automated personal digest workflow built with n8n and Telegram that delivers useful daily information in a single message.

### Key Features

- Daily scheduled execution
- Weather data from Open-Meteo
- BBC World news headline
- To-do items from Google Sheets
- Motivational quote
- Combined Markdown Telegram digest
- Asia/Baku timezone configuration

### Bonus Features

- Manual `/digest` command
- Motivational quote integration
- Dynamic weather image/icon

### Files

- [`OPTIONAL-TASK-01-DAILY-PERSONAL-DIGEST-BOT.md`](./OPTIONAL-TASK-01-DAILY-PERSONAL-DIGEST-BOT.md) — Original task requirements
- [`Daily-Personal-Digest-Bot/`](./Daily-Personal-Digest-Bot/) — Complete implementation, workflow, documentation, and screenshots

---

## Optional Task 02 — FAQ Bot Backed by a Knowledge-Base Spreadsheet

A Telegram FAQ bot that retrieves question/answer pairs from Google Sheets and uses generic Levenshtein Distance similarity matching to find the closest FAQ.

### Key Features

- Google Sheets FAQ knowledge base
- Generic Levenshtein similarity matching
- 0.60 threshold-based fallback
- Unanswered-question logging
- Telegram responses
- No hardcoded question-specific matching

### Bonus Features

- Live FAQ creation with the admin `/addfaq` command
- Similarity threshold tuning for typo tolerance
- Follow-up `/yes` and `/no` confirmation flow

### Files

- [`OPTIONAL-TASK-02-FAQ-BOT-BACKED-BY-A-KNOWLEDGE-BASE-SPREADSHEET.md`](./OPTIONAL-TASK-02-FAQ-BOT-BACKED-BY-A-KNOWLEDGE-BASE-SPREADSHEET.md) — Original task requirements
- [`FAQ-Bot/`](./FAQ-Bot/) — Complete implementation, workflow, documentation, and screenshots
