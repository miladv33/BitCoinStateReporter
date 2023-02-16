import pandas as pd
import yfinance as yf

# Download the daily price data for Bitcoin
btc_data = yf.download("BTC-USD", period="max", interval="1d")

# Calculate the On Balance Volume (OBV) for Bitcoin
def calculate_obv(data):
    close = data['Close']
    volume = data['Volume']
    prev_obv = pd.Series([0], index=data.index[:1])
    for i in range(1, len(close)):
        if close[i] > close[i-1]:
            current_obv = prev_obv[i-1] + volume[i]
        elif close[i] < close[i-1]:
            current_obv = prev_obv[i-1] - volume[i]
        else:
            current_obv = prev_obv[i-1]
        prev_obv = prev_obv.append(pd.Series(current_obv, index=[data.index[i]]))
    return prev_obv

btc_obv = calculate_obv(btc_data)

# Determine the current trend and sentiment based on OBV
last_close = btc_data['Close'][-1]
last_obv = btc_obv[-1]

if last_close > btc_data['Close'].rolling(window=20).mean()[-1]:
    trend = "Bullish"
else:
    trend = "Bearish"
    
if last_obv > btc_obv.rolling(window=20).mean()[-1]:
    sentiment = "Positive"
else:
    sentiment = "Negative"

# Generate the report
report = f"Based on OBV indicators, the current trend is {trend}, which means that the price is expected to go up.\n\
The sentiment is {sentiment}, which means that there is a positive outlook.\n ------------------------------\n"

# Save the report to a file
with open("prediction.txt", "a") as file:
    file.write(report)
