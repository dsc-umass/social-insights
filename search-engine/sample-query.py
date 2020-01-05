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