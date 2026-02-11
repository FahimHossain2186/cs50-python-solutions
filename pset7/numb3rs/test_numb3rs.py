from numb3rs import validate

def test_under255():
    assert validate("1.2.3.4 ")         == False
    assert validate("127.0.0.1")        == True
    assert validate("255.255.255.0")    == True

def test_above255():
    assert validate("255.255.255.256")  == False
    assert validate("1.2.3.1000")       == False
    assert validate("1.999.999.999")    == False

def test_leading_zeros():
    assert validate("1.5.001.8")        == False
    assert validate("1.2.3.07")         == False

def test_negative():
    assert validate("-1.2.3.4")         == False
    assert validate("1.2.-3.5")         == False

def test_partial_numbers():
    assert validate("1.2.3.4")          == True
    assert validate("2.3.4 ")           == False
    assert validate("2.3.4.7.8")        == False
    assert validate("1..2.3")           == False
    assert validate(".1.2.3.4")         == False
    assert validate("1.2.3.4.")         == False

def test_non_numeric():
    assert validate("cat")              == False
    assert validate("cat.dog.1.2")      == False
    assert validate("1.2.3.a")          == False
