-- Creates role, database, and table
CREATE ROLE trumpuser WITH LOGIN PASSWORD 'TempPa55';
ALTER ROLE trumpuser CREATEDB;
CREATE DATABASE trumpratings OWNER trumpuser;
\connect trumpratings;
CREATE TABLE twitter_info(
  tweet_id integer unique not null,
  date_posted varchar (50)
);
