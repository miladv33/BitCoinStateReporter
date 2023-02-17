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


def save(report):
    with open("README.md", "a") as file:
        file.write(report)

#bollingerBands indicator
symbol = "BTC-USD"
timeframe = "1d"
bollingerBands = BollingerBands.BoillingerBands(symbol=symbol, timeframe=timeframe)
bollingerBandsOutput = bollingerBands.calculate()

fibonacci = FibonacciRetracementLevels.FibonacciRetracementLevels(symbol, timeframe)
fibonacci_report = fibonacci.calculate()

moving_average = MA.MovingAverage(symbol=symbol, timeframe=timeframe)
ma_report = moving_average.calculate()

macd = MACD.MACD(symbol = symbol, timeframe = timeframe)
macd_report = macd.calculate()

obv = OBV.OBV(symbol= symbol, timeframe= timeframe)
OBV_report = obv.generate_report()

rsi = RSI.RSI(symbol=symbol, timeframe=timeframe)
rsi_report = rsi.calculate_trend_sentiment()

stoch = StochasticOscillator.StochasticOscillator(symbol=symbol)
stoch_report = stoch.calculate()

wr = WilliamsR.WilliamsR(symbol=symbol, timeframe=timeframe, period=14)
wr_report = wr.generate_report()

# ichimokuCloud = IchimokuCloud.IchimokuCloud(symbol=symbol, timeframe=timeframe)
# ichimokuCloudReport = ichimokuCloud.calculate()

# save(ichimokuCloudReport)
save(fibonacci_report)
save(bollingerBandsOutput)
save(ma_report)
save(macd_report)
save(OBV_report)
save(rsi_report)
save(stoch_report)
save(wr_report)