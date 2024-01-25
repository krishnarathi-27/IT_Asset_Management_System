import logging
from mysql.connector import IntegrityError, Error
from flask_jwt_extended import create_access_token, create_refresh_token

# local imports
from config.queries import Queries
from database.database import db as db_object
from src.utils.secure_password import HashPassword
from utils.mapped_roles import MappedRole
from utils.exceptions import InvalidCredentials, DBException

logger = logging.getLogger("auth_handler")

class AuthHandler:

    def validate_user(self, username: str, input_password: str, obj_secure_password) -> bool:
        """
        Method for validating user by their credentials Paramters : self, username, input_password Return type : bool
        """
        try: 
            user_data = db_object.fetch_data(Queries.FETCH_USER_CREDENTIALS, (username,))
            if user_data:
                password = user_data[0]['password']
                role = user_data[0]['role']
                is_changed = user_data[0]['is_changed']
                user_id = user_data[0]['user_id']
                hashed_password = obj_secure_password.secure_password(input_password)

                if hashed_password == password:
                    return (role, user_id)
                else:
                    raise InvalidCredentials(401, "Unauthorised", "Invalid credentials entered try again with valid one")

            raise InvalidCredentials(401, "Unauthorised", "Invalid credentials entered try again with valid one")
        
        except Error as error:
            logger.error(f"Error occured in database {error}")
            raise DBException(500, "Internal server error", "Server not responding try again after sometime")
    
    def generate_token(self,role,user_id):
        get_role = MappedRole.get_mapped_role(role)
        access_token = create_access_token(identity=user_id,additional_claims={"role": get_role})
        
        return access_token
    