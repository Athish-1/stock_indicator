import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

symbol = "AAPL"  
start_date = "2023-10-10"
end_date = "2024-01-10"

stock_data = yf.download(symbol, start=start_date, end=end_date)

stock_data['sma_50'] = stock_data['Close'].rolling(window=50).mean()

plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Close'], label='Closing Price')
plt.plot(stock_data.index, stock_data['sma_50'], label='50-day SMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'{symbol} Stock Price with 50-day SMA')
plt.legend()
plt.grid(True)
plt.show()
