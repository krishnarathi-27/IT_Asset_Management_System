from flask.views import MethodView
from flask_smorest import Blueprint

from database.database import db
from schemas.user_schema import LoginSchema, LoginSuccessSchema
from controller.auth.login import LoginController

blp = Blueprint("authentication", __name__, description="Operations on authentication task")

obj_auth = LoginController()

@blp.route("/login")
class Login(MethodView):

    @blp.arguments(LoginSchema)
    @blp.response(200,LoginSuccessSchema)
    def post(self,user_data):
        
        token = obj_auth.login(user_data)
        return token
        
@blp.route("/logout")
class Logout(MethodView):

    def post(self):
        pass