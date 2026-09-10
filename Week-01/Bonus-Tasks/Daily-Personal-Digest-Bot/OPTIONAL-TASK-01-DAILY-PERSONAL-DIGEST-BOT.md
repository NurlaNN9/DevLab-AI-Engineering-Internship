# Daily Personal Digest Bot

Build a scheduled n8n workflow that every morning fetches the weather, a news headline, and a to-do reminder from a spreadsheet, then sends it as one formatted Telegram message. This introduces scheduled (Cron) triggers and merging multiple data sources, as opposed to the reactive, message-driven workflow from the mandatory task.

## Learning objectives

- Use a Cron/Schedule Trigger to run a workflow automatically at a fixed time
- Call two or more external APIs and merge their results using Merge/Set nodes
- Format a single outgoing message with Markdown for Telegram
- Read structured data from a spreadsheet as workflow input
- Test a workflow with n8n's manual execution feature before enabling its schedule

## Must-have features

- **Schedule Trigger** — Fires automatically once a day at a fixed, configured time.
- **Weather API Call** — Fetches current weather for a fixed city using a free weather API.
- **News/Headline Fetch** — Pulls at least one current headline via an RSS feed or a news API.
- **To-Do Read from Sheet** — Reads at least one reminder/to-do row from a connected spreadsheet.
- **Merge & Format Single Message** — All three sources are merged into one Markdown-formatted Telegram message, not three separate messages.
- **Timezone Correctness** — The schedule explicitly runs on Azerbaijan/Baku time, not the server default UTC, verified by a documented test.

## Bonus features

- Add an on-demand `/digest` command so the user can trigger it outside the schedule
- Include a motivational quote pulled from a public quotes API
- Attach an image (e.g. a weather icon) alongside the text message

## Technical requirements

- **n8n Schedule Trigger node** — Used instead of the Telegram Trigger for this task.
- **Free weather API** — e.g. OpenWeatherMap free tier.
- **Spreadsheet or Notion database** — Source of the to-do/reminder rows.

## n8n Schedule Trigger docs

n8n's Cron/Schedule Trigger documentation explains interval and cron-expression based scheduling:

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/
