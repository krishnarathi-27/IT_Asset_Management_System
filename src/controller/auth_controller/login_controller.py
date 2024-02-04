import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.handlers.auth_handler import AuthHandler
from utils.exceptions import MyBaseException
from utils.secure_password import HashPassword
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('login_controller')

class LoginController:
    """Controller for authenticating user and generating access token"""

    def __init__(self) -> None:
        self.obj_auth_handler = AuthHandler(db_object)

    def login(self, user_data: dict) -> dict:
        """Function for login where user is authenticated and JWT token is issues"""
        logger.debug('User authenticating and issuing access token')
        
        try:
            username = user_data['username']
            password = user_data['password']

            obj_secure_password = HashPassword()

            result = self.obj_auth_handler.validate_user(username, password, obj_secure_password)
            
            if result:
                role = result[0]
                user_id = result[1]
                token = self.obj_auth_handler.generate_token(role,user_id)
                
                response = {
                    'access_token': token,
                    'message' : PromptConfig.USER_LOGGED_IN
                }
                
                return SuccessResponse.success_message(StatusCodes.OK, PromptConfig.USER_LOGGED_IN, response)
            
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
