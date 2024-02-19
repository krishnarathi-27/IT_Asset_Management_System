from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.user_handler.create_user_handler import CreateUserHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class CreateUserController:
    """Controller to create new user in database"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_user_handler = CreateUserHandler(db_object)

    def create_user(self, user_data: dict) -> dict:
        """Method to create new user"""
        app.logger.info('Method that created new user in database')

        try:
            username = user_data['username']
            role = user_data['role']

            self.obj_user_handler.create_new_user(role,username)

            app.logger.info(f'New user created {username}')
            return SuccessResponse.success_message(PromptConfig.USER_CREATED), StatusCodes.CREATED
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
