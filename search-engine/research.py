# import jwt
# import json

# with open('secret.json') as json_file:
#     secret = json.load(json_file)['secret']

# dataJson = {
#     'hello': 'weird'
# }

# encoded = jwt.encode(dataJson, secret, algorithm='HS256')

# print(encoded)

# encoded_test = encoded

# decoded = jwt.decode(encoded_test, secret, algorithms=['HS256'])

# print(decoded)


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. It is pretty good except that."

import nltk
allWords = nltk.tokenize.word_tokenize(text)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)

stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)   


mostCommon = allWordExceptStopDist.most_common(10)

test = []
for word, frequency in mostCommon:
    if word != '.' and word != ',':
        test.append(word)

print(test)

# for word, frequency in allWordDist.most_common(10):
#     print('%s;%d' % (word, frequency))