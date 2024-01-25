from flask_smorest import abort
from handlers.vendor import VendorHandler
from utils.exceptions import VendorAlreadyExistsException

class CreateVendorController:

    def __init__(self):
        self.obj_vendor_handler = VendorHandler()

    def create_new_vendor(self, request_data):

        try:
            vendor_name = request_data['vendor_name']
            vendor_email = request_data['vendor_email']

            vendor_id = self.obj_vendor_handler.create_vendor(vendor_name, vendor_email)

            response = {
                    "vendor_id": vendor_id,
                    "vendor_name": vendor_name,
                    "vendor_email": vendor_email,
                    "message": "Vendor created successfully"
                }
            return response
        
        except VendorAlreadyExistsException:
            abort (409, message="Vendor already exists in database")
