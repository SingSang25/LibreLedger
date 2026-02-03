from __future__ import annotations

from datetime import date
from pydantic import BaseModel, Field, computed_field, field_validator

from src.schema.currency import Currency


class FiscalYearBase(BaseModel):
    model_config = {"from_attributes": True}


class FiscalYear(FiscalYearBase):
    uuid: str
    name: str
    description: str | None = None
    start_date: date
    end_date: date
    base_currency: Currency = Field(exclude=True)

    @computed_field
    @property
    def base_currency_code(self) -> str:
        return self.base_currency.code


class FiscalYearCreate(FiscalYearBase):
    name: str
    description: str | None = None
    start_date: date
    end_date: date
    base_currency_id: int

    @field_validator("end_date")
    @classmethod
    def end_must_be_after_start(cls, end_date: date, info):
        start_date = info.data.get("start_date")
        if start_date and end_date < start_date:
            raise ValueError("end_date must be on or after start_date")
        return end_date


class FiscalYearUpdate(FiscalYearBase):
    name: str | None = None
    description: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    base_currency_id: int | None = None

    @field_validator("end_date")
    @classmethod
    def end_must_be_after_start(cls, end_date: date, info):
        start_date = info.data.get("start_date")
        if start_date and end_date < start_date:
            raise ValueError("end_date must be on or after start_date")
        return end_date
