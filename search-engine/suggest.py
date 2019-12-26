import nltk
"""
Suggest will work the following way:
    Spellcheck 
        Both have to be as close as the current query:
        Sugges queries that you have searched before
        Trending search 

"""
def context(query):
    tokens = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    properNouns = [word for word,pos in tagged if pos == 'NNP'] 
    nouns = [word for word,pos in tagged if pos == 'NN'] 
    print(properNouns)
    return "done"

context("Michael Jackson was a legandary basketball player who played in New York.")

def suggest(query):
    return "did you mean this?"