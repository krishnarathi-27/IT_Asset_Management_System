import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.vendor_handler.delete_vendor_handler import DeleteVendorHandler
from utils.exceptions import ApplicationException, DBException
from utils.response import ErrorResponse, SuccessResponse

logger = logging.getLogger('delete_vendor_controller')

class DeleteVendorController:
    """Controller to deactivate vendor status"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_vendor_handler = DeleteVendorHandler(db_object)

    def delete_vendor(self,vendor_id: str) -> dict:
        """Method to deactivate vendor from database"""
        logger.info("Deactivating vendor from database")

        try:
            self.obj_vendor_handler.deactivate_vendor(vendor_id)

            logger.info(f'Vendor {vendor_id} deactiavted successfully')
            return SuccessResponse.success_message(PromptConfig.VENDOR_DEACTIVATED), StatusCodes.OK

        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        