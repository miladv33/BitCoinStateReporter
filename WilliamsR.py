import pandas as pd
import yfinance as yf

class WilliamsR:
    def __init__(self, symbol, timeframe, period):
        self.bitcoin = yf.download(symbol, period="max", interval=timeframe)
        self.data = pd.DataFrame(self.bitcoin[['Close', 'High', 'Low']])
        self.period = period
        self.williams_r_data = self.calculate()

    # Define a function to calculate the Williams %R indicator
    def calculate(self):
        # Calculate the highest high and lowest low for the specified period
        high_max = self.data['High'].rolling(window=self.period).max()
        low_min = self.data['Low'].rolling(window=self.period).min()

        # Calculate the Williams %R indicator
        williams_r = ((high_max - self.data['Close']) / (high_max - low_min)) * -100

        # Return a DataFrame with the Williams %R values
        return pd.DataFrame({'Williams %R': williams_r}, index=self.data.index)

    def determine_trend(self):
        # Determine the current trend based on the Williams %R indicator
        if self.williams_r_data['Williams %R'].iloc[-1] < -80:
            trend = 'Bullish'
        else:
            trend = 'Bearish'
        return trend

    def determine_sentiment(self):
        # Determine the sentiment based on the position of the current Williams %R value relative to the oversold level
        if self.williams_r_data['Williams %R'].iloc[-1] > -20:
            sentiment = 'Positive'
        else:
            sentiment = 'Neutral'
        return sentiment

    def generate_report(self):
        trend = self.determine_trend()
        sentiment = self.determine_sentiment()

        # Generate the report
        report = f"Based on Williams %R indicators, the current trend is {trend}, which means that the price is expected to go {'up' if trend == 'Bullish' else 'down'}. The sentiment is {sentiment}, which means that there is a {'positive' if sentiment == 'Positive' else 'neutral'} outlook.\n ------------------------------\n"
        return report