# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt used:**

```
Use your AI coding assistant to identify three potential "edge case" inputs
(e.g., negative numbers, decimals, or extremely large values) that might
still break your game. Then generate a suite of pytest cases in
tests/test_game_logic.py that verify the game handles these inputs gracefully.
```

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number guess (e.g., `"-5"`) | (see prompt above) | `test_parse_guess_handles_negative_numbers` and `test_negative_guess_is_too_low` — confirm `parse_guess("-5")` returns `(True, -5, None)` and `check_guess(-5, 50)` returns `"Too Low"` without crashing | Yes | A player could type a negative number, which is outside the 1-100 range. Since `parse_guess` only checks for empty input, a negative number could slip through and potentially cause weird comparisons — good to confirm it's just treated as "Too Low" instead of erroring. |
| Decimal guess (e.g., `"50.5"`) | (see prompt above) | `test_parse_guess_handles_decimal_input` and `test_decimal_guess_can_still_win` — confirm `parse_guess("50.5")` truncates to `50` instead of being rejected as "not a number" | Yes | The input box is free text, so a player could easily type a decimal by mistake. `parse_guess` has special-case logic (`int(float(raw))`) for strings containing `"."`, so it's worth a test to make sure that branch truncates correctly instead of throwing or returning an error. |
| Extremely large guess (e.g., `"999999999999999999999999999999"`) | (see prompt above) | `test_parse_guess_handles_extremely_large_numbers` and `test_extremely_large_guess_is_too_high` — confirm a 30-digit number string parses without overflow and is correctly reported as `"Too High"` | Yes | Unlike many languages, Python integers don't overflow, but it's still worth verifying that nothing downstream (string conversion, comparisons) breaks when a guess is dramatically larger than any possible secret. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
