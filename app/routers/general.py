from fastapi import (
    APIRouter,
    Depends,
)
from ..schemas import (
    OKResponse,
    ErrorResponse,
)
from ..auth import auth


router = APIRouter()


@router.get(
    "/ping", 
    response_model=OKResponse | ErrorResponse,
)
def ping():
    return OKResponse(message="App work")


@router.get(
    "/ping-with-token", 
    response_model=OKResponse | ErrorResponse,
    dependencies=[Depends(auth.auth)])
def ping_with_token():
    return OKResponse(message="App work")
