import pandas as pd 
import re

# Cleaning script --> needs to be optimized for any dataset entry

tweets_new = []
def clean_data():
    tweets = pd.read_csv("../assets/@realDonaldTrump_tweets_V1.csv", encoding="utf-8")
    pattern1 = re.compile(" ' # S % & ' ( ) * + , - . / : ; < = >  @ [ / ] ^ _ { | } ~")
    pattern2 = re.compile("@[A-Za-z0-9]+") 
    pattern3 = re.compile("https?://[A-Za-z0-9./]+")

    for item in tweets:
        tweet = re.sub(pattern1, "", item)   # version 1 of the tweet
        tweet = re.sub(pattern2, "", tweet)
        tweet = re.sub(pattern3, "", tweet)
        tweets_new.append(tweet)

    return pd.DataFrame(tweets_new,columns = ['tweet'])