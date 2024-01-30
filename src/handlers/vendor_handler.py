import logging
import shortuuid
from mysql.connector import IntegrityError, Error

# local imports
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataNotExists, DataAlreadyExists, DBException

logger = logging.getLogger('vendor_handler')

class VendorHandler:
    """
    Class containinig methods to create and view both category and vendor
    """
    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def view_all_vendor(self) -> list:
        try:
            data = self.db_object.fetch_data(Queries.FETCH_VENDOR_TABLE)

            if data:
                return data
            
            raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
    def deactivate_vendor(self, vendor_id: str) -> bool:

        try:
            data = self.db_object.fetch_data(Queries.FETCH_VENDOR_BY_ID, (vendor_id,))
           
            if not data:
                raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)

            self.db_object.save_data(Queries.UPDATE_VENDOR_ACTIVE_STATUS, (vendor_id,))
            logger.info("Vendor deactivated successfully from database")
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)

    def create_vendor(self,vendor_name: str, vendor_email: str) -> None:    

        try:
            vendor_id = PromptConfig.VENDOR_ID_PREFIX + shortuuid.ShortUUID().random(length=4)
            self.db_object.save_data(
                        Queries.INSERT_VENDOR_DETAILS,
                        (vendor_id,vendor_name,vendor_email,))
            
            logging.info("New vendor added in database")
            return vendor_id

        except IntegrityError as err:
            logger.error(f"Integrity error raised while creating vendor {err}")
            raise DataAlreadyExists(409, PromptConfig.CONFLICT_MSG, PromptConfig.VENDOR_ALREADY_EXISTS)

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        