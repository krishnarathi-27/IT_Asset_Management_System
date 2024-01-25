from flask_smorest import abort
from handlers.user import UserHandler
from utils.exceptions import NoDataExistsException

class ViewUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler()

    def view_all_user(self):
        try:
            response = self.obj_user_handler.view_all_user()
            return response

        except NoDataExistsException:
            abort(404, message="Resource of user data not found")


    def view_user_by_id(self, user_id):
        try:

            response = self.obj_user_handler.view_user_by_id(user_id)
            return response

        except NoDataExistsException:
            abort(404, message="Resource of user data not found")

