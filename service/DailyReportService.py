from model import DailyReport
from repository.DailyReportRepository import DailyReportRepository
from datetime import datetime
from decimal import Decimal

class DailyReportService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        self.csv_repo = DailyReportRepository()
        self._initialized = True

    def delete_everything_from_database(self):
        self.csv_repo.delete_everything_from_database()

    def create_daily_report(
            self,
            day: datetime,
            time_high: datetime,
            time_low: datetime,
            open_value: Decimal,
            high_value: Decimal,
            low_value: Decimal,
            close_value: Decimal,
            circulating_currency: int
    ) -> DailyReport:
        return self.csv_repo.save_daily_report(day, time_high, time_low, open_value, high_value, low_value, close_value, circulating_currency)
