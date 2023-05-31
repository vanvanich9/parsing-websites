from fastapi import (
    APIRouter,
    Body,
    Response,
    Depends,
    Request,
)
from datetime import datetime, timedelta

from ..schemas import (
    OKResponse,
    ErrorCode,
    ErrorResponse,
    UserRequest,
)
from ..database import users
from ..auth import auth


router = APIRouter()


@router.post(
    "/auth/signin", 
    response_model=OKResponse | ErrorResponse,
)
def signin(response: Response, user: UserRequest = Body()):
    user_uuid = users.get_user_uuid(user)
    if user_uuid is None:
        return ErrorResponse(message="Invalid user login and/or password", error_code=ErrorCode.NOT_FOUND)

    token = auth.secure({'user_uuid': user_uuid, 'exp': datetime.now() + timedelta(days=1)})
    response.set_cookie(key="access_token", value=token)
    return OKResponse(message="Authorization completed successfully")


@router.delete(
    "/auth/logout", 
    response_model=OKResponse | ErrorResponse,
    dependencies=[Depends(auth.auth)]
)
def logout(response: Response):
    response.delete_cookie(key='access_token')
    return OKResponse(message="Logout successful")


@router.get(
    '/auth/is_auth',
    response_model=OKResponse | ErrorResponse,
    dependencies=[Depends(auth.auth)]
)
def is_auth():
    return OKResponse()


@router.post(
    '/auth/resecure', 
    response_model=OKResponse | ErrorResponse, 
    dependencies=[Depends(auth.auth)]
)
def resecure(req: Request, response: Response):
    access_token = req.cookies.get("access_token")
    payload = auth.decode_token(access_token)
    user_id = payload.get("user_uuid")
    token = auth.secure({'user_uuid': user_id, 'exp': datetime.now() + timedelta(days=1)})
    response.set_cookie(key="access_token", value=token)
    return OKResponse(message="Token resecured successfully")
