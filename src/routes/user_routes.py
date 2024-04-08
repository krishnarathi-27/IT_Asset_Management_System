from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from src.config.app_config import AppConfig
from src.controller.user_controller.create_user_controller import CreateUserController
from src.controller.user_controller.view_user_controller import ViewUserController
from src.controller.user_controller.update_user_controller import UpdateUserController
from src.schemas.user_schema import UserCreateSchema, UserDetailsSchema, UserPassword
from src.utils.rbac import access_required, ROLE_REQUIRED

blp = Blueprint("users",__name__, description="Operations on users")

@blp.route("/v1/users")
class Users(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @access_required([ROLE_REQUIRED['admin'],ROLE_REQUIRED['asset manager']])
    @blp.response(200,UserDetailsSchema(many=True))
    def get(self):

        obj_view_user = ViewUserController()
        response = obj_view_user.view_all_user()
            
        return response
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @access_required([ROLE_REQUIRED['admin']])
    @blp.arguments(UserCreateSchema)
    @blp.response(201,UserCreateSchema)
    def post(self,user_data):

        obj_create_user= CreateUserController()
        response = obj_create_user.create_user(user_data)

        return response
    
@blp.route("/v1/users/profile")
class UserProfile(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @blp.response(200,UserDetailsSchema(many=True))
    @jwt_required()
    def get(self):

        obj_view_user = ViewUserController()
        response = obj_view_user.view_user_by_id()

        return response

@blp.route("/v1/users/change-password")
class UserPassword(MethodView):
     
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @blp.arguments(UserPassword)
    @jwt_required()
    def put(self,user_data):

        obj_update_user = UpdateUserController()
        response = obj_update_user.update_password(user_data)

        return response
