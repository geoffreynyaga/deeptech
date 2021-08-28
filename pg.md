sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo apt install postgis postgresql-12-postgis-3

sudo -u postgres psql


CREATE DATABASE deeptechwsl;
CREATE USER deeptech_user WITH PASSWORD 'deeptech_password';

ALTER ROLE deeptech_user SET client_encoding TO 'utf8';
ALTER ROLE deeptech_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE deeptech_user SET timezone TO 'UTC';


GRANT ALL PRIVILEGES ON DATABASE deeptechwsl TO deeptech_user;

\q

sudo -i -u postgres;
psql -d deeptechwsl;
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_raster;
