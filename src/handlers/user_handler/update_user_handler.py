"""Module having buisness logic of user related functionalities"""
import logging
import pymysql
from flask_jwt_extended import get_jwt

from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException
from utils.common_helper import verify_user_password
from utils.token import Token

logger = logging.getLogger("update_user_handler")

class UpdateUserHandler:
    """Class containing to update any of user details"""

    def __init__(self, db_object) -> None:
        self.token_object = Token()
        self.db_object = db_object

    def change_password(self,user_id: str, old_password: str, new_password: str, confirm_password: str, obj_hash_password) -> None:
        """Method to change user password if old password is correct"""
        logger.info('Changing user password is old password is valid')

        try:
            user_data = self.db_object.fetch_data(Queries.FETCH_PASSWORD, (user_id,))

            password = user_data[0]['password']
            role = user_data[0]['role']
            is_changed = user_data[0]['is_changed']
            
            if not verify_user_password(password,old_password,is_changed,obj_hash_password):
                raise ApplicationException(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)
            
            if new_password != confirm_password:
                raise ApplicationException(400, PromptConfig.BAD_REQUEST, PromptConfig.PASSWORDS_NOT_MATCH)
            
            hashed_password = obj_hash_password.secure_password(new_password)
            self.db_object.save_data(Queries.UPDATE_PASSWORD, (hashed_password, user_id,))

            self.token_object.revoke_token(get_jwt())
            token = self.token_object.generate_token(role, user_id)

            return token
        
        except pymysql.Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
 