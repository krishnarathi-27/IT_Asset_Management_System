import logging
import shortuuid
from mysql.connector import IntegrityError, Error

# local imports
from database.database import db as db_object
from config.queries import Queries
from config.log_prompts.logs_config import LogsConfig
from utils.exceptions import DataNotExists, DataAlreadyExists, DBException

logger = logging.getLogger('vendor_handler')

class VendorHandler:
    """
    Class containinig methods to create and view both category and vendor
    """
    def view_all_vendor(self) -> list:
        try:
            data = db_object.fetch_data(Queries.FETCH_VENDOR_TABLE)

            if data:
                return data
            
            raise DataNotExists(404, 'Resource not found', 'Vendor not exists to deactivate')
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
    
    def deactivate_vendor(self, vendor_id: str) -> bool:

        try:
            data = db_object.fetch_data(Queries.FETCH_VENDOR_BY_ID, (vendor_id,))
           
            if not data:
                raise DataNotExists(404, 'Resource not found', 'Vendor not exists to deactivate')

            db_object.save_data(Queries.UPDATE_VENDOR_ACTIVE_STATUS, (vendor_id,))
            logger.info(LogsConfig.LOG_VENDOR_DEACTIVATED)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")

    def create_vendor(self,vendor_name: str, vendor_email: str) -> None:    

        try:
            vendor_id = "VEN" + shortuuid.ShortUUID().random(length=4)
            db_object.save_data(
                        Queries.INSERT_VENDOR_DETAILS,
                        (vendor_id,vendor_name,vendor_email,))
            
            logging.info(LogsConfig.LOG_VENDOR_ADDED)
            return vendor_id

        except IntegrityError as err:
            logger.error(f"Integrity error raised while creating vendor {err}")
            raise DataAlreadyExists(409, 'Conflict', 'Vendor already exists in database')

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, "Internal server error", "Server not responding. Try again after some time")
        