from sqlalchemy import Column, Integer, DateTime, Numeric
from database.database import Base


class DailyReport(Base):
    __tablename__ = "daily_report"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # date / time (UTC)
    day = Column(DateTime(timezone=True), nullable=False)
    time_high = Column(DateTime(timezone=True), nullable=False)
    time_low = Column(DateTime(timezone=True), nullable=False)

    # prices (BTC)
    open = Column(Numeric(20, 8), nullable=False)
    high = Column(Numeric(20, 8), nullable=False)
    low = Column(Numeric(20, 8), nullable=False)
    close = Column(Numeric(20, 8), nullable=False)

    # supply
    circulating_currency = Column(Integer, nullable=False)

    def toString(self) -> str:
        return (
            f"DailyReport:\n"
            f"  id: {self.id}\n"
            f"  day: {self.day}\n"
            f"  time_high: {self.time_high}\n"
            f"  time_low: {self.time_low}\n"
            f"  open: {self.open}\n"
            f"  high: {self.high}\n"
            f"  low: {self.low}\n"
            f"  close: {self.close}\n"
            f"  circulating_currency: {self.circulating_currency}"
        )
