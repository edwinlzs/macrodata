# Data Access Object defines classes for updating database
from sqlalchemy import Column, Float, Date, Table, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base()

class Macro_Data():
    
    def __init__(self, tablename):
        self.tablename = tablename

    def create_table(self):
        return Table(self.tablename, meta,
            Column('date', Date, primary_key=True),
            Column('value', Float(precision=2))
            )
    