#! /usr/bin/python3

# Runs the Python job

from lib.twitter.twitter_actions import Twinterface
from lib.pollster.ratings_pull import CSV_URL
from settings import TWITTER_SETTINGS

tweeting = Twinterface()
tweeter = TWITTER_SETTINGS.get('username')

tweeting.update_status(tweeter, CSV_URL)
