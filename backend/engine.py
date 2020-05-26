# Search Engine/Query Management System for Health Insights

import nltk
import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
import datetime

# Use a service account with DB
cred = credentials.Certificate('firebase-admin-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


# Main Method to Manipulate and understand queries
def query(query):
    tokens = nltk.word_tokenize(query)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    if(len(tokens) == 1):
        return singleWordQuery(query)


def singleWordQuery(query):
    return "this is a single word query"


# Method to Retrive simple dataset queries that query the dataset tables directly
def rawDataSetQuery(query):
    return "This is a raw query to the dataset"

# Method to understand context in query and sentence structure
def context(query):
    tokens = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    properNouns = [word for word,pos in tagged if pos == 'NNP'] 
    nouns = [word for word,pos in tagged if pos == 'NN'] 
    print(properNouns)
    return "done"

def updateLogs(query):
    doc_ref = db.collection('trending-searches').document('searches-log')
    try:
        doc_ref.set({
            query: datetime.datetime.now()
        }, merge=True)
        print("Logs Updated")
    except:
        print("Error updating logs")


def engine(query):
    updateLogs(query)
    context(query)
    return query