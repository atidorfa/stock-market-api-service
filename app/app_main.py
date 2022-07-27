from fastapi import FastAPI
from app.config import get_settings
from app.api.api import api_router

app = FastAPI(title=get_settings().APP_DESC, openapi_url="/openapi.json")

# add api routers
app.include_router(api_router)
