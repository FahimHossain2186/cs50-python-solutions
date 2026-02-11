from um import count

def test_normal():
    assert count("hello, um, world")            == 1
    assert count("um, hello, um, world ")       == 2
    assert count("UM....")                      == 1
    assert count("Um, thanks for the album.")   == 1
    assert count("Um, thanks, um...,")          == 2

def test_punctuation():
    assert count("um?")                         == 1

def test_um_in_word():
    assert count("yum")                         == 0
    assert count("yummy")                       == 0
