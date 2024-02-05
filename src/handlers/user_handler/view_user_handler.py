"""Module having buisness logic of user related functionalities"""
import logging
from mysql.connector import Error

from config.queries import Queries
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataNotExists, CustomException, DBException, InvalidCredentials

logger = logging.getLogger("view_user_handler")

class ViewUserHandler:
    """Class containing to view users in database and to view a single user"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def view_all_user(self) -> dict:
        """Method for viewing all users in database"""
        logger.info('Viewining user details')

        try: 
            data = self.db_object.fetch_data(Queries.FETCH_AUTHENTICATION_TABLE)
            return data
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
    def view_user_by_id(self, user_id: str) -> dict:
        """Method to view any user details by user id"""
        logger.info('Viewing user detail by user id')

        try:
            data = self.db_object.fetch_data(Queries.FETCH_DETAILS_BY_UID, (user_id,))
            if data:
                return data
            else:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.USER_NOT_EXISTS)
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
                 