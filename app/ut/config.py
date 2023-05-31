import requests
from typing import Any
from dotenv import load_dotenv
import os

load_dotenv()
TESTING_TOKEN = os.getenv("TESTING_TOKEN")


class TestClient():
    SERVER_URL = os.getenv("SERVER_URL")
    
    def __init__(self):
        self.enable_testing_token()

    def get(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        if self.with_testing_token:
            if cookies:
                cookies['access_token'] = TESTING_TOKEN
            else:
                cookies = dict(access_token=TESTING_TOKEN)
        return requests.get(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )

    def post(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        if self.with_testing_token:
            if cookies:
                cookies['access_token'] = TESTING_TOKEN
            else:
                cookies = dict(access_token=TESTING_TOKEN)
        return requests.post(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )

    def delete(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        if self.with_testing_token:
            if cookies:
                cookies['access_token'] = TESTING_TOKEN
            else:
                cookies = dict(access_token=TESTING_TOKEN)
        return requests.delete(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )

    def put(self, url, params: Any = None, json: Any = None, cookies: Any = None, headers: Any = None):
        if self.with_testing_token:
            if cookies:
                cookies['access_token'] = TESTING_TOKEN
            else:
                cookies = dict(access_token=TESTING_TOKEN)
        return requests.put(
            url=self.SERVER_URL + url, 
            params=params,
            json=json,
            cookies=cookies,
            headers=headers,
            )

    def disable_testing_token(self):
        self.with_testing_token = False

    def enable_testing_token(self):
        self.with_testing_token = True


test_client = TestClient()
