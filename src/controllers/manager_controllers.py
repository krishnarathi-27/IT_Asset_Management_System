"""Module having buisness logic of manager functionalities"""
import logging
import shortuuid
from datetime import datetime
from config.queries import Header
from config.app_config import AppConfig
from config.log_prompts.logs_config import LogsConfig
from models.database_helper import DatabaseHelper
from utils.common_helper import CommonHelper

logger = logging.getLogger('manager_controller')

class ManagerControllers:
    """
        Class containing methods to track assets
        Attributes 
        ----------
        db_helper_obj -> object of DatabaseHelper class for accessing its methods
        Methods
        -------
    """
    
    def __init__(self) -> None:
        self.obj_db_helper = DatabaseHelper()
        self.obj_common_helper = CommonHelper()

    def fetch_by_username(self,user_id) -> bool:
        data_user = self.obj_db_helper.fetch_user_exists(user_id)
        if not data_user:
            return False
        
        data = self.obj_db_helper.fetch_asset_by_userid(user_id)
        if not data:
            return False
        
        CommonHelper.display_table(data,Header.SCHEMA_ASSETS_BY_USER_ID)
        return True
    
    def fetch_by_category(self,category_id) -> bool:
        data_category = self.obj_db_helper.fetch_category_exists(category_id)
        if not data_category:
            return False
        
        CommonHelper.display_table(data_category,Header.SCHEMA_ASSETS_BY_CATEGORY_ID)
        return True
    
    def fetch_by_vendor(self,vendor_email) -> bool:
        data_vendor = self.obj_db_helper.fetch_vendor_exists(vendor_email)
        if not data_vendor:
            return False
        
        CommonHelper.display_table(data_vendor,Header.SCHEMA_ASSETS_BY_VENDOR_EMAIL)
        return True

    def fetch_asset_available(self) -> bool:
        data = self.obj_db_helper.fetch_asset_available()
        if not data:
            return False
        
        CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)
        return True
    
    def fetch_asset_maintenance(self) -> bool:
        data = self.obj_db_helper.fetch_asset_maintenance()
        if not data:
            return False
        
        CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)
        return True
    
    def view_pending_issues(self) -> bool:
        data = self.obj_db_helper.fetch_pending_issues()
        if not data:
            return False
        
        CommonHelper.display_table(data, Header.SCHEMA_PENDING_ISSUES)
        return True
    
    def send_asset(self,issue_id, user_id) -> bool:
        asset_id = self.obj_db_helper.fetch_asset_by_issueid(issue_id)
        if not asset_id:
            return False
        
        asset_id = asset_id[0][0]
        maintenance_id = "MTN" + shortuuid.ShortUUID().random(length=4)
        dt = datetime.now()
        start_date = dt.strftime(AppConfig.DATE_FORMAT)

        tuple1 = (user_id,issue_id)
        tuple2 = (maintenance_id,asset_id,start_date)
        tuple3 = (asset_id,)
        self.obj_db_helper.save_maintenance_status(tuple1,tuple2,tuple3)