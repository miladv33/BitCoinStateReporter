import os

class ReportSaver:
    @staticmethod
    def save_report(report):
        with open("README.md", "a", encoding="utf-8") as file:
            file.write(report)

    @staticmethod
    def remove_readme():
        if os.path.exists("README.md"):
            os.remove("README.md")
            print("Existing report file has been deleted.")
