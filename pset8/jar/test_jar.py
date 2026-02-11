import pytest
from jar import Jar

def test_init():
    jar = Jar()

    assert jar._size == 0
    assert jar._capacity == 12

def test_str():
    jar = Jar()

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()

    assert jar.deposit(12) == None
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    assert jar.withdraw(3) == None
    with pytest.raises(ValueError):
        jar.withdraw(7)
