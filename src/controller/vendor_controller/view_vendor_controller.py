import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.vendor_handler.view_vendor_handler import ViewVendorHandler
from utils.exceptions import ApplicationException, DBException
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
            return SuccessResponse.success_message(PromptConfig.VENDOR_DATA_FETCHED,
                                                       response), StatusCodes.OK

        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
