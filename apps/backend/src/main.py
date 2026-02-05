from fastapi import FastAPI

# Ensure all SQLAlchemy models are registered before app usage.
import src.models  # noqa: F401

from src.router import router

app = FastAPI()
app.include_router(router.router, prefix="/api/v1")
