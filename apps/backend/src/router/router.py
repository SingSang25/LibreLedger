from datetime import datetime
from fastapi import APIRouter

from src.router.fiscal_year import router as fiscal_year


router = APIRouter()


@router.get("/health")
async def read_root():
    return {"message": "Live", "timestamp": datetime.now().isoformat()}


router.include_router(fiscal_year.router, prefix="/fiscal_year", tags=["fiscal_year"])
