#%% Program to prepare the dataset
import numpy as np 
import pandas as pd
import os, sys, glob
from time import time
import io # for handling files
import pickle# for storing large files

#%% Setting the directory
dataset_path = '../dataset/'
models_path = '../models/'

os.chdir(sys.path[0])
os.chdir(dataset_path)
print(os.getcwd())

#%% Part - I: Collecting domain names from summary.txt
domains = set()
summary = open(dataset_path + 'summary.txt')
contents = summary.read().split('\n')

for i in range(len(contents)-1):
    content = contents[i]
    # print(i, content)
    domain = ""
    for ch in content:
        if ch!='/':
            domain += ch
        else:
            break
    domains.add(domain)

domains = list(domains)
for i in range(len(domains)):
    domains[i] = domains[i].replace(' ', '_')

for ind, domain in enumerate(domains):
    print(ind + 1, domain)


#%% Part-II: Function which returns reviews and ratings for given domain
def getReviewsRatings(domain, ind):
    doc = io.open(dataset_path + domain + '/all.review', 'rb')
    buff = io.BufferedReader(doc)

    ct = 1

    reviews = []
    ratings = []

    content = "abv"

    while True:

        while content[:-1] != b'<rating>' and content:
            content = buff.readline()

        if not content:
            break

        rating = buff.readline()[:-1]
        
        while content[:-1] != b'<review_text>' and content:
            content = buff.readline()
        
        if not content:
            break

        review = buff.readline()[:-1]

        try:
            ratings += [rating.decode('utf-8')]
            reviews += [review.decode('utf-8')]
        except UnicodeDecodeError as err:
            # obj = UnicodeDecodeError['object']
            review = rating[:err.start].decode('utf-8') + rating[err.end+1:].decode('utf-8')
            reviews += [review]

        ct+=1

    print("Domain %d has %d reviews and %d ratings" %(ind, len(reviews), len(ratings)))

    return ratings, reviews
    
#%% Part-III:  Preparing the dataset
all_reviews = []
all_ratings = []
all_domains = []

start = time()
for ind, domain in enumerate(domains):
    if ind==14:
        break
    print(domain, "books" in domain)
    for dom in ["music", "books"]:
        if dom in domain:
            continue
    rating, review = getReviewsRatings(domain, ind+1)
    all_ratings += rating
    all_reviews += review
    all_domains += [domain]*len(rating)
end = time()
print("Total # of ratings = %d" %(len(all_ratings)))
print("Total # of reviews = %d" %(len(all_reviews)))
print("Total time taken : %.2f secs" %(end - start))

#%% Part-IV: Creating labels 
start = time()
labels = []
text = []
product_type = []
for i in range(len(all_ratings)):
    if float(all_ratings[i]) > 3.0:   # positive is 1
        labels += [1]  
        text += [all_reviews[i]]
        product_type += [all_domains[i]]
    elif float(all_ratings[i]) < 3.0:
        labels += [0]
        text += [all_reviews[i]]
        product_type += [all_domains[i]]

#%% Part-V:  Storing the dataset
df = pd.DataFrame()
df['Type'] = product_type
df['Review'] = text
df['Label'] = labels

file_db = open(dataset_path + 'Annotated_Dataset', 'wb')
pickle.dump(df, file_db)
end = time()

print("Dataset stored in %s" %(dataset_path))
print("Time taken %.2f secs" %(end - start))

# %% Loading the dataset
start = time()
file_db = open(dataset_path + 'Annotated_Dataset', 'rb')
df = pickle.load(file_db)
end = time()
print("Time taken to load the dataset %.2f secs" %(end - start))


# %%
