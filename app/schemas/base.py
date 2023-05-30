from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    OK = "OK"
    ERROR = "ERROR"


class BaseResponse(BaseModel):
    status: Status
    message: str


class OKResponse(BaseResponse):
    status: Status = Status.OK


class ErrorResponse(BaseResponse):
    status: Status = Status.ERROR
