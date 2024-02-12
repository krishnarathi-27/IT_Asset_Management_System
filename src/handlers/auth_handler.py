import logging
from mysql.connector import Error

# local imports
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException

logger = logging.getLogger("auth_handler")

class AuthHandler:

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def validate_user(self, username: str, input_password: str, obj_secure_password) -> tuple:
        """
        Method for validating user by their credentials Paramters : self, username, input_password Return type : bool
        """
        try: 
            user_data = self.db_object.fetch_data(Queries.FETCH_USER_CREDENTIALS, (username,))
            if user_data:
                password = user_data[0]['password']
                role = user_data[0]['role']
                is_changed = user_data[0]['is_changed']
                user_id = user_data[0]['user_id']
                hashed_password = obj_secure_password.secure_password(input_password)

                if hashed_password == password:
                    return (role, user_id, is_changed)
                else:
                    raise ApplicationException(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)

            raise ApplicationException(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)
        
        except Error as error:
            logger.error(f"Error occured in database {error}")
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    