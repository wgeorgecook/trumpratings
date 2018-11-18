# Runs the Python job

from code.settings import TWITTER_SETTINGS
from code.lib.twitter.twitter_actions import Twinterface


tweeting = Twinterface()
tweeter = TWITTER_SETTINGS.get('username')


tweeting.update_status(tweeter)
