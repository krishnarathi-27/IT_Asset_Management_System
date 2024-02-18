import logging
import pymysql

# local imports
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException

logger = logging.getLogger('delete_vendor_handler')

class DeleteVendorHandler:
    """Class containinig methods to deactivate vendor from database"""

    def __init__(self, db_object) -> None:
        self.db_object = db_object

    def deactivate_vendor(self, vendor_id: str) -> bool:
        """Method deactivating vendor that are active in database"""
        logger.info('Deactivating vendor from database')
        
        try:
            data = self.db_object.fetch_data(Queries.FETCH_VENDOR_BY_ID, (vendor_id,))
           
            if not data:
                raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)

            self.db_object.save_data(Queries.UPDATE_VENDOR_ACTIVE_STATUS, (vendor_id,))
            logger.info("Vendor deactivated successfully from database")
        
        except pymysql.Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500,PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        