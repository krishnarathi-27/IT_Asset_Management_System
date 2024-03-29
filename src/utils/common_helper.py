import shortuuid
import random
import re
import string
import pymysql
from flask import current_app as app

from src.database.database import Database
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.exceptions import ApplicationException, DBException


db_object = Database()

def fetch_vendor_details(vendor_email: str) -> str:
    """Function for fetching vendor details from database"""
    app.logger.info('Fetching vendor details from database')

    try:
        vendor_id = db_object.fetch_data(Queries.FETCH_VENDOR_BY_EMAIL, 
                                                (vendor_email,))
        if not vendor_id:
            raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.VENDOR_NOT_EXISTS)
        
        return vendor_id[0]['vendor_id']
    
    except pymysql.Error as err:
        app.logger.error(f"Error occured in mysql database {err}") 
        raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)

def fetch_category_details(category_name: str, brand_name: str) -> str:
    """Function for fetching category details from database"""
    app.logger.info('Fetching category details from database')

    try:
        category_id = db_object.fetch_data(Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME, 
                                                (category_name,brand_name,))

        if not category_id:
            raise ApplicationException(404, PromptConfig.RESOURCE_NOT_FOUND, PromptConfig.CATEGORY_NOT_EXISTS)
        
        return category_id[0]['category_id']
    
    except pymysql.Error as err:
        app.logger.error(f"Error occured in mysql database {err}") 
        raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
def verify_user_password(password: str,input_password: str ,password_type: str, obj_hash_password):
    """Function to verify user password is correct or not"""
    app.logger.info('Verifying user password')

    try:

        if password_type == 'false':
            return password == input_password
        
        old_password_hashed = obj_hash_password.secure_password(input_password)

        return password == old_password_hashed
    
    except pymysql.Error as err:
        app.logger.warning(f"Error occured in mysql database {err}") 
        raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
    
def generate_password():
    'Generate a random password using string combinations'

    characters = string.ascii_letters + string.digits + '@#$&'
    password = ''.join(random.choice(characters) for _ in range(6))
    return password

def regex_validation(regex_pattern, user_input):

    result = re.match(regex_pattern, user_input)
    
    if result is None:
        app.logger.info('Regex validation failed for user input')
        return False
    
    return True

def generate_shortuuid(prefix: str) -> str:
    id = prefix + shortuuid.ShortUUID().random(length=5)
    return id