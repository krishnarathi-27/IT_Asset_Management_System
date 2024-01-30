import logging
import shortuuid
from mysql.connector import Error

from config.queries import Queries
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from config.app_config import AppConfig
from utils.exceptions import DataNotExists, DBException

logger = logging.getLogger("asset_handler")

class AssetHandler:
     
    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def view_all_asset(self) -> list:
        try: 
            data = self.db_object.fetch_data(Queries.FETCH_ASSETS_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSETS_NOT_EXISTS)
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)

    def create_asset(self, category_name, vendor_email, brand_name, asset_type) -> None:
        try:
            asset_id = PromptConfig.ASSET_ID_PREFIX + shortuuid.ShortUUID().random(length=4)

            vendor_id = self.db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, 
                                             (vendor_email,))
            if not vendor_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)
            
            category_id = self.db_object.fetch_data(Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME, 
                                               (category_name,brand_name,))

            if not category_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.CATEGORY_NOT_EXISTS)    

            mapping_id = self.db_object.fetch_data(Queries.FETCH_MAPPING_ID, 
                                                (category_id[0][AppConfig.CATEGORY_ID], vendor_id[0][AppConfig.VENDOR_ID],))

            self.db_object.save_data(
                Queries.INSERY_ASSET_DETAILS,
                (asset_id, mapping_id[0][AppConfig.MAPPING_ID], asset_type,)
            )
            logger.info("Asset added in inventory")
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        
    def assign_asset(self,asset_id, employee_id):
       try:
            data_asset_id = self.db_object.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

            if not data_asset_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_ID_NOT_EXISTS)

            data_user_id = self.db_object.fetch_data(Queries.FETCH_IF_USER_EXISTS, (employee_id,))

            if not data_user_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.USER_NOT_EXISTS)

            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                (employee_id,AppConfig.UNAVAILABLE_STATUS,asset_id,)
            )
       
       except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
       
    def unassign_asset(self,asset_id):
       try:
            data_asset_id = self.db_object.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

            if not data_asset_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_ID_NOT_EXISTS)

            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                                    (AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,asset_id,))
       
       except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        