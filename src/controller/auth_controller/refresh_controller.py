import logging
from flask_jwt_extended import get_jwt

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from utils.exceptions import DBException, ApplicationException
from utils.response import SuccessResponse, ErrorResponse
from utils.token import Token

logger = logging.getLogger('refresh_controller')

class RefreshController:
    """Controller for authenticating user and generating access token"""

    def __init__(self) -> None:
        self.token_obj = Token()

    def refresh(self):
        try:
            user_id = get_jwt()['sub']
            role = get_jwt()['tent']

            self.token_obj.revoke_token(get_jwt())

            token = self.token_obj.generate_token(role,user_id)

            response = [{
                    'access_token': token[0],
                    'refresh_token' : token[1]
                }]

            return SuccessResponse.success_message(PromptConfig.USER_LOGGED_OUT,response), StatusCodes.OK
        
        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code