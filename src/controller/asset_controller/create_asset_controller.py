from flask import jsonify
from handlers.asset_handler import AssetHandler
from utils.exceptions import MyBaseException

class CreateAssetController:

    def __init__(self):
        self.obj_asset_handler = AssetHandler()

    def create_asset(self, request_data):

        try:
            category_name = request_data['category_name']
            vendor_email = request_data['vendor_email']
            asset_type = request_data['asset_type']

            self.obj_asset_handler.create_new_asset(category_name, vendor_email, asset_type)

            response = jsonify({
                "category_name": request_data['category_name'],
                "vendor_email": request_data['vendor_email'],
                "message": "Asset created in inventory successfully"
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code

            