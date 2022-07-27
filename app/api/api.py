from fastapi import APIRouter
from app.api.endpoints import fast
from app.api.external import extapi

api_router = APIRouter()
api_router.include_router(fast.router, tags=["FastAPI"])
api_router.include_router(extapi.router, tags=["External API"])
