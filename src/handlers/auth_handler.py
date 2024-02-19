import logging
import pymysql
from flask import current_app as app

# local imports
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException
from utils.common_helper import verify_user_password


class AuthHandler:

    def __init__(self, db_object, obj_secure_password) -> None:
        self.db_object = db_object
        self.obj_secure_password = obj_secure_password    

    def validate_user(self, username: str, input_password: str) -> tuple:
        """
        Method for validating user by their credentials Paramters : self, username, input_password Return type : bool
        """
        try:
            user_data = self.db_object.fetch_data(Queries.FETCH_USER_CREDENTIALS, (username,))

            if not user_data:
                raise ApplicationException(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)

            password = user_data[0]['password']
            role = user_data[0]['role']
            is_changed = user_data[0]['is_changed']
            user_id = user_data[0]['user_id']
            
            if verify_user_password(password,input_password,is_changed,self.obj_secure_password):
                return (role, user_id, is_changed)
            else:
                raise ApplicationException(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)
    
        except pymysql.Error as error:
            app.logger.error(f"Error occured in database {error}")
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    