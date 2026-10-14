import requests

from abc import ABC, abstractclassmethod
from models import JsonObject

from requests.exceptions import RequestException, Timeout, HTTPError, ConnectionError


class HTTPClient:

    def __init__(self, base_url: str, timeout: float) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def request(
        self,
        method: str,
        path: str = "",
        payload: JsonObject | None = None,
    ) -> requests.Response:
        url = f"{self.base_url}{path}"
        match method:
            case "GET":
                return requests.get(
                    url=url,
                    timeout=self.timeout,
                )
            case "POST":
                return requests.post(
                    url=url,
                    timeout=self.timeout,
                    json=payload,
                )
            case "PUT":
                return requests.put(
                    url=url,
                    timeout=self.timeout,
                    json=payload,
                )

            case "PATCH":
                response = requests.patch(
                    url=url,
                    timeout=self.timeout,
                    json=payload,
                )
                return response
            case "DELETE":
                response = requests.delete(
                    url=url,
                    timeout=self.timeout,
                )
                return response
            case _:
                raise ValueError(f"Невалидный метод HTTP: {method}")