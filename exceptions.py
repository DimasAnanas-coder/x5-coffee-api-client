class CoffeeApiError(Exception):
    pass

class CoffeeNotFoundError(CoffeeApiError):
    pass
