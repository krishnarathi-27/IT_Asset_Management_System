from flask import jsonify
from utils.secure_password import HashPassword
from handlers.user_handler import UserHandler
from utils.exceptions import MyBaseException

class CreateUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler()

    def create_user(self, user_data):

        try:
            username = user_data['username']
            password = user_data['password']
            role = user_data['user_role']

            obj_secure_password = HashPassword()
            self.obj_user_handler.create_new_user(role,username,password, obj_secure_password)

            response = jsonify({
                "username": user_data['username'],
                "user_role": user_data['user_role'],
                "message": "User created successfully"
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code

            