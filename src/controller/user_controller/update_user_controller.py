from flask import current_app as app
from flask_jwt_extended import get_jwt_identity

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.utils.secure_password import HashPassword
from src.handlers.user_handler.update_user_handler import UpdateUserHandler
from src.utils.response import SuccessResponse, ErrorResponse
from src.utils.exceptions import ApplicationException, DBException

class UpdateUserController:
    """Controller to update user details"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_user_handler = UpdateUserHandler(db_object)

    def update_password(self, user_data: dict) -> dict:
        """Method to update password of user"""
        app.logger.info("Method to update user password")

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
            app.logger.info("Password of user updated successfully")
            return SuccessResponse.success_message(PromptConfig.PASSWORD_UPDATED, 
                                                   response), StatusCodes.OK

        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
            