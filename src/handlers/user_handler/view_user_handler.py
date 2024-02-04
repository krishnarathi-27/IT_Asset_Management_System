"""Module having buisness logic of user related functionalities"""
import logging
import shortuuid
from mysql.connector import IntegrityError, Error

from config.queries import Queries
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataAlreadyExists, DataNotExists, CustomException, DBException, InvalidCredentials

logger = logging.getLogger("user_handler")

class UserHandler:

    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def create_new_user(self, user_role: str, username: str, password: str, obj_hash_password) -> str:
        try:
            user_id = PromptConfig.USER_ID_PREFIX + shortuuid.ShortUUID().random(length=4)
            
            hashed_password = obj_hash_password.secure_password(password)
            self.db_object.save_data(
                Queries.INSERT_USER_CREDENTIALS,
                (
                    user_id,
                    username,
                    hashed_password,
                    user_role,
                ),
            )  
            return user_id
        
        except IntegrityError as err:
            logger.info(f"User with same username already exists {err}")
            raise DataAlreadyExists(409, PromptConfig.CONFLICT_MSG, PromptConfig.USERNAME_EXISTS)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)

    def view_all_user(self) -> list:
        try: 
            data = self.db_object.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.USER_NOT_EXISTS)
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
    def view_user_by_id(self, user_id: str) -> list:
        try:
            data = self.db_object.fetch_data(Queries.FETCH_DETAILS_BY_UID, (user_id,))
            if data:
                return data
            else:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.USER_NOT_EXISTS)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
    def change_password(self,user_id: str, old_password: str, new_password: str, confirm_password: str, obj_hash_password) -> None:
        try:
            actual_password = self.db_object.fetch_data(Queries.FETCH_PASSWORD,(user_id,))

            old_password_hashed = obj_hash_password.secure_password(old_password)

            if actual_password[0][AppConfig.PASSWORD] != old_password_hashed:
                raise InvalidCredentials(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)
            
            if new_password != confirm_password:
                raise CustomException(400, PromptConfig.BAD_REQUEST, PromptConfig.PASSWORDS_NOT_MATCH)
            
            hashed_password = obj_hash_password.secure_password(new_password)
            self.db_object.save_data(Queries.UPDATE_PASSWORD, (hashed_password, user_id,))

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
              