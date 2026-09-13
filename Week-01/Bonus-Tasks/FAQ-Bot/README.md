# FAQ Bot Backed by a Knowledge-Base Spreadsheet

An automated FAQ support bot built with n8n, Telegram, and Google Sheets.

The bot reads FAQ question/answer pairs from a Google Sheets knowledge base and uses a generic Levenshtein Distance algorithm to calculate text similarity between the user's question and stored FAQ questions.

Instead of using hardcoded rules for individual questions, the workflow automatically selects the closest FAQ match and only returns the answer when the similarity score passes a defined threshold.

## Features

- Telegram-based FAQ bot
- Google Sheets as the FAQ knowledge base
- Generic text similarity matching
- Hand-written Levenshtein Distance algorithm in JavaScript
- Best-match FAQ selection
- 0.60 similarity threshold
- Typo-tolerant question matching
- Safe fallback when no suitable answer is found
- Automatic unanswered-question logging
- Telegram escalation response
- No hardcoded question-specific routing

## Bonus Features

### Live FAQ Management

An authorized admin can add new FAQ question/answer pairs directly through Telegram using:

`/addfaq Question | Answer`

The workflow verifies the admin, parses the command, and appends the new FAQ pair to Google Sheets.

New FAQ entries become available to the matching system without changing the workflow code.

### Threshold Tuning

The similarity threshold was set to **0.60** after testing different question variations.

For example:

`How reset pasword`

correctly matched:

`How can I reset my password?`

with a similarity score of approximately **0.607**.

A 0.60 threshold was selected to balance typo tolerance and false matches. Higher thresholds may reject valid but heavily misspelled or shortened questions, while lower thresholds may increase incorrect matches.

### Follow-Up Confirmation

After a successful FAQ response, the bot asks:

> Did that answer your question?

The user can reply with:

- `/yes` — sends a positive confirmation
- `/no` — acknowledges that the answer was not helpful

These commands are routed separately and do not enter the normal FAQ similarity-matching process.

## Workflow Architecture

```text
Telegram Trigger
        ↓
Route Telegram Message
   ├── /yes
   │      ↓
   │   Positive Confirmation
   │
   ├── /no
   │      ↓
   │   Negative Confirmation
   │
   ├── /addfaq
   │      ↓
   │   Verify Admin
   │      ↓
   │   Parse New FAQ
   │      ↓
   │   Add New FAQ to Google Sheets
   │
   └── Normal Question
          ↓
      Read FAQ Knowledge Base
          ↓
      Calculate FAQ Similarity
          ↓
      Check Similarity Threshold (0.60)
          ↓
       ┌──┴──┐
      TRUE  FALSE
       ↓      ↓
   Send FAQ  Log Unanswered Question
    Answer          ↓
       ↓       Send Escalation Message
   Ask for
  Confirmation
```

## Similarity Matching

The workflow uses a hand-written **Levenshtein Distance** implementation inside an n8n Code node.

For every incoming question, the workflow:

1. Reads all FAQ rows from Google Sheets.
2. Normalizes the user's question.
3. Calculates its similarity with every stored FAQ question.
4. Selects the question with the highest similarity score.
5. Returns the stored answer only if the score is at least **0.60**.

This provides generic matching and avoids hardcoded `if/else` conditions for individual FAQ questions.

## Safe Fallback

If the best similarity score is below **0.60**, the bot does not guess an answer.

Instead, it:

1. Logs the user's question in the `Unanswered Questions` Google Sheet.
2. Sends an escalation message to the user.
3. Allows unanswered questions to be reviewed later and potentially added to the FAQ knowledge base.

## Google Sheets Structure

The project uses a Google Sheets document named:

`FAQ Knowledge Base`

### FAQ Sheet

| question | answer |
| --- | --- |
| FAQ question | Stored answer |

### Unanswered Questions Sheet

| timestamp | user_question |
| --- | --- |
| Time of request | Question that did not pass the threshold |

## Technologies Used

- n8n
- Telegram Bot API
- Google Sheets
- JavaScript
- Levenshtein Distance

## Project Files

- `workflow/faq-bot.json` — exported n8n workflow
- `workflow/README.md` — workflow-specific information
- `screenshots/` — workflow and testing evidence
- `RESOURCES.md` — documentation and references used for the project

## Testing

The workflow was tested with:

- Exact FAQ questions
- Slightly reworded questions
- Misspelled questions
- Questions below the similarity threshold
- Unanswered-question logging
- Admin `/addfaq` commands
- Newly added FAQ questions
- `/yes` confirmation
- `/no` confirmation

All required workflow paths and bonus features were tested successfully.
