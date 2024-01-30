from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from utils.secure_password import HashPassword
from handlers.user_handler import UserHandler
from utils.exceptions import MyBaseException

class CreateUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler(db_object)

    def create_user(self, user_data):

        try:
            username = user_data[AppConfig.USERNAME]
            password = user_data[AppConfig.PASSWORD]
            role = user_data[AppConfig.ROLE]

            obj_secure_password = HashPassword()
            self.obj_user_handler.create_new_user(role,username,password, obj_secure_password)

            response = jsonify({
                AppConfig.USERNAME : user_data[AppConfig.USERNAME],
                AppConfig.ROLE : user_data[AppConfig.ROLE],
                AppConfig.MESSAGE : PromptConfig.USER_CREATED
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code

            