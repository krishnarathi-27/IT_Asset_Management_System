import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from handlers.vendor_handler import VendorHandler
from utils.exceptions import MyBaseException
from utils.response import ErrorResponse, SuccessResponse

logger = logging.getLogger('delete_vendor_controller')

class DeleteVendorController:
    """Controller to deactivate vendor status"""

    def __init__(self) -> None:
        self.obj_vendor_handler = VendorHandler(db_object)

    def delete_vendor(self,vendor_id: str) -> dict:
        """Method to deactivate vendor from database"""
        logger.info("Deactivating vendor from database")

        try:
            self.obj_vendor_handler.deactivate_vendor(vendor_id)

            response = {
                'vendor_id' : vendor_id,
                'message' : PromptConfig.VENDOR_DEACTIVATED
            }

            logger.info(f'Vendor {vendor_id} deactiavted successfully')
            return SuccessResponse.success_message(StatusCodes.OK, 
                                                       PromptConfig.VENDOR_DEACTIVATED,
                                                       response), StatusCodes.OK

        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        