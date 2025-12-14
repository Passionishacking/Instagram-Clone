# This is our main app.

from fastapi import FastAPI
from .database import Base, engine
from .api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Instagram Clone App",
    description="Engine Behind Instagram Clone App",
    version="0.1",
)
app.include_router(router)