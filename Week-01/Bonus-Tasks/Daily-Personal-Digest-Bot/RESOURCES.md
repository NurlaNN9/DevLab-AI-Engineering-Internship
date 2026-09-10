# Resources

Resources, APIs, and documentation used to build the Daily Personal Digest Bot.

## n8n

### Schedule Trigger
Used to automatically run the workflow every morning at 08:00 Asia/Baku.

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/

### Telegram Integration
Used to send the daily digest and weather image to Telegram and to receive the `/digest` command.

https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/

https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/

## Weather

### Open-Meteo
Used to retrieve the current temperature, WMO weather code, and day/night status for Baku.

https://open-meteo.com/

https://open-meteo.com/en/docs

## News

### BBC World RSS
Used to retrieve the latest BBC World news headline.

https://feeds.bbci.co.uk/news/world/rss.xml

## To-Do Data

### Google Sheets
Used as the spreadsheet source for daily to-do reminders.

https://www.google.com/sheets/about/

## Motivational Quote

### ZenQuotes API
Used to retrieve a random motivational quote and author.

https://zenquotes.io/

https://zenquotes.io/api/random

## Weather Icons

### Xweather Weather Icons
Used to provide PNG weather images with separate day and night variants.

https://www.xweather.com/docs/weather-api/reference/icon-list

The Open-Meteo WMO weather code and `is_day` value are used to dynamically select the appropriate Xweather icon.

## Workflow Platform

### n8n
The complete automation workflow was built and executed using n8n.

https://n8n.io/
