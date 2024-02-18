import logging
from flask_jwt_extended import get_jwt_identity

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from utils.secure_password import HashPassword
from handlers.user_handler.update_user_handler import UpdateUserHandler
from utils.response import SuccessResponse, ErrorResponse
from utils.exceptions import ApplicationException, DBException

logger = logging.getLogger('update_user_controller')

class UpdateUserController:
    """Controller to update user details"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_user_handler = UpdateUserHandler(db_object)

    def update_password(self, user_data: dict) -> dict:
        """Method to update password of user"""
        logger.info("Method to update user password")

        try:
            old_password = user_data['old_password']
            new_password = user_data['new_password']
            confirm_password = user_data['confirm_password']

            user_id = get_jwt_identity()

            obj_secure_password = HashPassword()

            token = self.obj_user_handler.change_password(
                                    user_id,old_password,new_password,
                                    confirm_password, obj_secure_password)

            response = [{
                "access_token" : token[0],
                "refesh_token" : token[1]
            }]
            logger.info("Password of user updated successfully")
            return SuccessResponse.success_message(PromptConfig.PASSWORD_UPDATED, 
                                                   response), StatusCodes.OK

        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
            