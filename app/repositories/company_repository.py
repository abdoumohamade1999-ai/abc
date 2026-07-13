from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate


def create_company(db: Session, company: CompanyCreate):
    new_company = Company(
        name=company.name,
        email=str(company.email),
        phone=company.phone,
    )
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company
