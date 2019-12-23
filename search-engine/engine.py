# Search Engine/Query Management System for Health Insights

import nltk


def query(query):
    tokens = nltk.word_tokenize(query)
    print(tokens)
    if(len(tokens) == 1):
        return singleWordQuery(query)


def singleWordQuery(query):
    return "this is a single word query"


def rawDataSetQuery(query):
    return "This is a raw query to the dataset"


print(query("test"))