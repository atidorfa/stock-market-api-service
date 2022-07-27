from fastapi import APIRouter

router = APIRouter()

supported = {'FB', 'AAPL', 'MSFT', 'GOOGL', 'AMZN'}


@router.get("/import-stock/{stock_symbol}")
def import_league(stock_symbol: str):
    if stock_symbol in supported:
        return {"message": "OK"}
    else:
        return {"message": stock_symbol + " is not supported by the API"}
