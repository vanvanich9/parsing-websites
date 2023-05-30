from fastapi import APIRouter
from ..schemas import OKResponse


router = APIRouter()


@router.get("/ping", response_model=OKResponse)
def ping():
    return OKResponse(message="App work")
