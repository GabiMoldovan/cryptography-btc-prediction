from .dailyReport import DailyReport
from sqlalchemy import Index

Index("idx_daily_report_day", DailyReport.day)
