# import ATR
import BollingerBands
import FibonacciRetracementLevels
import IchimokuCloud
import MA
import MACD
import OBV
import RSI
import StochasticOscillator
import WilliamsR
import os

def save(report):
    with open("README.md", "a") as file:
        file.write(report)

def deleteReadMe():
    if os.path.exists('README.md'):
        os.remove('README.md')
        print('README.md file has been deleted.')
    else:
        print('README.md file does not exist.')

#bollingerBands indicator
symbol = "BTC-USD"
timeframe = "1d"
bollingerBands = BollingerBands.BoillingerBands(symbol=symbol, timeframe=timeframe)
bollingerBands_trend, bollingerBands_sentiment  = bollingerBands.calculate()

fibonacci = FibonacciRetracementLevels.FibonacciRetracementLevels(symbol, timeframe)
fibonacci_trend, fibonacci_sentiment = fibonacci.calculate()

moving_average = MA.MovingAverage(symbol=symbol, timeframe=timeframe)
moving_average_trend, moving_average_sentiment = moving_average.calculate()

macd = MACD.MACD(symbol = symbol, timeframe = timeframe)
macd_trend, macd_sentiment = macd.calculate()

obv = OBV.OBV(symbol= symbol, timeframe= timeframe)
obv_trend, obv_sentiment = obv.calculate_trend_sentiment()

rsi = RSI.RSI(symbol=symbol, timeframe=timeframe)
rsi_trend, rsi_sentiment = rsi.calculate_trend_sentiment()

stoch = StochasticOscillator.StochasticOscillator(symbol=symbol, interval = timeframe)
stoch_trend, stoch_sentiment = stoch.calculate()

wr = WilliamsR.WilliamsR(symbol=symbol, timeframe=timeframe, period=14)
wr_trend, wr_sentiment = wr.generate_report()

# ichimokuCloud = IchimokuCloud.IchimokuCloud(symbol=symbol, timeframe=timeframe)
# ichimokuCloudReport = ichimokuCloud.calculate()
# save(ichimokuCloudReport)


deleteReadMe()
save(bollingerBands_trend+ "\n")
save(bollingerBands_sentiment+ "\n")
save(fibonacci_trend+ "\n")
save(fibonacci_sentiment+ "\n")
save(moving_average_trend+ "\n")
save(moving_average_sentiment+ "\n")
save(macd_trend+ "\n")
save(macd_sentiment+ "\n")
save(obv_trend+ "\n")
save(obv_sentiment+ "\n")
save(rsi_trend+ "\n")
save(rsi_sentiment+ "\n")
save(stoch_trend+ "\n")
save(stoch_sentiment+ "\n")
save(wr_trend+ "\n")
save(wr_sentiment+ "\n")