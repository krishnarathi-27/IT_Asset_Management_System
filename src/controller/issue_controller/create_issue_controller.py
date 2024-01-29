from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from handlers.issue_handler import IssueHandler
from utils.exceptions import MyBaseException

class CreateIssueController:

    def __init__(self):
        self.obj_issue_handler = IssueHandler()

    def create_issue(self, request_data):

        try:
            asset_id = request_data['asset_id']
            user_id = get_jwt_identity()
            
            self.obj_issue_handler.create_issue(asset_id, user_id)

            response = jsonify({
                "message": "Issue created successfully"
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                "message": error.error_message,
                "description": error.error_description
            })

            return error_response, error.error_code
            