import sys
sys.path.append("../")
from suggest import edit_distance

def test_edit_distance():
    assert edit_distance("hello", "hel") == 2

