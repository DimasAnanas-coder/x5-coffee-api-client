from uuid import uuid4
from clients.sample_api_cofee import SampleApisCoffeeClient

from exceptions import CoffeeApiError, CoffeeNotFoundError

def main() -> int:
    client = SampleApisCoffeeClient()
    marker = uuid4().hex[:8]
    created_id = None
    try:
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
