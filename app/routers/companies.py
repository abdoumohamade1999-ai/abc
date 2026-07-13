from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.repositories.company_repository import CompanyRepository
from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["companies"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    repository = CompanyRepository(db)
    service = CompanyService(repository)
    return service.create_company(company)


@router.get("", response_model=list[CompanyResponse])
def list_companies(db: Session = Depends(get_db)):
    repository = CompanyRepository(db)
    service = CompanyService(repository)
    return service.list_companies()
