from fastapi import FastAPI

from src.models import (
    currency,
    entry,
    fiscal_year,
    ledger_account,
    ledger_account_budget,
    transaction,
)
from src.database.database import engine
from src.router import router

app = FastAPI()

currency.Currency.metadata.create_all(bind=engine)
fiscal_year.FiscalYear.metadata.create_all(bind=engine)
ledger_account.LedgerAccount.metadata.create_all(bind=engine)
ledger_account_budget.LedgerAccountBudget.metadata.create_all(bind=engine)
transaction.Transaction.metadata.create_all(bind=engine)
entry.Entry.metadata.create_all(bind=engine)

app.include_router(router.router, prefix="/api/v1")
