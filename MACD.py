import pandas as pd
import yfinance as yf

class MACD:
    def __init__(self, symbol, timeframe):
        # Load the data from Yahoo Finance into a pandas DataFrame
        self.data = yf.download(symbol, period="max", interval=timeframe)
        
    def calculate(self, slow=26, fast=12, signal=9):
        # Calculate the MACD for the loaded data
        exp1 = self.data['Close'].ewm(span=fast, adjust=False).mean()
        exp2 = self.data['Close'].ewm(span=slow, adjust=False).mean()
        macd = exp1 - exp2
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        histogram = macd - signal_line
        
        # Determine the current trend and sentiment based on MACD
        last_macd = macd[-1]
        last_signal = signal_line[-1]

        if last_macd > last_signal:
            trend = "Bullish"
        else:
            trend = "Bearish"

        if last_macd > 0:
            sentiment = "Positive"
        else:
            sentiment = "Negative"

        # Generate the report
        
        return trend, sentiment