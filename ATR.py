import pandas as pd
import yfinance as yf

# Download the daily price data for Bitcoin
btc_data = yf.download("BTC-USD", period="max", interval="1d")

# Calculate the ATR for Bitcoin
def calculate_atr(data, period=14):
    high = data['High']
    low = data['Low']
    close = data['Close']
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift()))
    tr3 = pd.DataFrame(abs(low - close.shift()))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis=1, join='inner')
    atr = tr.rolling(window=period).mean()
    atr.columns = ['ATR']
    return atr

btc_atr = calculate_atr(btc_data, 14)

# Determine the current trend and sentiment based on ATR
last_close = btc_data['Close'][-1]
last_atr = btc_atr['ATR'][-1]

if last_close > last_atr:
    trend = "Bullish"
else:
    trend = "Bearish"
    
if last_atr < last_close * 0.01:
    sentiment = "Positive"
else:
    sentiment = "Negative"

# Generate the report
report = f"Based on ATR indicators, the current trend is {trend}, which means that the price is expected to go up.\n\
The sentiment is {sentiment}, which means that there is a positive outlook.\n ------------------------------\n"

# Save the report to a file
with open("README.md", "a") as file:
    file.write(report)