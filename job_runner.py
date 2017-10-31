#! /usr/bin/python3

# Runs the Python job

from lib.twitter.post_to_twitter import update_status
from settings import TWITTER_SETTINGS

update_status(TWITTER_SETTINGS.get('username'))
