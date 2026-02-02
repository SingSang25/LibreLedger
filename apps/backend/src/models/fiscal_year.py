from __future__ import annotations

from datetime import date

from sqlalchemy import ForeignKey, String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base
from src.database.dependencies import generate_uuid


class FiscalYear(Base):
    __tablename__ = "fiscal_years"

    uuid: Mapped[str] = mapped_column(
        String(36), primary_key=True, index=True, default=generate_uuid
    )
    name: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(256), nullable=True)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    base_currency_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("currencies.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    base_currency: Mapped["Currency"] = relationship(back_populates="fiscal_years")

    __repr__ = (
        lambda self: f"<FiscalYear uuid={self.uuid} name={self.name} base_currency={self.base_currency_id} start_date={self.start_date} end_date={self.end_date} >"
    )
    __str__ = (
        lambda self: f"FiscalYear {self.name} ({self.start_date} to {self.end_date}) in {self.base_currency_id}"
    )
