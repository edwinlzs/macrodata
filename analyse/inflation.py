from retrievedb import retrieve_data

import sys
sys.path.append("..\collect")

from datafetch import sources

# Commodity Price Inflation

commodities = [
    'Copper Futures', 'Crude Oil Futures', 'Natural Gas Futures', 'Gold Futures', 'Silver Futures', 'Platinum Futures',
    'Palladium Futures', 'Feeder Cattle Futures', 'Live Cattle Futures', 'Cocoa Futures', 'Lumber Futures', 'Cotton Futures',
    'Wheat Futures', 'Corn Futures', 'Soybean Futures', 'Sugar #11 Futures', 'Oat Futures', 'Rough Rice Futures'
]



for commodity in commodities:
    commodity = commodity.lower()
    price_data = retrieve_data(commodity) # retrieve from database
    