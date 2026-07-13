from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine
import app.models.company

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartSupport AI")


@app.get("/")
def root():
    return {"message": "SmartSupport AI Running"}
