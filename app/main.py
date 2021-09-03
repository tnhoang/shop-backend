from app.core.config import settings
from fastapi import FastAPI
from app.api.api_v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.1.236:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")
