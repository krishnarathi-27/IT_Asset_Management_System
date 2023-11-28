import logging
import shortuuid
#local imports
from config.queries_config.queries_config import ConfigQueries
from config.prompts_config.prompts_config import PromptsConfig
from config.statements.statements import StatementsConfig
from database.database_helper import db
from utils.helper_functions import HelperFunctions
from utils.validators.type_id_validations import TypeIdValidations
from config.logs_config.log_statements import LogStatements

logger = logging.getLogger('asset_operation')

class AssetOperation:
    '''Class to perform all the admin related operation'''

    def view_assets_details(self) -> None:
        result = db.display_data(
                    ConfigQueries.fetch_assets_table,
                    ConfigQueries.schema_asset_table
                )
        if result == False:
            return
    
    def add_asset(self) -> None:
        '''Method to add asset in the inventory'''
        asset_id = "ASN" + shortuuid.ShortUUID().random(length=4)       
        result = db.display_data(
                    ConfigQueries.fetch_mapping_id, 
                    ConfigQueries.schema_mapping_category_vendor_table
                )
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        mapping_id = TypeIdValidations.input_mapping_id()
        mapping_exists = db.fetch_data(
                            ConfigQueries.fetch_if_mapping_id_exists,
                            (mapping_id,)
                        )
        if len(mapping_exists) == 0:
            print(StatementsConfig.mapping_id_not_exists)
            return        
        asset_type_choice = int(input(PromptsConfig.asset_assignable_prompt))
        purchased_date = TypeIdValidations.input_date()    
        try:
            if asset_type_choice == 1:
                new_tuple = (asset_id,mapping_id,StatementsConfig.assignable_asset_type,purchased_date)
            elif asset_type_choice == 2:
                new_tuple = (asset_id,mapping_id,StatementsConfig.unassignable_asset_type,purchased_date)
            else:
                print(StatementsConfig.invalid_input)
        except ValueError:
            print(StatementsConfig.invalid_input)
        db.save_data(
            ConfigQueries.insert_asset_details,
            new_tuple
        )
        print(StatementsConfig.asset_added_success)
        logging.info(LogStatements.asset_added)

    def assign_asset(self) -> None:
        '''Method to assign asset to user'''
        print(StatementsConfig.assign_asset_statement)       
        result = db.display_data(
                    ConfigQueries.fetch_assignable_assets, 
                    ConfigQueries.schema_assignable_asset_details
                )  
        if result == False:
            return
        data = db.fetch_data(
                    ConfigQueries.fetch_assignable_assets_to_assign
                )
        if len(data) == 0:
            return   
        print(StatementsConfig.select_from_table) 
        asset_id = TypeIdValidations.input_asset_id()
        if not HelperFunctions.is_asset(asset_id):
            return       
        result = db.display_data(
                    ConfigQueries.fetch_authentication_table,
                    ConfigQueries.schema_user_table
                )
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        user_id = TypeIdValidations.input_user_id()
        if not HelperFunctions.is_user(user_id):
            return       
        db.save_data(
            ConfigQueries.update_asset_status,
            (user_id,StatementsConfig.unavailable_status,asset_id,)
        )
        print(StatementsConfig.asset_assign_success)
        logging.info(LogStatements.asigned_assets)
    
    def unassign_asset(self) -> None:
        '''Method to unassign asset from user'''
        print(StatementsConfig.unassign_asset_statement)
        result = db.display_data(
                    ConfigQueries.fetch_assigned_assets_to_unassign ,
                    ConfigQueries.schema_asset_table
                )
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        asset_id = TypeIdValidations.input_asset_id()
        if not HelperFunctions.is_asset(asset_id):
            return
        db.save_data(
            ConfigQueries.update_asset_status,
            (StatementsConfig.asset_location,StatementsConfig.available_status,asset_id,)
        )
        print(StatementsConfig.unassign_asset_success)
        logging.info(LogStatements.unassigned_asset)
