#! /usr/bin/python3

# All the tweepy stuff

import tweepy
from lib.pollster.ratings_pull import DataRead, CSV_URL
from datetime import datetime
from settings import *


auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))

api = tweepy.API(auth)
tweeter = TWITTER_SETTINGS.get('username')
timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
reading = DataRead()
twitter_ids = []

class Twinterface(object):
    def __init__(self):
        self.api = api
        self.auth = auth
        self.tweeter = tweeter
        self.timestamp = timestamp
        self.CSV_URL = CSV_URL
        self.reading = reading

    def read_status(self, username):
        user_tweets = api.user_timeline(id=username, count=1)
        for tweet in user_tweets:
            return tweet.id

    def update_id_list(self, tweet_ID, username):
        tweet_ID = self.read_status(username)
        if tweet_ID not in twitter_ids:
            twitter_ids.insert(0, tweet_ID)

    def retweet_status(self, username):
        tweetID = self.read_status(username)
        retweet_url = "https://twitter.com/{0}/status/{1}".format(username, tweetID)
        self.update_id_list(tweetID, username)
        return retweet_url

    def update_status(self, username, CSV_URL):
        print("############# Time is: ", timestamp, ' #############')
        ratings = reading.get_data(CSV_URL)
        tweet = ".@realDonaldTrump's latest approval rating from Gallup is {0}% \n{1} ".format(ratings, self.retweet_status(username))
        api.update_status(tweet)
        print("############# Tweet posted! #############")
