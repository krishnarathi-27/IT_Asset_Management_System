from flask_smorest import abort
from handlers.user import UserHandler
from utils.exceptions import UserAlreadyExistsException, DBException

class CreateUserController:

    def __init__(self):
        self.obj_user_handler = UserHandler()

    def create_user(self, user_data):

        try:
            username = user_data['username']
            password = user_data['password']
            role = user_data['user_role']

            self.obj_user_handler.create_new_user(role,username,password)

            response = {
            "username": user_data['username'],
            "user_role": user_data['user_role'],
            "message": "User created successfully"
            }
            return response
        
        except UserAlreadyExistsException:
            abort (409, message="User already exists in database")

        except DBException:
            abort (500, message="Server not responding. Try again after some time")
            