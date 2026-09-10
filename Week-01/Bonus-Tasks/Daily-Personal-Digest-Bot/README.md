# Daily Personal Digest Bot

An automated n8n workflow that sends a personalized daily digest to Telegram every morning.

The workflow collects data from multiple external sources, merges the results, formats them into a single Markdown message, and delivers the digest through a Telegram bot.

## Features

- Automatic daily execution at 08:00
- Asia/Baku timezone configuration
- Current weather for Baku
- Latest BBC World news headline
- Daily to-do reminder from Google Sheets
- Single Markdown-formatted Telegram digest

### Bonus Features

- `/digest` command for on-demand execution
- Motivational quote from ZenQuotes
- Dynamic weather image
- Automatic day/night weather icon selection

## Workflow

The workflow supports two trigger methods:

**Scheduled execution**

`Daily 08:00 Schedule → Data Sources → Merge Digest Data → Format Daily Digest → Telegram`

**On-demand execution**

`Telegram Trigger → Check /digest Command → Data Sources → Merge Digest Data → Format Daily Digest → Telegram`

## Data Sources

- Open-Meteo — current Baku weather
- BBC World RSS — latest world news headline
- Google Sheets — daily to-do reminder
- ZenQuotes — motivational quote
- Xweather — dynamic weather icons

## Timezone

The workflow timezone is explicitly configured as:

`Asia/Baku (UTC+04:00)`

The Schedule Trigger runs every day at **08:00 Baku time**.

The schedule was also tested with a temporary scheduled execution before the final 08:00 schedule was enabled.

## Output

The Telegram bot sends:

- Current temperature and weather code
- Latest news headline and source link
- Today's to-do and status
- Motivational quote and author
- Dynamic weather image appropriate for the current day/night condition

## Files

- `workflow.json` — exported n8n workflow
- `RESOURCES.md` — APIs, services, and documentation used
- `screenshots/` — workflow and execution evidence

## Tech Stack

n8n · Telegram Bot API · Open-Meteo · BBC RSS · Google Sheets · ZenQuotes · Xweather
