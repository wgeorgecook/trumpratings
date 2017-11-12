# DB Models
from peewee import *
from settings import *


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

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class Twitter_info(BaseModel):
    name = CharField(max_length=255)
    tweet_id = BigIntegerField()
    date_posted = CharField(max_length=50)
    twitter_url = CharField(max_length=255)
    approval_num = IntegerField()
    disapproval_num = IntegerField()