# Uses PeeWee to update DB with Twitter IDs
from peewee import *
from settings import *
from datetime import datetime
from lib.psql.models import Twitter_info
from lib.twitter.twitter_actions import Twinterface


twitter = Twinterface()
username = TWITTER_SETTINGS.get('username')
tweet_ID = twitter.get_tweet_id(username)
twitter_url = twitter.get_tweet_url(username)
date_posted = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

dbconnection = DB_SETTINGS.get('db')
dbuser = DB_SETTINGS.get('user')
dbpass = DB_SETTINGS.get('password')
dbhost = DB_SETTINGS.get('host')

psql_db = PostgresqlDatabase(
    dbconnection,
    user=dbuser,
    password=dbpass,
    host=dbhost,
    )



class DB(object):

    def __init__(self):
        self.db = psql_db
        self.username = username
        self.tweet_ID = tweet_ID
        self.date_posted = date_posted
        self.twitter_url = twitter_url

    def open_connection(self):
        self.db.connect()
        return "Connection to {} open.".format(dbconnection)

    def close_connection(self):
        self.db.close()
        return "Connection to {} closed.".format(dbconnection)

    def rollback_txn(self):
        self.db.rollback()

    def post_tweet_info(self, username, tweet_ID, date_posted, twitter_url):
        if self.search_tweets(tweet_ID) == False:
            self.open_connection()
            posting = Twitter_info(name = self.username, tweet_id = self.tweet_ID, date_posted = self.date_posted, twitter_url = self.twitter_url)
            posting.save()
            self.close_connection()

    def search_tweets(self, tweet_ID):
        try:
            if Twitter_info.get(Twitter_info.tweet_id == tweet_ID):
                return True
        except:
            return False

data = DB()
