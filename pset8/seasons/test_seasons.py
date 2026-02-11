import pytest
from seasons import to_min

def test_imperfect_format():
    with pytest.raises(ValueError):
        to_min('January 1, 1999')
    with pytest.raises(ValueError):
        to_min('2000-03-98')


