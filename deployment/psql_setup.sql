-- Creates role, database, and table
CREATE ROLE trumpuser WITH LOGIN PASSWORD 'TempPa55';
ALTER ROLE trumpuser CREATEDB;
CREATE DATABASE trumpratings OWNER trumpuser;
GRANT ALL PRIVILEGES ON DATABASE trumpratings TO trumpuser;
