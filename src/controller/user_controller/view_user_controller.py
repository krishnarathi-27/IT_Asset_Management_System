import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from flask_jwt_extended import get_jwt_identity
from src.handlers.user_handler import UserHandler
from utils.response import SuccessResponse, ErrorResponse
from utils.exceptions import MyBaseException

logger = logging.getLogger('view_user_controller')

class ViewUserController:
    """Controller to view all user details or view user profile"""

    def __init__(self) -> None:
        self.obj_user_handler = UserHandler(db_object)

    def view_all_user(self) -> None:
        """Method to view all user details"""
        logger.info('Viewing all user details')

        try:
            response = self.obj_user_handler.view_all_user()
            return SuccessResponse.success_message(StatusCodes.OK, PromptConfig.USER_DATA_FETCHED, response), StatusCodes.OK

        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code


    def view_user_by_id(self) -> None:
        """Method to view user profile"""
        logger.info('Viewing user profile')

        try:
            user_id = get_jwt_identity()

            response = self.obj_user_handler.view_user_by_id(user_id)
            return SuccessResponse.success_message(StatusCodes.OK, PromptConfig.USER_DATA_FETCHED, response), StatusCodes.OK

        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        