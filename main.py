import BollingerBands
import FibonacciRetracementLevels
import MA
import MACD
import OBV
import RSI
import StochasticOscillator
import WilliamsR
import os
import FinancialReportGenerator
import FinancialReportAnalyzer


# Define a function to save the report to a Markdown file
def save_report(report):
    with open("README.md", "a", encoding="utf-8") as file:
        file.write(report)

def removeReadMe():
    if os.path.exists("README.md"):
        os.remove("README.md")
        print("Existing report file has been deleted.")



# Define the symbol and timeframe for analysis
symbol = "BTC-USD"
timeframe = "1d"

# Define the indicators to use for analysis
indicators = [
    BollingerBands.BoillingerBands(symbol=symbol, timeframe=timeframe),
    FibonacciRetracementLevels.FibonacciRetracementLevels(symbol=symbol, timeframe=timeframe),
    MA.MovingAverage(symbol=symbol, timeframe=timeframe),
    MACD.MACD(symbol=symbol, timeframe=timeframe),
    OBV.OBV(symbol=symbol, timeframe=timeframe),
    RSI.RSI(symbol=symbol, timeframe=timeframe),
    StochasticOscillator.StochasticOscillator(symbol=symbol, interval=timeframe),
    WilliamsR.WilliamsR(symbol=symbol, timeframe=timeframe, period=14),
]

# Generate the report
report_generator = FinancialReportGenerator.FinancialReportGenerator(symbol, timeframe, indicators)
report = report_generator.generate_report()

# Analyze the report
report_analyzer = FinancialReportAnalyzer.FinancialReportAnalyzer()
analysis = report_analyzer.analyze_report(report)

removeReadMe()
save_report(analysis)

print("Financial report has been generated and saved.")
