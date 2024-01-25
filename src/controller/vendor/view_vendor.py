from flask_smorest import abort
from handlers.category import CategoryHandler
from utils.exceptions import NoDataExistsException

class ViewVendorController:

    def __init__(self):
        self.obj_category_handler = CategoryHandler()

    def view_all_category(self):
        try:
            response = self.obj_category_handler.view_all_category()
            return response

        except NoDataExistsException:
            abort(404, message="Resource of user data not found")

