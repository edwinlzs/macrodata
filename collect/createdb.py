# script to create tables in database
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from database.macrodata_db import Macro_Data, meta
from datafetch import from_yahoofinance, from_fred

# use in SQL to create scheme: CREATE DATABASE IF NOT EXISTS macrodata DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

# create an engine & connect to it
engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/macrodata')

# create database

# if not database_exists(engine.url):
#     create_database(engine.url)
#     print("Created database.")
# else:
#     print("Database found, creating tables now.")

# create table objects
for name in from_yahoofinance:
    print("creating table for: " + name)
    Macro_Data(name).create_table()
    print("created.")

for name in from_fred:
    print("creating table for: " + name)
    Macro_Data(name).create_table()
    print("created.")

print("Database and table creation complete.")

# map and create all tables in database
meta.create_all(engine, checkfirst=True)
