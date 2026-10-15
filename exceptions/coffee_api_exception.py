class CoffeeApiError(Exception):
    pass

class CoffeeNotFoundError(CoffeeApiError):
    pass

class CoffeeUnprocessableEntityError(CoffeeApiError):
    pass

class CoffeeBadRequestError(CoffeeApiError):
    pass