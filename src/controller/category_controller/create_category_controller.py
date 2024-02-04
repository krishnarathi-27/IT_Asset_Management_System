import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.handlers.category_handler import CategoryHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('create_category_controller')

class CreateCategoryController:
    """Controller for creating category"""

    def __init__(self) -> None:
        self.obj_category_handler = CategoryHandler(db_object)

    def create_new_category(self, request_data: dict) -> dict:
        """Method to create new category if vendor exists and if same category already not exists"""
        logger.info('Controller for creating new category')

        try:
            category_name = request_data['category_name']
            brand_name = request_data['brand_name']
            vendor_email = request_data['vendor_email']

            category_id = self.obj_category_handler.create_category(category_name, brand_name, vendor_email)

            if category_id:
                response = {
                    "category_id": category_id,
                    "category_name": category_name,
                    "brand_name": brand_name,
                    "vendor_email": vendor_email,
                    "message" : PromptConfig.CATEGORY_CREATED
                }
                return SuccessResponse.success_message(StatusCodes.CREATED, 
                                                       PromptConfig.CATEGORY_CREATED,
                                                       response), StatusCodes.CREATED
        
        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
