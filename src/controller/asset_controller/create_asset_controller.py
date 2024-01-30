from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from handlers.asset_handler import AssetHandler
from utils.exceptions import MyBaseException

class CreateAssetController:

    def __init__(self):
        self.obj_asset_handler = AssetHandler(db_object)

    def create_asset(self, request_data):

        try:
            category_name = request_data[AppConfig.CATEGORY_NAME]
            brand_name = request_data[AppConfig.BRAND_NAME]
            vendor_email = request_data[AppConfig.VENDOR_EMAIL]
            asset_type = request_data[AppConfig.ASSET_TYPE]

            self.obj_asset_handler.create_asset(category_name, vendor_email, brand_name, asset_type)

            response = jsonify({
                AppConfig.CATEGORY_NAME : request_data[AppConfig.CATEGORY_NAME],
                AppConfig.VENDOR_EMAIL: request_data[AppConfig.VENDOR_EMAIL],
                AppConfig.MESSAGE: PromptConfig.ASSET_CREATED
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE: error.error_message,
                AppConfig.DESCRIPTION: error.error_description
            })

            return error_response, error.error_code
            