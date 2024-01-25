"""Module having buisness logic of user related functionalities"""
import logging
import shortuuid
from mysql.connector import IntegrityError, Error

from config.queries import Queries
from database.database import db as db_object
from utils.exceptions import DataAlreadyExists, DataNotExists, CustomException, DBException, InvalidCredentials

logger = logging.getLogger("user_controller")

class UserHandler:

    def create_new_user(self, user_role: str, username: str, password: str, obj_hash_password) -> str:
        try:
            user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
            
            hashed_password = obj_hash_password.secure_password(password)
            db_object.save_data(
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
            raise DataAlreadyExists(409, 'conflict', 'Username already exists')
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")

    def view_all_user(self) -> list:
        try: 
            data = db_object.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, 'Resource not found', 'Vendor not exists to deactivate')
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
    
    def view_user_by_id(self, user_id: str) -> list:
        try:
            data = db_object.fetch_data(Queries.FETCH_DETAILS_BY_UID, (user_id,))
            if data:
                return data
            else:
                raise DataNotExists(404, 'Resource not found', 'Vendor not exists to deactivate')
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
    
    def change_password(self,user_id: str, old_password: str, new_password: str, confirm_password: str, obj_hash_password) -> None:
        try:
            actual_password = db_object.fetch_data(Queries.FETCH_PASSWORD,(user_id,))

            old_password_hashed = obj_hash_password.secure_password(old_password)

            if actual_password[0]['password'] != old_password_hashed:
                raise InvalidCredentials(401, 'Unauthorised', 'Invalid credentials entered')
            
            if new_password != confirm_password:
                raise CustomException(400, 'Bad request', 'New password and old password do not match')
            
            hashed_password = obj_hash_password.secure_password(new_password)
            db_object.save_data(Queries.UPDATE_PASSWORD, (hashed_password, user_id,))

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
              