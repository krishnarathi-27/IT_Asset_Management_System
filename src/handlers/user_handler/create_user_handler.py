"""Module having buisness logic of user related functionalities"""
import shortuuid
import pymysql
from flask import current_app as app

from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import ApplicationException, DBException
from src.utils.common_helper import generate_password

class CreateUserHandler:
    """Class containing methods for creating new user in database"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def create_new_user(self, user_role: str, username: str) -> str:
        """Method for creating new user in database"""
        app.logger.info('Creating new user in database')

        try:
            user_id = PromptConfig.USER_ID_PREFIX + shortuuid.ShortUUID().random(length=4)      

            password = generate_password()
            
            self.db_object.save_data(Queries.INSERT_USER_CREDENTIALS,
                (user_id,username,password,user_role,)
            )  
            app.logger.info('New user with default password created')
        
        except pymysql.IntegrityError as err:
            app.logger.info(f"User with same username already exists {err}")
            raise ApplicationException(409, PromptConfig.CONFLICT_MSG, PromptConfig.USERNAME_EXISTS)
        
        except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        