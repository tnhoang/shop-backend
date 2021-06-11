from app.core.config import settings
from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix="/api/v1")
