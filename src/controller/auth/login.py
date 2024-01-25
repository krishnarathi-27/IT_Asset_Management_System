from flask_smorest import abort
from handlers.auth import AuthHandler
from utils.exceptions import InvalidUserCredentials

class LoginController:

    def __init__(self):
        self.obj_auth_handler = AuthHandler()

    def login(self, user_data):
        
        try:
            username = user_data['username']
            password = user_data['password']

            result = self.obj_auth_handler.validate_user(username, password)
            if result:
                role = result[0]
                user_id = result[1]
                token = self.obj_auth_handler.generate_token(role,user_id)
                
                response = {
                    "access_token": token,
                    "message": "User logged in successfully"
                }
                
                return response
            
        except InvalidUserCredentials:
            abort(401, "USer credentials are invalid")

