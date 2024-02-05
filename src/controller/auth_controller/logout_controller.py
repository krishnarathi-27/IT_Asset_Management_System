import logging
from flask_jwt_extended import get_jwt

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from utils.exceptions import MyBaseException
from utils.secure_password import HashPassword
from utils.response import SuccessResponse, ErrorResponse
from utils.token import Token

logger = logging.getLogger('logout_controller')

class LogoutController:
    """Controller for authenticating user and generating access token"""

    def __init__(self) -> None:
        self.token_obj = Token()

    def logout(self):
        self.token_obj.revoke_token(get_jwt())

        response = {
            "message" : PromptConfig.USER_LOGGED_OUT
        }

        return SuccessResponse.success_message(StatusCodes.OK, 
                                               PromptConfig.USER_LOGGED_OUT, 
                                               response), StatusCodes.OK
    