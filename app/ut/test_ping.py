from .config import test_client
from ..schemas import Status


def test_ping_app():
    test_client.enable_testing_token()

    res = test_client.get("/api/ping")

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK


def test_ping_with_token():
    test_client.enable_testing_token()

    res = test_client.get("/api/ping-with-token")

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK


def test_ping_without_token():
    test_client.disable_testing_token()

    res = test_client.get("/api/ping-with-token")

    assert res.status_code == 403
