from .http import HTTPClient
from exceptions import CoffeeNotFoundError, CoffeeApiError

from models import JsonObject


class SampleApisCoffeeClient:
    def __init__(
        self,
        base_url: str = "https://api.sampleapis.com/coffee/hot",
        timeout: float = 10.0,
    ) -> None:
        base_url = base_url.rstrip("/")
        self.http_client = HTTPClient(base_url, timeout)

    def list_drinks(self) -> list[JsonObject]:
        try:
            response = self.http_client.request("GET", "/")
            if response.status_code != 200:
                raise CoffeeApiError
            return response.json()
        except CoffeeApiError:
            raise
        except Exception as e:
            raise CoffeeApiError(e)

    def get_drink(self, drink_id: int) -> JsonObject:
        try:
            response = self.http_client.request("GET", f"/{drink_id}")
            if response.status_code == 404:
                raise CoffeeNotFoundError
            elif response.status_code in (400, 422):
                raise CoffeeApiError("Invalid request")
            elif response.status_code != 200:
                raise CoffeeApiError
            return response.json()
        except CoffeeNotFoundError:
            raise
        except CoffeeApiError:
            raise
        except Exception as e:
            raise CoffeeApiError(e)

    def create_drink(self, payload: JsonObject) -> JsonObject:
        try:
            response = self.http_client.request("POST", "/", payload)
            if response.status_code == 400:
                raise CoffeeApiError("Malformed request")
            elif response.status_code == 422:
                raise CoffeeApiError("Validation failed")
            elif response.status_code != 201:
                raise CoffeeApiError
            return response.json()
        except CoffeeApiError:
            raise
        except Exception as e:
            raise CoffeeApiError(e)

    def replace_drink(
        self,
        drink_id: int,
        payload: JsonObject,
    ) -> JsonObject:
        try:
            response = self.http_client.request("PUT", f"/{drink_id}", payload)
            if response.status_code == 404:
                raise CoffeeNotFoundError
            elif response.status_code == 400:
                raise CoffeeApiError("Malformed request")
            elif response.status_code == 422:
                raise CoffeeApiError("Validation failed")
            elif response.status_code != 200:
                raise CoffeeApiError
            return response.json()
        except CoffeeNotFoundError:
            raise
        except CoffeeApiError:
            raise
        except Exception as e:
            raise CoffeeApiError(e)

    def update_drink(
        self,
        drink_id: int,
        changes: JsonObject,
    ) -> JsonObject:
        try:
            response = self.http_client.request("PATCH", f"/{drink_id}", changes)
            if response.status_code == 404:
                raise CoffeeNotFoundError
            elif response.status_code == 400:
                raise CoffeeApiError("Malformed request")
            elif response.status_code == 422:
                raise CoffeeApiError("Validation failed")
            elif response.status_code != 200:
                raise CoffeeApiError
            return response.json()
        except CoffeeNotFoundError:
            raise
        except CoffeeApiError:
            raise
        except Exception as e:
            raise CoffeeApiError(e)

    def delete_drink(self, drink_id: int) -> None:
        try:
            response = self.http_client.request("DELETE", f"/{drink_id}")
            if response.status_code == 404:
                raise CoffeeNotFoundError
            elif response.status_code in (400, 422):
                raise CoffeeApiError("Invalid request")
            elif response.status_code not in (200, 204):
                raise CoffeeApiError
        except CoffeeNotFoundError:
            raise
        except CoffeeApiError:
            raise
        except Exception as e:
            raise CoffeeApiError(e)