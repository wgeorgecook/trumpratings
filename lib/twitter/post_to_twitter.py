#! /usr/bin/python3

# All the tweepy stuff

import tweepy
from settings import CONSUMER_SETTINGS, ACCESS_SETTINGS, TWITTER_SETTINGS
from lib.pollster.ratings_pull import get_data, CSV_URL
from lib.twitter.read_from_twitter import retweet_status, read_status, twitter_ids


auth = tweepy.OAuthHandler(CONSUMER_SETTINGS.get('consumer_key'), CONSUMER_SETTINGS.get('consumer_secret'))
auth.set_access_token(ACCESS_SETTINGS.get('access_token'), ACCESS_SETTINGS.get('access_secret'))

api = tweepy.API(auth)

tweetID = read_status(TWITTER_SETTINGS.get('username'))

def update_status(username):
    print("ID's already tweeted:", twitter_ids)
    ratings = get_data(CSV_URL)
    tweet = "@realDonaldTrump's latest approval rating from Gallup is {0}% \n{1} ".format(ratings, retweet_status(username))
    api.update_status(tweet)
    print("Tweet posted!")
