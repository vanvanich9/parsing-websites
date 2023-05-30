from .config import test_client
from ..schemas import Status


def test_ping_app():
    res = test_client.get("/ping")

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK
