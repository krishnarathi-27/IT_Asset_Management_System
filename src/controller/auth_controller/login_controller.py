from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.auth_handler import AuthHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.secure_password import HashPassword
from src.utils.response import SuccessResponse, ErrorResponse
from src.utils.token import Token

class LoginController:
    """Controller for authenticating user and generating access token"""

    def __init__(self) -> None:
        db_object = Database()
        self.token_obj = Token()
        obj_secure_password = HashPassword()
        self.obj_auth_handler = AuthHandler(db_object,obj_secure_password)

    def login(self, user_data: dict) -> dict:
        """Function for login where user is authenticated and JWT token is issues"""
        app.logger.debug('User authenticating and issuing access token')
        
        try:
            username = user_data['username']
            password = user_data['password']   

            result = self.obj_auth_handler.validate_user(username, password)
            
            if result:
                role = result[0]
                user_id = result[1]
                is_changed = result[2]

                token = self.token_obj.generate_token(role,user_id,is_changed)
                
                response = [{
                    'access_token': token[0],
                    'refresh_token' : token[1]
                }]
                
                return SuccessResponse.success_message(PromptConfig.USER_LOGGED_IN, response), StatusCodes.OK
            
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
