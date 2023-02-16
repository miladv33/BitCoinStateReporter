import pandas as pd
import yfinance as yf

# Download the daily price data for Bitcoin
btc_data = yf.download("BTC-USD", period="max", interval="1d")

# Calculate the 14-day Stochastic Oscillator for Bitcoin
def calculate_stochastic(data, k=14, d=3):
    high = data['High'].rolling(window=k).max()
    low = data['Low'].rolling(window=k).min()
    close = data['Close']
    stoch_k = 100 * (close - low) / (high - low)
    stoch_d = stoch_k.rolling(window=d).mean()
    return stoch_k, stoch_d

btc_stoch_k, btc_stoch_d = calculate_stochastic(btc_data, 14, 3)

# Determine the current trend and sentiment based on Stochastic Oscillator
last_stoch_k = btc_stoch_k[-1]
last_stoch_d = btc_stoch_d[-1]

if last_stoch_k > last_stoch_d:
    trend = "Bullish"
else:
    trend = "Bearish"
    
if last_stoch_k > 80:
    sentiment = "Very Positive"
elif last_stoch_k > 50:
    sentiment = "Positive"
elif last_stoch_k > 20:
    sentiment = "Neutral"
else:
    sentiment = "Negative"

# Generate the report
report = f"Based on Stochastic Oscillator indicators, the current trend is {trend}, which means that the price is expected to go up.\n\
The sentiment is {sentiment}, which means that there is a positive outlook.\n ------------------------------\n"

# Save the report to a file
with open("prediction.txt", "a") as file:
    file.write(report)