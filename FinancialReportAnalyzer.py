class FinancialReportAnalyzer:
    def analyze_report(self, report):
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

        report_with_analysis = report + "\n\n"
        report_with_analysis += "## Analysis\n\n"
        report_with_analysis += analysis

        return report_with_analysis
