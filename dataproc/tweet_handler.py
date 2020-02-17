
import tweepy 
import pandas as pd
import sys
import csv

from twitter_auth import *
from keys import *

# Function to extract tweets 
def get_tweets(username): 

    authorize()          
    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

    # Access to user's access key and access secret 
    auth.set_access_token(access_token_key, access_token_secret) 

    # Calling api 
    api = tweepy.API(auth) 
    #set count to however many tweets you want - max count is 3200 and this doesn't have any effect if it is more than 3200
    number_of_tweets = 3200

    twitter_record = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):

    #username, tweet id, date/time, text
        twitter_record.append([username, tweet.id_str,tweet.source, tweet.created_at,tweet.retweet_count,tweet.favorite_count, tweet.text.encode("utf-8")])

    #write to a new csv file from the array of tweets
    outfile = "../assets/" + username + "_tweets_V1.csv"
    print ("writing to " + outfile)
    with open(outfile, 'w+') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['User_Name', 'Tweet_ID', 'Source', 'Created_date','Retweet_count','Favorite_count','Tweet'])
        writer.writerows(twitter_record)
    # user name
get_tweets("@realDonaldTrump")  