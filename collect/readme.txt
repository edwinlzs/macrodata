These are scripts to extract, process and store macroeconomic/financial data for later analysis

1. Run macrodata.txt in SQL database to generate schema and tables

------ TECH: ------

1. python
2. sqlalchemy (python)

------ DATABASES: ------

1. phpMyAdmin

------ DATA SOURCES: ------

1. yahoo finance (yfinance)
    1a. Stock market indices (S&P500, NASDAQ Composite, FTSE100, HSI, SZSE Composite, SSE Composite)
    1b. Commodity futures (gold, silver, copper, crude oil)
    1c. Govt yields (10y treasury yield)

2. fred (fredapi)
    2a. M2 Money Supply (USD billions, Monthly, seasonally adjusted)
    2b. M2 Money Velocity (Ratio, Quarterly, seasonally adjusted, ratio of quarterly nominal GDP to quarterly average of M2 Money Supply)
    2c. Effective Federal Funds Rate (Percent, average of daily figures, Monthly, not seasonally adjusted, Federal Reserve)
    2d. Total Monetary Base (USD millions, Monthly, not seasonally adjusted, Federal Reserve)
    2c. Personal Consumption Expenditures (Index 2012=100, Monthly, seasonally adjusted, US Bureau of Economic Analysis, Chain-type price index)