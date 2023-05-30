import requests
from typing import Any


class TestClient():
    SERVER_URL = "http://0.0.0.0:4567"

    def get(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        return requests.get(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )


    def post(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        return requests.post(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )


    def delete(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        return requests.delete(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )
    

    def put(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        return requests.put(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )


test_client = TestClient()
