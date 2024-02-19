from flask import current_app as app
from flask_jwt_extended import get_jwt_identity

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.user_handler.view_user_handler import ViewUserHandler
from src.utils.response import SuccessResponse, ErrorResponse
from src.utils.exceptions import ApplicationException, DBException

class ViewUserController:
    """Controller to view all user details or view user profile"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_user_handler = ViewUserHandler(db_object)

    def view_all_user(self) -> None:
        """Method to view all user details"""
        app.logger.info('Viewing all user details')

        try:
            response = self.obj_user_handler.view_all_user()
            return SuccessResponse.success_message(PromptConfig.USER_DATA_FETCHED, response), StatusCodes.OK

        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code


    def view_user_by_id(self) -> None:
        """Method to view user profile"""
        app.logger.info('Viewing user profile')

        try:
            user_id = get_jwt_identity()

            response = self.obj_user_handler.view_user_by_id(user_id)
            return SuccessResponse.success_message(PromptConfig.USER_DATA_FETCHED, response), StatusCodes.OK

        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        