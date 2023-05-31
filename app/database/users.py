from ..schemas import UserRequest
from . import methods as db_methods


def create_user(user: UserRequest) -> None:
    db_methods.db_add_user(user.username, user.password)


def get_user_uuid(user: UserRequest) -> str | None:
    user = db_methods.db_get_user(user.username, user.password)

    user_uuid = None
    if user:
        user_uuid = user[0]
    return user_uuid


def user_exists(user_uuid: str) -> bool:
    return bool(db_methods.db_get_user_by_uuid(user_uuid))
