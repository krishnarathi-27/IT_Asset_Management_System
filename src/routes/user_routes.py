from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from utils.mapped_roles import MappedRole
from controller.user_controller.create_user_controller import CreateUserController
from controller.user_controller.view_user_controller import ViewUserController
from controller.user_controller.update_user_controller import UpdateUserController
from schemas.user_schema import UserCreateSchema, UserDetailsSchema, UserPassword
from utils.rbac import role_required

blp = Blueprint("users",__name__, description="Operations on users")

@blp.route("/users")
class Users(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,UserDetailsSchema(many=True))
    def get(self):

        obj_view_user = ViewUserController()
        response = obj_view_user.view_all_user()
            
        return response
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @blp.arguments(UserCreateSchema)
    @blp.response(201,UserCreateSchema)
    def post(self,user_data):

        obj_create_user= CreateUserController()
        response = obj_create_user.create_user(user_data)

        return response
    
@blp.route("/user/profile")
class UserProfile(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.response(200,UserDetailsSchema(many=True))
    @jwt_required()
    def get(self):

        obj_view_user = ViewUserController()
        response = obj_view_user.view_user_by_id()

        return response

@blp.route("/user/change-password")
class UserPassword(MethodView):
     
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(UserPassword)
    @jwt_required()
    def put(self,user_data):

        obj_update_user = UpdateUserController()
        response = obj_update_user.update_password(user_data)

        return response
    