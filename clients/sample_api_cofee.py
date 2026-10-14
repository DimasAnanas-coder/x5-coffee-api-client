from .http import HTTPClient
from exceptions import CoffeeNotFoundError, CoffeeApiErrors

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
            if response.status != 200:
                raise CoffeeApiErrors
            return response.json()
        except CoffeeApiErrors:
            raise
        except Exception as e:
            raise CoffeeApiErrors(e)

    def get_drink(self, drink_id: int) -> JsonObject:
        try:
            response = self.http_client.request("GET", f"/{drink_id}")
            if response.status == 404:
                raise CoffeeNotFoundError
            elif response.status in (400, 422):
                raise CoffeeApiErrors("Invalid request")
            elif response.status != 200:
                raise CoffeeApiErrors
            return response.json()
        except CoffeeNotFoundError:
            raise
        except CoffeeApiErrors:
            raise
        except Exception as e:
            raise CoffeeApiErrors(e)

    def create_drink(self, payload: JsonObject) -> JsonObject:
        try:
            response = self.http_client.request("POST", "/", payload)
            if response.status == 400:
                raise CoffeeApiErrors("Malformed request")
            elif response.status == 422:
                raise CoffeeApiErrors("Validation failed")
            elif response.status != 201:
                raise CoffeeApiErrors
            return response.json()
        except CoffeeApiErrors:
            raise
        except Exception as e:
            raise CoffeeApiErrors(e)

    def replace_drink(
        self,
        drink_id: int,
        payload: JsonObject,
    ) -> JsonObject:
        try:
            response = self.http_client.request("PUT", f"/{drink_id}", payload)
            if response.status == 404:
                raise CoffeeNotFoundError
            elif response.status == 400:
                raise CoffeeApiErrors("Malformed request")
            elif response.status == 422:
                raise CoffeeApiErrors("Validation failed")
            elif response.status != 200:
                raise CoffeeApiErrors
            return response.json()
        except CoffeeNotFoundError:
            raise
        except CoffeeApiErrors:
            raise
        except Exception as e:
            raise CoffeeApiErrors(e)

    def update_drink(
        self,
        drink_id: int,
        changes: JsonObject,
    ) -> JsonObject:
        try:
            response = self.http_client.request("PATCH", f"/{drink_id}", changes)
            if response.status == 404:
                raise CoffeeNotFoundError
            elif response.status == 400:
                raise CoffeeApiErrors("Malformed request")
            elif response.status == 422:
                raise CoffeeApiErrors("Validation failed")
            elif response.status != 200:
                raise CoffeeApiErrors
            return response.json()
        except CoffeeNotFoundError:
            raise
        except CoffeeApiErrors:
            raise
        except Exception as e:
            raise CoffeeApiErrors(e)

    def delete_drink(self, drink_id: int) -> None:
        try:
            response = self.http_client.request("DELETE", f"/{drink_id}")
            if response.status == 404:
                raise CoffeeNotFoundError
            elif response.status in (400, 422):
                raise CoffeeApiErrors("Invalid request")
            elif response.status not in (200, 204):
                raise CoffeeApiErrors
        except CoffeeNotFoundError:
            raise
        except CoffeeApiErrors:
            raise
        except Exception as e:
            raise CoffeeApiErrors(e)