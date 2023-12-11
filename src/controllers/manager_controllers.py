"""Module having buisness logic of manager functionalities"""
import logging
import shortuuid
from datetime import datetime
from models.database import db
from config.queries import Queries
from config.app_config import AppConfig
from config.log_prompts.logs_config import LogsConfig

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
    def fetch_by_username(self,user_id) -> bool:
        data_user = data = db.fetch_data(
                        Queries.FETCH_IF_USER_EXISTS,
                        (user_id,))
        if not data_user:
            return data_user    
        data = db.fetch_data(
                    Queries.FETCH_ASSETS_BY_USER_ID,
                    (user_id,))
        if not data:
            return data
        return data
    
    def fetch_by_category(self,category_id) -> bool:
        data = db.fetch_data(
                            Queries.FETCH_ASSETS_BY_CATEGORY_ID,
                            (category_id,))
        return data
    
    def fetch_by_vendor(self,vendor_email) -> bool:
        data = db.fetch_data(
                            Queries.FETCH_ASSETS_BY_VENDOR_EMAIL,
                            (vendor_email,))
        return data

    def fetch_asset_available(self) -> bool:
        data = db.fetch_data(
                Queries.FETCH_ASSETS_AVAILABLE)
        return data
    
    def fetch_asset_maintenance(self) -> bool:
        data = db.fetch_data(
                Queries.FETCH_ASSETS_UNDER_MAINTENANCE)
        return data
    
    def view_pending_issues(self) -> bool:
        data = db.fetch_data(
                Queries.FETCH_ISSUES_PENDING)
        return data
    
    def send_asset(self,issue_id, user_id) -> bool:
        asset_id = db.fetch_data(
                        Queries.FETCH_ASSET_ID_BY_ISSUE_ID,
                        (issue_id,))
        if not asset_id:
            return False
        
        asset_id = asset_id[0][0]
        maintenance_id = "MTN" + shortuuid.ShortUUID().random(length=4)
        dt = datetime.now()
        start_date = dt.strftime(AppConfig.DATE_FORMAT)

        db.save_data([
                Queries.UPDATE_ISSUE_STATUS_UNDER_MAINTENANCE,
                Queries.INSERT_IN_MAINTENANCE_TABLE,
                Queries.UPDATE_ASSET_STATUS_UNDER_MAINTENANCE],
                [(user_id,issue_id,), (maintenance_id,asset_id,start_date,), (asset_id,)]
        )
        return True

    def recieve_asset(self,maintenance_id: str) -> bool:
        asset_id = db.fetch_data(
                        Queries.FETCH_ASSET_ID_BY_MAINTENANCE_TABLE,
                        (maintenance_id,))
        if not asset_id:
            return False
        
        asset_id = asset_id[0][0]
        dt = datetime.now()
        return_date = dt.strftime(AppConfig.DATE_FORMAT)

        db.save_data([
            Queries.UPDATE_MAINTENANCE_RETURN_DATE,
            Queries.UPDATE_ASSET_STATUS_AGAIN_TO_AVAILABLE
        ],
        [(return_date,maintenance_id,),(asset_id,)]
        )
        return True
    
    def display_maintenance_table(self) -> None:
        data = data = db.fetch_data(
            Queries.FETCH_MAINTENANCE_TABLE)
        return data
        