from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AAABBEEDDCAAB") == 375
    def test_empty(self):
        assert checkout_solution.checkout("") == 0