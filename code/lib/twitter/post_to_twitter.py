#! /usr/bin/python3

# All the tweepy stuff

import tweepy
from datetime import datetime
from settings import *
from lib.pollster.ratings_pull import DataRead
from lib.twitter.read_from_twitter import Twinterface


auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))
tweeter = TWITTER_SETTINGS.get('username')
api = tweepy.API(auth)

timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
tweetID = Twinterface.read_status(tweeter)

class UpdateTwitter(object):
    def __init__(self):
        self.auth = auth
        self.api = api
        self.timestamp = timestamp
        self.tweetID = tweetID

    def update_status(self, username):
        print("############# Time is: ", timestamp, ' #############')
        ratings = DataRead.get_data(CSV_URL)
        tweet = ".@realDonaldTrump's latest approval rating from Gallup is {0}% \n{1} ".format(ratings, retweet_status(username))
        api.update_status(tweet)
        print("############# Tweet posted! #############")
