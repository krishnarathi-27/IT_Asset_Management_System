import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.issue_handler.view_issue_handler import ViewIssueHandler
from utils.exceptions import ApplicationException, DBException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('view_issue_controller')

class ViewIssueController:
    """Controller to view all the issues"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_issue_handler = ViewIssueHandler(db_object)

    def view_all_issue(self) -> dict:
        """Method to view all the issues"""
        logger.debug('Method to view all the issues')

        try:
            response = self.obj_issue_handler.view_issues()
            return SuccessResponse.success_message(PromptConfig.ISSUE_DATA_FETCHED,
                                                       response), StatusCodes.OK

        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
    def view_issue(self,user_id: str) -> dict:
        """Method to view all the issues created by any user"""
        logger.debug('Method to view all the issues created by an user')

        try:
            response = self.obj_issue_handler.view_issue_by_userid(user_id)
            return SuccessResponse.success_message(PromptConfig.ISSUE_USER_DATA_FETCHED,
                                                       response), StatusCodes.OK

        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        