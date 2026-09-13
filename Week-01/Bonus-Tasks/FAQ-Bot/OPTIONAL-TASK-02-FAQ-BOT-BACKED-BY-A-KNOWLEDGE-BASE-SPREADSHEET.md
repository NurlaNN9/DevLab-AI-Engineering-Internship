# FAQ Bot Backed by a Knowledge-Base Spreadsheet

Build a bot that answers frequently asked questions from a Google Sheet of question/answer pairs using computed text similarity in an n8n Function node, rather than a fixed button menu. This introduces generic text-matching logic that foreshadows the retrieval concept used in Week 4's RAG task.

## Learning Objectives

- Read a spreadsheet as a lookup table inside a workflow
- Use a Function/Code node to compute string similarity between the user's question and stored questions
- Return the closest-matching answer only when it is above a similarity threshold
- Handle the 'no match found' case by escalating instead of guessing
- Log unanswered questions so the FAQ set can be grown over time

## Must-Have Features

- **FAQ Spreadsheet Source** — Question/answer pairs are stored and read from a spreadsheet, not hardcoded in the workflow.
- **Similarity Matching Code Node** — A Function/Code node computes a similarity score between the incoming question and every stored question.
- **Threshold-Based Fallback** — Below a configured similarity threshold, the bot does not guess an answer.
- **Unanswered-Question Logging** — Every question that falls below threshold is logged to a sheet/table for later review.
- **Telegram Reply** — The matched answer (or the escalation message) is sent back to the user through Telegram.
- **Anti-Cheat: Generic Matching Only** — Matching must be computed generically via a similarity function; hardcoding if/else per individual question is not accepted and will be rejected.

## Bonus Features

- Add an admin command that lets you append a new FAQ pair live via chat
- Tune the similarity threshold for typo tolerance and document the trade-off
- Add a follow-up 'did that answer your question?' confirmation step

## Technical Requirements

- **n8n Code/Function Node** — JavaScript-based; used to compute similarity.
- **A String-Similarity Approach** — An npm string-similarity library or a hand-written Levenshtein-distance implementation.

## Levenshtein Distance Explainer

A plain-language explanation of edit distance and how it is used for fuzzy text matching:

https://en.wikipedia.org/wiki/Levenshtein_distance
