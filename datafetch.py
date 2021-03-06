# uses extraction tools to fetch data
from extraction.yahoofinance import yf_object
from extraction.fred import fred_object
import pandas as pd
import numpy as np

historicals = {}

start_date = "1991-01-01"
end_date = "2021-01-01"
interval = "1d"

# yahoofinance data types available: open, high, low, close, volume, dividends, stock_splits
# yahoofinance data available: S&P500, NASDAQ Composite, FTSE100,
    # HSI, SZSE Composite, SSE Composite,
    # Gold Futures, Silver Futures, Copper Futures, Crude Oil Futures
    # Treasury Yield 10 Years

from_yahoofinance = {"S&P500":"SPY", "NASDAQ Composite":"^IXIC", "FTSE100":"^FTSE", "Hang Seng Index":"^HSI",
                    "SZSE Composite":"399106.SZ", "SSE Composite":"000001.SS",
                    "Gold Futures":"GC=F", "Silver Futures":"SI=F", "Copper Futures":"HG=F", "Crude Oil Futures":"CL=F",
                    "10y Treasury Yield":"^TNX"}

for name in from_yahoofinance:
    print("fetching data for: " + name)
    symbol = from_yahoofinance[name]
    target = yf_object(symbol)
    historicals[name] = (target.get_close(interval=interval, start_date=start_date, end_date=end_date))
    print("success")

# FRED API key = b296451576f9df1503841719b3d24ea5
# FRED data available: M2SL (M2 Money Supply), FEDFUNDS (Federal Funds Rate), M2V (M2 Velocity)
    # BOGMBASE (Monetary Base Total)
from_fred = {"M2 Money Supply":"M2SL", "M2 Velocity":"M2V", "Federal Funds Rate":"FEDFUNDS",
            "Monetary Base Total":"BOGMBASE", "Personal Consumption Expenditures":"PCEPI"}

api_key = 'b296451576f9df1503841719b3d24ea5'
fred = fred_object(api_key=api_key)

for name in from_fred:
    print("fetching data for: " + name)
    symbol = from_fred[name]
    historicals[name] = fred.get_historical(symbol)
    print("success")

print("Script run complete.")
