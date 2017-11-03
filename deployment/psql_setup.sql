-- Creates role, database, and table
CREATE ROLE trumpuser WITH LOGIN PASSWORD 'TempPa55';
ALTER ROLE trumpuser CREATEDB;
CREATE DATABASE trumpratings OWNER trumpuser;
GRANT ALL PRIVILEGES ON DATABASE trumpratings TO trumpuser;
\connect trumpratings;
CREATE TABLE twitter_user (
  username varchar(50) PRIMARY KEY
);
CREATE TABLE twitter_info (
  username varchar(50) REFERENCES twitter_user(username),
  tweet_id integer unique not null PRIMARY KEY,
  date_posted varchar (50),
  twitter_url varchar (255) unique
);
GRANT ALL PRIVILEGES ON TABLE user, twitter_info TO trumpuser;
