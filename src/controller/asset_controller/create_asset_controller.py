from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.asset_handler.create_asset_handler import CreateAssetHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class CreateAssetController:
    """Controller to add new asset in inventory"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_asset_handler = CreateAssetHandler(db_object)

    def create_asset(self, request_data: dict) -> dict:
        """Function to add new asset in inventory"""
        app.logger.info('Function to add asset in inventory')

        try:
            category_name = request_data['category_name']
            brand_name = request_data['brand_name']
            vendor_email = request_data['vendor_email']
            asset_type = request_data['asset_type']

            self.obj_asset_handler.create_asset(category_name, vendor_email, brand_name, asset_type)

            return SuccessResponse.success_message(PromptConfig.ASSET_CREATED), StatusCodes.CREATED
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code      
            