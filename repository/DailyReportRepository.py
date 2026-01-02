from database import Database, Base
from model import DailyReport
from datetime import datetime
from decimal import Decimal

class DailyReportRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if getattr(self, "_initialized", False):
            return

        self.__db = Database()
        self._initialized = True

    def delete_everything_from_database(self):
        with self.__db.session() as session:
            for table in reversed(Base.metadata.sorted_tables):
                session.execute(table.delete())
            session.commit()

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
        daily_report = DailyReport(
            day=day,
            time_high=time_high,
            time_low=time_low,
            open=open_value,
            high=high_value,
            low=low_value,
            close=close_value,
            circulating_currency=circulating_currency
        )

        with self.__db.session() as session:
            session.add(daily_report)
            session.flush()

        return daily_report
