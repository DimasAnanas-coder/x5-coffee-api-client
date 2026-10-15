from ..http import HTTPClient, GET, POST, PUT, PATCH, DELETE
from .exceptions_mapper import get_coffee_exception

from models import JsonObject


class SampleApisCoffeeClient:
    def __init__(
        self,
        base_url: str = "https://api.sampleapis.com/coffee/hot",
        timeout: float = 10.0,
    ) -> None:
        base_url = base_url.rstrip("/")
        self.http_client = HTTPClient(base_url, timeout)

    def __request(self, method: str, endpoint: str, payload: JsonObject | None = None):
        try:
            response = self.http_client.request(method, endpoint, payload)
        except Exception as e:
            raise get_coffee_exception(e)
        return response

    def list_drinks(self) -> list[JsonObject]:
        return self.__request(GET, "/")

    def get_drink(self, drink_id: int) -> JsonObject:
        return self.__request(GET, f"/{drink_id}")

    def create_drink(self, payload: JsonObject) -> JsonObject:
        return self.__request(POST, "/", payload)

    def replace_drink(self, drink_id: int, payload: JsonObject) -> JsonObject:
        return self.__request(PUT, f"/{drink_id}", payload)

    def update_drink(self, drink_id: int, changes: JsonObject) -> JsonObject:
        return self.__request(PATCH, f"/{drink_id}", changes)

    def delete_drink(self, drink_id: int) -> None:
        self.__request(DELETE, f"/{drink_id}")