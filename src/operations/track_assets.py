import logging
import sqlite3
from os import system
from config.queries_config.queries_config import ConfigQueries
from config.prompts_config.prompts_config import PromptsConfig
from config.statements.statements import StatementsConfig
from database.database_helper import db
from utils.helper_functions import HelperFunctions
from utils.validators.type_id_validations import TypeIdValidations
from utils.validators.user_details_validations import UserDetailsValidations

logger = logging.getLogger('track_assets')

class TrackAssets:
    
    '''Class to track assets'''
    @property
    def fetch_by_username(self) -> None:
        '''Method to track asset by user id'''
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
        result = db.display_data(
                    ConfigQueries.fetch_assets_by_user_id,
                    ConfigQueries.schema_assets_by_user_id,
                    (user_id,)
                )
        if result == False:
            return

    @property
    def fetch_by_category(self) -> None:
        '''Method to track asset by category id'''       
        result = db.display_data(
                    ConfigQueries.fetch_category_table, 
                    ConfigQueries.schema_category_details_table
                )
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        category_id = TypeIdValidations.input_category_id()
        if not HelperFunctions.is_category(category_id):
            return
        result = db.display_data(
                    ConfigQueries.fetch_assets_by_category_id, 
                    ConfigQueries.schema_assets_by_category_id,
                    (category_id,)
                )
        if result == False:
            return

    @property
    def fetch_by_vendor(self) -> None:
        '''Method to track asset by vendor email'''
        result = db.display_data(
                    ConfigQueries.fetch_vendor_table,
                    ConfigQueries.schema_vendor_table
                )
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        vendor_email = UserDetailsValidations.input_email()
        if not HelperFunctions.is_vendor(vendor_email):
            return
        result = db.display_data(
                    ConfigQueries.fetch_assets_by_vendor_email,
                    ConfigQueries.schema_assets_by_vendoremail, 
                    (vendor_email,)
                )
        if result == False:
            return

    def menu_options(self) -> None:
        '''Method to show menu option of tracking assets'''
        while True:
            try:
                user_input = int(input(PromptsConfig.track_assets_prompt))
                match user_input:
                    case 1:
                        self.fetch_by_username
                    case 2:
                        self.fetch_by_category
                    case 3:
                        self.fetch_by_vendor
                    case 4:
                        result = db.display_data(
                                    ConfigQueries.fetch_assets_available,
                                    ConfigQueries.schema_asset_table
                                )
                        if result == False:
                            return
                    case 5:
                        result = db.display_data(
                                ConfigQueries.fetch_assets_under_maintenance,
                                ConfigQueries.schema_asset_table
                            )
                        if result == False:
                            return
                    case 6:
                        return
                    case _:
                        print(StatementsConfig.invalid_input)
                        logging.debug(ValueError)

            except sqlite3.Error as err:
                print(StatementsConfig.exception_message)
                logger.error(err)
            except ValueError:
                print(StatementsConfig.invalid_input)   
                logging.debug(ValueError)
            if input("Press any key to continue....\n"):
                system('cls')  
                