from lib.solutions.HLO.hello_solution import hello

class TestHlo():
    def test_hlo(self):
        assert hello("Adam") == "Hello, Adam"

TestHlo.test_hlo()