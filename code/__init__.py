import flask
from flask_cors import CORS
from flask import request, jsonify, Response, json
from peewee import PostgresqlDatabase
from code.lib.psql.models import Twitter_info
from code.settings import DB_SETTINGS

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
CORS(app)
app.config["DEBUG"] = True

def custom_response(res):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res.__dict__),
    status=200
  )

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
    results = []
    psql_db.connect()
    all_ratings = Twitter_info.select()
    for result in all_ratings:
        results.append(
            {'tweet_id': result.tweet_id, 'tweet_url': result.twitter_url, 'approval': result.approval_num, 'disapproval': result.disapproval_num, 'date_posted': result.date_posted, 'tweet_text': result.tweet_text})
    psql_db.close()
    return jsonify(results)

@app.route('/api/v1/resources/top10', methods=['GET'])
def all_ratings():
    results = []
    psql_db.connect()
    for result in Twitter_info.select().order_by(result.posted_date):
        results.append(
            {'tweet_id': result.tweet_id, 'tweet_url': result.twitter_url, 'approval': result.approval_num, 'disapproval': result.disapproval_num, 'date_posted': result.date_posted, 'tweet_text': result.tweet_text})
    psql_db.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0") # vagrant