from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0

def test_h():
    assert value("How are you doing?") == 20

def test_non_h():
    assert value("What's up?") == 100
