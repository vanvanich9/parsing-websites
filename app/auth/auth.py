from datetime import datetime
from fastapi import HTTPException, Request, Body, Header
import jwt

from .config import JWT_SECRET, JWT_ALGORITHM, TESTING_TOKEN
from ..database import users


def secure(payload: dict) -> str:
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token


def decode_token(token: str) -> dict:
    payload = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
    return payload


def is_valid_token(token: str) -> bool:
    payload = decode_token(token)
    if payload['exp'] < datetime.now().timestamp():
        return False

    return users.user_exists(payload['user_uuid'])


def auth(request: Request):
    token = request.cookies.get("access_token", None)
    if not token:
        raise HTTPException(status_code=403, detail="Not authorized")

    try:
        if _in_testing(token):
            return

        payload = decode_token(token)
        if payload['exp'] < datetime.now().timestamp():
            raise HTTPException(status_code=403, detail="Token expired")

        if not users.user_exists(payload['user_uuid']):
            raise HTTPException(status_code=403, detail="Invalid token")
    except:
        raise HTTPException(status_code=403, detail="Token does not exist")


def _in_testing(access_token):
    return access_token == TESTING_TOKEN


def parse_uuid(req: Request):
    access_token = req.cookies.get("access_token")
    if _in_testing(access_token):
        return "test_user"
    return access_token.get("user_uuid")
