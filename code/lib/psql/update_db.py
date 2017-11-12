# Uses PeeWee to update DB with Twitter IDs
from peewee import *
from settings import *
from datetime import datetime
from lib.psql.models import Twitter_info
from lib.pollster.ratings_pull import DataRead, CSV_URL



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
    """
    Connects to a Postgresl database.
    Can search database for tweet ID's and passes
    true/false to Twinterface object. Will also
    update DB with relevant Twitter data after
    posting tweet via Twinterface object.

    """

    def __init__(self, username, tweet_ID, twitter_url, approval_num, disapproval_num):

        self.reading = DataRead()
        self.CSV_URL = CSV_URL

        self.db = psql_db
        self.username = username
        self.tweet_ID = tweet_ID
        self.date_posted = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.twitter_url = twitter_url
        ratings = self.reading.get_data(CSV_URL)
        self.approval = ratings[0]
        self.disapproval = ratings[1]

    def open_connection(self):
        self.db.connect()
        return "Connection to {} open.".format(dbconnection)

    def close_connection(self):
        self.db.close()
        return "Connection to {} closed.".format(dbconnection)

    def rollback_txn(self):
        self.db.rollback()

    def post_tweet_info(self):
        if self.search_tweets(self.tweet_ID) is False:
            self.open_connection()
            posting = Twitter_info(
                name=self.username,
                tweet_id=self.tweet_ID,
                date_posted=self.date_posted,
                twitter_url=self.twitter_url,
                approval_num = self.approval,
                disapproval_num = self.disapproval
            )
            posting.save()

            self.close_connection()

    def search_tweets(self, tweet_ID):
        try:
            if Twitter_info.get(Twitter_info.tweet_id == tweet_ID):
                return True
                self.close_connection()

        except:
            return False
            self.close_connection()
