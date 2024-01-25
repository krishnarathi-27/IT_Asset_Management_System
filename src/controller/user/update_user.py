from flask_smorest import abort
from handlers.user import UserHandler
from utils.exceptions import InvalidUserCredentials, PasswordsNotMatchException

class UpdateUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler()

    def update_password(self,user_id, user_data):

        try:
            old_password = user_data['old_password']
            new_password = user_data['new_password']
            confirm_password = user_data['confirm_password']

            self.obj_user_handler.change_password(user_id,old_password,new_password,confirm_password)

            response = {
                "message": "Password updated successfully"
            }
            return response

        except InvalidUserCredentials:
            abort (401, message="Invalid credentials. Try again with valid one")

        except PasswordsNotMatchException:
            abort (400, message="New and old passwords not matches")
            