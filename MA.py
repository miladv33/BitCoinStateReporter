import pandas as pd
import yfinance as yf

class MovingAverage:
    def __init__(self, symbol, timeframe):    
        # Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
        self.bitcoin = yf.download(symbol, period="max", interval=timeframe)
        self.data = pd.DataFrame(self.bitcoin['Close'])

    # Calculate the moving averages and determine the trend and sentiment
    def calculate(self):
        ma_20 = self.data['Close'].rolling(window=20).mean()
        ma_50 = self.data['Close'].rolling(window=50).mean()

        if ma_20[-1] > ma_50[-1]:
            trend = 'Bullish'
        else:
            trend = 'Bearish'

        if ma_20[-1] > ma_50[-1] and ma_20[-1] - ma_50[-1] > 0.02 * self.data['Close'][-1]:
            sentiment = 'Positive'
        else:
            sentiment = 'Neutral'

        # Generate the report
        report = f"Based on MA indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"
        return report