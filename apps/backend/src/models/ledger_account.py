from datetime import date
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum as SAEnum, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base
from src.database.dependencies import generate_uuid

if TYPE_CHECKING:
    from src.models.ledger_account_budget import LedgerAccountBudget
    from src.models.currency import Currency
    from src.models.entry import Entry


class LedgerAccountType(str, Enum):
    ASSET = "asset"
    LIABILITY = "liability"
    INCOME = "income"
    EXPENSE = "expense"
    EQUITY = "equity"


class LedgerAccount(Base):
    __tablename__ = "ledger_accounts"

    uuid: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=generate_uuid,
        index=True,
    )

    code: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(256), nullable=True)

    type: Mapped[LedgerAccountType] = mapped_column(
        SAEnum(LedgerAccountType),
        nullable=False,
        index=True,
    )

    opened_on: Mapped[date | None] = mapped_column(Date, nullable=True)

    currency_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("currencies.id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    currency: Mapped["Currency | None"] = relationship(
        "Currency",
        back_populates="ledger_accounts",
    )

    entries: Mapped[list["Entry"]] = relationship(
        "Entry",
        back_populates="ledger_account",
    )

    budgets: Mapped[list["LedgerAccountBudget"]] = relationship(
        "LedgerAccountBudget",
        back_populates="ledger_account",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<LedgerAccount uuid={self.uuid} code={self.code} name={self.name} type={self.type}>"
