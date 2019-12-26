import nltk
import time


start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))
    

"""
Suggest will work the following way:
    - Spellcheck 
    - Both have to be as close as the current query:
        Sugges queries that you have searched before
        Trending searchs

"""
def context(query):
    tokens = nltk.word_tokenize(query)
    tagged = nltk.pos_tag(tokens)
    print(tagged)
    properNouns = [word for word,pos in tagged if pos == 'NNP'] 
    nouns = [word for word,pos in tagged if pos == 'NN'] 
    print(properNouns)
    return "done"


def suggest(query):
    return "did you mean this?"

startTime()
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

print(edit_distance("Helloworld ahsd", "HalloWorld"))
