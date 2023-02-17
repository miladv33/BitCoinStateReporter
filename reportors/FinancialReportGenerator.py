class FinancialReportGenerator:
    def __init__(self, symbol, timeframe, indicators):
        self.symbol = symbol
        self.timeframe = timeframe
        self.indicators = indicators
    
    def format_result(self, result):
        trend = result[0]
        sentiment = result[1]

        if trend == "Bullish":
            trend_icon = "📈"
        elif trend == "Bearish":
            trend_icon = "📉"
        else:
            trend_icon = "🔺"

        if "Positive" in sentiment:
            sentiment_icon = "👍"
        elif "Negative" in sentiment:
            sentiment_icon = "👎"
        else:
            sentiment_icon = "🤏"

        return f"{trend_icon} {trend.capitalize()} / {sentiment_icon} {sentiment.capitalize()}"

    def generate_report(self):
        report = f"# Financial Report for {self.symbol} ({self.timeframe})\n\n"

        for indicator in self.indicators:
            name = indicator.__class__.__name__
            result = indicator.calculate_trend_sentiment()

            trend_sentiment = self.format_result(result)
            report += f"## {name}\n\n{trend_sentiment}\n\n"

        return report
