# n8n Workflow

This directory contains the exported n8n workflow for the **Customer Support Ticket Bot**, developed as the Week 01 Required Task of the DevLab AI Engineering Internship.

## Workflow File

The exported JSON file contains the complete n8n workflow, including:

- Telegram message trigger
- Input validation
- Local Gemma 4 classification through Ollama
- AI JSON parsing and validation
- Google Sheets ticket logging
- AI-based category routing
- Billing, Technical, General, and Fallback branches
- Live external API integration
- API retry and error handling
- Ollama failure handling
- Technical ticket admin notification
- Telegram responses

## Importing the Workflow

The JSON file can be imported into a self-hosted n8n instance.

After importing, external credentials and environment-specific configuration must be configured separately, including:

- Telegram Bot credentials
- Google Sheets OAuth credentials
- Ollama connection
- Public webhook configuration

## Security

Authentication credentials, access tokens, and private API secrets should not be stored directly in this repository.

Environment-specific credentials must be configured securely inside n8n before running the workflow.

---

**DevLab AI Engineering Internship — Week 01 Required Task**
