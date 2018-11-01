#!/home/vagrant/python3_env/bin/python3
# Runs the Python job


# from lib.pollster.ratings_pull import CSV_URL
from settings import TWITTER_SETTINGS
from lib.twitter.twitter_actions import Twinterface


tweeting = Twinterface()
tweeter = TWITTER_SETTINGS.get('username')


tweeting.update_status(tweeter, CSV_URL)
