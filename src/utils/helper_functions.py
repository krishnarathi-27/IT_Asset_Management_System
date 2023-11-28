import logging
from config.statements.statements import StatementsConfig
from config.logs_config.log_statements import LogStatements
from config.prompts_config.prompts_config import PromptsConfig
from database.database_helper import db
from config.queries_config.queries_config import ConfigQueries
from config.statements.statements import StatementsConfig

logger = logging.getLogger('helper_functions')

def config_loader(func):  
    '''Loads all configuration file'''
    def wrapper():
        try:
            LogStatements.load()
            PromptsConfig.load()
            StatementsConfig.load()
            ConfigQueries.load()      
            db.create_all_tables()
            func()
        except Exception as err:
            print(StatementsConfig.exception_message)
            logger.error(err)
    return wrapper

class HelperFunctions:    
    '''Class of helper functions used throughout the code'''

    @staticmethod
    def is_category(category_id: str) -> bool:
        '''Method to check if categry id exists'''
        category_exists = db.fetch_data(
                            ConfigQueries.fetch_if_category_exists, 
                            (category_id,)
                        )
        if category_exists:
            return True
        print(StatementsConfig.category_id_not_exists)
        return False
    
    @staticmethod
    def is_asset(asset_id: str) -> bool:
        '''Method to check if asset id exists'''
        asset_exists = db.fetch_data(
                            ConfigQueries.fetch_if_asset_exists,
                            (asset_id,)
                        )
        if asset_exists:
            return True
        print(StatementsConfig.assetid_not_exists)
        return False
    
    @staticmethod
    def is_user(user_id: str) -> bool:
        '''Method to check if category id exists'''
        user_exists = db.fetch_data(
                        ConfigQueries.fetch_if_user_exists,
                        (user_id,)
                    )
        if user_exists:
            return True
        print(StatementsConfig.user_not_exists)
        return False
    
    @staticmethod
    def is_vendor(vendor_email: str) -> bool:
        '''Method to check if vendor email exists'''
        vendor_exists = db.fetch_data(
                            ConfigQueries.fetch_vendor_by_email,
                            (vendor_email,)
                        )
        if vendor_exists:
            print(StatementsConfig.vendor_not_exists)
            return True       
        return False
