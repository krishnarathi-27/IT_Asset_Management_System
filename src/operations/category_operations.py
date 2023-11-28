import logging
import shortuuid
#local imports
from config.queries_config.queries_config import ConfigQueries
from config.statements.statements import StatementsConfig
from config.logs_config.log_statements import LogStatements
from database.database_helper import db
from utils.helper_functions import HelperFunctions
from utils.validators.user_details_validations import UserDetailsValidations

logger = logging.getLogger('category_operations')

class CategoryOperations:
    '''Class to perform category operations'''
 
    def category_vendor_exists(self,mapping_id: str,category_id: str, vendor_id: str) -> None:
        '''Method to check if catgeory with same vendor exists or not'''
        mapping_data = db.fetch_data(
                            ConfigQueries.fetch_from_mapping_table,
                            (category_id,vendor_id,)
                        )
        if len(mapping_data) == 0:
            db.save_data(
                ConfigQueries.insert_mapping_details,
                (mapping_id,category_id,vendor_id,)
            )
            logging.info(LogStatements.category_added)
            print(StatementsConfig.category_added)
        else:
            print(StatementsConfig.category_vendor_exists)

    def create_category(self) -> None:
        '''Method to create new category of assets'''
        category_id = "CAT" + shortuuid.ShortUUID().random(length=4) 
        category_name = input(StatementsConfig.enter_category_name).strip().lower()
        brand_name = input(StatementsConfig.enter_brand_name).strip().lower()
        vendor_email = UserDetailsValidations.input_email()
        vendor_id = db.fetch_data(
                        ConfigQueries.fetch_vendor_by_email,
                        (vendor_email,)
                    )      
        if not HelperFunctions.is_vendor(vendor_email):
            return
        vendor_id = vendor_id[0][0]
        category_exists = db.fetch_data(
                            ConfigQueries.fetch_by_category_and_brand_name,
                            (category_name,brand_name,)
                        )
        mapping_id = "MPN" + shortuuid.ShortUUID().random(length=4)
        if len(category_exists) == 0:
            new_tuple = (category_id,category_name,brand_name)
            db.save_data(
                ConfigQueries.insert_category_details,
                new_tuple
            )
            db.save_data(
                ConfigQueries.insert_mapping_details,
                (mapping_id,category_id,vendor_id)
            )
            print(StatementsConfig.category_added)
        else:
            category_id = category_exists[0][0]
            self.category_vendor_exists(mapping_id,category_id,vendor_id)

    def view_category_details(self) -> None:
        '''Method to view catgeory details'''
        result = db.display_data(
                    ConfigQueries.fetch_category_details,
                    ConfigQueries.schema_category_table
                )
        if result == False:
            return
