from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.handlers.category_handler import CategoryHandler
from utils.exceptions import MyBaseException

class CreateCategoryController:

    def __init__(self):
        self.obj_category_handler = CategoryHandler()

    def create_new_category(self, request_data):

        try:
            category_name = request_data[AppConfig.CATEGORY_NAME]
            brand_name = request_data[AppConfig.BRAND_NAME]
            vendor_email = request_data[AppConfig.VENDOR_EMAIL]

            category_id = self.obj_category_handler.create_category(category_name, brand_name, vendor_email)

            if category_id:
                response = jsonify({
                    AppConfig.CATEGORY_ID : category_id,
                    AppConfig.CATEGORY_NAME : category_name,
                    AppConfig.BRAND_NAME : brand_name,
                    AppConfig.VENDOR_EMAIL : vendor_email,
                    AppConfig.MESSAGE : PromptConfig.CATEGORY_CREATED
                })
                return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE: error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
