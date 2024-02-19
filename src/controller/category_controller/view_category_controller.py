from flask import current_app as app

from src.config.app_config import StatusCodes
from src.config.prompts.prompts import PromptConfig
from src.database.database import Database
from src.handlers.category_handler.view_category_handler import ViewCategoryHandler
from src.utils.exceptions import ApplicationException, DBException
from src.utils.response import SuccessResponse, ErrorResponse


class ViewCategoryController:
    """Controller to view all the category of assets"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_category_handler = ViewCategoryHandler(db_object)

    def view_all_category(self) -> dict:
        """Method to view all categories of assets data"""
        app.logger.info('Viewing all categories of any asset')

        try:
            response = self.obj_category_handler.view_all_category()
            return SuccessResponse.success_message(PromptConfig.CATEGORY_DATA_FETCHED, response), StatusCodes.OK

        except ApplicationException as error:
            app.logger.error(f'Error handled by application custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        
        except DBException as error:
            app.logger.error(f'Error handled by database custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        