import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root@localhost:3306/macrodata')

def retrieve_data(tablename):
    df = pd.read_sql(tablename, engine, index_col='date')
    return df