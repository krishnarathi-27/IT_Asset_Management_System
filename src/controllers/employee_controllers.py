"""Module contains methods for employee"""
import logging
import shortuuid
from models.database import db
from config.queries import Queries
from config.queries import Header
from utils.common_helper import CommonHelper
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('employee_controller')

class EmployeeControllers:
    """
        Class containinig methods for employee operations
        ...
        Attributes
        ----------
        db_obj -> object of DatabaseHelper class for accessing its methods.
        Methods
        -------
    """
    def display_employee_details(self,user_id):

        data = db.fetch_data(
                    Queries.FETCH_DETAILS_BY_UID,
                    (user_id,))
        CommonHelper.display_table(data, Header.SCHEMA_USER_TABLE)

    def display_assets_assigned(self,user_id):

        data = db.fetch_data(
                    Queries.FETCH_ASSIGNED_ASSETS_BY_UID,
                    (user_id,))
        if not data:
            return False
        
        CommonHelper.display_table(data, Header.SCHEMA_ASSETS_TO_USER)
        return True
    
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
    