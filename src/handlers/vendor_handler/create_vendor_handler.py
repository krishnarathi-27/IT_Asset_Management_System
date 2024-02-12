import logging
import shortuuid
from mysql.connector import IntegrityError, Error

# local imports
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException

logger = logging.getLogger('create_vendor_handler')

class CreateVendorHandler:
    """ Class containinig methods to create new vendor"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def create_vendor(self,vendor_name: str, vendor_email: str) -> str:    
        """Method to create vendor if vendor not exists already in database"""
        logger.info('Creating new vendor in database')

        try:
            vendor_id = PromptConfig.VENDOR_ID_PREFIX + shortuuid.ShortUUID().random(length=4)
            self.db_object.save_data(
                        Queries.INSERT_VENDOR_DETAILS,
                        (vendor_id,vendor_name,vendor_email,))
            
            logging.info("New vendor added in database")
            return vendor_id

        except IntegrityError as err:
            logger.error(f"Integrity error raised while creating vendor {err}")
            raise ApplicationException(409, PromptConfig.CONFLICT_MSG, PromptConfig.VENDOR_ALREADY_EXISTS)

        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        