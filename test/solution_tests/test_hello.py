from test_import import hello

class TestHlo():
    def test_hlo(self):
        assert hello() == "Hello, Adam"

test = TestHlo()
test.test_hlo()