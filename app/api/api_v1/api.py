from fastapi import APIRouter
from app.api.api_v1.endpoints import items, authentication, products

api_router = APIRouter()

api_router.include_router(items.router, prefix="/items")
api_router.include_router(products.router, prefix="/products")
api_router.include_router(authentication.router, prefix="/authen")
