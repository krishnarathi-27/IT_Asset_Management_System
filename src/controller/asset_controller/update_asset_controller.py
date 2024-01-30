from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from handlers.asset_handler import AssetHandler
from utils.exceptions import MyBaseException

class UpdateAssetController:

    def __init__(self):
        self.obj_asset_handler = AssetHandler(db_object)

    def assign_asset(self, request_data, asset_id):

        try:
            mapping_id  = request_data[AppConfig.MAPPING_ID]
            asset_type= request_data[AppConfig.ASSET_TYPE]
            assigned_to= request_data[AppConfig.ASSIGNED_TO]
            asset_status= request_data[AppConfig.ASSET_STATUS]
            
            self.obj_asset_handler.assign_asset(asset_id, assigned_to)

            response = jsonify({
                AppConfig.ASSET_ID : asset_id,
                AppConfig.USER_ID : request_data[AppConfig.ASSIGNED_TO],
                AppConfig.MESSAGE : PromptConfig.ASSET_ASSIGNED
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
        
    def unassign_asset(self, request_data, asset_id):

        try:
            mapping_id  = request_data[AppConfig.MAPPING_ID]
            asset_type= request_data[AppConfig.ASSET_TYPE]
            assigned_to= request_data[AppConfig.ASSIGNED_TO]
            asset_status= request_data[AppConfig.ASSET_STATUS]

            self.obj_asset_handler.unassign_asset(asset_id)

            response = jsonify({
                AppConfig.ASSET_ID : asset_id,
                AppConfig.MESSAGE : PromptConfig.ASSET_UNASSIGNED
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
        