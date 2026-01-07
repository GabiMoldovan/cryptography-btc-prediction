from database import Database, Base
from model import DailyReport
from datetime import datetime, timezone
from decimal import Decimal

class DailyReportRepository:
    def __init__(self):
        self.__db = Database()

    def delete_everything_from_database(self):
        with self.__db.session() as session:
            for table in reversed(Base.metadata.sorted_tables):
                session.execute(table.delete())
            session.commit()

    def save_daily_report(
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

    def get_annual_report(self, year: int) -> list[DailyReport]:
        start_date = datetime(year, 1, 1, tzinfo=timezone.utc)
        end_date = datetime(year + 1, 1, 1, tzinfo=timezone.utc)

        with self.__db.session() as session:
            reports = (
                session.query(DailyReport)
                .filter(DailyReport.day >= start_date)
                .filter(DailyReport.day < end_date)
                .order_by(DailyReport.day.asc())
                .all()
            )

        return reports

    def get_reports_between(self, start_dt: datetime, end_dt: datetime) -> list[DailyReport]:
        with self.__db.session() as session:
            reports = (
                session.query(DailyReport)
                .filter(DailyReport.day >= start_dt)
                .filter(DailyReport.day < end_dt)
                .order_by(DailyReport.day.asc())
                .all()
            )
        return reports
