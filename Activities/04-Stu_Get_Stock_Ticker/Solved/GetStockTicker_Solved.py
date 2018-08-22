# Dependencies
import quandl
import json

# API Key
from config import API_KEY

# Setup Quandl API Authentication
quandl.ApiConfig.api_key = API_KEY

# Get stock ticker information for Apple
appl = quandl.get("EOD/AAPL")
print(appl.head())

# Bonus: Loop through ticker and print last five closing prices
tickers = ["EOD/GE", "EOD/MMM", "XNYS/ABC"]

for ticker in tickers:
    print("Last 5 End of Day Prices for {0}".format(ticker))
    ticker_info = quandl.get(ticker)
    last_five = ticker_info["Close"].tail()
    print(last_five)
