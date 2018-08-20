# Dependencies
import quandl
import json

# Api Key
from config import API_KEY

# Setup Quandl API Authentication
# YOUR CODE HERE
quandl.ApiConfig.api_key = API_KEY

# Get stock ticker information from Apple
# YOUR CODE HERE
appl = quandl.get("EOD/AAPL")

# Loop through ticker and print last five closing prices 
tickers = ["EOD/GE", "EOD/MMM", "XNYS/ABC"]

for ticker in tickers:
    print("Last 5 End of Day Prices for {0}".format(ticker))
    ticker_info = quandl.get(ticker)
    last_five = ticker_info["Close"].tail()
    print(last_five)
