import pymysql
from flask import current_app as app

from src.config.app_config import AppConfig
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import DBException, ApplicationException
from src.utils.common_helper import regex_validation

class ViewIssueHandler:
    """Class containing method to view all issue and issue raised by any user"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def view_issues(self) -> dict:
        """Method to view all the issues in database"""
        app.logger.info('View all issues in database')

        try: 
            data = self.db_object.fetch_data(Queries.FETCH_ISSUE_TABLE)
            return data
            
        except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        
    def view_issue_by_userid(self,user_id: str) -> dict:
        """Method to view issue raised by any user id"""
        app.logger.info('Viewing all issues raised by any user id')

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
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        