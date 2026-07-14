from datetime import datetime

from pydantic import BaseModel, EmailStr


class CompanyCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str


class CompanyResponse(CompanyCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
