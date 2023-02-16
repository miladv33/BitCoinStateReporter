import pandas as pd
import yfinance as yf

# Download the daily price data for Bitcoin
btc_data = yf.download("BTC-USD", period="max", interval="1d")

# Calculate the MACD for Bitcoin
def calculate_macd(data, slow=26, fast=12, signal=9):
    exp1 = data['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = data['Close'].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

btc_macd, btc_signal, btc_histogram = calculate_macd(btc_data, 26, 12, 9)

# Determine the current trend and sentiment based on MACD
last_macd = btc_macd[-1]
last_signal = btc_signal[-1]

if last_macd > last_signal:
    trend = "Bullish"
else:
    trend = "Bearish"
    
if last_macd > 0:
    sentiment = "Positive"
else:
    sentiment = "Negative"

# Generate the report
report = f"Based on MACD indicators, the current trend is {trend}, which means that the price is expected to go up.\n\
The sentiment is {sentiment}, which means that there is a positive outlook.\n ------------------------------\n"

# Save the report to a file
with open("prediction.txt", "a") as file:
    file.write(report)