import pandas as pd
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
from datafetch import fetch_data

Base = declarative_base()

# create database engine
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root@localhost:3306/macrodata')

# initialize session
# Session = sessionmaker(bind=engine)
# session = Session()

# pull data
start_date = "1991-01-01"
end_date = "2021-01-01"
interval = "1d"

data = fetch_data(start_date=start_date, end_date=end_date, interval=interval)

for name, df in data.items():
    name = name.lower()
    print("updating: " + name)
    df.to_sql(name, engine, if_exists='append')
    print("success.")
