from flask import jsonify
from src.handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException

class CreateVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler()

    def create_new_vendor(self, request_data):

        try:
            vendor_name = request_data['vendor_name']
            vendor_email = request_data['vendor_email']

            vendor_id = self.obj_vendor_handler.create_vendor(vendor_name, vendor_email)

            response = jsonify({
                    "vendor_id": vendor_id,
                    "vendor_name": vendor_name,
                    "vendor_email": vendor_email,
                    "message": "Vendor created successfully"
                })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
