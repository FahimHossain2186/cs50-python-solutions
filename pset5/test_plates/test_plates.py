from plates import is_valid

def test_cs50():
    assert is_valid("CS50")     == True
    assert is_valid("CS05")     == False
    assert is_valid("CS50P")    == False


def test_beginning_alphabet():
    assert is_valid("50CS")     == False
    assert is_valid("1S50")     == False
    assert is_valid("C150")     == False
    assert is_valid("H")        == False
    assert is_valid("HA")       == True

def test_decimal():
    assert is_valid("PI3.14")   == False

def test_blank_space():
    assert is_valid("CS 50")    == False

def test_length():
    assert is_valid("OUTTIME")  == False
    assert is_valid("ABCDEF")   == True


