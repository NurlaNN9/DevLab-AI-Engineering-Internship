# n8n Workflow

This directory contains the exported n8n workflow for the **Daily Personal Digest Bot**, developed as a Week 01 Optional Task of the DevLab AI Engineering Internship.

## Workflow File

The exported JSON file contains the complete n8n workflow, including:

- Daily Schedule Trigger at 08:00
- Asia/Baku timezone configuration
- On-demand `/digest` Telegram command
- Open-Meteo weather integration
- BBC World RSS headline retrieval
- Google Sheets to-do retrieval
- ZenQuotes motivational quote integration
- Four-source data merging
- Markdown digest formatting
- Telegram digest delivery
- Dynamic Xweather weather image retrieval
- Automatic day/night weather icon selection

## Importing the Workflow

The JSON file can be imported into an n8n instance.

After importing, external credentials and environment-specific configuration must be configured separately, including:

- Telegram Bot credentials
- Google Sheets OAuth credentials
- Google Sheets document configuration
- Workflow timezone (`Asia/Baku`)

The workflow uses public HTTP/RSS endpoints for Open-Meteo, BBC World RSS, ZenQuotes, and Xweather weather icons.

## Security

Authentication credentials, access tokens, and private API secrets should not be stored directly in this repository.

Environment-specific credentials must be configured securely inside n8n before running the workflow.

---

**DevLab AI Engineering Internship — Week 01 Optional Task**
