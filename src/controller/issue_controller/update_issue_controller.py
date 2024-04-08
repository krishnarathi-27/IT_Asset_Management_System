from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.issue_handler.update_issue_handler import UpdateIssueHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class UpdateIssueController:
    """Class to update issue status that are pending"""

    def __init__(self):
        db_object = Database()
        self.obj_issue_handler = UpdateIssueHandler(db_object)

    def update_issue(self, request_data: dict, issue_id: str) -> dict:
        """Method to resolve issue status of issue_id that is pending"""
        app.logger.info('Resolving pending issue')

        try:
            asset_id = request_data['asset_id']
            user_id = request_data['user_id']
            issue_status = request_data['issue_status']
            self.obj_issue_handler.update_issue_status(user_id,asset_id,issue_id)

            app.logger.info('Issue successfully resolved')
            return SuccessResponse.success_message(PromptConfig.ISSUE_RESOLVED), StatusCodes.OK
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        