import pytest
from twttr import shorten
#from pset2.twttr.twttr import shorten

shortened_text = {
    "twitter": "twttr",
    "what's yOur name?": "wht's yr nm?",
    "CS50": "CS50"
}

def test_shorten():
    for text in shortened_text:
        assert shorten(text) == shortened_text[text]
