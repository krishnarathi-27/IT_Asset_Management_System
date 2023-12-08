"""Module contains methods for employee"""
import logging
import shortuuid
from config.queries import Header
from utils.common_helper import CommonHelper
from models.database_helper import DatabaseHelper
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
    def __init__(self) -> None:
        self.obj_db_delper = DatabaseHelper()

    def display_employee_details(self,user_id):
        data = self.obj_db_delper.fetch_employee_details(user_id)
        CommonHelper.display_table(data, Header.SCHEMA_USER_TABLE)

    def display_assets_assigned(self,user_id):
        data = self.obj_db_delper.fetch_assets_assigned_to_user(user_id)
        if not data:
            return False
        
        CommonHelper.display_table(data, Header.SCHEMA_ASSETS_TO_USER)
        return True
    
    def raise_issue(self, user_id: str, asset_id :str) -> bool:
        issue_id = "ISN" + shortuuid.ShortUUID().random(length=4)
        asset_exists= self.obj_db_delper.fetch_asset_id_exists_for_user(asset_id,user_id)
        if not asset_exists:
            return False
    
        self.obj_db_delper.save_raised_issue(issue_id,user_id,asset_id)
        return True