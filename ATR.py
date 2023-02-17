import pandas as pd
import yfinance as yf

class ATR:
    def __init__(self):
    # Download the daily price data for Bitcoin
        self.btc_data = yf.download("BTC-USD", period="max", interval="1d")

    # Calculate the ATR for Bitcoin
    def calculate_atr(self, period=14):
        close = self.btc_data['Close']
        tr1 = pd.DataFrame(self.btc_data['High'] - self.btc_data['Low'])
        tr2 = pd.DataFrame(abs(self.btc_data['High'] - close.shift()))
        tr3 = pd.DataFrame(abs(self.btc_data['Low'] - close.shift()))
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis=1, join='inner')
        atr = tr.rolling(window=period).mean()
        atr.columns = ['ATR']
        return atr


    def generateReport(self):
        btc_atr = self.calculate_atr(14)
        # Determine the current trend and sentiment based on ATR
        last_close = self.btc_data['Close'][-1]
        last_atr = btc_atr['ATR'][-1]

        if last_close > last_atr:
             trend = "Bullish"
        else:
            trend = "Bearish"

        if last_atr < last_close * 0.01:
            sentiment = "Positive"
        else:
            sentiment = "Negative"

        # Generate the report
        report = f"Based on ATR indicators, the current trend is {trend}, which means that the price is expected to go up.\n\
        The sentiment is {sentiment}, which means that there is a positive outlook.\n ------------------------------\n"
        return report
        