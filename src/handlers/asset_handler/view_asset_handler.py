import logging
import pymysql

from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DBException

logger = logging.getLogger("view_asset_handler")

class ViewAssetHandler:
    """Class Containing buisness logic to fetch assets from database"""
     
    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def view_all_asset(self) -> list:
        """Method to fetch assets from database"""
        logger.info('Fetching assets from database')

        try: 
            data = self.db_object.fetch_data(Queries.FETCH_ASSETS_TABLE)
            return data
            
        except pymysql.Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        