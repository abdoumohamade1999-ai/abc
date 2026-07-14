from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.company import CompanyCreate, CompanyResponse
from app.services import company_service

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/", response_model=CompanyResponse)
def create(company: CompanyCreate, db: Session = Depends(get_db)):
    return company_service.create(db, company)


@router.get("/", response_model=list[CompanyResponse])
def get_all(db: Session = Depends(get_db)):
    return company_service.get_all(db)
