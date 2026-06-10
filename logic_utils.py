# FIX: Refactored these functions out of app.py's stubs into logic_utils.py
# (with the "Too High"/"Too Low" hint and scoring fixes applied) using
# Claude Code, agent mode, so tests/test_game_logic.py can import and pass.

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    Returns: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score


def guess_distance(guess, secret) -> int:
    """Return absolute distance between guess and secret as ints."""
    try:
        return abs(int(guess) - int(secret))
    except (ValueError, TypeError):
        return 10_000


def closeness(distance: int, span: int) -> tuple:
    """Return (fraction 0..1, label) indicating how close guess was."""
    if span <= 0:
        span = 1
    fraction = max(0.0, 1.0 - distance / span)
    if fraction >= 0.85:
        label = "🔥 Hot"
    elif fraction >= 0.5:
        label = "🌤️ Warm"
    else:
        label = "❄️ Cold"
    return fraction, label
