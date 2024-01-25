"""Module having buisness logic of user related functionalities"""
import logging
import shortuuid
from mysql.connector import IntegrityError

from config.queries import Queries
from utils.hash_password import HashPassword
from database.database import db as db_object
from utils.exceptions import UserAlreadyExistsException, NoDataExistsException, InvalidUserCredentials, PasswordsNotMatchException

logger = logging.getLogger("user_controller")

class UserHandler:

    def create_new_user(self, user_role: str, username: str, password: str) -> str:
        try:
            user_id = "EMP" + shortuuid.ShortUUID().random(length=4)
            
            hashed_password = HashPassword.hash_password(password)
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

    def view_all_user(self) -> list:
        data = db_object.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)
        if data:
            return data
        else:
            raise NoDataExistsException
    
    def view_user_by_id(self, user_id: str) -> list:
        data = db_object.fetch_data(Queries.FETCH_DETAILS_BY_UID, (user_id,))
        if data:
            return data
        else:
            raise NoDataExistsException
    
    def change_password(self,user_id: str, old_password: str, new_password: str, confirm_password: str) -> None:

        actual_password = db_object.fetch_data(Queries.FETCH_PASSWORD,(user_id,))

        old_password_hashed = HashPassword.hash_password(old_password)

        if actual_password[0]['password'] != old_password_hashed:
            raise InvalidUserCredentials
        
        if new_password != confirm_password:
            raise PasswordsNotMatchException
        
        hashed_password = HashPassword.hash_password(new_password)
        db_object.save_data(Queries.UPDATE_PASSWORD, (hashed_password, user_id,))
              