# Uses PeeWee to update DB with Twitter IDs
from peewee import *
from settings import *


psql_db = PostgresqlDatabase(
    'trumpratings',
    user='trumpuser',
    password='TempPa55',
    host='localhost',
    )


class DB(object):

    def __init__(self):
        self.db = db
        self.db.connect()

    def search_id(self):
        Twitter_info.get(Twitter_info.tweet_id ==


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class User(BaseModel):
    username = CharField()

class Twitter_info(BaseModel):
    tweet_id = IntegerField(default=0)
    date_posted = CharField(maxlength=50)
