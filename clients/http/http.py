import requests
from models import JsonObject

from requests.exceptions import Timeout, HTTPError, ConnectionError
from .constants import GET, POST, PUT, PATCH, DELETE, CONTENT_TYPE
from exceptions import (
    BadRequestError,
    NotFoundError,
    TooManyRequestsError,
    InternalServerError,
    UnprocessableEntityError,
    ServerUnavailableError,
    UnknownError,
    InvalidContentTypeError,
)   

class HTTPClient:

    def __init__(self, base_url: str, timeout: float) -> None:
        self.base_url = base_url
        self.timeout = timeout

    def request(
        self,   
        method: str,
        path: str = "",
        payload: JsonObject | None = None,
    ) -> dict:
        try:
            url = f"{self.base_url}{path}"
            response = self.__process_request(url, method, payload)
            response.raise_for_status()
            if response.status_code == 204 or not response.content:
                return {}
            if response.headers.get("Content-Type", "").find(CONTENT_TYPE) == -1:
                raise InvalidContentTypeError("Ответ не является JSON")
            return response.json()
        except HTTPError as e:
            if e.response.status_code == 400:
                raise BadRequestError("Передан невалидный запрос")
            elif e.response.status_code == 404:
                raise NotFoundError("Запрашиваемый ресурс не найден")
            elif e.response.status_code == 429:
                raise TooManyRequestsError("Слишком много запросов")
            elif e.response.status_code >= 500:
                raise InternalServerError("Внутренняя ошибка сервера")
            elif e.response.status_code == 422:
                raise UnprocessableEntityError("Невалидные данные")
            raise UnknownError("Неизвестная ошибка")
        except (ConnectionError, Timeout) as e:
            raise ServerUnavailableError("Сервер недоступен")

    def __process_request(self, url: str, method: str, payload: JsonObject | None = None) -> requests.Response:
        match method:
            case GET:
                return requests.get(url, timeout = self.timeout)
            case POST:
                return requests.post(url, json=payload, timeout = self.timeout)
            case PUT:
                return requests.put(url, json=payload, timeout = self.timeout)
            case PATCH:
                return requests.patch(url, json=payload, timeout = self.timeout)
            case DELETE:
                return requests.delete(url, timeout = self.timeout)
            case _:
                raise ValueError(f"Неизвестный метод: {method}")
