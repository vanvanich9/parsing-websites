from .config import test_client
from ..schemas import Status


def test_parse_data():
    test_client.enable_testing_token()

    res = test_client.post(
        "/parse/data",
        json={"url": "https://example.com/"}
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK
    assert res.json().get("url") == "https://example.com/"

    assert res.json().get("data").get("elements") == [
        {'word': '{', 'value': 5},
        {'word': '}', 'value': 5},
        {'word': '/>', 'value': 3},
        {'word': '<meta', 'value': 3},
        {'word': 'auto;', 'value': 3},
        {'word': 'in', 'value': 3},
        {'word': 'margin:', 'value': 3},
        {'word': '0;', 'value': 2},
        {'word': '2px', 'value': 2},
        {'word': 'background-color:', 'value': 2},
    ]


def test_get_parse_history():
    test_client.enable_testing_token()

    res = test_client.get(
        "/parse/history",
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK
    assert res.json().get("data") == [
        {'id': -3, 'url': 'https://example.com/'}, 
        {'id': -2, 'url': 'http://info.cern.ch/'},
    ]


def test_get_notice_with_big_id():
    test_client.enable_testing_token()
    id = 10 ** 10

    res = test_client.get(
        f"/parse/history/{id}",
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.ERROR


def test_get_notice_not_owner():
    test_client.enable_testing_token()
    id = -1      # Testing notice

    res = test_client.get(
        f"/parse/history/{id}",
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.ERROR


def test_get_notice():
    test_client.enable_testing_token()
    id = -3     # Testing notice

    res = test_client.get(
        f"/parse/history/{id}",
    )

    assert res.status_code == 200
    assert res.json().get("status") == Status.OK
    assert res.json().get("url") == "https://example.com/"

    assert res.json().get("data").get("elements") == [
        {'word': '{', 'value': 5},
        {'word': '}', 'value': 5},
        {'word': '/>', 'value': 3},
        {'word': '<meta', 'value': 3},
        {'word': 'auto;', 'value': 3},
        {'word': 'in', 'value': 3},
        {'word': 'margin:', 'value': 3},
        {'word': '0;', 'value': 2},
        {'word': '2px', 'value': 2},
        {'word': 'background-color:', 'value': 2},
    ]
