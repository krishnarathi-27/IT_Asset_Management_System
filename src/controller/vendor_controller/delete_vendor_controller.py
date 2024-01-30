from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException

class DeleteVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler(db_object)

    def delete_vendor(self,vendor_id):
        try:
            self.obj_vendor_handler.deactivate_vendor(vendor_id)

            response = jsonify({
                AppConfig.MESSAGE : PromptConfig.VENDOR_DEACTIVATED
            })

            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code