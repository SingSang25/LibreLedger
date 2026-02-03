from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.dependencies import get_db
from src.router.fiscal_year import fiscal_year_uuid
from src.schema.fiscal_year import FiscalYearCreate, FiscalYear
from src.service.fiscal_year import (
    create_fiscal_year as create_fiscal_year_service,
    get_fiscal_years as get_fiscal_years_service,
)

router = APIRouter()


@router.get("", response_model=list[FiscalYear])
async def get_fiscal_years(
    db: Session = Depends(get_db),
):
    return get_fiscal_years_service(db)


@router.post("", response_model=FiscalYearCreate)
async def create_fiscal_year(
    fiscal_year_data: FiscalYearCreate,
    db: Session = Depends(get_db),
):
    return create_fiscal_year_service(fiscal_year_data, db)


router.include_router(
    fiscal_year_uuid.router, prefix="/{fiscal_year_uuid}", tags=["fiscal_year"]
)
