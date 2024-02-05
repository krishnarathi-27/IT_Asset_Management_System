import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.asset_handler.update_asset_handler import UpdateAssetHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('update_asset_controller')

class UpdateAssetController:
    """Controller to update assets status"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_asset_handler = UpdateAssetHandler(db_object)

    def assign_asset(self, request_data: dict, asset_id: str) -> dict:
        """Function to assign asset to user"""
        logger.info("Assigning assets to user")

        try:
            mapping_id  = request_data['mapping_id']
            asset_type= request_data['asset_type']
            assigned_to= request_data['assigned_to']
            asset_status= request_data['asset_status']
            
            self.obj_asset_handler.assign_asset(asset_id, assigned_to)

            response = {
                'asset_id' : asset_id,
                'user_id' : request_data['assigned_to'],
                'message' : PromptConfig.ASSET_ASSIGNED
            }
            logger.info(f'Assets assigned to user {assigned_to}')
            return SuccessResponse.success_message(StatusCodes.OK, 
                                                       PromptConfig.ASSET_ASSIGNED,
                                                       response), StatusCodes.OK
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
    def unassign_asset(self, request_data: dict, asset_id: str) -> dict:
        """Function to unassign assigned asset from user"""
        logger.info('Asset unassigned successfully')

        try:
            mapping_id  = request_data['mapping_id']
            asset_type= request_data['asset_type']
            assigned_to= request_data['assigned_to']
            asset_status= request_data['asset_status']

            self.obj_asset_handler.unassign_asset(asset_id)

            response = {
                'asset_id' : asset_id,
                'message' : PromptConfig.ASSET_UNASSIGNED
            }
            return SuccessResponse.success_message(StatusCodes.OK, 
                                                       PromptConfig.ASSET_UNASSIGNED,
                                                       response), StatusCodes.OK
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        