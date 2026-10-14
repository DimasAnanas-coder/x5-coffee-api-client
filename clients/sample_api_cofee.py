from models import JsonObject

class SampleApisCoffeeClient:
    def __init__(
        self,
        base_url: str = "https://api.sampleapis.com/coffee/hot",
        timeout: float = 10.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout

    def list_drinks(self) -> list[JsonObject]:
        raise NotImplementedError

    def get_drink(self, drink_id: int) -> JsonObject:
        raise NotImplementedError

    def create_drink(self, payload: JsonObject) -> JsonObject:
        raise NotImplementedError

    def replace_drink(
        self,
        drink_id: int,
        payload: JsonObject,
    ) -> JsonObject:
        raise NotImplementedError

    def update_drink(
        self,
        drink_id: int,
        changes: JsonObject,
    ) -> JsonObject:
        raise NotImplementedError

    def delete_drink(self, drink_id: int) -> None:
        raise NotImplementedError
