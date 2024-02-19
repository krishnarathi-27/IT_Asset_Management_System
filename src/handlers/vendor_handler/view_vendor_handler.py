import pymysql
from flask import current_app as app

# local imports
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import DBException

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
        
        except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
