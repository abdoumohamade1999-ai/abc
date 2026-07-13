from pydantic import BaseModel, EmailStr


class CompanyCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
