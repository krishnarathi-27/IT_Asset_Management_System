import shortuuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt

from models.database import db
from utils.mapped_roles import MappedRole
from controllers.user_controllers import UserController
from schemas.user_schema import UserCreateSchema, UserDetailsSchema, UserPassword
from utils.rbac import role_required

blp = Blueprint("users",__name__, description="Operations on users")

obj_user_controller = UserController(db)

@blp.route("/user")
class Users(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE,MappedRole.MANAGER_ROLE])
    @blp.response(200,UserDetailsSchema(many=True))
    def get(self):
        data = obj_user_controller.view_users()

        if not data:
            abort(404,message="Users not exists")
            
        return data
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.ADMIN_ROLE])
    @blp.arguments(UserCreateSchema)
    @blp.response(201,UserCreateSchema)
    def post(self,user_data):
        user_id = "EMP" + shortuuid.ShortUUID().random(length=4)

        obj_user_controller.create_new_user(user_id,user_data['user_role'],user_data['username'],user_data['password'])

        response = {
            "user_id": user_id,
            "username": user_data['username'],
            "user_role": user_data['user_role'],
            "message": "User created successfully"
        }
        return response
    
@blp.route("/user/profile")
class UserProfile(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.response(200,UserDetailsSchema(many=True))
    @jwt_required()
    def get(self):
        claims = get_jwt()
        user_id = claims['sub']
        data = obj_user_controller.view_user_by_id(user_id)

        if not data:
            abort(404, message="User data not exists")

        return data

@blp.route("/user/change-password")
class UserPassword(MethodView):
     
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(UserPassword)
    @jwt_required()
    def put(self,user_data):
        claims = get_jwt()
        user_id = claims['sub']
        result = obj_user_controller.change_password(user_id, user_data['new_password'], user_data['confirm_password'])

        if not result:
            abort(400, message="Passwords do not match")

        return {"message": "Passwords updated successfully"}
    