# Runs the Python job

from settings import TWITTER_SETTINGS
from lib.twitter.twitter_actions import Twinterface


tweeting = Twinterface()
tweeter = TWITTER_SETTINGS.get('username')


tweeting.update_status(tweeter)
