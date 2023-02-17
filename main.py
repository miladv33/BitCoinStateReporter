from indicators.BollingerBands import BoillingerBands
from indicators.FibonacciRetracementLevels import FibonacciRetracementLevels
from indicators.MA import MovingAverage
from indicators.MACD import MACD
from indicators.OBV import OBV
from indicators.RSI import RSI
from indicators.StochasticOscillator import StochasticOscillator
from indicators.WilliamsR import WilliamsR
from reportors.FinancialReportGenerator import FinancialReportGenerator
from reportors.FinancialReportAnalyzer import FinancialReportAnalyzer
from fileManager.ReportSaver import ReportSaver

# Define the symbol and timeframe for analysis
symbol = "BTC-USD"
timeframe = "1d"
report_saver = ReportSaver()

# Define the indicators to use for analysis
indicators = [
    BoillingerBands(symbol=symbol, timeframe=timeframe),
    FibonacciRetracementLevels(symbol=symbol, timeframe=timeframe),
    MovingAverage(symbol=symbol, timeframe=timeframe),
    MACD(symbol=symbol, timeframe=timeframe),
    OBV(symbol=symbol, timeframe=timeframe),
    RSI(symbol=symbol, timeframe=timeframe),
    StochasticOscillator(symbol=symbol, interval=timeframe),
    WilliamsR(symbol=symbol, timeframe=timeframe, period=14),
]

# Generate the report
report_generator = FinancialReportGenerator(symbol, timeframe, indicators)
report = report_generator.generate_report()

# Analyze the report
report_analyzer = FinancialReportAnalyzer()
analysis = report_analyzer.analyze_report(report)

report_saver.remove_readme()
report_saver.save_report(analysis)

print("Financial report has been generated and saved.")
