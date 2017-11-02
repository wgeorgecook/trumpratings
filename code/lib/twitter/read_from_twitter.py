#! /usr/bin/python3

# All the tweepy stuff

import tweepy
from lib.pollster.ratings_pull import get_data 
from settings import CONSUMER_SETTINGS, ACCESS_SETTINGS, TWITTER_SETTINGS


auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))

api = tweepy.API(auth)

twitter_ids = []


def read_status(username):
    user_tweets = api.user_timeline(id=username, count=1)
    for tweet in user_tweets:
        return tweet.id

def update_id_list(tweet_ID, username):
    tweet_ID = read_status(username)
    if tweet_ID not in twitter_ids:
        twitter_ids.insert(0, tweet_ID)



def retweet_status(username):
    tweetID = read_status(username)
    retweet_url = "https://twitter.com/{0}/status/{1}".format(username, tweetID)
    update_id_list(tweetID, username)
    return retweet_url
