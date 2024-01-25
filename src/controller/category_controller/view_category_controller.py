from flask import jsonify
from src.handlers.category_handler import CategoryHandler
from utils.exceptions import MyBaseException

class ViewCategoryController:

    def __init__(self):
        self.obj_category_handler = CategoryHandler()

    def view_all_category(self):
        try:
            response = self.obj_category_handler.view_all_category()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code