import logging
from mysql.connector import Error
from flask_jwt_extended import create_access_token, create_refresh_token

# local imports
from config.queries import Queries
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from utils.mapped_roles import MappedRole
from utils.exceptions import InvalidCredentials, DBException

logger = logging.getLogger("auth_handler")

class AuthHandler:

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def validate_user(self, username: str, input_password: str, obj_secure_password) -> tuple:
        """
        Method for validating user by their credentials Paramters : self, username, input_password Return type : bool
        """
        try: 
            user_data = self.db_object.fetch_data(Queries.FETCH_USER_CREDENTIALS, (username,))
            if user_data:
                password = user_data[0][AppConfig.PASSWORD]
                role = user_data[0][AppConfig.ROLE]
                is_changed = user_data[0][AppConfig.IS_CHANGED]
                user_id = user_data[0][AppConfig.USER_ID]
                hashed_password = obj_secure_password.secure_password(input_password)

                if hashed_password == password:
                    return (role, user_id)
                else:
                    raise InvalidCredentials(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)

            raise InvalidCredentials(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)
        
        except Error as error:
            logger.error(f"Error occured in database {error}")
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
    def generate_token(self,role,user_id):
        get_role = MappedRole.get_mapped_role(role)
        access_token = create_access_token(identity=user_id,additional_claims={AppConfig.ROLE: get_role})
        
        return access_token
    