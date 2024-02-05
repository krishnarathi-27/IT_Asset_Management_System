from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from utils.mapped_roles import MappedRole
from controller.issue_controller.create_issue_controller import CreateIssueController
from controller.issue_controller.update_issue_controller import UpdateIssueController
from controller.issue_controller.view_issue_controller import ViewIssueController
from schemas.user_schema import UserDetailsSchema, UserPassword
from schemas.issue_schema import IssueSchema, IssueCreateSchema
from utils.rbac import role_required

blp = Blueprint("issues",__name__, description="Operations on issues")

@blp.route("/issues")
class Issues(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_required([MappedRole.MANAGER_ROLE])
    @blp.response(200,IssueSchema(many=True))
    def get(self):

        obj_view_issue = ViewIssueController()
        response = obj_view_issue.view_all_issue()
            
        return response
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(IssueCreateSchema)
    @blp.response(201,IssueCreateSchema)
    @jwt_required()
    def post(self,request_data):

        obj_create_issue= CreateIssueController()
        response = obj_create_issue.create_issue(request_data)

        return response
    
@blp.route("/issue/<string:user_id>")
class IssueId(MethodView):
    
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.response(200,IssueSchema(many=True))
    @jwt_required()
    def get(self, user_id):

        obj_view_issue = ViewIssueController()
        response = obj_view_issue.view_issue(user_id)

        return response
     
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @blp.arguments(IssueSchema)
    @jwt_required()
    def put(self,user_data, user_id):

        obj_update_issue = UpdateIssueController()
        response = obj_update_issue.update_issue(user_data, user_id)

        return response
    