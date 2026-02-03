from fastapi import APIRouter
from src.router.fiscal_year import router as fiscal_year


router = APIRouter()


@router.get("")
async def read_root():
    return {"message": "Welcome to the LibreLedger Backend API"}


router.include_router(fiscal_year.router, prefix="/fiscal_year", tags=["fiscal_year"])
