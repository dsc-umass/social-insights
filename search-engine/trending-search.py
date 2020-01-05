import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import nltk

cred = credentials.Certificate('firebase-admin-key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
searches_log = db.collection('trending-searches').document('searches-log')

text = ""
try:
    doc = searches_log.get()
    returnJson = doc.to_dict()
    for key in returnJson:
        text = text + key + " "
    print("Text Created")
except google.cloud.exceptions.NotFound:
    print('No such document!')

allWords = nltk.tokenize.word_tokenize(text)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)

stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)   


mostCommon = allWordExceptStopDist.most_common(10)

mostCommonQuery = []
for word, frequency in mostCommon:
    if word != '.' and word != ',':
        mostCommonQuery.append(word)

print(mostCommonQuery)

topSearches_tags = db.collection('trending-searches').document('top-searches-tags')

for i in range(len(mostCommonQuery) - 1):
    try :
        topSearches_tags.set({
            mostCommonQuery[i]: i
        }, merge=True)
    except:
        print("error")



