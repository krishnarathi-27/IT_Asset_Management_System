import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.asset_handler.create_asset_handler import CreateAssetHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('create_asset_controller')

class CreateAssetController:
    """Controller to add new asset in inventory"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_asset_handler = CreateAssetHandler(db_object)

    def create_asset(self, request_data: dict) -> dict:
        """Function to add new asset in inventory"""
        logging.info('Function to add asset in inventory')

        try:
            category_name = request_data['category_name']
            brand_name = request_data['brand_name']
            vendor_email = request_data['vendor_email']
            asset_type = request_data['asset_type']

            asset_id = self.obj_asset_handler.create_asset(category_name, vendor_email, brand_name, asset_type)

            response = {
                'asset_id': asset_id,
                'category_name' : request_data['category_name'],
                'vendor_email': request_data['vendor_email'],
                'message': PromptConfig.ASSET_CREATED
            }
            return SuccessResponse.success_message(StatusCodes.CREATED, 
                                                       PromptConfig.ASSET_CREATED,
                                                       response), StatusCodes.CREATED
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
            