from retrievedb import retrieve_data
from dateutil.relativedelta import relativedelta

import sys
sys.path.append("..\collect")

from datafetch import sources

import pandas as pd
import numpy as np
import datetime as dt
from pandas.tseries.offsets import BDay

# Commodity Price Inflation

commodities = [
    'Copper Futures', 'Crude Oil Futures', 'Natural Gas Futures', 'Gold Futures', 'Silver Futures', 'Platinum Futures',
    'Palladium Futures', 'Feeder Cattle Futures', 'Live Cattle Futures', 'Cocoa Futures', 'Lumber Futures', 'Cotton Futures',
    'Wheat Futures', 'Corn Futures', 'Soybean Futures', 'Sugar no11 Futures', 'Oat Futures', 'Rough Rice Futures'
]

end_date = dt.date.today() - BDay(1)
start_date = end_date - relativedelta(years=5) - BDay(1) # -1 BDay to ensure start_date is on a trading day

ix = pd.bdate_range(start=start_date, end=end_date, freq='B')
normalized_df = pd.DataFrame(index=ix)

for commodity in commodities:
    commodity = commodity.lower()
    price_data = retrieve_data(commodity) # retrieve from database

    start_price = price_data.loc[start_date]
    normalized_df[commodity] = price_data[price_data.index >= start_date]/start_price

print(normalized_df)