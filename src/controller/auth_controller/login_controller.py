from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.handlers.auth_handler import AuthHandler
from utils.exceptions import MyBaseException
from utils.secure_password import HashPassword

class LoginController:

    def __init__(self):
        self.obj_auth_handler = AuthHandler(db_object)

    def login(self, user_data):
        
        try:
            username = user_data[AppConfig.USERNAME]
            password = user_data[AppConfig.PASSWORD]

            obj_secure_password = HashPassword()

            result = self.obj_auth_handler.validate_user(username, password, obj_secure_password)
            
            if result:
                role = result[0]
                user_id = result[1]
                token = self.obj_auth_handler.generate_token(role,user_id)
                
                response = jsonify({
                    AppConfig.ACCESS_TOKEN: token,
                    AppConfig.MESSAGE : PromptConfig.USER_LOGGED_IN
                })
                
                return response
            
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code

