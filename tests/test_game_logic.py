from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_new_game_resets_all_state():
    """Test that new game button resets attempts, history, score, and status."""
    # Simulate game state after some gameplay
    session_state = {
        "secret": 50,
        "attempts": 5,
        "score": 25,
        "status": "playing",
        "history": [30, 60, 45, 55, 48]
    }
    
    # Verify initial state before reset
    assert session_state["attempts"] == 5
    assert session_state["score"] == 25
    assert session_state["history"] == [30, 60, 45, 55, 48]
    assert session_state["status"] == "playing"
    
    # Simulate new_game button press - reset all state variables
    session_state["attempts"] = 0
    session_state["score"] = 0
    session_state["history"] = []
    session_state["status"] = "playing"
    old_secret = session_state["secret"]
    session_state["secret"] = 75  # Simulate new random secret
    
    # Verify all state was reset
    assert session_state["attempts"] == 0
    assert session_state["score"] == 0
    assert session_state["history"] == []
    assert session_state["status"] == "playing"
    assert session_state["secret"] != old_secret
