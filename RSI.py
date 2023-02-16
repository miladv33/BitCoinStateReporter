import pandas as pd
import yfinance as yf

# Download the daily price data for Bitcoin
btc_data = yf.download("BTC-USD", period="max", interval="1d")

# Calculate the 14-day RSI for Bitcoin
def calculate_rsi(data, window_length=14):
    close = data['Close']
    delta = close.diff()
    delta = delta[1:]
    up = delta.where(delta > 0, 0)
    down = -delta.where(delta < 0, 0)
    rolling_up = up.rolling(window_length).mean()
    rolling_down = down.rolling(window_length).mean()
    rs = rolling_up / rolling_down
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

btc_rsi = calculate_rsi(btc_data, 14)

# Determine the current trend and sentiment based on RSI
last_rsi = btc_rsi[-1]
if last_rsi > 50:
    trend = "Bullish"
else:
    trend = "Bearish"
    
if last_rsi > 70:
    sentiment = "Very Positive"
elif last_rsi > 50:
    sentiment = "Positive"
elif last_rsi > 30:
    sentiment = "Neutral"
elif last_rsi > 0:
    sentiment = "Negative"
else:
    sentiment = "Very Negative"

# Generate the report
report = f"Based on RSI indicators, the current trend is {trend}, which means that the price is expected to go up.\n\
The sentiment is {sentiment}, which means that there is a positive outlook.\n ------------------------------\n"

# Save the report to a file
with open("prediction.txt", "a") as file:
    file.write(report)