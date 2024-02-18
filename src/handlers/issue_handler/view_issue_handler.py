import logging
import pymysql

from config.app_config import AppConfig
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DBException, ApplicationException
from utils.common_helper import regex_validation

logger = logging.getLogger('view_issue_handler')

class ViewIssueHandler:
    """Class containing method to view all issue and issue raised by any user"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def view_issues(self) -> dict:
        """Method to view all the issues in database"""
        logger.info('View all issues in database')

        try: 
            data = self.db_object.fetch_data(Queries.FETCH_ISSUE_TABLE)
            return data
            
        except pymysql.Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        
    def view_issue_by_userid(self,user_id: str) -> dict:
        """Method to view issue raised by any user id"""
        logger.info('Viewing all issues raised by any user id')

        try: 
            result = regex_validation(AppConfig.REGEX_USER_ID, user_id)

            if not result:
                raise ApplicationException(422, PromptConfig.UNPROCESSIBLE_ENTITY, PromptConfig.INVALID_USER_ID)
            
            data = self.db_object.fetch_data(Queries.FETCH_ISSUE_BY_USER_ID,(user_id,))
            if data:
                return data
            else:
                raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ISSUE_NOT_EXISTS)
            
        except pymysql.Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        