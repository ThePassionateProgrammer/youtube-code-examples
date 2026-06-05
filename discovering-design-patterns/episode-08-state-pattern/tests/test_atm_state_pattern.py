from src import procedural_atm as procedural
from src.state_atm import ATMSession, WELCOME, AUTHENTICATED, WITHDRAW, DEPOSIT


def test_same_input_has_different_meanings_in_procedural_version():
    session = procedural.ATMSession()
    procedural.enter_number(session, "1234")
    assert session.pin == "1234"

    session.mode = "withdraw"
    procedural.enter_number(session, 100)
    assert session.amount == 100

    session.mode = "deposit"
    procedural.enter_number(session, 250)
    assert session.amount == 250


def test_state_pattern_moves_meaning_into_current_state():
    session = ATMSession()
    session.enter_number("1234")
    assert session.pin == "1234"
    session.press_ok()
    assert session.state is AUTHENTICATED

    session.select_withdraw()
    assert session.state is WITHDRAW
    session.enter_number(100)
    session.press_ok()
    assert session.balance == 400
    assert session.state is AUTHENTICATED

    session.select_deposit()
    assert session.state is DEPOSIT
    session.enter_number(250)
    session.press_ok()
    assert session.balance == 650
    assert session.deposits == [250]


def test_state_objects_are_shared_flyweights():
    first = ATMSession()
    second = ATMSession()

    assert first.state is WELCOME
    assert second.state is WELCOME
    assert first.state is second.state

    first.enter_number("1234")
    first.press_ok()
    first.select_withdraw()

    second.enter_number("1234")
    second.press_ok()
    second.select_withdraw()

    assert first.state is WITHDRAW
    assert second.state is WITHDRAW
    assert first.state is second.state
    assert first is not second


def test_cancel_transition_is_shared_default_behavior():
    session = ATMSession()
    session.enter_number("1234")
    session.press_ok()
    session.select_withdraw()
    session.enter_number(75)

    session.press_cancel()

    assert session.state is AUTHENTICATED
    assert session.amount is None
    assert "Cancelled" in session.messages
