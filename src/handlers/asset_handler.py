import logging
import shortuuid
from mysql.connector import Error

from config.queries import Queries
from database.database import db as db_object
from config.log_prompts.logs_config import LogsConfig
from config.app_config import AppConfig
from utils.exceptions import DataNotExists, DBException

logger = logging.getLogger("asset_handler")

class AssetHandler:
     
    def view_all_asset(self) -> list:
        try: 
            data = db_object.fetch_data(Queries.FETCH_ASSETS_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, 'Resource not found', 'No assets available in inventory')
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")

    def create_asset(self, category_name, vendor_email, brand_name, asset_type) -> None:
        try:
            asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)

            vendor_id = db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, 
                                             (vendor_email,))
            if not vendor_id:
                raise DataNotExists(404, "Resource not found", "Vendor not exists in database")
            
            category_id = db_object.fetch_data(Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME, 
                                               (category_name,brand_name,))

            if not category_id:
                raise DataNotExists(404, "Resource not found", "Category not exists in database")    

            mapping_id = db_object.fetch_data(Queries.FETCH_MAPPING_ID, 
                                                (category_id[0]['category_id'], vendor_id[0]['vendor_id'],))

            db_object.save_data(
                Queries.INSERY_ASSET_DETAILS,
                (asset_id, mapping_id[0]['mapping_id'], asset_type,)
            )
            logger.info(LogsConfig.LOG_ASSET_ADDED_INVENTORY)
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        
    def assign_asset(self,asset_id, employee_id):
       try:
            data_asset_id = db_object.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

            if not data_asset_id:
                raise DataNotExists(404, "Resource not found", "Asset id not exists")

            data_user_id = db_object.fetch_data(Queries.FETCH_IF_USER_EXISTS, (employee_id,))

            if not data_user_id:
                raise DataNotExists(404, "Resource not found", "Employee id not exists")

            db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                (employee_id,AppConfig.UNAVAILABLE_STATUS,asset_id,)
            )
       
       except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
       
    def unassign_asset(self,asset_id):
       try:
            data_asset_id = db_object.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

            if not data_asset_id:
                raise DataNotExists(404, "Resource not found", "Asset id not exists")

            db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                                    (AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,asset_id,))
       
       except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        