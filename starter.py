import requests
from uuid import uuid4


JsonObject = dict[str, object]


class CoffeeApiError(Exception):
    pass


class CoffeeNotFoundError(CoffeeApiError):
    pass


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

    def _request(
        self,
        method: str,
        path: str = "",
        payload: JsonObject | None = None,
    ) -> requests.Response:
        raise NotImplementedError


def main() -> int:
    client = SampleApisCoffeeClient()
    marker = uuid4().hex[:8]
    created_id = None
    try:
        # GET коллекции.
        # POST: исследуйте поля, добавьте marker в название.
        # Сразу сохраните id из ответа в created_id.
        # GET: сравните сохранённые поля с отправленными.
        # PUT и повторный GET: проверьте все заменённые поля.
        # PATCH и повторный GET: проверьте изменённое поле
        # и убедитесь, что остальные поля сохранились.
        # DELETE и GET: убедитесь, что вернулся ожидаемый 404.
        # После подтверждения удаления: created_id = None.
        raise NotImplementedError("Заполните этапы сценария")
    except (CoffeeApiError, ValueError) as error:
        print(f"Ошибка: {error}. Метка группы: {marker}")
        return 1
    finally:
        if created_id is not None:
            try:
                client.delete_drink(created_id)
            except CoffeeNotFoundError:
                pass
            except CoffeeApiError as error:
                print(f"Не удалось удалить id={created_id}: {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
