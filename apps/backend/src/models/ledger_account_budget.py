from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, UniqueConstraint, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base

if TYPE_CHECKING:
    from src.models.ledger_account import LedgerAccount
    from src.models.fiscal_year import FiscalYear


class LedgerAccountBudget(Base):
    __tablename__ = "ledger_account_budgets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    ledger_account_id: Mapped[str] = mapped_column(
        ForeignKey("ledger_accounts.uuid", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    fiscal_year_id: Mapped[str] = mapped_column(
        ForeignKey("fiscal_years.uuid", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    budget_monthly: Mapped[Decimal | None] = mapped_column(
        Numeric(14, 2), nullable=True
    )
    budget_yearly: Mapped[Decimal | None] = mapped_column(Numeric(14, 2), nullable=True)

    ledger_account: Mapped["LedgerAccount"] = relationship(back_populates="budgets")
    fiscal_year: Mapped["FiscalYear"] = relationship()

    __table_args__ = (
        UniqueConstraint(
            "ledger_account_id", "fiscal_year_id", name="uq_budget_account_year"
        ),
        Index("ix_budget_account_year", "ledger_account_id", "fiscal_year_id"),
    )

    def __repr__(self) -> str:
        return (
            f"<LedgerAccountBudget id={self.id} "
            f"ledger_account_id={self.ledger_account_id} "
            f"fiscal_year_id={self.fiscal_year_id} "
            f"monthly={self.budget_monthly} yearly={self.budget_yearly}>"
        )
