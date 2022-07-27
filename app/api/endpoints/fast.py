import logging
from fastapi import APIRouter

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/check")
def check():
    return {"message": "OK"}
