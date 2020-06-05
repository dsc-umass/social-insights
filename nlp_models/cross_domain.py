#%% Program for implementing cross domain sentiment classification
import pickle
import os
import scipy
import numpy as np 
import pandas as pd   
from time import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from nltk.stem.porter import PorterStemmer
import re


#%% Setting the directory
dataset_path = '../dataset/'
models_path = '../models/'

#%% Loading the dataset
start = time()
db = open(dataset_path + 'Annotated_Dataset', 'rb')
df = pickle.load(db)
product_type = df['Type']
reviews = df['Review']
labels = df['Label']
end = time()
print("Time taken to load dataset %.2f secs" %(end -start))

#%% Sample of dataset
df.head()

#%% Distribution of class labels
print("Distribution of class labels : ")
print(df['Label'].value_counts())

#%% Distribution of reviews domain-wise
print("Domain-wise distribution :")
print(df['Type'].value_counts())

# %% Consider two domains
domain1 = "video"
domain2 = "apparel"

X_train, y_train = [], []
X_test, y_test = [], []

for i in range(len(df)):
    if df['Type'][i]==domain1:
        X_train.append(df['Review'][i])
        y_train.append(df['Label'][i])
    if df['Type'][i]==domain2:
        X_test.append(df['Review'][i])
        y_test.append(df['Label'][i])

X_train, y_train = np.array(X_train), np.array(y_train)
X_test, y_test = np.array(X_test), np.array(y_test)

print("Train-test split : %d - %d" %(len(y_train), len(y_test)))

# %% Stored dataset
# pickle.dump([(X_train, y_train), (X_test, y_test)], open(dataset_path + "CrossDomain", "wb"))

def loadData():
    db = pickle.load(open(dataset_path + "CrossDomain", "rb"))
    X_train, y_train = db[0]
    X_test, y_test = db[1]


    X_train, y_train = np.array(X_train), np.array(y_train)
    X_test, y_test = np.array(X_test), np.array(y_test)
    print("Train-test split : %d - %d" %(len(y_train), len(y_test)))

#%% Functions to preprocess the data

useless_symbols = re.compile("[.;:!\'?,\"()\[\]`~#$&*{}]")
space_reqd = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def cleanReviews(reviews):
    reviews = [useless_symbols.sub("", line.lower()) for line in reviews]
    reviews = [space_reqd.sub(" ", line) for line in reviews]
    return reviews
# Function to remove stop words
def removeStopwords(reviews):
    stop_words = stopwords.words('english')
    clean_reviews = []
    for review in reviews:
        words = review.split()
        cleaned = [word for word in words if word not in stop_words]
        cleaned = ' '.join(cleaned)
        clean_reviews.append(cleaned)
    return clean_reviews

# Function for Stemming
def stemReview(reviews):
    clean_reviews = []
    stemmer = PorterStemmer()
    for review in reviews:
        words = review.split()
        cleaned = [stemmer.stem(word) for word in words]
        cleaned = ' '.join(cleaned)
        clean_reviews.append(cleaned)
    return clean_reviews

# Funtion for lemmatization
def lemmatizeReview(reviews):
    clean_reviews = []
    lemmatizer = WordNetLemmatizer()
    for review in reviews:
        words = review.split()
        cleaned = [lemmatizer.lemmatize(word) for word in words]
        cleaned = ' '.join(cleaned)
        clean_reviews.append(cleaned)
    return clean_reviews

# Utility method to apply suitable preprocessor
def preprocessReview(reviews, clean = False, remove_stopwords = False, stemming = False, lemmatize = False):
    if clean:
        reviews = cleanReviews(reviews)
    if remove_stopwords:
        reviews = removeStopwords(reviews)
    if stemming:
        reviews = stemReview(reviews)
    if lemmatize:
        reviews = lemmatizeReview(reviews)
    return reviews

# %% Preprocessing the data

X_train = preprocessReview(X_train, clean = True)
X_test = preprocessReview(X_test, clean = True)

# %% Functions to vectorize the data

# One-hot encoding vectorizer
def oneHotVectorize(X_train, X_test):
    cv = CountVectorizer(binary=True)
    cv.fit(X_train)
    X_train= cv.transform(X_train)
    X_test = cv.transform(X_test)
    return X_train, X_test

# Bag of Words vectorizer
def wordCountVectorize(X_train, X_test):
    cv = CountVectorizer(binary = False)
    cv.fit(X_train)
    X_train= cv.transform(X_train)
    X_test = cv.transform(X_test)
    return X_train, X_test

# TF-IDF Vectorizer 
def tfidfVectorize(X_train, X_test):
    tfidf = TfidfVectorizer()
    tfidf.fit(X_train)
    X_train = tfidf.transform(X_train)
    X_test = tfidf.transform(X_test)
    return X_train, X_test

def vectorize(X_train, X_test, one_hot = False, bag_of_words = False, Tfidf = False):
    if one_hot:
        X_train, X_test = oneHotVectorize(X_train, X_test)
    if bag_of_words:
        X_train, X_test = wordCountVectorize(X_train, X_test)
    if Tfidf:
        X_train, X_test = tfidfVectorize(X_train, X_test)
    return X_train, X_test

# %% Vectorizing the data
train_dummy, test_dummy = X_train, X_test

tfidf = TfidfVectorizer()
tfidf.fit(train_dummy)
train_dummy = tfidf.transform(train_dummy)

tfidf = TfidfVectorizer()
tfidf.fit(test_dummy)
test_dummy = tfidf.transform(test_dummy)

min_features = min(train_dummy.shape[1], test_dummy.shape[1])
print(train_dummy.shape, test_dummy.shape)

tfidf = TfidfVectorizer(max_features=min_features)
tfidf.fit(X_train)
X_train = tfidf.transform(X_train)
X_test = tfidf.transform(X_test)
# tfidf = TfidfVectorizer(max_features=min_features)
# tfidf.fit(X_test)
# X_test = tfidf.transform(X_test)
print(X_train.shape, X_test.shape)

# %% Fitting the classifier

lr = LogisticRegression(C=1)
lr.fit(X_train, y_train)

# Performance of best model on unseen data
test_acc = accuracy_score(y_test, lr.predict(X_test))
print("\nLogReg accuracy on test-set = %.4f" % (test_acc))

dt = DecisionTreeClassifier(criterion='entropy', random_state=589)
dt.fit(X_train, y_train)

# Performance of best model on unseen data
test_acc = accuracy_score(y_test, dt.predict(X_test))
print("\nDTree accuracy on test-set = %.4f" % (test_acc))

xgb = XGBClassifier(random_state=589)
xgb.fit(X_train, y_train)

# Performance of best model on unseen data
test_acc = accuracy_score(y_test, xgb.predict(X_test))
print("\nXGB accuracy on test-set = %.4f" % (test_acc))


# %%
