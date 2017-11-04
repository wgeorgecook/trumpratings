# Runs the Python job


from lib.pollster.ratings_pull import CSV_URL
from settings import TWITTER_SETTINGS
from lib.twitter import twitter_actions

tweeting = twitter_actions.Twinterface()
tweeter = TWITTER_SETTINGS.get('username')

tweeting.update_status(tweeter, CSV_URL)
