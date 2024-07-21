from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AAABBBD") == 220 #130(deal) + 45(deal) + 30 + 15