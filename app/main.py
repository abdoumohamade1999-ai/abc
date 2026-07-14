from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine
from app.routers.companies import router as company_router
import app.models.company

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartSupport AI")
app.include_router(company_router)


@app.get("/")
def root():
    return {"message": "SmartSupport AI Running"}
