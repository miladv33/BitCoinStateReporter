import pandas as pd
import yfinance as yf

# Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
symbol = "BTC-USD"
timeframe = "1d"
bitcoin = yf.download(symbol, period="max", interval=timeframe)
data = pd.DataFrame(bitcoin['Close'])

# Calculate the Bollinger Bands indicator
n = 20  # Number of days for the moving average
k = 2  # Number of standard deviations for the bands
rolling_mean = data['Close'].rolling(window=n).mean()
rolling_std = data['Close'].rolling(window=n).std()
upper_band = rolling_mean + k * rolling_std
lower_band = rolling_mean - k * rolling_std

# Determine the current trend based on the Bollinger Bands
if data['Close'][-1] > upper_band[-1]:
    trend = 'Bullish'
elif data['Close'][-1] < lower_band[-1]:
    trend = 'Bearish'
else:
    trend = 'Neutral'

# Determine the sentiment based on the distance between the current price and the lower band
distance_to_lower_band = (data['Close'][-1] - lower_band[-1]) / lower_band[-1]
if distance_to_lower_band > 0.05:
    sentiment = 'Positive'
else:
    sentiment = 'Neutral'

# Generate the report
report = f"Based on BollingerBands indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"

# Save the report to a file
with open("prediction.txt", "a") as file:
    file.write(report)