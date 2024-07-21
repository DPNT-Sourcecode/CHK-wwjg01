from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("AAABBEEDDCAAB") == 375
    def test_empty(self):
        assert checkout_solution.checkout("") == 0
    def test_invalid(self):
        assert checkout_solution.checkout("zczxv(#!__E(fdj))") == -1
    def test_U_bogof(self):
        assert checkout_solution.checkout("UUUU") == 120
    def test_checkout_new_items(self):
        assert checkout_solution.checkout("QQQVZYYXAAA") == 322
