# Testing & Validation

This document describes the tests performed to verify the functionality of the **Customer Support Ticket Bot**.

The workflow was tested through the live Telegram bot after the complete n8n workflow was configured and published.

## Test 1 — Billing Request

### Input

```text
My payment was charged twice. Can you help me with my billing issue?
```

### Expected Behavior

- The Telegram message is received by n8n.
- Input validation accepts the message.
- Gemma 4 classifies the request as `billing`.
- The ticket is logged to Google Sheets.
- The Switch node routes the request to the Billing branch.
- The customer receives the Billing response.

### Result

**Passed**

Evidence:

`../screenshots/01-billing-test.png`

---

## Test 2 — Technical Request & Admin Notification

### Input

```text
My application keeps crashing and I cannot log in. Can you help me fix it?
```

### Expected Behavior

- Gemma 4 classifies the request as `technical`.
- The ticket is logged to Google Sheets.
- The customer receives the Technical support response.
- A separate Technical ticket alert is sent to the administrator.

### Result

**Passed**

This test also validates the implemented admin notification feature.

Evidence:

`../screenshots/02-technical-admin-test.png`

---

## Test 3 — General Request & Live External API

### Input

```text
Hello, I have a general question. Can you also show me the current USD to EUR exchange rate?
```

### Expected Behavior

- Gemma 4 classifies the request as `general`.
- The request is routed to the General branch.
- n8n calls the external exchange-rate API.
- Live USD to EUR data is retrieved.
- The live value is included in the Telegram response.

### Result

**Passed**

Evidence:

`../screenshots/03-general-live-api-test.png`

> The displayed exchange rate may vary because it is retrieved from a live external API.

---

## Test 4 — Invalid / Emoji-Only Input

### Input

```text
❤️
```

### Expected Behavior

- The input validation node detects that the message does not contain meaningful text.
- The message is not sent to the AI classifier.
- The customer receives an invalid-input response.

### Result

**Passed**

Evidence:

`../screenshots/04-invalid-input-test.png`

---

## Test 5 — Valid Text Containing Emoji

### Input

```text
My payment failed 😭 and I need help.
```

### Expected Behavior

- The message passes input validation because it contains meaningful text.
- The emoji does not cause the message to be rejected.
- Gemma 4 classifies the support request.
- The request is routed to the appropriate support branch.

### Result

**Passed**

Evidence:

`../screenshots/05-text-with-emoji-test.png`

---

## Additional Error Handling Tests

During development, additional failure scenarios were manually tested.

### External API Failure

The external API endpoint was temporarily made unavailable during testing.

The workflow:

- Retried the API request.
- Used the API error output after the retries failed.
- Sent a graceful Telegram response informing the customer that the external service was temporarily unavailable.

**Result: Passed**

### Local AI / Ollama Failure

The workflow includes a dedicated error path for failures from the local Ollama service.

When the AI service is unavailable:

- The workflow follows the AI error output.
- The failed ticket is logged.
- The customer receives a graceful service error response.

**Result: Passed**

### Malformed AI Output

The AI parsing logic validates the returned JSON and category.

Malformed JSON or an unsupported category is converted to:

```text
fallback
```

The Switch node then routes the request to the Fallback response.

**Result: Passed**

---

## Test Summary

| Test | Status |
| --- | --- |
| Billing classification and routing | Passed |
| Technical classification and routing | Passed |
| Technical admin notification | Passed |
| General classification and routing | Passed |
| Live external API integration | Passed |
| Google Sheets ticket logging | Passed |
| Emoji-only input rejection | Passed |
| Text with emoji acceptance | Passed |
| External API error handling | Passed |
| Local AI error handling | Passed |
| Malformed AI output fallback | Passed |

## Workflow Evidence

The complete n8n workflow canvas is available at:

`../screenshots/workflow-full-canvas.png`

The exported n8n workflow is available in:

`../workflow/`

---

**DevLab AI Engineering Internship — Week 01 Required Task**
