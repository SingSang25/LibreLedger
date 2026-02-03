from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from src.models.fiscal_year import FiscalYear
from src.schema.fiscal_year import FiscalYearCreate, FiscalYearUpdate
from src.schema.response import DeleteResponse


def get_fiscal_years(db: Session) -> list[FiscalYear]:
    return db.query(FiscalYear).all()


def get_fiscal_year_by_uuid(fiscal_year_uuid: str, db: Session) -> FiscalYear:
    fiscal_year = (
        db.query(FiscalYear).filter(FiscalYear.uuid == fiscal_year_uuid).one_or_none()
    )

    if fiscal_year is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Fiscal Year not found"
        )

    return fiscal_year


def create_fiscal_year(
    fiscal_year_data: FiscalYearCreate,
    db: Session,
) -> FiscalYear:
    fiscal_year = FiscalYear(**fiscal_year_data.model_dump())

    try:
        db.add(fiscal_year)
        db.flush()
        db.commit()
        db.refresh(fiscal_year)
        return fiscal_year

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Fiscal year violates a database constraint (e.g. base_currency_id does not exist).",
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create fiscal year",
        )


def update_fiscal_year(
    fiscal_year_uuid: str,
    fiscal_year_data: FiscalYearUpdate,
    db: Session,
):
    fiscal_year = get_fiscal_year_by_uuid(fiscal_year_uuid, db)

    for field, value in fiscal_year_data.model_dump(exclude_unset=True).items():
        setattr(fiscal_year, field, value)

    try:
        db.flush(fiscal_year)
        db.commit()
        db.refresh(fiscal_year)
        return fiscal_year

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Fiscal year violates a database constraint (e.g. base_currency_id does not exist).",
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update fiscal year",
        )


def delete_fiscal_year(fiscal_year_uuid: str, db: Session):
    fiscal_year = get_fiscal_year_by_uuid(fiscal_year_uuid, db)

    try:
        db.delete(fiscal_year)
        db.commit()
        return DeleteResponse(
            id=fiscal_year_uuid, message="Fiscal year deleted successfully"
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete fiscal year",
        )
