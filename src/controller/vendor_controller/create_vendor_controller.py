import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from src.handlers.vendor_handler.create_vendor_handler import CreateVendorHandler
from utils.exceptions import MyBaseException
from utils.response import ErrorResponse, SuccessResponse

logger = logging.getLogger('create_vendor_controller')

class CreateVendorController:
    """Controller to create new vendor"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_vendor_handler = CreateVendorHandler(db_object)

    def create_new_vendor(self, request_data: dict) -> dict:
        """Method to create new vendor in database"""
        logger.info("Creating new vendor in database")

        try:
            vendor_name = request_data['vendor_name']
            vendor_email = request_data['vendor_email']

            vendor_id = self.obj_vendor_handler.create_vendor(vendor_name, vendor_email)

            response = {
                    'vendor_id' : vendor_id,
                    'vendor_name' : vendor_name,
                    'vendor_email' : vendor_email,
                    'message' : PromptConfig.VENDOR_CREATED
                }
            
            logger.info(f'Vendor created successfully {vendor_id}')
            return SuccessResponse.success_message(StatusCodes.CREATED, 
                                                       PromptConfig.VENDOR_CREATED,
                                                       response), StatusCodes.CREATED
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
