from flask import jsonify
from src.handlers.auth_handler import AuthHandler
from utils.exceptions import MyBaseException
from utils.secure_password import HashPassword

class LoginController:

    def __init__(self):
        self.obj_auth_handler = AuthHandler()

    def login(self, user_data):
        
        try:
            username = user_data['username']
            password = user_data['password']

            obj_secure_password = HashPassword()

            result = self.obj_auth_handler.validate_user(username, password, obj_secure_password)
            
            if result:
                role = result[0]
                user_id = result[1]
                token = self.obj_auth_handler.generate_token(role,user_id)
                
                response = jsonify({
                    "access_token": token,
                    "message": "User logged in successfully"
                })
                
                return response
            
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code

