from suggest import spellcheck
from engine import query


# Tests on Core Search
def singleQueryTest():
    print("Single work query:")
    assert query("hello") == "this is a single word query"

# Spellcheck Tests
def spellCheckTest():
    print("SpellCheckTest:")
    assert spellcheck("thingg") == "things "



def master():
    queryTest()
    spellCheckTest()

master()