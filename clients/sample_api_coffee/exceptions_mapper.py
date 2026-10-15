from exceptions import (
    BadRequestError,
    NotFoundError,
    TooManyRequestsError,
    InternalServerError,
    UnprocessableEntityError,
    ServerUnavailableError,
    UnknownError,
    InvalidContentTypeError,

    CoffeeApiError,
    CoffeeNotFoundError,
    CoffeeBadRequestError,
    CoffeeUnprocessableEntityError,
)   


exception_associativity = {
    BadRequestError: CoffeeBadRequestError,
    NotFoundError: CoffeeNotFoundError,
    TooManyRequestsError: CoffeeApiError,
    InternalServerError: CoffeeApiError,
    UnprocessableEntityError: CoffeeUnprocessableEntityError,
    ServerUnavailableError: CoffeeApiError,
    UnknownError: CoffeeApiError,
    InvalidContentTypeError: CoffeeApiError,

    Exception: CoffeeApiError
}


def get_coffee_exception(e: Exception) -> CoffeeApiError:
    for cls in type(e).__mro__:
        coffee_cls = exception_associativity.get(cls)
        if coffee_cls is not None:
            return coffee_cls(str(e))
    return CoffeeApiError(str(e))
