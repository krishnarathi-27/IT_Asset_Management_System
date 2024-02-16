"""Module having buisness logic of user related functionalities"""
import logging
import shortuuid
from mysql.connector import IntegrityError, Error

from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException
from utils.password_generator import generate_password

logger = logging.getLogger("create_user_handler")

class CreateUserHandler:
    """Class containing methods for creating new user in database"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def create_new_user(self, user_role: str, username: str) -> str:
        """Method for creating new user in database"""
        logger.info('Creating new user in database')

        try:
            user_id = PromptConfig.USER_ID_PREFIX + shortuuid.ShortUUID().random(length=4)      

            password = generate_password()
            
            self.db_object.save_data(Queries.INSERT_USER_CREDENTIALS,
                (user_id,username,password,user_role,)
            )  
            logger.info('New user with default password created')
        
        except IntegrityError as err:
            logger.info(f"User with same username already exists {err}")
            raise ApplicationException(409, PromptConfig.CONFLICT_MSG, PromptConfig.USERNAME_EXISTS)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        