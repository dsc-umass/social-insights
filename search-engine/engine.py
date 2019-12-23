# Search Engine/Query Management System for Health Insights

import nltk

# Main Method to Manipulate and understand queries
def query(query):
    tokens = nltk.word_tokenize(query)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    if(len(tokens) == 1):
        return singleWordQuery(query)

# Method to handle single word queries like:
""" 
Hospital

San Francisco

"""

def singleWordQuery(query):
    return "this is a single word query"


# Method to Retrive simple dataset queries that query the dataset tables directly
def rawDataSetQuery(query):
    return "This is a raw query to the dataset"

# Method to understand context in query and sentence structure
def context(query):
    return "This is the context of the query"

# Method for query suggest on the frontend
def suggest(query):
    return "did you mean this?"