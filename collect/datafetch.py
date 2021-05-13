# uses extraction tools to fetch data
from sources.yahoofinance import yf_object
from sources.fred import fred_object
import pandas as pd
import numpy as np

historicals = {}

from_yahoofinance = {"SP500":"SPY", "NASDAQ Composite":"^IXIC", "FTSE100":"^FTSE", "Hang Seng Index":"^HSI",
                        # equities
                        "SZSE Composite":"399106.SZ", "SSE Composite":"000001.SS",
                        # bonds
                        "10y Treasury Yield":"^TNX",
                        # commodities: metals
                        "Gold Futures":"GC=F", "Silver Futures":"SI=F", "Platinum Futures":"PL=F", "Palladium Futures":"PA=F", "Copper Futures":"HG=F",
                        # commodities: energy
                        "Crude Oil Futures":"CL=F", "Natural Gas Futures":"NG=F",
                        # commodities: agriculture
                        "Feeder Cattle Futures":"GF=F", "Live Cattle Futures":"LE=F", "Cocoa Futures":"CC=F", "Lumber Futures":"LBS=F",
                        "Cotton Futures":"CT=F", "Wheat Futures":"ZW=F", "Corn Futures":"ZC=F", "Soybean Futures":"ZS=F", "Sugar no11 Futures":"SB=F",
                        "Oat Futures":"ZO=F", "Rough Rice Futures":"ZR=F"
                        }

from_fred = {"M2 Money Supply":"M2SL", "M2 Money Velocity":"M2V", "Federal Funds Rate":"FEDFUNDS",
                "Monetary Base Total":"BOGMBASE", "Personal Consumption Expenditures":"PCEPI"}

sources = [from_yahoofinance, from_fred]

def fetch_data(start_date, end_date, interval):
    # yahoofinance data types available: open, high, low, close, volume, dividends, stock_splits
    # yahoofinance data available: S&P500, NASDAQ Composite, FTSE100,
        # HSI, SZSE Composite, SSE Composite,
        # Treasury Yield 10 Years,
        # Gold Futures, Silver Futures, Crude Oil Futures, Copper Futures,

    for name in from_yahoofinance:
        print("fetching data for: " + name)
        symbol = from_yahoofinance[name]
        target = yf_object(symbol)
        df = target.get_close(interval=interval, start_date=start_date, end_date=end_date)
        df.rename(index='value',inplace=True) # standardization for storing in db
        df.index.name = 'date'
        historicals[name] = df
        print("success.")

    # FRED API key = b296451576f9df1503841719b3d24ea5
    # FRED data available: M2SL (M2 Money Supply), FEDFUNDS (Federal Funds Rate), M2V (M2 Velocity)
        # BOGMBASE (Monetary Base Total), PCEPI (Personal Consumption Expenditures)

    api_key = 'b296451576f9df1503841719b3d24ea5'
    fred = fred_object(api_key=api_key)

    for name in from_fred:
        print("fetching data for: " + name)
        symbol = from_fred[name]
        df = fred.get_historical(symbol)
        df.rename(index='value',inplace=True) # standardization for storing in db
        df.index.name = 'date'
        historicals[name] = df
        print("success.")

    print("Data fetch complete.")

    return historicals
