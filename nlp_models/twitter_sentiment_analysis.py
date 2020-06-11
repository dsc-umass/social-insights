#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re
import os
import sys
import nltk
from nltk.corpus import stopwords
from numpy import array
from numpy import asarray
from numpy import zeros
import matplotlib.pyplot as plt
from numpy import array

from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten
from keras.layers import GlobalMaxPooling1D
from keras.layers import Conv1D
from keras.layers.embeddings import Embedding
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.layers import LSTM


# In[59]:


dataset_path = sys.path[0] + '/dataset/'
model_path  = sys.path[0] + '/models/'


# ### Loading the Twitter dataset

# In[60]:


tweets_dataset = pd.read_csv(dataset_path + 'twitter_sentiments.csv')


# In[61]:


print(tweets_dataset.shape)
print(tweets_dataset.head(10))


# In[62]:


print(tweets_dataset['tweet'][5])


# ### Preprocessing of tweets

# In[63]:


def remove_tags(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)

def preprocess_text(sen):
    # Removing html tags
    sentence = remove_tags(sen)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


# In[64]:


X = []
sentences = list(tweets_dataset['tweet'])
for sen in sentences:
    X.append(preprocess_text(sen))


# In[65]:


print(X[5])


# In[75]:


y = tweets_dataset['label']
y = np.array(y)


# In[76]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=682)


# In[77]:


tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)


# In[78]:


find_len = lambda x: len(x)
longest_sentence_len = max(find_len(sent) for sent in X_train)
print(longest_sentence_len)


# In[79]:


# Adding 1 because of reserved 0 index
vocab_size = len(tokenizer.word_index) + 1

maxlen = 35

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)


# In[80]:


embeddings_dictionary = dict()
glove_file = open(dataset_path + 'glove.6B.100d.txt', encoding="utf8")

for line in glove_file:
    records = line.split()
    word = records[0]
    vector_dimensions = asarray(records[1:], dtype='float32')
    embeddings_dictionary [word] = vector_dimensions
glove_file.close()


# In[81]:


embedding_matrix = zeros((vocab_size, 100))
for word, index in tokenizer.word_index.items():
    embedding_vector = embeddings_dictionary.get(word)
    if embedding_vector is not None:
        embedding_matrix[index] = embedding_vector


# ## RNN (LSTM)

# In[83]:


model = Sequential()
embedding_layer = Embedding(vocab_size, 100, weights=[embedding_matrix], input_length=maxlen , trainable=False)
model.add(embedding_layer)
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

print(model.summary())


# In[84]:


history = model.fit(X_train, y_train, batch_size=128, epochs=6, verbose=1, validation_split=0.2)


# In[85]:


score = model.evaluate(X_test, y_test, verbose=1)

print("Test Accuracy:", score[1])


# In[86]:


plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'], loc = 'upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train','test'], loc = 'upper left')
plt.show()


# In[87]:


model.save(model_path + 'rnn_lstm_twitter.h5')

