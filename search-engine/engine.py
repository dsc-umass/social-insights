# Search Engine/Query Management System for Health Insights

import nltk


def query(query):
    tokens = nltk.word_tokenize(query)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    if(len(tokens) == 1):
        return singleWordQuery(query)


def singleWordQuery(query):
    return "this is a single word query"


def rawDataSetQuery(query):
    return "This is a raw query to the dataset"


def context(query):
    return "This is the context of the query"


print(query("test"))


def suggest(query):
    return "did you mean this?"