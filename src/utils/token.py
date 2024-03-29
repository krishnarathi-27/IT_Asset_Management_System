from flask import current_app as app
from flask_jwt_extended import get_jti, create_access_token, create_refresh_token

from src.config.queries import Queries
from src.database.database import Database
from src.utils.rbac import ROLE_REQUIRED

class Token:
    """Class containing methods of token related functionalities"""

    def __init__(self):
        self.db_object = Database()

    def check_token_revoked(self, jwt_payload, token_name) -> bool:
        """Method to check if token is revoked"""
        app.logger.info('Checking if token is revoked or not')

        jti_access_token = jwt_payload["jti"]

        query = Queries.FETCH_IF_TOKEN_REVOKED.format(token_name)
        result = self.db_object.fetch_data(query,(jti_access_token,))
        if not result:
            return False
        
        if result[0]['token_status'] == "revoked":
            return True
        
        return False

    def revoke_token(self, jwt_payload)-> None:
        """Method to revoke a token"""
        app.logger.info("Revoking token")

        user_id = jwt_payload["sub"]

        self.db_object.save_data(Queries.UPDATE_TOKEN_STATUS,('revoked',user_id,))

    def generate_token(self,role: str,user_id: str,is_changed = None) -> tuple :
        """Method to generate new access and refresh token and saving token in database"""
        app.logger.info('New access and refresh token issued')
  
        if not role in ROLE_REQUIRED:
            get_role = role
        else:
            get_role = ROLE_REQUIRED[role]
            
        if is_changed == "false":
            password_type = 0
        else:
            password_type = 1

        access_token = create_access_token(identity=user_id,additional_claims={'tent': get_role,'house': password_type})
        jti_access_token = get_jti(access_token)
        
        refresh_token = create_refresh_token(identity=user_id,additional_claims={'tent': get_role})
        jti_refresh_token = get_jti(refresh_token)

        self.db_object.save_data(Queries.INSERT_TOKEN_DETAILS,(user_id,jti_access_token,jti_refresh_token,))

        return (access_token, refresh_token)
    