from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    OK = "OK"
    ERROR = "ERROR"


class ErrorCode(int, Enum):
    UNKNOWN = -1
    NOT_FOUND = 1
    NOT_OWNER = 2
    NOT_EXIST = 3


class BaseResponse(BaseModel):
    status: Status
    message: str = ""


class OKResponse(BaseResponse):
    status: Status = Status.OK


class ErrorResponse(BaseResponse):
    status: Status = Status.ERROR
    error_code: ErrorCode = ErrorCode.UNKNOWN
