import pytest
from working import convert

def test_amtopm():
    assert convert("9 AM to 5 PM")          == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM")    == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM")      == "10:00 to 20:50"

def test_pmtoam():
    assert convert("10:30 PM to 8 AM")      == "22:30 to 08:00"
    assert convert("7:30 PM to 6:00 AM")    == "19:30 to 06:00"

def test_corner_cases():
    assert convert("12:00 PM to 10:30 PM")  == "12:00 to 22:30"
    assert convert("12:00 AM to 10:30 AM")  == "00:00 to 10:30"

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("12:60 PM to 10:30 PM")

def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13:00 PM to 10:30 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("12:00 to 10:30")
    with pytest.raises(ValueError):
        convert("12:00 PM - 10:30AM")
    with pytest.raises(ValueError):
        convert("working from 12:00 PM to 10:30 AM")
