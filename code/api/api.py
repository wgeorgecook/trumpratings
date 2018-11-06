import flask
from flask import request, jsonify
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


app = flask.Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Polling data yeah!</h1>"

@app.route('/api/vi/resources/approvals', methods='[GET')
def approvals():

    return jsonify(approval_ratings)