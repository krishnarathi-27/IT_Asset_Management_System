"""Module contains different types of decorator used across the projects"""
import functools
import logging
from mysql.connector import IntegrityError, Error

from utils.exceptions import CustomException, DBException

logger = logging.getLogger("app_decorator")

def error_handler(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        
        except IntegrityError as error:
            logger.error(f"Tried to insert duplicate entry in database {error}")
            raise DBException(409,"","")
        
        except Error as error:
            logger.error(f"Error occured in database {error}")
            raise DBException
    
    return wrapper