from .config import test_client
from ..schemas import Status


def test_ping_app():
    test_client.enable_testing_token()

    res = test_client.get("/ping")

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK


def test_ping_with_token():
    test_client.enable_testing_token()

    res = test_client.get("/ping-with-token")

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK


def test_ping_without_token():
    test_client.disable_testing_token()

    res = test_client.get("/ping-with-token")

    assert res.status_code == 403
