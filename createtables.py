# script to create tables in database
import sqlalchemy as db
from DBobjects import Macro_Data, meta

# use in SQL to create scheme: CREATE DATABASE IF NOT EXISTS macrodata DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

# create an engine & connect to it
engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/macrodata')

####### TESTING STAGE #######

# create tables
sp500 = Macro_Data('S&P500').create_table()

# create all tables
meta.create_all(engine, checkfirst=True)
