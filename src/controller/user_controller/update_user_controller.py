from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.utils.secure_password import HashPassword
from src.handlers.user_handler import UserHandler
from utils.exceptions import MyBaseException

class UpdateUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler(db_object)

    def update_password(self, user_data):

        try:
            old_password = user_data[AppConfig.OLD_PASSWORD]
            new_password = user_data[AppConfig.NEW_PASSWORD]
            confirm_password = user_data[AppConfig.CONFIRM_PASSWORD]

            user_id = get_jwt_identity()

            obj_secure_password = HashPassword()

            self.obj_user_handler.change_password(user_id,old_password,new_password,confirm_password, obj_secure_password)

            response = {
                AppConfig.MESSAGE : PromptConfig.PASSWORD_UPDATED
            }
            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
            