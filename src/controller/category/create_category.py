from flask_smorest import abort
from handlers.category import CategoryHandler
from utils.exceptions import CategoryAlreadyExistsException, VendorNotExistsException

class CreateCategoryController:

    def __init__(self):
        self.obj_category_handler = CategoryHandler()

    def create_new_category(self, request_data):

        try:
            category_name = request_data['category_name']
            brand_name = request_data['brand_name']
            vendor_email = request_data['vendor_email']

            category_id = self.obj_category_handler.create_category(category_name, brand_name, vendor_email)

            if category_id:
                response = {
                    "category_id": category_id,
                    "category_name": category_name,
                    "brand_name": brand_name,
                    "vendor_email": vendor_email,
                    "message": "Category created successfully"
                }
                return response
        
        except CategoryAlreadyExistsException:
            abort (409, message="Category already exists in database")

        except VendorNotExistsException:
            abort (404, message="Vendor email not exist")
