import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from src.handlers.vendor_handler.view_vendor_handler import ViewVendorHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('view_vendor_controller')

class ViewVendorController:
    """Controller to view vendor details"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_vendor_handler = ViewVendorHandler(db_object)

    def view_all_vendor(self) -> dict:
        """Method to display all vendors of database"""
        logger.info('Viewing vendors of database')

        try:
            response = self.obj_vendor_handler.view_all_vendor()
            return SuccessResponse.success_message(StatusCodes.OK, 
                                                       PromptConfig.VENDOR_DATA_FETCHED,
                                                       response), StatusCodes.OK

        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
