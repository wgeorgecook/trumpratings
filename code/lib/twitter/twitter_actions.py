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
        user_tweets = self.api.user_timeline(id=username, count=1)
        for tweet in user_tweets:
            return tweet.id

    def get_tweet_id(self, username):
        tweet_ID = self.read_status(username)
        return tweet_ID

    def get_tweet_url(self, username):
        tweetID = self.read_status(username)
        tweet_url = "https://twitter.com/{0}/status/{1}".format(username, tweetID)
        self.get_tweet_id(username)
        return tweet_url

    def update_status(self, username, CSV_URL):
        print("############# Time is: ", timestamp, ' #############')
        approve = reading.get_data(CSV_URL)[0]
        disapprove = reading.get_data(CSV_URL)[1]
        tweet = "Latest @realDonaldTrump, @POTUS Gallup approval rating is {0}%. Disapproval rating is {1}%. \n{2} ".format(approve, disapprove, self.retweet_status(username))
        # self.api.update_status(tweet)
        print("Tweeting currently turned off")
        print("Virtual tweet:")
        print(tweet)
        print("############# Tweet posted! #############")
