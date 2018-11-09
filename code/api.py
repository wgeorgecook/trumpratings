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
    return jsonify(approval_ratings.approval_num)

@app.route('/api/v1/resources/disapprovals', methods=['GET'])
def disapprovals():
    if 'id' in request.args:
        tweet_id = int(request.args['id'])
    else:
        return "<h1>Please specify a tweet id</h1>"
    psql_db.connect()
    disapproval_ratings = Twitter_info.get(Twitter_info.tweet_id == tweet_id)
    psql_db.close()
    return jsonify(disapproval_ratings.disapproval_num)

@app.route('/api/v1/resources/all', methods=['GET'])
def all_ratings():
    results = {}
    psql_db.connect()
    all_ratings = Twitter_info.select()
    for result in all_ratings:
        results.update({result.tweet_id: {'tweet_url': result.twitter_url, 'approval': result.approval_num, 'disapproval': result.disapproval_num, 'date_posted': result.date_posted, 'tweet_text': result.tweet_text}})
    psql_db.close()
    return jsonify(results)

app.run(host="0.0.0.0")