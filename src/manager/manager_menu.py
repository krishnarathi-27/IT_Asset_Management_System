import logging
import sqlite3
from os import system
#local imports
from config.queries_config.queries_config import ConfigQueries
from config.prompts_config.prompts_config import PromptsConfig
from config.statements.statements import StatementsConfig
from config.logs_config.log_statements import LogStatements
from database.database_helper import db
from operations.vendor_operations import VendorOperations
from operations.category_operations import CategoryOperations
from operations.track_assets import TrackAssets
from manager.asset_operations import AssetOperation
from manager.maintenance import Maintenance

logger = logging.getLogger('manager_menu')

class ManagerMenu(VendorOperations, CategoryOperations):
    '''Class for manager operations'''

    def __init__(self,user_id: str) -> None:
        logging.info(LogStatements.manager_logged_in)
        print(StatementsConfig.welcome_manager)
        self.user_id = user_id
        self.asset_obj = AssetOperation()
        self.track_asset_obj = TrackAssets()
        self.resolve_issue_obj = Maintenance(self.user_id)

    def manager_operations(self) -> None:
        '''Method to perform menu operations of manager'''    
        while True:
            user_choice = int(input(PromptsConfig.manager_prompt))
            if user_choice == "1" :
                result = db.display_data(
                            ConfigQueries.fetch_authentication_table,
                            ConfigQueries.schema_user_table
                        )
                if result == False:
                    return
            elif user_choice == "2" :
                self.view_vendors()
            elif user_choice == "3" :
                self.create_vendor()
            elif user_choice == "4" :
                self.view_category_details()
            elif user_choice == "5" :
                self.create_category()
            elif user_choice == "6" :
                self.asset_obj.add_asset()
            elif user_choice == "7" :
                self.asset_obj.view_assets_details()
            elif user_choice == "8" :
                self.asset_obj.assign_asset()
            elif user_choice == "9" : 
                self.asset_obj.unassign_asset()
            elif user_choice == "10":
                self.track_asset_obj.menu_options()
            elif user_choice == "11":
                self.resolve_issue_obj.menu_operation()
            elif user_choice == "12":
                return
            else :
                print(StatementsConfig.invalid_input)
                logger.debug(ValueError)
            if input("Press any key to continue....\n"):
                system('cls')
                