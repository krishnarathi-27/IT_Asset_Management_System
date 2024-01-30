from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException

class CreateVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler(db_object)

    def create_new_vendor(self, request_data):

        try:
            vendor_name = request_data[AppConfig.VENDOR_NAME]
            vendor_email = request_data[AppConfig.VENDOR_EMAIL]

            vendor_id = self.obj_vendor_handler.create_vendor(vendor_name, vendor_email)

            response = jsonify({
                    AppConfig.VENDOR_ID : vendor_id,
                    AppConfig.VENDOR_NAME : vendor_name,
                    AppConfig.VENDOR_EMAIL : vendor_email,
                    AppConfig.MESSAGE : PromptConfig.VENDOR_CREATED
                })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
