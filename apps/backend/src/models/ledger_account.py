from datetime import date
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum as SAEnum, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base
from src.database.dependencies import generate_uuid

if TYPE_CHECKING:
    from src.models.ledger_account_budget import LedgerAccountBudget


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

    # "Konto" - stable code, e.g. "1000" or "asset:bank:checking"
    code: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(256), nullable=True)

    type: Mapped[LedgerAccountType] = mapped_column(
        SAEnum(LedgerAccountType),
        nullable=False,
        index=True,
    )

    opened_on: Mapped[date | None] = mapped_column(Date, nullable=True)

    # Optional: if null -> default to fiscal year's base currency
    currency_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("currencies.id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    currency: Mapped["Currency | None"] = relationship(back_populates="ledger_accounts")
    budgets: Mapped[list["LedgerAccountBudget"]] = relationship(
        back_populates="ledger_account",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<LedgerAccount uuid={self.uuid} code={self.code} name={self.name} type={self.type}>"
