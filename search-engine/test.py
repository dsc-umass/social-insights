from suggest import spellcheck

def spellCheckTest():
    print("SpellCheckTest:")
    assert spellcheck("thingg") == "things "

spellCheckTest()