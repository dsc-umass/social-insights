import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
# print(datetime.datetime.now())
# Use a service account
cred = credentials.Certificate('firebase-admin-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection('trending-searches').document('searches-log')

# try:
#     doc = doc_ref.get()
#     print('Document data: {}'.format(doc.to_dict()))
# except google.cloud.exceptions.NotFound:
#     print('No such document!')

doc_ref.set({
    "hello world": datetime.datetime.now(),
    "hello": datetime.datetime.now()
}, merge=True)
