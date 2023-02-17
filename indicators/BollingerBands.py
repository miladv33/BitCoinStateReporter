import pandas as pd
import yfinance as yf

class BoillingerBands:
    def __init__(self, symbol, timeframe):    
        # Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
        self.bitcoin = yf.download(symbol, period="max", interval=timeframe)
        self.data = pd.DataFrame(self.bitcoin['Close'])

    # Calculate the Bollinger Bands indicator
    def calculate_trend_sentiment(self):
        n = 20  # Number of days for the moving average
        k = 2  # Number of standard deviations for the bands
        rolling_mean = self.data['Close'].rolling(window=n).mean()
        rolling_std = self.data['Close'].rolling(window=n).std()
        upper_band = rolling_mean + k * rolling_std
        lower_band = rolling_mean - k * rolling_std

        # Determine the current trend based on the Bollinger Bands
        if self.data['Close'][-1] > upper_band[-1]:
            trend = 'Bullish'
        elif self.data['Close'][-1] < lower_band[-1]:
            trend = 'Bearish'
        else:
            trend = 'Neutral'

        # Determine the sentiment based on the distance between the current price and the lower band
        distance_to_lower_band = (self.data['Close'][-1] - lower_band[-1]) / lower_band[-1]
        if distance_to_lower_band > 0.05:
            sentiment = 'Positive'
        else:
            sentiment = 'Neutral'

        # Generate the report
        return trend, sentiment