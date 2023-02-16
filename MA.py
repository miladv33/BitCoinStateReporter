import pandas as pd
import yfinance as yf

# Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
symbol = "BTC-USD"
timeframe = "1d"
bitcoin = yf.download(symbol, period="max", interval=timeframe)
data = pd.DataFrame(bitcoin['Close'])

# Calculate the MA indicators
ma_20 = data['Close'].rolling(window=20).mean()
ma_50 = data['Close'].rolling(window=50).mean()

# Determine the current trend based on the MA indicators
if ma_20[-1] > ma_50[-1]:
    trend = 'Bullish'
else:
    trend = 'Bearish'

# Determine the sentiment based on the difference between the MA indicators
if ma_20[-1] > ma_50[-1] and ma_20[-1] - ma_50[-1] > 0.02 * data['Close'][-1]:
    sentiment = 'Positive'
else:
    sentiment = 'Neutral'

# Generate the report
report = f"Based on MA indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"

# Save the report to a file
with open("README.md", "a") as file:
    file.write(report)