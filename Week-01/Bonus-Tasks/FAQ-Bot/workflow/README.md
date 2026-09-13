# Workflow

This folder contains the exported n8n workflow for the FAQ Bot Backed by a Knowledge-Base Spreadsheet.

## File

`faq-bot.json`

The workflow includes:

- Telegram message handling
- Generic Levenshtein similarity matching
- Google Sheets FAQ lookup
- 0.60 similarity threshold
- Threshold-based fallback
- Unanswered-question logging
- Telegram FAQ responses
- Admin `/addfaq` command
- `/yes` and `/no` follow-up confirmation routing

## Import

To use the workflow:

1. Open n8n.
2. Create a new workflow.
3. Import `faq-bot.json`.
4. Configure your own Telegram and Google Sheets credentials.
5. Select the appropriate FAQ Google Sheets document.
6. Update the admin Telegram ID if necessary.
7. Test the workflow before publishing it.

> Credentials and sensitive authentication information are not included in the repository.
