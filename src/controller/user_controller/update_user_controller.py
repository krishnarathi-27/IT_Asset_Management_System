from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from src.utils.secure_password import HashPassword
from src.handlers.user_handler import UserHandler
from utils.exceptions import MyBaseException

class UpdateUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler()

    def update_password(self, user_data):

        try:
            old_password = user_data['old_password']
            new_password = user_data['new_password']
            confirm_password = user_data['confirm_password']

            user_id = get_jwt_identity()

            obj_secure_password = HashPassword()

            self.obj_user_handler.change_password(user_id,old_password,new_password,confirm_password, obj_secure_password)

            response = {
                "message": "Password updated successfully"
            }
            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
            