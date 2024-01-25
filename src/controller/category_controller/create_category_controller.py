from flask import jsonify
from src.handlers.category_handler import CategoryHandler
from utils.exceptions import MyBaseException

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
                response = jsonify({
                    "category_id": category_id,
                    "category_name": category_name,
                    "brand_name": brand_name,
                    "vendor_email": vendor_email,
                    "message": "Category created successfully"
                })
                return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
