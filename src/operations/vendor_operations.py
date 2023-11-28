import logging
import shortuuid
from config.queries_config.queries_config import ConfigQueries
from config.statements.statements import StatementsConfig
from config.logs_config.log_statements import LogStatements
from database.database_helper import db
from utils.helper_functions import HelperFunctions
from utils.validators.user_details_validations import UserDetailsValidations

logger = logging.getLogger('vendor_operations')

class VendorOperations:
    '''Class to perform vendor operations'''

    def create_vendor(self) -> None:
        '''Method to create new vendor'''
        vendor_id = "VEN" + shortuuid.ShortUUID().random(length=4)         
        vendor_email = UserDetailsValidations.input_email()     
        if HelperFunctions.is_vendor(vendor_email):
            print(StatementsConfig.vendor_not_exists)
            return   
        vendor_name = input(StatementsConfig.input_vendor_name).strip().lower()
        new_tuple = (vendor_id,vendor_name,vendor_email)
        db.save_data(
            ConfigQueries.insert_vendor_details,
            new_tuple
        )
        print(StatementsConfig.vendor_added)
        logging.info(LogStatements.vendor_added)
    
    def view_vendors(self) -> None:
        '''Method to view vendor details'''
        result = db.display_data(
                    ConfigQueries.fetch_vendor_table,
                    ConfigQueries.schema_vendor_table
                )
        if result == False:
            return
  