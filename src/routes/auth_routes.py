import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from config.app_config import AppConfig
from schemas.user_schema import LoginSchema, LoginSuccessSchema
from controller.auth_controller.login_controller import LoginController
from controller.auth_controller.logout_controller import LogoutController
from controller.auth_controller.refresh_controller import RefreshController

logger = logging.getLogger('auth_routes')

blp = Blueprint("authentication", __name__, description="Operations on authentication task")

obj_auth = LoginController()

@blp.route("/v1/login")
class Login(MethodView):
    """Blueprint for login endpoint where user is authenticated and authenticate user gets JWT token"""
    logger.info('User trying to authenticate and get JWT token')

    @blp.arguments(LoginSchema)
    @blp.response(200,LoginSuccessSchema)
    def post(self,user_data):
        
        token = obj_auth.login(user_data)
        return token
        
@blp.route("/v1/logout")
class Logout(MethodView):

    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @jwt_required()
    def post(self):
        
        obj = LogoutController()
        response = obj.logout()

        return response
    
@blp.route("/v1/refresh")
class Refresh(MethodView):

    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @jwt_required(refresh=True)
    def post(self):
        
        obj = RefreshController()
        response = obj.refresh()

        return response