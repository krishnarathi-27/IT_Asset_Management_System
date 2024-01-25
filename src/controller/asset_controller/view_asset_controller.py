from flask import jsonify
from src.handlers.asset_handler import AssetHandler
from utils.exceptions import MyBaseException

class ViewAssetController:

    def __init__(self):
        self.obj_asset_handler = AssetHandler()

    def view_all_asset(self):
        try:
            response = self.obj_asset_handler.view_all_asset()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code