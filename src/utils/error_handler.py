from functools import wraps

from utils.exceptions import MyBaseException
from utils.response import ErrorResponse

def error_handler(func):
    @wraps(func)

    def wrapper(*args: tuple, **kwargs: dict) -> None:
        try:
            return func(*args, **kwargs)
        except MyBaseException as error:
            return ErrorResponse.error_message(error), error.error_code
        
    return wrapper