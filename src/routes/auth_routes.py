from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token

from models.database import db
from utils.mapped_roles import MappedRole
from schemas.user_schema import LoginSchema, LoginSuccessSchema
from controllers.auth_controllers import AuthControllers

blp = Blueprint("authentication", __name__, description="Operations on authentication task")

obj_auth = AuthControllers(db)

@blp.route("/login")
class Login(MethodView):

    @blp.arguments(LoginSchema)
    @blp.response(200,LoginSuccessSchema)
    def post(self,user_data):
        
        data = obj_auth.validate_user(user_data['username'],user_data['password'])

        if data:
            get_role = MappedRole.get_mapped_role(data[0])
            access_token = create_access_token(identity=data[1],additional_claims={"role": get_role})
            refresh_token = create_refresh_token(identity=data[1])

            response = {
                "access_token": access_token, 
                "refresh_token": refresh_token,
                "message": "Logged in successfully"
            }
            return response
        else:
            abort(401, message="Invalid credentials")