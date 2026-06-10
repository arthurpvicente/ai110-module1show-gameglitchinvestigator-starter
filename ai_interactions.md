# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Add a "Guess History" feature to the Glitchy Guesser Streamlit app. The feature should:
- Store rich per-guess records (attempt number, guess value, outcome, closeness fraction, and a 🔥/🌤️/❄️ label) in `st.session_state.history` instead of a flat list of raw values.
- Compute closeness against the true integer secret at submit time (not the glitched even-attempt string secret) so the data is correct even after New Game resets the secret.
- Render a 📜 Guess History section in the sidebar (newest-first) with a direction arrow (⬆️/⬇️/✅/⚠️), a labeled progress bar, and an empty-state caption when no guesses exist.
- Persist history across New Games (do not clear it on reset).
- Expose two pure helper functions (`guess_distance` and `closeness`) in `logic_utils.py` and cover them with pytest unit tests.

**What did the agent do?**

1. Read `logic_utils.py`, `app.py`, `tests/test_game_logic.py`, and `ai_interactions.md` to understand the existing code structure.
2. Added `guess_distance(guess, secret) -> int` and `closeness(distance, span) -> (float, str)` to `logic_utils.py` after `update_score`, with a try/except sentinel for un-coercible inputs and a guard against zero span.
3. Added `from logic_utils import guess_distance, closeness` to `app.py`.
4. Added the 📜 Guess History sidebar block after the existing sidebar captions, reading from `st.session_state.get("history", [])` (guarded so it works before session-state initializes).
5. Replaced the two flat `st.session_state.history.append(...)` calls inside the `if submit:` block with structured dict records; invalid guesses get `fraction=None` and `outcome="Invalid"`, valid guesses get closeness computed against `st.session_state.secret` (the true int).
6. Added 9 new pytest cases in `tests/test_game_logic.py` covering `guess_distance` (exact, symmetric, str secret, un-coercible sentinel) and `closeness` (Hot/Warm/Cold thresholds, negative-fraction clamp, zero-span no-crash).
7. Ran `python -m pytest -q` — all 21 tests (12 original + 9 new) passed.

**What did you have to verify or fix manually?**

No manual corrections were needed. The agent read the files before editing to match existing code style, used `st.session_state.get("history", [])` to avoid a KeyError in the sidebar (which renders before the `if "history" not in st.session_state` init block), and directed closeness computation at `st.session_state.secret` rather than the glitched local `secret` variable — all identified from reading the code rather than requiring human correction.

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
