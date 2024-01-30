from flask import jsonify

from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from database.database import db as db_object
from src.handlers.issue_handler import IssueHandler
from utils.exceptions import MyBaseException

class ViewIssueController:

    def __init__(self):
        self.obj_issue_handler = IssueHandler()

    def view_all_issue(self):
        try:
            response = self.obj_issue_handler.view_issues()
            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
        
    def view_issue(self,user_id):
        try:

            response = self.obj_issue_handler.view_issue_by_userid(user_id)
            return response

        except MyBaseException as error:
            error_response = jsonify({
                AppConfig.MESSAGE : error.error_message,
                AppConfig.DESCRIPTION : error.error_description
            })

            return error_response, error.error_code
        