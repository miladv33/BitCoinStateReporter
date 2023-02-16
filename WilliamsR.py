import pandas as pd
import yfinance as yf

# Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
symbol = "BTC-USD"
timeframe = "1d"
bitcoin = yf.download(symbol, period="max", interval=timeframe)
data = pd.DataFrame(bitcoin['Close'])

# Define a function to calculate the Williams %R indicator
def williams_r(data, period=14):
    # Calculate the highest high and lowest low for the specified period
    high_max = data['High'].rolling(window=period).max()
    low_min = data['Low'].rolling(window=period).min()
    # Calculate the Williams %R indicator
    williams_r = ((high_max - data['Close']) / (high_max - low_min)) * -100
    # Return a DataFrame with the Williams %R values
    return pd.DataFrame({'Williams %R': williams_r}, index=data.index)

# Calculate the Williams %R indicator
williams_r_data = williams_r(data)

# Determine the current trend based on the Williams %R indicator
if williams_r_data['Williams %R'].iloc[-1] < -80:
    trend = 'Bullish'
else:
    trend = 'Bearish'

# Determine the sentiment based on the position of the current Williams %R value relative to the oversold level
if williams_r_data['Williams %R'].iloc[-1] > -20:
    sentiment = 'Positive'
else:
    sentiment = 'Neutral'

# Generate the report
report = f"Based on Williams %R indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"

# Save the report to a file
with open("README.md", "a") as file:
    file.write(report)