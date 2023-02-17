import pandas as pd
import yfinance as yf

class OBV:
    def __init__(self, symbol, timeframe):
        # Load the data from Yahoo Finance into a pandas DataFrame
        self.data = yf.download(symbol, period="max", interval=timeframe)
        self.obv = self.calculate_obv()

    def calculate_obv(self):
        close = self.data['Close']
        volume = self.data['Volume']
        prev_obv = pd.Series([0], index=self.data.index[:1])
        for i in range(1, len(close)):
            if close[i] > close[i-1]:
                current_obv = prev_obv[i-1] + volume[i]
            elif close[i] < close[i-1]:
                current_obv = prev_obv[i-1] - volume[i]
            else:
                current_obv = prev_obv[i-1]
            prev_obv = prev_obv.append(pd.Series(current_obv, index=[self.data.index[i]]))
        return prev_obv

    def calculate_trend_sentiment(self):
        last_close = self.data['Close'][-1]
        last_obv = self.obv[-1]
        rolling_mean_close = self.data['Close'].rolling(window=20).mean()
        rolling_mean_obv = self.obv.rolling(window=20).mean()

        if last_close > rolling_mean_close[-1]:
            trend = "Bullish"
        else:
            trend = "Bearish"

        if last_obv > rolling_mean_obv[-1]:
            sentiment = "Positive"
        else:
            sentiment = "Negative"

        return trend, sentiment

    def generate_report(self):
        trend, sentiment = self.calculate_trend_sentiment()
        report = f"Based on OBV indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}.\n\
The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'negative'} outlook.\n ------------------------------\n"
        return report