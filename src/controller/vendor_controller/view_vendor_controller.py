from flask import jsonify
from src.handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException

class ViewVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler()

    def view_all_vendor(self):
        try:
            response = self.obj_vendor_handler.view_all_vendor()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code

