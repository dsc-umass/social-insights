import twitter
from keys import *

def authorize():
    api = twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token_key,
                        access_token_secret=access_token_secret)

    print(api.VerifyCredentials())
