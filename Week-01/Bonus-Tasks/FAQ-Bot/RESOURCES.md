# Resources

The following documentation and references were used while building the FAQ Bot.

## n8n

### Code Node
Used to implement the Levenshtein Distance algorithm and calculate similarity scores between user questions and FAQ questions.

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/

### Google Sheets Node
Used to read FAQ question/answer pairs, append new FAQ entries, and log unanswered questions.

https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/

### Telegram Trigger
Used to receive messages and commands from Telegram.

https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/

### Telegram Node
Used to send FAQ answers, fallback messages, and confirmation responses.

https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/

### Switch Node
Used to route `/yes`, `/no`, `/addfaq`, and normal FAQ messages into separate workflow branches.

https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/

## Levenshtein Distance

Levenshtein Distance is used to measure the difference between two strings based on the minimum number of insertions, deletions, and substitutions required.

https://en.wikipedia.org/wiki/Levenshtein_distance

A hand-written JavaScript implementation was used in the n8n Code node instead of hardcoding individual FAQ questions.

## Google Sheets

Google Sheets is used as the project's knowledge base and unanswered-question log.

https://www.google.com/sheets/about/

## Telegram Bot API

Telegram provides the messaging interface used by the FAQ bot.

https://core.telegram.org/bots/api
