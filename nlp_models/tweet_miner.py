import tweepy
import json
import sys, os
import pandas as pd
from datetime import datetime
from twitter_credentials import twitter_keys
import pickle

file_key = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)


auth = tweepy.OAuthHandler(twitter_keys['CONSUMER_KEY'], twitter_keys['CONSUMER_SECRET'])
auth.set_access_token(twitter_keys['ACCESS_TOKEN_KEY'], twitter_keys['ACCESS_TOKEN_SECRET'])

api = tweepy.API(auth)

class TweetMiner:

    def __init__(self):
        self.directory = {'home_dir': sys.path[0]}
        self.directory['db_dir'] = sys.path[0] + 'static/dataset/'

    def deCrypt(self, text):
        if text:
            return text.encode('ascii', 'ignore').decode('ascii')
        else:
            return None
    
    def loadIDs(self):
        os.chdir(self.directory['db_dir'])
        pickle_file = open("id_set.pickle", "rb")
        self.idSet = pickle.load(pickle_file)

    def getTweets(self, keyword):
        tweet_id = []
        tweet_date = []
        tweet_text = []
        user_created_at = []
        user_location = []
        tweet_location = []
        tweets = api.search(q = keyword, count = 100)
        for i in range(len(tweets)):
            tweet = tweets[i]
            if tweet.id in self.idSet:
                continue
            tweet_id += tweet.id,
            tweet_date += tweet.created_at,
            tweet_text += self.deCrypt(tweet.text),
            user_created_at += tweet.user.created_at, 
            user_location += None,
            tweet_location += (None, None),
            # print("End")
            # if tweet.coordinates:
            
            # longitude = tweet.coordinates['coordinates'][0]
            # latitude = tweet.coordinates['coordinates'][1]
            # tweet_location += (latitude, longitude),
            # else:
            
        return tweet_id, tweet_date, tweet_text, user_created_at, user_location, tweet_location


    def mineTweets(self, keyword, count):
        tweets_df = pd.DataFrame()
        tweets_df['id'] = list()
        tweets_df['date'] = list()
        tweets_df['text'] = list()
        tweets_df['user_created_at'] = list()
        tweets_df['user_location'] = list()
        tweets_df['tweet_location'] = list()
        id_checker = {}
        self.loadIDs() # to load previously scraped tweets 

        exception = False 

        while len(tweets_df) < count:
            try:
                tweet_id, tweet_date, tweet_text, user_created_at, user_location, tweet_location = self.getTweets(keyword)
                for i in range(len(tweet_id)):
                    if tweet_id[i] not in id_checker:
                        tweets_df = tweets_df.append({'id': tweet_id[i], 'date': tweet_date[i], 'text': tweet_text[i], 'user_created_at': user_created_at[i], 'user_location': user_location[i], 'tweet_location': tweet_location[i]}, ignore_index = True)
                        id_checker[tweet_id[i]] = 1
                print('Fetched ', len(id_checker), ' tweets')
            except Exception as e:
                print("Exception: ", str(e))
                tweets_df.to_csv(self.directory['db_dir'] + file_key + "_" + keyword + '_tweets.csv', index = False)
                exception = True
                break

        
        print("# of " + keyword + " tweets", len(tweets_df))
        print('ID check = ', len(id_checker))
        
        if not exception:
            tweets_df.to_csv(self.directory['db_dir'] + file_key + "_" + keyword + '_tweets.csv', index = False)

    def unitTest(self):
        tweets = api.search(q = 'Trump', count = 100)
        for status in tweets:
            print(status.id)
    

    

if __name__ == "__main__":
    tweet_miner = TweetMiner()
    keyword = sys.argv[1] if len(sys.argv)>1 else 'USElections'
    tweet_miner.mineTweets(keyword, 5000)
    # tweet_miner.mineTweets('us election', 5000)
    # tweet_miner.unitTest()




