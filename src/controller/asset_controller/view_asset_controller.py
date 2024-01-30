from flask import jsonify

from config.app_config import AppConfig
from database.database import db as db_object
from src.handlers.asset_handler import AssetHandler
from utils.exceptions import MyBaseException

class ViewAssetController:

    def __init__(self):
        self.obj_asset_handler = AssetHandler(db_object)

    def view_all_asset(self):
        try:
            response = self.obj_asset_handler.view_all_asset()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code