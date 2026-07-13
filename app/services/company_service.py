from app.repositories.company_repository import CompanyRepository
from app.schemas.company import CompanyCreate


class CompanyService:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    def create_company(self, company_data: CompanyCreate):
        payload = company_data.model_dump()
        return self.repository.create(payload)

    def list_companies(self):
        return self.repository.list()
