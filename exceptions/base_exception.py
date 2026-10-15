class BadRequestError(Exception):
    pass

class NotFoundError(Exception):
    pass

class TooManyRequestsError(Exception):
    pass

class InternalServerError(Exception):
    pass

class UnprocessableEntityError(Exception):
    pass

class ServerUnavailableError(Exception):
    pass

class UnknownError(Exception):
    pass

class InvalidContentTypeError(Exception):
    pass