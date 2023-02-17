import pandas as pd
import yfinance as yf

class FibonacciRetracementLevels:
    def __init__(self, symbol, timeframe):
        # Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
        self.bitcoin = yf.download(symbol, period="max", interval=timeframe)
        self.data = pd.DataFrame(self.bitcoin['Close'])

        # Calculate the Fibonacci retracement levels
        self.start_price = self.data['Close'].iloc[-1]
        self.low_price = self.data['Close'].min()
        self.high_price = self.data['Close'].max()
        diff = self.high_price - self.low_price
        self.fibonacci_levels = [
            self.start_price,
            self.start_price - 0.236 * diff,
            self.start_price - 0.382 * diff,
            self.start_price - 0.5 * diff,
            self.start_price - 0.618 * diff,
            self.start_price - 0.786 * diff,
            self.low_price
        ]

    def calculate(self):
        # Determine the current trend based on the Fibonacci retracement levels
        if self.start_price > self.fibonacci_levels[3]:
            trend = 'Bullish'
        elif self.start_price < self.fibonacci_levels[3]:
            trend = 'Bearish'
        else:
            trend = 'Neutral'

        # Determine the sentiment based on the distance between the current price and the nearest Fibonacci level
        distances = [abs(self.start_price - level) / level for level in self.fibonacci_levels]
        min_distance = min(distances)
        if min_distance < 0.02:
            sentiment = 'Positive'
        else:
            sentiment = 'Neutral'

        # Generate the report
        report = f"Based on Fibonacci Retracement Levels indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"
        return report