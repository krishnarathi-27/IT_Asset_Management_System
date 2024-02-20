import os
import functools
from flask_jwt_extended import get_jwt
from flask_jwt_extended import verify_jwt_in_request

from src.utils.exceptions import ApplicationException

ROLE_REQUIRED = {
    "admin": os.getenv('ADMIN'),
    "asset manager": os.getenv('MANAGER'),
    "employee": os.getenv('employee')
}

def access_required(role_list: list):
    def wrapper(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["house"] == 0:
                raise ApplicationException(403, "Forbidden", "Change default password first")
            if claims["tent"] in role_list:
                return fn(*args, **kwargs)
            else:
                raise ApplicationException(403, "Forbidden", "Access denied to this route")
            
        return inner

    return wrapper