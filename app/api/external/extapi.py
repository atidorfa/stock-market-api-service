from fastapi import APIRouter

router = APIRouter()


@router.get("/import-league/{league_code}")
def import_league(league_code: str):
    return {"message": league_code + " is not supported by the API"}