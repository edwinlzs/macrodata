# Data Access Object defines classes for updating database
from sqlalchemy import Column, Text, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

indicators_data_association = Table(
    'indicators_data', Base.metadata,
    Column('symbol', String(10), ForeignKey('macro_indicators.symbol')),
    Column('date', Date, ForeignKey('macro_data.date'))
)

class Macro_Indicators(Base):
    __tablename__ = 'macro_indicators'
    symbol = Column('symbol', String(10), primary_key=True)
    name = Column('name', String(16), unique=True)
    source = Column('source', String(16))
    macro_data = relationship('Macro_Data', secondary=indicators_data_association)

    def __init__(self, name, symbol, source):
        self.name = name
        self.symbol = symbol
        self.source = source

class Macro_Data(Base):
    __tablename__ = 'macro_data'
    symbol = Column('symbol', String(10), ForeignKey('macrodata.macro_indicators.symbol'), primary_key=True)
    name = Column('name', String(16), ForeignKey('macrodata.macro_indicators.name'), unique=True)
    date = Column('date', Date, primary_key=True)
    value = Column('value', Decimal(precision=2))

    def __init(self, name, date):
        self.date = date
