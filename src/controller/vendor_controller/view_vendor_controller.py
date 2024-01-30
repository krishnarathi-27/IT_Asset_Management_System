from flask import jsonify

from config.app_config import AppConfig
from database.database import db as db_object
from src.handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException

class ViewVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler(db_object)

    def view_all_vendor(self):
        try:
            response = self.obj_vendor_handler.view_all_vendor()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code

