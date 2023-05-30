from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

from .config import test_client
from ..schemas import Status
from ..auth import auth
from ..database import methods as db_methods

load_dotenv()
TESTING_USER = os.getenv("TESTING_USER")
TESTING_PASSWORD = os.getenv("TESTING_PASSWORD")

def test_auth():
    test_client.disable_testing_token()

    res = test_client.post(
        "/auth/signin", 
        json={
            "username": TESTING_USER, 
            "password": TESTING_PASSWORD
        },
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK

    assert dict(res.cookies).get("access_token", None)

    user_uuid = db_methods.db_get_user(
        username=TESTING_USER, 
        password=TESTING_PASSWORD
    )[0]
    payload = auth.decode_token(dict(res.cookies).get("access_token"))

    assert payload['user_uuid'] == user_uuid


def test_logout():
    test_client.disable_testing_token()

    user_uuid = db_methods.db_get_user(
        username=TESTING_USER, 
        password=TESTING_PASSWORD
    )[0]
    token = auth.secure(
        {
            'user_uuid': user_uuid, 
            'exp': datetime.now() + timedelta(days=1)
        }
    )

    res = test_client.delete(
        "/auth/logout", 
        cookies=dict(access_token=token),
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK
    
    assert dict(res.cookies).get("access_token", None) is None


def test_is_auth():
    test_client.disable_testing_token()

    user_uuid = db_methods.db_get_user(
        username=TESTING_USER, 
        password=TESTING_PASSWORD
    )[0]
    token = auth.secure(
        {
            'user_uuid': user_uuid, 
            'exp': datetime.now() + timedelta(days=1)
        }
    )

    res = test_client.get(
        "/auth/is_auth", 
        cookies=dict(access_token=token),
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK
def test_resecure_token():
    test_client.disable_testing_token()

    user_uuid = db_methods.db_get_user(
        username=TESTING_USER, 
        password=TESTING_PASSWORD
    )[0]
    token = auth.secure(
        {
            'user_uuid': user_uuid, 
            'exp': datetime.now() + timedelta(days=1)
        }
    )

    res = test_client.post(
        "/auth/resecure", 
        cookies=dict(access_token=token),
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK

    assert dict(res.cookies).get("access_token", None)

    user_uuid = db_methods.db_get_user(
        username=TESTING_USER, 
        password=TESTING_PASSWORD
    )[0]
    payload = auth.decode_token(dict(res.cookies).get("access_token"))

    assert payload['user_uuid'] == user_uuid
