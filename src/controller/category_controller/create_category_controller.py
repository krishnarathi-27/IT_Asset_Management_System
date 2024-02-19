from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.category_handler.create_category_handler import CreateCategoryHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse

class CreateCategoryController:
    """Controller for creating category"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_category_handler = CreateCategoryHandler(db_object)

    def create_new_category(self, request_data: dict) -> dict:
        """Method to create new category if vendor exists and if same category already not exists"""
        app.logger.info('Controller for creating new category')

        try:
            category_name = request_data['category_name']
            brand_name = request_data['brand_name']
            vendor_email = request_data['vendor_email']

            category_name = category_name.lower()
            brand_name = brand_name.lower()
            self.obj_category_handler.create_category(category_name, brand_name, vendor_email)
            return SuccessResponse.success_message(PromptConfig.CATEGORY_CREATED), StatusCodes.CREATED
        
        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
