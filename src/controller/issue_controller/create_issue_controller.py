from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from flask_jwt_extended import get_jwt_identity
from handlers.issue_handler import IssueHandler
from utils.exceptions import MyBaseException

class CreateIssueController:

    def __init__(self):
        self.obj_issue_handler = IssueHandler(db_object)

    def create_issue(self, request_data):

        try:
            asset_id = request_data[AppConfig.ASSET_ID]
            user_id = get_jwt_identity()
            
            self.obj_issue_handler.create_issue(asset_id, user_id)

            response = jsonify({
                AppConfig.MESSAGE : PromptConfig.ISSUE_CREATED
            })
            return response
        
        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
            