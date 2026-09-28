import yfinance as yf
import pandas as pd

START_DATE = "2025-01-01"
END_DATE = "2026-09-28"

def get_pct_change(assets):
    data = yf.download(assets, start=START_DATE, end=END_DATE)["Close"]
    returns = data.pct_change()
    returns = returns.dropna()
    formatted_returns = returns.map(lambda x: round(x,3))
    formatted_returns.index = pd.to_datetime(formatted_returns.index).strftime('%Y-%m-%d')
    formatted_returns.index.name = 'Date'
    return formatted_returns

#print(get_pct_change(["AAPL","NVDA"]))





