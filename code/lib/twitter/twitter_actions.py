# All the tweepy stuff

import tweepy
from lib.pollster.ratings_pull import DataRead, CSV_URL
from datetime import datetime
from settings import *
from lib.psql.update_db import DB
from lib.psql.configure_db import MakeDB



class Twinterface(object):
    """
    Uses Tweepy library to interface with all things Twitter. Gathers
    info such as the President's last tweet ID, the full URL
    for the Preseident's last tweet, and finally will
    make the write call to the Twitter API.
    """

    def __init__(self):

        self.auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
        self.auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))
        self.tweeter = TWITTER_SETTINGS.get('username')
        self.timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")
        self.CSV_URL = CSV_URL
        self.reading = DataRead()
        self.config = MakeDB()
        self.api = tweepy.API(self.auth)


    def read_status(self, username): #TODO investigate streaming API calls for this
        user_tweets = self.api.user_timeline(id=username, count=1)
        for tweet in user_tweets:
            return [tweet.id, tweet.text]

    def get_tweet_id(self, username):
        tweet_ID = self.read_status(username)[0]
        return tweet_ID


    def get_tweet_url(self, username):
        tweetID = self.read_status(username)[0]
        tweet_url = "https://twitter.com/{0}/status/{1}".format(username, tweetID)
        self.get_tweet_id(username)
        return tweet_url

    def update_status(self, username, CSV_URL):
        ratings_list = self.reading.get_data(CSV_URL)
        tweet_ID = self.get_tweet_id(username)
        twitter_url = self.get_tweet_url(username)
        tweet_text = self.read_status(username)[1]
        approval_num = ratings_list[0]
        disapproval_num = ratings_list[1]

        data = DB(username=username, tweet_ID=tweet_ID, twitter_url=twitter_url, tweet_text=tweet_text, approval_num=approval_num, disapproval_num=disapproval_num)

        if self.config.check_tables() is True:
            print("Tables exist. No need to reconfigure.")
        else:
            print("Database needs configured. Configureing database.")
            self.config.create_tables()

        if data.search_tweets(tweet_ID) is False:
            print("############# Time is: ", self.timestamp, ' #############')
           # ratings = self.reading.get_data(CSV_URL)
            approve = approval_num
            disapprove = disapproval_num
            tweet = "Latest @realDonaldTrump, @POTUS Gallup approval rating is {0}%. Disapproval rating is {1}%. \n{2} ".format(approve, disapprove, self.get_tweet_url(username))
            self.api.update_status(tweet)
            print("Virtual tweet preview:")
            print(tweet)
            print("############# Tweet posted! #############")
            data.post_tweet_info()
        else:
            print("############# Time is: ", self.timestamp, ' #############')
            print("############# Tweet already posted! Will not update! #############")
