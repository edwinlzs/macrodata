# source: https://github.com/ranaroussi/yfinance
import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt

class yf_object():
    """
        get_historical(self, interval, start_date, end_date)
        get_close(self)
    """

    def __init__(self, ticker):
        self.target = yf.Ticker(ticker)

    def get_historical(self, interval, start_date, end_date=dt.date.today()):
        return self.target.history(interval=interval, start=start_date, end=end_date)

    def get_close(self, interval, start_date, end_date=dt.date.today()):
        return self.target.history(interval=interval, start=start_date, end=end_date)["Close"]