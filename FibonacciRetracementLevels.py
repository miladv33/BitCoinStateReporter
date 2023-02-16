import pandas as pd
import yfinance as yf

# Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
symbol = "BTC-USD"
timeframe = "1d"
bitcoin = yf.download(symbol, period="max", interval=timeframe)
data = pd.DataFrame(bitcoin['Close'])

# Calculate the Fibonacci retracement levels
start_price = data['Close'].iloc[-1]
low_price = data['Close'].min()
high_price = data['Close'].max()
diff = high_price - low_price
fibonacci_levels = [
    start_price,
    start_price - 0.236 * diff,
    start_price - 0.382 * diff,
    start_price - 0.5 * diff,
    start_price - 0.618 * diff,
    start_price - 0.786 * diff,
    low_price
]

# Determine the current trend based on the Fibonacci retracement levels
if start_price > fibonacci_levels[3]:
    trend = 'Bullish'
elif start_price < fibonacci_levels[3]:
    trend = 'Bearish'
else:
    trend = 'Neutral'

# Determine the sentiment based on the distance between the current price and the nearest Fibonacci level
distances = [abs(start_price - level) / level for level in fibonacci_levels]
min_distance = min(distances)
if min_distance < 0.02:
    sentiment = 'Positive'
else:
    sentiment = 'Neutral'

# Generate the report
report = f"Based on Fibonacci Retracement Levels indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"

# Save the report to a file
with open("prediction.txt", "a") as file:
    file.write(report)