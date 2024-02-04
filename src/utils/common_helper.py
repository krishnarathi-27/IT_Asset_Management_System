import logging
from mysql.connector import Error

from database.database import db as db_object
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataNotExists, DBException

logger = logging.getLogger('common_helper')

def fetch_vendor_details(vendor_email: str) -> str:
    """Function for fetching vendor details from database"""
    logger.info('Fetching vendor details from database')

    try:
        vendor_id = db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, 
                                                (vendor_email,))
        if not vendor_id:
            raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)
        
        return vendor_id[0]['vendor_id']
    
    except Error as err:
        logger.error(f"Error occured in mysql database {err}") 
        raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)

def fetch_category_details(category_name: str, brand_name: str) -> str:
    """Function for fetching category details from database"""
    logger.info('Fetching category details from database')

    try:
        category_id = db_object.fetch_data(Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME, 
                                                (category_name,brand_name,))

        if not category_id:
            raise DataNotExists(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.CATEGORY_NOT_EXISTS)
        
        return category_id[0]['category_id']
    
    except Error as err:
        logger.error(f"Error occured in mysql database {err}") 
        raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    