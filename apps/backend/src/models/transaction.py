from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    Index,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base
from src.database.dependencies import generate_uuid


class Transaction(Base):
    __tablename__ = "transactions"

    uuid: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
        index=True,
    )

    booking_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)

    # Optional "Beleg" reference
    receipt_no: Mapped[str | None] = mapped_column(
        String(64), nullable=True, index=True
    )

    # Human readable description
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Helpful for bank statement imports (merchant / payee)
    payee: Mapped[str | None] = mapped_column(String(128), nullable=True, index=True)

    # For CSV import deduplication (hash or provider id)
    import_id: Mapped[str | None] = mapped_column(
        String(128), nullable=True, unique=True, index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )

    fiscal_year_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("fiscal_years.uuid", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    # If null -> use fiscal year's base currency
    currency_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("currencies.id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    fiscal_year: Mapped["FiscalYear"] = relationship()
    currency: Mapped["Currency | None"] = relationship()

    entries: Mapped[list["Entry"]] = relationship(
        back_populates="transaction",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("ix_transactions_year_date", "fiscal_year_id", "booking_date"),
    )

    def __repr__(self) -> str:
        return f"<Transaction uuid={self.uuid} date={self.booking_date} fiscal_year_id={self.fiscal_year_id}>"
