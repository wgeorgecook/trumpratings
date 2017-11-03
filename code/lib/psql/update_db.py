# Uses PeeWee to update DB with Twitter IDs
from peewee import *
from settings import *


psql_db = PostgresqlDatabase(
    'trumpratings',
    user='trumpuser',
    password='TempPa55',
    host='localhost',
    )

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class User(BaseModel):
    username = CharField()

class Twitter_info(BaseModel):
    tweet_id = IntegerField(default=0)
    date_posted = CharField(max_length=50)
    twitter_url = CharField(max_length=255)

class DB(object):

    def __init__(self):
        self.db = psql_db
        self.db.connect()

    def search_id(self, **kwargs):
        Twitter_info.get(Twitter_info.tweet_id)
