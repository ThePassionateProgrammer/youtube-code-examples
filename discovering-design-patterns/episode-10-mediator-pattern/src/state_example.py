"""State comparison: behavior changes based on the current mode/state."""


class WithdrawState:
    def enter_number(self, session, value: int) -> None:
        session.amount = value

    def press_ok(self, session) -> None:
        session.withdraw(session.amount)
        session.state = session.authenticated_state
