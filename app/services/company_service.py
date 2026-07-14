from sqlalchemy.orm import Session

from app.repositories.company_repository import create_company, get_companies
from app.schemas.company import CompanyCreate


def create(db: Session, company: CompanyCreate):
    return create_company(db, company)


def get_all(db: Session):
    return get_companies(db)
