from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from src.handlers.user_handler import UserHandler
from utils.exceptions import MyBaseException

class ViewUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler()

    def view_all_user(self):
        try:
            response = self.obj_user_handler.view_all_user()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code


    def view_user_by_id(self):
        try:
            user_id = get_jwt_identity()

            response = self.obj_user_handler.view_user_by_id(user_id)
            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
