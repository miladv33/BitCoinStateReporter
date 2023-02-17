import pandas as pd
import yfinance as yf


class RSI:
    def __init__(self, symbol, timeframe, window_length=14):
        # Load the Bitcoin data from Yahoo Finance into a pandas DataFrame
        self.bitcoin = yf.download(symbol, period="max", interval=timeframe)
        self.data = pd.DataFrame(self.bitcoin['Close'])
        self.window_length = window_length

    def calculate_rsi(self):
        close = self.data['Close']
        delta = close.diff()
        delta = delta[1:]
        up = delta.where(delta > 0, 0)
        down = -delta.where(delta < 0, 0)
        rolling_up = up.rolling(self.window_length).mean()
        rolling_down = down.rolling(self.window_length).mean()
        rs = rolling_up / rolling_down
        rsi = 100.0 - (100.0 / (1.0 + rs))
        return rsi

    def calculate_trend_sentiment(self):
        # Calculate the RSI
        btc_rsi = self.calculate_rsi()

        # Determine the current trend and sentiment based on RSI
        last_rsi = btc_rsi[-1]
        if last_rsi > 50:
            trend = "Bullish"
        else:
            trend = "Bearish"

        if last_rsi > 70:
            sentiment = "Very Positive"
        elif last_rsi > 50:
            sentiment = "Positive"
        elif last_rsi > 30:
            sentiment = "Neutral"
        elif last_rsi > 0:
            sentiment = "Negative"
        else:
            sentiment = "Very Negative"

        # Generate the report
        report = f"Based on RSI indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}.\n\
        The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"

        return report