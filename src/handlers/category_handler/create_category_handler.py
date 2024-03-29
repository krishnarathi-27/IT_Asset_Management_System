import shortuuid
import pymysql
from flask import current_app as app

# local imports
from src.config.queries import Queries
from src.config.prompts.prompts import PromptConfig
from src.utils.common_helper import fetch_vendor_details
from src.utils.exceptions import DBException, ApplicationException

class CreateCategoryHandler:
    """
    Class containinig methods to create and view both category and vendor
    """
    def __init__(self, db_object) -> None:
        self.db_object = db_object
    
    def check_category_with_same_vendor(self, mapping_id: str, category_id: str, vendor_id: str) -> None:
        """Method to check if category with same vendor exists"""
        app.logger.info('Checking with catgeory of same vendor exists or not')

        mapping_data = self.db_object.fetch_data(
                            Queries.FETCH_FROM_MAPPING_TABLE,
                            (category_id,vendor_id,))

        if not mapping_data:
            self.db_object.save_data(
                Queries.INSERT_MAPPING_DETAILS,
                (mapping_id,category_id, vendor_id,))
            
            app.logger.info("New category created in database")

        else:
            raise pymysql.IntegrityError

    def check_category(self, category_id: str,vendor_id: str, category_name: str, brand_name: str) -> None:
        """Method to check if category with same brand exists or not"""
        app.logger.info('Method to check if category with same brand exists')

        category_details = self.db_object.fetch_data(Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME, 
                                                (category_name,brand_name,))
        
        mapping_id = PromptConfig.MAPPING_ID_PREFIX + shortuuid.ShortUUID().random(length=4)
        
        if not category_details:
            self.db_object.save_data(Queries.INSERT_CATEGORY_DETAILS,(category_id, category_name,brand_name,))
            self.db_object.save_data(Queries.INSERT_MAPPING_DETAILS,(mapping_id,category_id,vendor_id,))

        else:
            category_id = category_details[0]['category_id']
            return self.check_category_with_same_vendor(mapping_id, category_id, vendor_id)

    def create_category(self,category_name: str, brand_name: str, vendor_email: str) -> bool:
        """Method to create new category in database"""
        app.logger.info('Method to create new category in database')

        try:
            vendor_id = fetch_vendor_details(vendor_email)
            category_id = PromptConfig.CATEGORY_ID_PREFIX + shortuuid.ShortUUID().random(length=4)
            self.check_category(category_id, vendor_id, category_name, brand_name)
        
        except pymysql.IntegrityError as err:
            app.logger.error(f'Same category name already exits {err}')
            raise ApplicationException(409, PromptConfig.CONFLICT_MSG, PromptConfig.CATEGORY_ALREADY_EXISTS)
        
        except pymysql.Error as err:
            app.logger.error(f"Error occured in mysql database {err}") 
            raise DBException(500, PromptConfig.INTERNAL_SERVER_ERROR, PromptConfig.SERVER_ERROR)
        