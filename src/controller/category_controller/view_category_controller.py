from flask import jsonify

from config.app_config import AppConfig
from database.database import db as db_object
from src.handlers.category_handler import CategoryHandler
from utils.exceptions import MyBaseException

class ViewCategoryController:

    def __init__(self):
        self.obj_category_handler = CategoryHandler(db_object)

    def view_all_category(self):
        try:
            response = self.obj_category_handler.view_all_category()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
        