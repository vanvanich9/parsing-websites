from pydantic import BaseModel
from .base import (
    BaseResponse,
    Status,
)


class ParsingElement(BaseModel):
    word: str
    value: int


class ParsingElementData(BaseModel):
    elements: list[ParsingElement]


class ParsingRequest(BaseModel):
    url: str
    save: bool = False


class ParsingResponse(BaseResponse):
    status: Status = Status.OK
    url: str
    data: ParsingElementData


class ParsingHistory(BaseModel):
    id: int
    url: str


class ParsingHistoryResponse(BaseResponse):
    status: Status = Status.OK
    data: list[ParsingHistory]