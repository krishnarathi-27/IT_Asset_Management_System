"""Module having buisness logic of user related functionalities"""
import logging
import hashlib

from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger("user_controller")

class UserController:
    """
        Class containing methods to perform operations on users 
    """ 
    
    def __init__(self,db_object) -> None:
        self.db_object = db_object

    def create_new_user(self,user_id, user_role: str, username: str, password: str) -> None:
        """
        Method for creating new user in the system with unique username
        Parameters : self, user_role, username, password
        Return Type : None
        """
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.db_object.save_data(
            Queries.INSERT_USER_CREDENTIALS,
            (
                user_id,
                username,
                hashed_password,
                user_role,
            ),
        )  

    def view_users(self) -> bool:
        """Method to display details of users"""

        data = self.db_object.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)

        return data
    
    def view_user_by_id(self, user_id: str) -> list:
        """Method that displays data for user by user id"""

        data = self.db_object.fetch_data(Queries.FETCH_DETAILS_BY_UID, (user_id,))
        return data
    
    def change_password(self,user_id: str, new_password: str, confirm_password: str) -> bool:
        """Method to change password"""
        if new_password != confirm_password:
            return False
        
        hashed_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
        result = self.db_object.save_data(Queries.UPDATE_PASSWORD, (hashed_password, user_id,))
        return True