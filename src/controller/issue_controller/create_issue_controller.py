import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from flask_jwt_extended import get_jwt_identity
from handlers.issue_handler.create_issue_handler import CreateIssueHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('create_issue_controller')

class CreateIssueController:
    """Controller to create new issue related to asset"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_issue_handler = CreateIssueHandler(db_object)

    def create_issue(self, request_data: dict) -> dict:
        """Method to create new issue for asset of an employee"""
        logger.debug('Method to create new issue')

        try:
            asset_id = request_data['asset_id']
            user_id = get_jwt_identity()
            
            issue_id  = self.obj_issue_handler.create_issue(asset_id, user_id)

            response = {
                "issue_id" : issue_id,
                "asset_id" : asset_id,
                "user_id" : user_id,
                "message" : PromptConfig.ISSUE_CREATED
            }
            return SuccessResponse.success_message(StatusCodes.CREATED, 
                                                       PromptConfig.ISSUE_CREATED,
                                                       response), StatusCodes.CREATED
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
            