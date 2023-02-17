import pandas as pd
import yfinance as yf

class StochasticOscillator:
    def __init__(self, symbol, k=14, d=3):
        self.data = yf.download(symbol, period="max", interval="1d")
        self.k = k
        self.d = d
    
    # Calculate the Stochastic Oscillator indicator
    def calculate(self):
        high = self.data['High'].rolling(window=self.k).max()
        low = self.data['Low'].rolling(window=self.k).min()
        close = self.data['Close']
        stoch_k = 100 * (close - low) / (high - low)
        stoch_d = stoch_k.rolling(window=self.d).mean()

        # Determine the current trend and sentiment based on Stochastic Oscillator
        last_stoch_k = stoch_k[-1]
        last_stoch_d = stoch_d[-1]

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
        report = f"Based on Stochastic Oscillator indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}.\n\
        The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' or sentiment == 'Very Positive' else 'negative' if sentiment == 'Negative' else 'neutral'} outlook.\n ------------------------------\n"

        return report