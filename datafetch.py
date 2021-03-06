# uses extraction tools to fetch data
from extraction.yahoofinance import yf_object
from extraction.fred import fred_object
import numpy as np

historicals = {}

start_date = "1991-01-01"
end_date = "2021-01-01"
interval = "1d"

# yahoofinance data types available: open, high, low, close, volume, dividends, stock_splits
# yahoofinance data available: S&P500, NASDAQ Composite, FTSE100,
    # HSI, SZSE Composite, SSE Composite,
    # Gold Futures, Silver Futures, Copper Futures, Crude Oil Futures
from_yahoofinance = ["SPY", "^IXIC", "^FTSE", "^HSI",
                    "399106.SZ", "000001.SS",
                    "GC=F", "SI=F", "HG=F", "CL=F"]

for symbol in from_yahoofinance:
    target = yf_object(symbol)
    historicals[symbol] = (target.get_close(interval=interval, start_date=start_date, end_date=end_date))

# FRED API key = b296451576f9df1503841719b3d24ea5
# FRED data available: M2SL (M2 Money Supply), FEDFUNDS (Federal Funds Rate), M2V (M2 Velocity)
    # BOGMBASE (Monetary Base Total)
from_fred = ["M2SL", "FEDFUNDS", "M2V",
            "BOGMBASE"]

fred = fred_object(api_key='b296451576f9df1503841719b3d24ea5')
for symbol in from_fred:
    historicals[symbol] = fred.get_historical(symbol)
print(historicals)

print("Script run complete.")
