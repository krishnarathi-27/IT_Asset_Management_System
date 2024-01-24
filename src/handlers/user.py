"""Module having buisness logic of user related functionalities"""
import logging
import hashlib
import shortuuid
from mysql.connector import IntegrityError, Error

from config.queries import Queries
from database.database import db as db_object
from utils.exceptions import UserAlreadyExistsException, DBException, NoDataExistsException

logger = logging.getLogger("user_controller")

class UserHandler:

    def create_new_user(self, user_role: str, username: str, password: str) -> None:
        try:
            user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
            
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
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
            raise UserAlreadyExistsException
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}")
            raise DBException

    def view_all_user(self) -> bool:
        try:
            data = db_object.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)
            if data:
                return data
            else:
                raise NoDataExistsException
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}")
            raise DBException
    
    def view_user_by_id(self, user_id: str) -> list:
        """Method that displays data for user by user id"""
        try:
            data = db_object.fetch_data(Queries.FETCH_DETAILS_BY_UID, (user_id,))
            if data:
                return data
            else:
                raise NoDataExistsException
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}")
            raise DBException
    
    def change_password(self,user_id: str, new_password: str, confirm_password: str) -> bool:

        if new_password != confirm_password:
            return False
        
        hashed_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
        result = db_object.save_data(Queries.UPDATE_PASSWORD, (hashed_password, user_id,))
        return True
    