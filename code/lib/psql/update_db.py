# Uses PeeWee to update DB with Twitter IDs
from peewee import *


db = PostgresqlDatabase(
    'trumpratings',  # Required by Peewee.
    user='trumpuser',  # Will be passed directly to psycopg2.
    password='TempPa55',  # Ditto.
    host='127.0.0.1:5432',  # Ditto.
)

psql_db = PostgresqlDatabase('trumpratings', user='trumpuser')
