import pandas as pd
import yfinance as yf

class StochasticOscillator:
    def __init__(self, symbol, period="max", interval="1d", k_period=14, d_period=3):
        self.data = yf.download(symbol, period=period, interval=interval)
        self.k_period = k_period
        self.d_period = d_period
    
    # Calculate the Stochastic Oscillator indicator
    def calculate(self):
        high_max = self.data['High'].rolling(window=self.k_period).max()
        low_min = self.data['Low'].rolling(window=self.k_period).min()
        close = self.data['Close']
        stoch_k = 100 * (close - low_min) / (high_max - low_min)
        stoch_d = stoch_k.rolling(window=self.d_period).mean()

        # Determine the current trend and sentiment based on Stochastic Oscillator
        current_stoch_k = stoch_k[-1]
        current_stoch_d = stoch_d[-1]

        if current_stoch_k > current_stoch_d:
            trend = "Bullish"
        else:
            trend = "Bearish"

        if current_stoch_k > 80:
            sentiment = "Very Positive"
        elif current_stoch_k > 50:
            sentiment = "Positive"
        elif current_stoch_k > 20:
            sentiment = "Neutral"
        else:
            sentiment = "Negative"

        # Generate the report
        report = f"Based on Stochastic Oscillator indicators for {self.k_period} and {self.d_period} periods on {self.data.index[-1].date()} ({self.data.index[-1].strftime('%H:%M:%S')}), the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}.\n\
        The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' or sentiment == 'Very Positive' else 'negative' if sentiment == 'Negative' else 'neutral'} outlook.\n ------------------------------\n"

        return report
