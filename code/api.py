import flask
from flask import request, jsonify
from peewee import PostgresqlDatabase
from lib.psql.models import Twitter_info
from settings import DB_SETTINGS

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


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=['GET'])
def home():
    return "Some tweets!"

@app.route('/api/v1/resources/approvals', methods=['GET'])
def approvals():
    if 'id' in request.args:
        tweet_id = int(request.args['id'])
    else:
        return "<h1>Please specify a tweet id</h1>"
    psql_db.connect()
    approval_ratings = Twitter_info.get(Twitter_info.tweet_id == tweet_id)
    psql_db.close()
    return approval_ratings.twitter_url

@app.route('/api/v1/resources/disapprovals', methods=['GET'])
def disapprovals():
    if 'id' in request.args:
        tweet_id = int(request.args['id'])
    else:
        return "<h1>Please specify a tweet id</h1>"
    psql_db.connect()
    disapproval_ratings = Twitter_info.get(Twitter_info.tweet_id == tweet_id)
    psql_db.close()
    return "<h1>Tweet: {}".format(disapproval_ratings.twitter_url)

@app.route('/api/v1/resources/all', methods=['GET'])
def get_all():
    psql_db.connect()
    all_ratings = Twitter_info.select("*")
    psql_db.close()
    return all_ratings

app.run(host="0.0.0.0")
# 1060022696703070208