import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from src.handlers.asset_handler.view_asset_handler import ViewAssetHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('view_asset_controller')

class ViewAssetController:
    """Controller to view assets in inventory"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_asset_handler = ViewAssetHandler(db_object)

    def view_all_asset(self) -> dict:
        """Function to view all assets in inventory"""
        logger.info('Function to view assets in inventory')

        try:
            response = self.obj_asset_handler.view_all_asset()
            return SuccessResponse.success_message(StatusCodes.OK, 
                                                    PromptConfig.ASSET_DATA_FETCHED,
                                                    response), StatusCodes.OK

        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        