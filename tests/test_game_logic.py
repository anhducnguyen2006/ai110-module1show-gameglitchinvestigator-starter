from logic_utils import check_guess

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


def test_check_guess_message_mapping_not_reversed():
    # Regression test: previously higher/lower hint mapping was inverted.
    high_outcome, high_message = check_guess(60, 50, with_message=True)
    low_outcome, low_message = check_guess(40, 50, with_message=True)

    assert high_outcome == "Too High"
    assert high_message == "📉 Go LOWER!"
    assert low_outcome == "Too Low"
    assert low_message == "📈 Go HIGHER!"
