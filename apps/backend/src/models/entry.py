from __future__ import annotations

from decimal import Decimal

from sqlalchemy import (
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base


class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    transaction_uuid: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("transactions.uuid", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    ledger_account_uuid: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("ledger_accounts.uuid", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    # Signed amount: sum(entries.amount) must equal 0 per transaction
    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)

    memo: Mapped[str | None] = mapped_column(Text, nullable=True)

    transaction: Mapped["Transaction"] = relationship(back_populates="entries")
    ledger_account: Mapped["LedgerAccount"] = relationship()

    def __repr__(self) -> str:
        return (
            f"<Entry id={self.id} tx={self.transaction_uuid} "
            f"account={self.ledger_account_uuid} amount={self.amount}>"
        )
