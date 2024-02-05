import logging
from mysql.connector import Error

from database.database import Database
from config.queries import Queries
from config.prompts.prompts import PromptConfig
from utils.exceptions import DataNotExists, DBException, InvalidCredentials

logger = logging.getLogger('common_helper')

db_object = Database()

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
    
def verify_user_password(user_id: str,password: str, obj_hash_password):
    """Function to verify user password is correct or not"""
    logger.info('Verifying user password')

    try:
        user_data = db_object.fetch_data(Queries.FETCH_PASSWORD,(user_id,))

        old_password_hashed = obj_hash_password.secure_password(password)

        if user_data[0]['password'] != old_password_hashed:
            raise InvalidCredentials(401, PromptConfig.UNAUTHORISED, PromptConfig.INVALID_CREDENTIALS_ENTERED)
        
        return user_data[0]['role']
    
    except Error as err:
        logger.warning(f"Error occured in mysql database {err}") 
        raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
