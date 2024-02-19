from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.vendor_handler.view_vendor_handler import ViewVendorHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class ViewVendorController:
    """Controller to view vendor details"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_vendor_handler = ViewVendorHandler(db_object)

    def view_all_vendor(self) -> dict:
        """Method to display all vendors of database"""
        app.logger.info('Viewing vendors of database')

        try:
            response = self.obj_vendor_handler.view_all_vendor()
            return SuccessResponse.success_message(PromptConfig.VENDOR_DATA_FETCHED,
                                                       response), StatusCodes.OK

        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
