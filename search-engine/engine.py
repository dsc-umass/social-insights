# Search Engine/Query Management System for Health Insights

import nltk

def context(query):
    tokens = nltk.word_tokenize(query)
    return tokens


print(context("hello world"))