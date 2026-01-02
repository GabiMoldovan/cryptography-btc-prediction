from datetime import datetime, timezone
from decimal import Decimal

from service.CSVService import CSVService
from service.DailyReportService import DailyReportService

if __name__ == '__main__':
    print('Goodbye, world!')

    """
    daily_report_service = DailyReportService()
    
    # Create a daily report example
    daily_report = daily_report_service.create_daily_report(
        day=datetime(2025, 1, 2, 0, 0, 0, tzinfo=timezone.utc),
        time_high=datetime(2025, 1, 2, 20, 25, 0, tzinfo=timezone.utc),
        time_low=datetime(2025, 1, 2, 4, 10, 0, tzinfo=timezone.utc),
        open_value=Decimal("94416.28655"),
        high_value=Decimal("97739.81684"),
        low_value=Decimal("94201.57042"),
        close_value=Decimal("96886.87827"),
        circulating_currency=19804871
    )

    print(daily_report.toString())
    """
    daily_report_service = DailyReportService()
    csv_service = CSVService()

    #daily_report_service.delete_everything_from_database()
    csv_service.parse_csvs()