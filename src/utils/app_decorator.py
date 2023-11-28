"""Module contains decorator for handling all the types of exception in the project"""
import functools
import sqlite3
import logging

from config.prompts.prompts import PromptConfig

logger = logging.getLogger('app_decorator')

def error_handler(func):
    """
        Method which acts as decorator for handling all types of exception
        Parameter = function
        Return type = function
    """
    @functools.wraps(func)
    def wrapper(*args : tuple,**kwargs : dict) -> None:
        """
            Method which handles exception
            Parameter = *args, **kwargs
            Return type = None
        """
        try:
            return func(*args,**kwargs)
        except sqlite3.IntegrityError as err:
            logger.exception(err)
            print(PromptConfig.DB_INTEGRITY_ERROR)
        except sqlite3.OperationalError as err:
            logger.exception(err)
            print(PromptConfig.DB_ERROR_MESSAGE)
        except sqlite3.ProgrammingError as err:
            logger.exception(err)
            print(PromptConfig.DB_ERROR_MESSAGE)
        except sqlite3.Error as err:
            logger.exception(err)
            print(PromptConfig.DB_GENERAL_ERROR)
        except ValueError as err:
            logger.exception(err)
            print(PromptConfig.INVALID_INPUT_ERROR)
        except TypeError as err:
            logger.exception(err)
            print(PromptConfig.INVALID_INPUT_ERROR)
        except Exception as err:
            logger.exception(err)
            print(PromptConfig.GENERAL_EXCEPTION_MSG)
    return wrapper
