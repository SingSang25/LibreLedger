from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base

if TYPE_CHECKING:
    from src.models.fiscal_year import FiscalYear
    from src.models.ledger_account import LedgerAccount


class Currency(Base):
    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(
        String(3), nullable=False, unique=True, index=True
    )

    # TODO: Multilingual support
    name: Mapped[str | None] = mapped_column(String(64), nullable=True)
    symbol: Mapped[str | None] = mapped_column(String(8), nullable=True)
    minor_units: Mapped[int] = mapped_column(Integer, nullable=False, default=2)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    fiscal_years: Mapped[list["FiscalYear"]] = relationship(
        "FiscalYear",
        back_populates="base_currency",
    )
    ledger_accounts: Mapped[list["LedgerAccount"]] = relationship(
        "LedgerAccount",
        back_populates="currency",
    )

    def __repr__(self) -> str:
        return (
            f"<Currency id={self.id} code={self.code} minor_units={self.minor_units}>"
        )
