from flask import current_app as app
from flask_jwt_extended import get_jwt_identity

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.issue_handler.create_issue_handler import CreateIssueHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class CreateIssueController:
    """Controller to create new issue related to asset"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_issue_handler = CreateIssueHandler(db_object)

    def create_issue(self, request_data: dict) -> dict:
        """Method to create new issue for asset of an employee"""
        app.logger.debug('Method to create new issue')

        try:
            asset_id = request_data['asset_id']
            user_id = get_jwt_identity()
            
            self.obj_issue_handler.create_issue(asset_id, user_id)

            return SuccessResponse.success_message(PromptConfig.ISSUE_CREATED), StatusCodes.CREATED

        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
            