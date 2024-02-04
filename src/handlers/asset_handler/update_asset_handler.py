import logging
from mysql.connector import Error

from config.app_config import AppConfig
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataNotExists, DBException

logger = logging.getLogger("update_asset_handler")

class UpdateAssetHandler:
    """Class containing business logic to update existing asset in database"""
     
    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def fetch_asset_exists(self, asset_id: str) -> str:
        """Method to fetch if asset exists or not"""
        logger.info('Fetching asset exists or not')

        mapping_id = self.db_object.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,))

        if not mapping_id:
            raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_ID_NOT_EXISTS)

        return mapping_id[0]['mapping_id']

    def assign_asset(self,asset_id: str, employee_id: str) -> None:
       """Method to assign asset to user"""
       logger.info('Assigning asset to user')

       try:
            mapping_id = self.fetch_asset_exists(asset_id)

            data_user_id = self.db_object.fetch_data(Queries.FETCH_IF_USER_EXISTS, (employee_id,))

            if not data_user_id:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.USER_NOT_EXISTS)

            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                (mapping_id, employee_id,AppConfig.UNAVAILABLE_STATUS,
                AppConfig.ASSIGNABLE_ASSET_TYPE,asset_id,)
            )
       
       except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
       
    def unassign_asset(self,asset_id: str) -> str:
       """Method to unassign asset from user"""
       logger.info('Method to unassign asset from user')

       try:
            mapping_id = self.fetch_asset_exists(asset_id)

            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                (mapping_id, AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,
                AppConfig.ASSIGNABLE_ASSET_TYPE,asset_id,)
            )
       
       except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
       