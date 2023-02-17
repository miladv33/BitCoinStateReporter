import BollingerBands
import FibonacciRetracementLevels
import MA
import MACD
import OBV
import RSI
import StochasticOscillator
import WilliamsR
import os

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

# Define a function to format the trend and sentiment results for each indicator
def format_result(result):
    trend = result[0]
    sentiment = result[1]

    if trend == "up":
        trend_icon = "📈"
    elif trend == "down":
        trend_icon = "📉"
    else:
        trend_icon = "🔺"

    if sentiment == "positive":
        sentiment_icon = "👍"
    elif sentiment == "negative":
        sentiment_icon = "👎"
    else:
        sentiment_icon = "🤏"

    return f"{trend_icon} {trend.capitalize()} / {sentiment_icon} {sentiment.capitalize()}"

def generate_report_with_analysis():
    # Generate the report
    report = generate_report()
    
    # Interpret the report
    analysis = ""
    bullish_indicators = 0
    bearish_indicators = 0
    
    for line in report.split("\n"):
        if "🔺 Bullish" in line:
            bullish_indicators += 1
        elif "🔺 Bearish" in line:
            bearish_indicators += 1
    
    if bullish_indicators == bearish_indicators:
        analysis = "The indicators are evenly split between bullish and bearish, so it's difficult to make a prediction about the future direction of BTC-USD."
    elif bullish_indicators > bearish_indicators:
        analysis = "The majority of indicators are bullish, which suggests that BTC-USD may be headed for a period of growth."
    else:
        analysis = "The majority of indicators are bearish, which suggests that BTC-USD may be headed for a period of decline."
    
    # Combine the report and the analysis
    report_with_analysis = report + "\n\n"
    report_with_analysis += "## Analysis\n\n"
    report_with_analysis += analysis
    
    return report_with_analysis


# Define a function to generate the financial report in Markdown format
def generate_report():
    report = f"# Financial Report for {symbol} ({timeframe})\n\n"

    for indicator in indicators:
        name = indicator.__class__.__name__
        result = indicator.calculate_trend_sentiment()

        trend_sentiment = format_result(result)
        report += f"## {name}\n\n{trend_sentiment}\n\n"

    return report

# Define a function to save the report to a Markdown file
def save_report(report):
    with open("README.md", "a", encoding="utf-8") as file:
        file.write(report)

# Delete any existing report file and generate a new report
if os.path.exists("README.md"):
    os.remove("README.md")
    print("Existing report file has been deleted.")

report = generate_report_with_analysis()
save_report(report)
print("Financial report has been generated and saved.")
