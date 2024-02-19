from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.vendor_handler.create_vendor_handler import CreateVendorHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import ErrorResponse, SuccessResponse

class CreateVendorController:
    """Controller to create new vendor"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_vendor_handler = CreateVendorHandler(db_object)

    def create_new_vendor(self, request_data: dict) -> dict:
        """Method to create new vendor in database"""
        app.logger.info("Creating new vendor in database")

        try:
            vendor_name = request_data['vendor_name']
            vendor_email = request_data['vendor_email']

            vendor_id = self.obj_vendor_handler.create_vendor(vendor_name, vendor_email)
            
            app.logger.info(f'Vendor created successfully {vendor_id}')
            return SuccessResponse.success_message(PromptConfig.VENDOR_CREATED
                                                       ), StatusCodes.CREATED
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
