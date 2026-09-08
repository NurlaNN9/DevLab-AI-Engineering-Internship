# Screenshots & Testing Evidence

This directory contains visual evidence of the completed **Customer Support Ticket Bot** workflow and its live Telegram tests.

## Workflow

### Full Workflow Canvas

`workflow-full-canvas.png`

Shows the complete n8n workflow, including:

- Telegram Trigger
- Input Validation
- Local AI Classification
- Google Sheets Logging
- AI-Based Routing
- Category Responses
- External API Integration
- Error Handling
- Technical Admin Notification
- Workflow Documentation Sticky Notes

## Telegram Tests

### 01 — Billing Test

`01-billing-test.png`

Demonstrates successful AI classification and routing of a Billing support request.

### 02 — Technical & Admin Notification Test

`02-technical-admin-test.png`

Demonstrates:

- Technical request classification
- Technical customer response
- Admin Telegram notification

### 03 — General & Live API Test

`03-general-live-api-test.png`

Demonstrates the General branch calling a live external API and returning the current USD to EUR exchange rate in the Telegram response.

### 04 — Invalid Input Test

`04-invalid-input-test.png`

Demonstrates rejection of emoji-only input before it reaches the AI classifier.

### 05 — Text with Emoji Test

`05-text-with-emoji-test.png`

Demonstrates that meaningful text containing an emoji is accepted and processed normally.

## Test Status

All documented test scenarios were successfully completed.

For detailed test cases, expected behavior, and results, see:

`../documentation/testing.md`

---

**DevLab AI Engineering Internship — Week 01 Required Task**
