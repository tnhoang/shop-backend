from fastapi import APIRouter
from app.api.api_v1.endpoints import items, lols

api_router = APIRouter()

api_router.include_router(items.router, prefix="/items")
api_router.include_router(lols.router, prefix="/lols")
