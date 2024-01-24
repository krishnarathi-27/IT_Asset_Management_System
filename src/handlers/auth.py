import hashlib
import logging
from flask_jwt_extended import create_access_token, create_refresh_token
from mysql.connector import Error

# local imports
from config.queries import Queries
from database.database import db as db_object
from utils.mapped_roles import MappedRole
from utils.exceptions import InvalidUserCredentials, DBException

logger = logging.getLogger("auth_handler")

class AuthHandler:

    def validate_user(self, username: str, input_password: str) -> bool:
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
                hashed_password = hashlib.sha256(input_password.encode()).hexdigest()

                if hashed_password == password:
                    return (role, user_id)
                else:
                    raise InvalidUserCredentials

            raise InvalidUserCredentials
        
        except Error as err:
            logger.error(f"Error occured in database {err}")
            raise DBException
    
    def generate_token(self,role,user_id):
        get_role = MappedRole.get_mapped_role(role)
        access_token = create_access_token(identity=user_id,additional_claims={"role": get_role})
        
        return access_token
    