import logging
import pymysql

from config.app_config import AppConfig
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.common_helper import regex_validation
from utils.exceptions import ApplicationException, DBException

logger = logging.getLogger('update_issue_handler')

class UpdateIssueHandler:
    """Class containing method to update any issue status"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def update_issue_status(self, user_id: str, asset_id: str, issue_id: str) -> None:
        """Method to update issue status of any issue"""
        logger.info('Updating status of issue')

        try:
            result = regex_validation(AppConfig.REGEX_USER_ID, issue_id)

            if not result:
                raise ApplicationException(422, PromptConfig.UNPROCESSIBLE_ENTITY, PromptConfig.INVALID_ISSUE_ID)
            
            fetched_issue_status = self.db_object.fetch_data(Queries.FETCH_IF_ISSUE_PENDING,(issue_id,))

            if fetched_issue_status[0]['issue_status'] == "resolved":
                raise ApplicationException(404,PromptConfig.RESOURCE_NOT_FOUND,PromptConfig.ISSUE_ALREADY_RESOLVED)
            
            self.db_object.save_data(Queries.UPDATE_ISSUE_STATUS,(user_id, asset_id,issue_id,))

        except pymysql.Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
            