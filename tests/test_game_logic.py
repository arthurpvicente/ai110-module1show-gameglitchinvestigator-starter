import os
import sys

# Allow running plain `pytest` from the project root by adding the project
# root (parent of this tests/ directory) to sys.path.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess
from app import check_guess as app_check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_hint_tells_player_to_go_lower():
    # Bug 2: a guess above the secret showed "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = app_check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_tells_player_to_go_higher():
    # Bug 2: a guess below the secret showed "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = app_check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_too_high_always_subtracts_points():
    # Bug 3: a "Too High" guess on an even attempt added 5 points instead of subtracting them
    assert update_score(50, "Too High", attempt_number=2) == 45
    assert update_score(50, "Too High", attempt_number=3) == 45
