import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from datetime import date
from DBobjects import Macro_Indicators, Macro_Data

# use in SQL to create scheme: CREATE DATABASE IF NOT EXISTS macrodata DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

# create an engine & connect to it
engine = db.create_engine('mysql+mysqlconnector://root@localhost:3306/macrodata')

# use Sessions based on the Unit of Work concept
# create a configured 'Session' class
Session = sessionmaker(bind=engine)

# create a session
session = Session()

# insert data
sp500 = Macro_Indicators("S&P500", "SPY", "yahoofinance")

# add to session
session.add(sp500)

# commit data & end session
session.commit()
session.close()
