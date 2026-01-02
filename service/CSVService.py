import pandas as pd
from decimal import Decimal

from service.DailyReportService import DailyReportService


class CSVService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        self.__daily_report_service = DailyReportService()
        self._initialized = True

    @staticmethod
    def parse_csvs() -> None:
        starting_year = 2020
        ending_year = 2025

        # range is [starting_year, ending_year + 1] => [2020, 2025]
        for year in range(starting_year, ending_year + 1):
            filepath = f"./bitcoin_csv/btc_{year}_clean.csv"

            csv_service = CSVService()
            csv_service.read_csv(filepath)
            print("Successfully saved the data for year " + str(year))

    def read_csv(self, filepath: str) -> None:
        df = pd.read_csv(filepath)

        for _, row in df.iterrows():
            day = pd.to_datetime(row["timeOpen"], utc=True).to_pydatetime()
            time_high = pd.to_datetime(row["timeHigh"], utc=True).to_pydatetime()
            time_low = pd.to_datetime(row["timeLow"], utc=True).to_pydatetime()

            open_value = Decimal(str(row["open"]))
            high_value = Decimal(str(row["high"]))
            low_value = Decimal(str(row["low"]))
            close_value = Decimal(str(row["close"]))

            circulating_currency = int(row["circulatingSupply"])

            self.__daily_report_service.create_daily_report(
                day=day,
                time_high=time_high,
                time_low=time_low,
                open_value=open_value,
                high_value=high_value,
                low_value=low_value,
                close_value=close_value,
                circulating_currency=circulating_currency
            )