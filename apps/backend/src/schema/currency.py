from pydantic import BaseModel


class CurrencyBase(BaseModel):
    id: int
    code: str
    name: str | None = None
    symbol: str | None = None
    minor_units: int

    model_config = {"from_attributes": True}


class Currency(CurrencyBase):
    is_active: bool


class CurrencyPayload(CurrencyBase):
    pass
