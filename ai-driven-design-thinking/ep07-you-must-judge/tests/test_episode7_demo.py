import unittest

from src.episode7_demo import (
    process_payment_procedural,
    PaymentProcessorOOish,
    CardPayment,
    PayPalPayment,
    BankTransfer,
    PaymentService,
    build_payment_service,
)


class TestEpisode7Demo(unittest.TestCase):
    def test_procedural_card(self) -> None:
        self.assertEqual("CHARGE CARD $100", process_payment_procedural("card", 100))

    def test_ooish_is_still_procedural(self) -> None:
        processor = PaymentProcessorOOish()
        self.assertEqual("CHARGE PAYPAL $50", processor.process("paypal", 50))

    def test_payment_methods_have_agency(self) -> None:
        self.assertEqual("CHARGE CARD $100", CardPayment().charge(100))
        self.assertEqual("CHARGE PAYPAL $100", PayPalPayment().charge(100))
        self.assertEqual("INITIATE BANK TRANSFER $100", BankTransfer().charge(100))

    def test_payment_service_routes_without_knowing_how(self) -> None:
        service = build_payment_service()
        self.assertEqual("CHARGE CARD $100", service.process("card", 100))

    def test_open_closed_add_a_method_without_touching_service(self) -> None:
        class CryptoPayment:
            # No inheritance needed for this test; duck typing works too.
            def charge(self, amount: int) -> str:
                return f"CHARGE CRYPTO ${amount}"

        service = PaymentService({"crypto": CryptoPayment()})  # type: ignore[arg-type]
        self.assertEqual("CHARGE CRYPTO $200", service.process("crypto", 200))

    def test_unknown_payment_type_raises(self) -> None:
        service = build_payment_service()
        with self.assertRaises(ValueError):
            service.process("cash", 10)


if __name__ == "__main__":
    unittest.main()
