import logging

from config.app_config import StatusCodes
from config.prompts.prompts import PromptConfig
from database.database import Database
from handlers.category_handler.view_category_handler import ViewCategoryHandler
from utils.exceptions import MyBaseException
from utils.response import SuccessResponse, ErrorResponse

logger = logging.getLogger('view_category_controller')

class ViewCategoryController:
    """Controller to view all the category of assets"""

    def __init__(self) -> None:
        db_object = Database()
        self.obj_category_handler = ViewCategoryHandler(db_object)

    def view_all_category(self) -> dict:
        """Method to view all categories of assets data"""
        logger.info('Viewing all categories of any asset')

        try:
            response = self.obj_category_handler.view_all_category()
            return SuccessResponse.success_message(StatusCodes.OK, PromptConfig.CATEGORY_DATA_FETCHED, response), StatusCodes.OK

        except MyBaseException as error:
            logger.error(f'Error handled by custom error handler {error.error_message}')
            return ErrorResponse.error_message(error), error.error_code
        