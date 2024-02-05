import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from src.handlers.auth_handler import AuthHandler
from utils.exceptions import MyBaseException
from utils.secure_password import HashPassword
from utils.response import SuccessResponse, ErrorResponse
from utils.token import Token

logger = logging.getLogger('login_controller')

class LoginController:
    """Controller for authenticating user and generating access token"""

    def __init__(self) -> None:
        db_object = Database()
        self.token_obj = Token()
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
                is_changed = result[2]

                token = self.token_obj.generate_token(role,user_id,is_changed)
                
                response = {
                    'access_token': token[0],
                    'refresh_token' : token[1],
                    'message' : PromptConfig.USER_LOGGED_IN
                }
                
                return SuccessResponse.success_message(StatusCodes.OK, 
                                                       PromptConfig.USER_LOGGED_IN, response), StatusCodes.OK
            
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
