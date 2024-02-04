import logging
import shortuuid
from mysql.connector import Error

from config.queries import Queries
from utils.common_helper import fetch_category_details, fetch_vendor_details
from config.prompts.prompts import PromptConfig
from utils.exceptions import DBException

logger = logging.getLogger("create_asset_handler")

class CreateAssetHandler:
    """Class containing business logic to create new asset in database"""
     
    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def create_asset(self, category_name: str, vendor_email: str, brand_name: str, asset_type: str) -> str:
        """Method for creating new assets in database"""
        logger.info('Creating new assets in inventory')

        try:
            asset_id = PromptConfig.ASSET_ID_PREFIX + shortuuid.ShortUUID().random(length=4)

            vendor_id = fetch_vendor_details(vendor_email)
            category_id = fetch_category_details(category_name, brand_name)   

            mapping_id = self.db_object.fetch_data(Queries.FETCH_MAPPING_ID, 
                                                (category_id, vendor_id,))

            self.db_object.save_data(
                Queries.INSERY_ASSET_DETAILS,
                (asset_id, mapping_id[0]['mapping_id'], asset_type,)
            )
            logger.info("Asset added in inventory")
            return asset_id
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        