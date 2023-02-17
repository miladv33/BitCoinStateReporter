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
import pandas as pd

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

# create a dictionary to store the trend and sentiment data for each indicator
indicators = {
    'Bollinger Bands': [bollingerBands_trend, bollingerBands_sentiment],
    'Fibonacci Retracement Levels': [fibonacci_trend, fibonacci_sentiment],
    'Moving Average': [moving_average_trend, moving_average_sentiment],
    'MACD': [macd_trend, macd_sentiment],
    'OBV': [obv_trend, obv_sentiment],
    'RSI': [rsi_trend, rsi_sentiment],
    'Stochastic Oscillator': [stoch_trend, stoch_sentiment],
    'Williams %R': [wr_trend, wr_sentiment]
}

# create a pandas dataframe from the dictionary
df = pd.DataFrame.from_dict(indicators, orient='index', columns=['Trend', 'Sentiment'])

# create a function to generate the financial report
def generate_report():
    report = 'Financial Report\n\n'
    report += 'Market Status:\n'
    report += 'Based on the following indicators:\n\n'
    report += df.to_string() + '\n\n'
    report += 'Summary:\n'
    report += 'The market is currently '
    
    # determine the overall trend and sentiment based on the indicators
    bullish_count = df['Trend'].str.contains('Bullish').sum()
    bearish_count = df['Trend'].str.contains('Bearish').sum()
    neutral_count = df['Trend'].str.contains('Neutral').sum()
    
    if bullish_count > bearish_count:
        report += 'Bullish'
    elif bearish_count > bullish_count:
        report += 'Bearish'
    else:
        report += 'Neutral'
    
    report += ' with a '
    
    if neutral_count > 0:
        report += 'slightly '
    
    if all(df['Sentiment'] == 'Positive'):
        report += 'positive sentiment.'
    elif all(df['Sentiment'] == 'Negative'):
        report += 'negative sentiment.'
    else:
        report += 'mixed sentiment.'
    
    return report


deleteReadMe()
save(generate_report())
