from flask import jsonify
from handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException

class DeleteVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler()

    def delete_vendor(self,vendor_id):
        try:
            self.obj_vendor_handler.deactivate_vendor(vendor_id)

            response = jsonify({
                "message": "Vendor deactivated successfully"
            })

            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code