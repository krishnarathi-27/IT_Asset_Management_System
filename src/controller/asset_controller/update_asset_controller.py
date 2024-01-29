from flask import jsonify
from handlers.asset_handler import AssetHandler
from utils.exceptions import MyBaseException

class UpdateAssetController:

    def __init__(self):
        self.obj_asset_handler = AssetHandler()

    def assign_asset(self, request_data, asset_id):

        try:
            print(request_data)
            mapping_id  = request_data["mapping_id"]
            asset_type= request_data["asset_type"]
            assigned_to= request_data["assigned_to"]
            asset_status= request_data["asset_status"]
            
            self.obj_asset_handler.assign_asset(asset_id, assigned_to)

            response = jsonify({
                "asset_id" : asset_id,
                "employee_id" : request_data['assigned_to'],
                "message": "Asset assigned to user successfully"
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
        
    def unassign_asset(self, request_data, asset_id):

        try:
            mapping_id  = request_data["mapping_id"]
            asset_type= request_data["asset_type"]
            assigned_to= request_data["assigned_to"]
            asset_status= request_data["asset_status"]

            self.obj_asset_handler.unassign_asset(asset_id)

            response = jsonify({
                "asset_id" : asset_id,
                "message": "Asset unassigned from user successfully"
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
        