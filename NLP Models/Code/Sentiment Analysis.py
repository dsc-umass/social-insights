#%%
import pickle
import os, sys
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

# %% Setting the directory
os.chdir(sys.path[0])
dataset_path = '../sorted_data/'
models_path = '../Models/'

#%% Loading the dataset
start = time()
db = open(dataset_path + 'Annotated_Dataset', 'rb')
df = pickle.load(db)
product_type = df['Type']
reviews = df['Review']
labels = df['Label']
end = time()
print("Time taken to load dataset %.2f secs" %(end -start))

# %% Sample of dataset
df.head()

#%% Distribution of class labels
print("Distribution of class labels : ")
print(df['Label'].value_counts())

#%% Fetching reviews and corresponding labels
X, y = [], []
for i in range(len(df)):
    X.append(df['Review'][i])
    y.append(df['Label'][i])
print("Fetched the dataset")

#%% Sampling of dataset to make class distribution equal

# Fetching index of positive and negative reviews
# pos_index = df['Label'].index[df['Label']==1].tolist()
# neg_index = df['Label'].index[df['Label']==0].tolist()

# size_of_smaller_class = 184231

# positive_reviews = df.iloc[pos_index, :].sample(size_of_smaller_class)
# negative_reviews = df.iloc[neg_index, :].sample(size_of_smaller_class)

# smol_df = positive_reviews.append(negative_reviews)
# smol_X = smol_df['Review']
# smol_y = smol_df['Label']
# X = np.array(smol_X)
# y = np.array(smol_y)

# print("Size of new dataset ", len(X))

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

# %% Preprocessing-I the data
# start = time()
# X = preprocessReview(X, remove_stopwords = True, stemming = True, lemmatize = True)
# end = time()
# print("Time taken to preprocess the data %.2f secs" %(end - start))

# # Split dataset into train and test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, shuffle = True, random_state = 589)
# print("Train-test split : %d-%d" %(len(X_train), len(X_test)))

# db = []
# db.append((X_train, y_train))
# db.append((X_test, y_test))
# v_db = open(dataset_path + 'SLS Preprocessed data', 'wb')
# pickle.dump(db, v_db)
# print("Stored SLS preprocessed dataset in %s" %(dataset_path))

# %% Preprocessing-II the data
start = time()
X = preprocessReview(X, clean=True)
end = time()
print("Time taken to preprocess the data %.2f secs" %(end - start))

# Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, shuffle = True, random_state = 589)
print("Train-test split : %d-%d" %(len(X_train), len(X_test)))

db = []
db.append((X_train, y_train))
db.append((X_test, y_test))
v_db = open(dataset_path + 'C Preprocessed data', 'wb')
pickle.dump(db, v_db)
print("Stored C preprocessed dataset in %s" %(dataset_path))

#%% Loading the SLS preprocessed dataset 
# start = time()
# v_db = open(dataset_path + 'SLS Preprocessed data', 'rb')
# db = pickle.load(v_db)
# X_train, y_train = db[0]
# X_test, y_test = db[1]
# end = time()
# print("Time taken to load SLS preprocessed data %.2f secs" %(end - start))

# X_train = np.array(X_train)
# X_test = np.array(X_test)
# y_train = np.array(y_train)
# y_test = np.array(y_test)

# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
#%% Loading the C preprocessed dataset 

# start = time()
# v_db = open(dataset_path + 'C Preprocessed data', 'rb')
# db = pickle.load(v_db)
# X_train, y_train = db[0]
# X_test, y_test = db[1]
# end = time()
# print("Time taken to load C preprocessed data %.2f secs" %(end - start))

# X_train = np.array(X_train)
# X_test = np.array(X_test)
# y_train = np.array(y_train)
# y_test = np.array(y_test)
# %% Sample of preprocessed data
print("Sample of preprocessed data : \n%s" %(X_train[0]))

#%% Functions to vectorize the data

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
# start = time()
# X_train_tf, X_test_tf = vectorize(X_train, X_test, Tfidf=True)
# end = time()
# print("Time taken to Tf-IDF vectorize the data %.2f secs" %(end - start))

start = time()
X_train_bow, X_test_bow = vectorize(X_train, X_test, bag_of_words = True)
end = time()
print("Time taken to BOW vectorize the data %.2f secs" %(end - start))


# %% Splitting the train set into train-validation set
# X_train, X_val, y_train, y_val = train_test_split(X_train_bow, y_train, test_size = 0.15, shuffle = True, random_state = 589)
# print("Train-Validation split : %d-%d" %(X_train.shape[0], X_val.shape[0]))

#%% Logistic Regression Classifier

# Hyper parameter tuning
# print("Grid Search for hyper-parameter tuning....\n")

# best_model = None
# best_acc = 0
# times = []
# c_values = [0.1, 0.25, 0.5, 0.75, 1]
# penalties = ['l1']
# solvers = ['saga']

# grid_params = [ (c, penalty, solver) for c in c_values for penalty in penalties for solver in solvers]
# best_params = None
# it = 0

# for (c, penalty, solver) in grid_params:
#     it += 1
#     # print (str(it) + "/"+ str(len(grid_params)), end = ", ")
#     lr = LogisticRegression(C=c, solver = solver, penalty = penalty)
#     lr.fit(X_train, y_train)
#     val_acc = accuracy_score(y_val, lr.predict(X_val))
#     print(val_acc)
#     if val_acc > best_acc:
#         best_acc = val_acc
#         best_model = lr
#         best_params = (c, penalty, solver)

# print("Best Params : ", best_params)

lr = LogisticRegression(C=1, solver = 'saga')
lr.fit(X_train_bow, y_train)

# Performance of best model on unseen data
test_acc = accuracy_score(y_test, lr.predict(X_test_bow))
print("\nLogReg accuracy on test-set = %.4f" % (test_acc))

#%% DecisionTree Classifier

# best_model = None
# best_acc = 0

# max_depths = [3, 5, 7, 9, 10]
# max_features = [4, 8, 12, 16, 20, 24]

# grid_params = [ (md, mf) for md in max_depths for mf in max_features]
# best_params = None
# it = 0

# for (md, mf) in grid_params:
#     it += 1
#     print (str(it) + "/"+ str(len(grid_params)), end = ", ")
#     dt = DecisionTreeClassifier(criterion='entropy', random_state=589, max_depth=md, max_features=mf)
#     dt.fit(X_train, y_train)
#     val_acc = accuracy_score(y_val, dt.predict(X_val))
#     if val_acc > best_acc:
#         best_acc = val_acc
#         best_model = dt
#         best_params = (md, mf)

# print("Best params", best_params)

dt = DecisionTreeClassifier(criterion='entropy', random_state=589)
dt.fit(X_train_bow, y_train)

# Performance of best model on unseen data
test_acc = accuracy_score(y_test, dt.predict(X_test_bow))
print("\nDTree accuracy on test-set = %.4f" % (test_acc))

#%% XGBoost Classifier

best_model = None
best_acc = 0

lrs = [0.01, 0.05, 0.1, 0.15, 0.2]
reg_alphas = [0, 0.001, 0.005, 0.01, 0.05]

grid_params = [ (lr, reg) for lr in lrs for reg in reg_alphas]

best_params = None
it = 0

# for (lr, reg) in grid_params:
#     it += 1
#     print (str(it) + "/"+ str(len(grid_params)), end = ", ")
#     try:
#         xgb = XGBClassifier(random_state=589, learning_rate=lr, reg_alpha = reg)
#         xgb.fit(X_train, y_train)
#         val_acc = accuracy_score(y_val, xgb.predict(X_val))
#         if val_acc > best_acc:
#             best_acc = val_acc
#             best_model = xgb
#             best_params = (lr, reg)
#     except:
#         continue

# print("Best params", best_params)

xgb = XGBClassifier(random_state=589)
xgb.fit(X_train_bow, y_train)

# Performance of best model on unseen data
test_acc = accuracy_score(y_test, xgb.predict(X_test_bow))
print("\nXGB accuracy on test-set = %.4f" % (test_acc))

