import pymysql
from flask import current_app as app

from src.config.app_config import AppConfig
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import DBException, ApplicationException
from src.utils.common_helper import regex_validation

class UpdateAssetHandler:
    """Class containing business logic to update existing asset in database"""
     
    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def fetch_asset_exists(self, asset_id: str, asset_status: str) -> str:
        """Method to fetch if asset exists or not"""
        app.logger.info('Fetching asset exists or not')

        is_asset_under_maintenance = self.db_object.fetch_data(Queries.FETCH_ASSET_ID_UNDER_MAINTENANCE,(asset_id,))

        if is_asset_under_maintenance:
            raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_UNDER_MAINTENANCE_CANT_ASSIGN)

        mapping_id = self.db_object.fetch_data(Queries.FETCH_IF_ASSET_EXISTS, (asset_id,asset_status,))

        if not mapping_id:
            raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.ASSET_ID_NOT_EXISTS)

        return mapping_id[0]['mapping_id']

    def assign_asset(self,asset_id: str, employee_id: str) -> None:
       """Method to assign asset to user"""
       app.logger.info('Assigning asset to user')

       try:
            result = regex_validation(AppConfig.REGEX_ASSET_ID, asset_id)

            if not result:
                raise ApplicationException(422, PromptConfig.UNPROCESSIBLE_ENTITY, PromptConfig.INVALID_ASSET_ID)
            
            mapping_id = self.fetch_asset_exists(asset_id,AppConfig.AVAILABLE_STATUS)

            data_user_id = self.db_object.fetch_data(Queries.FETCH_IF_USER_EXISTS, (employee_id,))

            if not data_user_id:
                raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.USER_NOT_EXISTS)

            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                (mapping_id, employee_id,AppConfig.UNAVAILABLE_STATUS,
                AppConfig.ASSIGNABLE_ASSET_TYPE,asset_id,)
            )
       
       except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
       
    def unassign_asset(self,asset_id: str) -> str:
       """Method to unassign asset from user"""
       app.logger.info('Method to unassign asset from user')

       try:
            result = regex_validation(AppConfig.REGEX_ASSET_ID, asset_id)

            if not result:
                raise ApplicationException(422, PromptConfig.UNPROCESSIBLE_ENTITY, PromptConfig.INVALID_ASSET_ID)
            
            mapping_id = self.fetch_asset_exists(asset_id,AppConfig.UNAVAILABLE_STATUS)

            self.db_object.save_data(Queries.UPDATE_ASSET_STATUS,
                (mapping_id, AppConfig.ASSET_LOCATION,AppConfig.AVAILABLE_STATUS,
                AppConfig.ASSIGNABLE_ASSET_TYPE,asset_id,)
            )
       
       except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
       