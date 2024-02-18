import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.category_handler.create_category_handler import CreateCategoryHandler
from utils.exceptions import ApplicationException, DBException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('create_category_controller')

class CreateCategoryController:
    """Controller for creating category"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_category_handler = CreateCategoryHandler(db_object)

    def create_new_category(self, request_data: dict) -> dict:
        """Method to create new category if vendor exists and if same category already not exists"""
        logger.info('Controller for creating new category')

        try:
            category_name = request_data['category_name']
            brand_name = request_data['brand_name']
            vendor_email = request_data['vendor_email']

            category_name = category_name.lower()
            brand_name = brand_name.lower()
            self.obj_category_handler.create_category(category_name, brand_name, vendor_email)
            return SuccessResponse.success_message(PromptConfig.CATEGORY_CREATED), StatusCodes.CREATED
        
        except ApplicationException as error:
            logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
