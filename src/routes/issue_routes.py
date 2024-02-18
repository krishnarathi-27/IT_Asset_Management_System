from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from config.app_config import AppConfig
from controller.issue_controller.create_issue_controller import CreateIssueController
from controller.issue_controller.update_issue_controller import UpdateIssueController
from controller.issue_controller.view_issue_controller import ViewIssueController
from schemas.issue_schema import IssueSchema, IssueCreateSchema
from utils.rbac import access_required, ROLE_REQUIRED

blp = Blueprint("issues",__name__, description="Operations on issues")

@blp.route("/issues")
class Issues(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @access_required([ROLE_REQUIRED['asset manager']])
    @blp.response(200,IssueSchema(many=True))
    def get(self):

        obj_view_issue = ViewIssueController()
        response = obj_view_issue.view_all_issue()
            
        return response
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @blp.arguments(IssueCreateSchema)
    @blp.response(201,IssueCreateSchema)
    @jwt_required()
    def post(self,request_data):

        obj_create_issue= CreateIssueController()
        response = obj_create_issue.create_issue(request_data)

        return response
    
@blp.route("/issues/<string:user_id>")
class IssueId(MethodView):
    
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @blp.response(200,IssueSchema(many=True))
    @jwt_required()
    def get(self, user_id):

        obj_view_issue = ViewIssueController()
        response = obj_view_issue.view_issue(user_id)

        return response
     
    @blp.doc(parameters=AppConfig.SWAGGER_AUTHORISATION_HEADER)
    @blp.arguments(IssueSchema)
    @jwt_required()
    def put(self,user_data, user_id):

        obj_update_issue = UpdateIssueController()
        response = obj_update_issue.update_issue(user_data, user_id)

        return response
    