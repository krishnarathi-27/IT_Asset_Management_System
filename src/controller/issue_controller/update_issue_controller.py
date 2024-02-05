import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.issue_handler.update_issue_handler import UpdateIssueHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('update_issue_controller')

class UpdateIssueController:
    """Class to update issue status that are pending"""

    def __init__(self):
        db_object = Database()
        self.obj_issue_handler = UpdateIssueHandler(db_object)

    def update_issue(self, request_data: dict, issue_id: str) -> dict:
        """Method to resolve issue status of issue_id that is pending"""
        logger.info('Resolving pending issue')

        try:
            asset_id = request_data['asset_id']
            user_id = request_data['user_id']
            issue_status = request_data['issue_status']
            
            self.obj_issue_handler.update_issue_status(user_id,asset_id,issue_id, issue_status)

            response = {
                "issue_id" : issue_id,
                "message" : PromptConfig.ISSUE_RESOLVED
            }

            logger.info('Issue successfully resolved')
            return SuccessResponse.success_message(StatusCodes.OK, 
                                                       PromptConfig.ISSUE_RESOLVED,
                                                       response), StatusCodes.OK
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        