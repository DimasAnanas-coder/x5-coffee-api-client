from uuid import uuid4
from clients.sample_api_cofee import SampleApisCoffeeClient

from exceptions import CoffeeApiError, CoffeeNotFoundError
from mock import CREATE_DRINK_REQUEST, PUT_DRINK_REQUEST

def main() -> int:
    client = SampleApisCoffeeClient()
    marker = uuid4().hex[:8]
    created_id = None
    
    try:
        print("Список напитков:")
        print(client.list_drinks(), end="\n\n")
        created_drink = client.create_drink({
            **CREATE_DRINK_REQUEST,
            "title": f"Test drink {marker}",
        })
        print("После добавления:")
        print(created_drink, end="\n\n")
        created_id = created_drink.get("id")
        if created_id is None:
            raise CoffeeApiError("Не удалось получить id созданного напитка")
        client.replace_drink(created_id, {
            **PUT_DRINK_REQUEST,
            "title": f"Test drink {marker} replaced",
        })
        print("После замены:")
        print(client.get_drink(created_id), end="\n\n")
        client.update_drink(created_id, {
            "title": f"Test drink {marker} updated"
        })
        print("После изменения:")
        print(client.get_drink(created_id), end="\n\n")
        client.delete_drink(created_id)
        print("После удаления:")
        print(client.get_drink(created_id), end="\n\n")
        created_id = None
    except CoffeeNotFoundError:
        print(f"Не удалось найти напиток с id={created_id}")
        return 1
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
