"""Module contains methods for employee"""
import logging
import shortuuid
from models.database import db
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('employee_controller')

class EmployeeControllers:
    """
        Class containinig methods for employee operations
        ...
        Methods
        -------
    """
    def display_employee_details(self,user_id) -> list:
        data = db.fetch_data(
                    Queries.FETCH_DETAILS_BY_UID,
                    (user_id,))
        return data

    def display_assets_assigned(self,user_id):
        data = db.fetch_data(
                    Queries.FETCH_ASSIGNED_ASSETS_BY_UID,
                    (user_id,))
        return data
    
    def raise_issue(self, user_id: str, asset_id :str) -> bool:    
        issue_id = "ISN" + shortuuid.ShortUUID().random(length=4)
        asset_exists=  db.fetch_data(
                            Queries.FETCH_IF_USER_HAVE_ASSET,
                            (asset_id,user_id,))
        if not asset_exists:
            return False
           
        db.save_data(
            Queries.INSERT_ISSUE_FOR_ASSET,
            (issue_id,user_id,asset_id,))
        return True
    