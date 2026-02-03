from pydantic import BaseModel


class DeleteResponse(BaseModel):
    id: str
    message: str
    status: str = "deleted"
