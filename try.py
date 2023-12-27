import pandas as pd
import matplotlib.pyplot as plt
from nsetools import Nse
import datetime

def download_nse_data(symbol, start_date, end_date):
    nse = Nse()
    historical_data = nse.get_hist(symbol, start=start_date, end=end_date)
    
    data = {
        'Date': [entry['Date'] for entry in historical_data],
        'Close': [entry['Close'] for entry in historical_data]
    }

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    return df

symbol = "AAPL"  
start_date = "2023-10-10"
end_date = "2024-01-10"

stock_data_nse = download_nse_data(symbol, start_date, end_date)

stock_data_nse['sma_50'] = stock_data_nse['Close'].rolling(window=50).mean()

plt.figure(figsize=(12, 6))
plt.plot(stock_data_nse.index, stock_data_nse['Close'], label='Closing Price')
plt.plot(stock_data_nse.index, stock_data_nse['sma_50'], label='50-day SMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'{symbol} Stock Price with 50-day SMA (NSE)')
plt.legend()
plt.grid(True)
plt.show()
