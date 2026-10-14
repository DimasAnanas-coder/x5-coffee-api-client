import requests

from abc import ABC, abstractclassmethod
from models import JsonObject


class HTTPClient:
    @abstractclassmethod
    def _request(
        self,
        method: str,
        path: str = "",
        payload: JsonObject | None = None,
    ) -> requests.Response:
        pass