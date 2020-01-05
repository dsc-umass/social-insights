import nltk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Use a service account with DB
cred = credentials.Certificate('firebase-admin-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def updateLogs(query):
    doc_ref = db.collection('trending-searches').document('searches-log')
    try:
        doc_ref.set({
            query: datetime.datetime.now()
        }, merge=True)
        print("Logs Updated")
    except:
        print("Error updating logs")


import random

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")

for i in range(10):
    num = random.randrange(0,5)
    randomQuery = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
    print (randomQuery)
    updateLogs(randomQuery)
