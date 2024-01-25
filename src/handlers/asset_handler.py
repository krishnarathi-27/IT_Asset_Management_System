import logging
import shortuuid
from mysql.connector import IntegrityError, Error

from config.queries import Queries
from database.database import db as db_object
from config.log_prompts.logs_config import LogsConfig
from utils.exceptions import DataAlreadyExists, DataNotExists, CustomException, DBException, InvalidCredentials

logger = logging.getLogger("asset_handler")

class AssetHandler:
     
    def view_all_asset(self) -> list:
        try: 
            data = db_object.fetch_data(Queries.FETCH_ASSETS_TABLE)
            if data:
                return data
            else:
                raise DataNotExists(404, 'Resource not found', 'Vendor not exists to deactivate')
            
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        
    def create_new_asset(category_name, vendor_email, asset_type) :
        pass

    def create_asset(self) -> None:
        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)
        data = db_object.fetch_data(Queries.FETCH_IF_MAPPING_ID_EXISTS, (mapping_id,))

        if not data:
            return False

        else:
            db_object.save_data(
                Queries.INSERY_ASSET_DETAILS,
                (asset_id, mapping_id, asset_type, purchased_date),
            )
            logger.info(LogsConfig.LOG_ASSET_ADDED_INVENTORY)
            return True
        
    def fetch_mapping_id(self, category_name, vendor_email):
        data = db_object.fetch_data()