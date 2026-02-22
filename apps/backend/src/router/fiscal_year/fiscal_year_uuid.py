from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.dependencies import get_db
from src.schema.fiscal_year import FiscalYear, FiscalYearUpdate
from src.schema.response import DeleteResponse
from src.service.fiscal_year import (
    get_fiscal_year_by_uuid,
    update_fiscal_year as update_fiscal_year_service,
    delete_fiscal_year as delete_fiscal_year_service,
)

router = APIRouter()


@router.get("", response_model=FiscalYear)
async def get_fiscal_year(
    fiscal_year_uuid: UUID,
    db: Session = Depends(get_db),
):
    return get_fiscal_year_by_uuid(str(fiscal_year_uuid), db)


@router.put("", response_model=FiscalYear)
async def update_fiscal_year(
    fiscal_year_uuid: UUID,
    fiscal_year_data: FiscalYearUpdate,
    db: Session = Depends(get_db),
):
    return update_fiscal_year_service(str(fiscal_year_uuid), fiscal_year_data, db)


@router.delete("", response_model=DeleteResponse)
async def delete_fiscal_year(
    fiscal_year_uuid: UUID,
    db: Session = Depends(get_db),
):
    return delete_fiscal_year_service(str(fiscal_year_uuid), db)
