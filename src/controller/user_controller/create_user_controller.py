import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from utils.secure_password import HashPassword
from handlers.user_handler.create_user_handler import CreateUserHandler
from utils.exceptions import ApplicationException, DBException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('create_user_controller')

class CreateUserController:
    """Controller to create new user in database"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_user_handler = CreateUserHandler(db_object)

    def create_user(self, user_data: dict) -> dict:
        """Method to create new user"""
        logger.info('Method that created new user in database')

        try:
            username = user_data['username']
            password = user_data['password']
            role = user_data['role']

            obj_secure_password = HashPassword()
            self.obj_user_handler.create_new_user(role,username,password, obj_secure_password)

            logger.info(f'New user created {username}')
            return SuccessResponse.success_message(PromptConfig.USER_CREATED), StatusCodes.CREATED
        
        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
