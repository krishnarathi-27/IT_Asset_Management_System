import logging
import shortuuid
from mysql.connector import Error

# local imports
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import ApplicationException, DBException

logger = logging.getLogger('view_vendor_handler')

class ViewVendorHandler:
    """
    Class containinig methods to create and view both category and vendor
    """
    def __init__(self, db_object) -> None:
        self.db_object = db_object
        
    def view_all_vendor(self) -> list:
        try:
            data = self.db_object.fetch_data(Queries.FETCH_VENDOR_TABLE)
            return data
        
        except Error as err:
            logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
