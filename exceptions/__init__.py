from .base_exception import (
    BadRequestError,
    NotFoundError,
    TooManyRequestsError,
    InternalServerError,
    UnprocessableEntityError,
    ServerUnavailableError,
    UnknownError,
    InvalidContentTypeError,
)

from .coffee_api_exception import (
    CoffeeApiError,
    CoffeeNotFoundError,
    CoffeeBadRequestError,
    CoffeeUnprocessableEntityError,
)

__all__ = [
    "BadRequestError",
    "NotFoundError",
    "TooManyRequestsError",
    "InternalServerError",
    "UnprocessableEntityError",
    "ServerUnavailableError",
    "UnknownError",
    "InvalidContentTypeError",

    "CoffeeApiError",
    "CoffeeNotFoundError",
    "CoffeeBadRequestError",
    "CoffeeUnprocessableEntityError",
]