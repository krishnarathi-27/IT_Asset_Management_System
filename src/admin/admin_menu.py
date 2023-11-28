import logging
from os import system
#local imports
from config.logs_config.log_statements import LogStatements
from config.prompts_config.prompts_config import PromptsConfig
from config.queries_config.queries_config import ConfigQueries
from config.statements.statements import StatementsConfig
from operations.track_assets import TrackAssets
from operations.vendor_operations import VendorOperations
from operations.category_operations import CategoryOperations
from utils.helper_functions import HelperFunctions
from database.database_helper import db
from utils.validators.user_details_validations import UserDetailsValidations
from admin.admin_actions import AdminActions

logger = logging.getLogger('admin_menu')

class AdminMenu(VendorOperations,CategoryOperations ):
    '''Class to perform admin menu operation'''
    
    def __init__(self) -> None:
        '''Initialises all objects'''
        logging.info(LogStatements.log_admin_logged_in)
        print(StatementsConfig.welcome_admin)
        self.admin_action_obj = AdminActions()
        self.vendor_obj = VendorOperations()
        self.category_obj = CategoryOperations()
        self.track_asset_obj = TrackAssets()

    def deactivate_vendor(self) -> None:
        '''deactivates or deletes the vendor existing'''
        result = db.display_data(
                    ConfigQueries.fetch_vendor_table,
                    ConfigQueries.schema_vendor_table
                )
        if result == False:
            return
        print(StatementsConfig.select_from_table)
        vendor_email = UserDetailsValidations.input_email()
        if not HelperFunctions.is_vendor(vendor_email):
            print(StatementsConfig.vendor_not_exist_to_delete)
            return
        db.save_data(
            ConfigQueries.delete_vendor_details,
            (vendor_email,)
        )
        print(StatementsConfig.deleted_vendor)
        logging.info(LogStatements.log_vendor_deactivated)

    def admin_operations(self) -> None:
        '''Menu options for admin'''
        while True:
                user_choice = input("\n" + PromptsConfig.admin_prompt)
                system('cls')
                if user_choice == "1" :
                    self.admin_action_obj.view_user_details()
                elif user_choice == "2" :
                    self.admin_action_obj.create_new_user()
                elif user_choice == "3" :
                    self.admin_action_obj.delete_user()
                elif user_choice == "4" :
                    self.vendor_obj.view_vendors()
                elif user_choice == "5" :
                    self.deactivate_vendor()
                elif user_choice == "6" :
                    self.vendor_obj.create_vendor()
                elif user_choice == "7" :
                    self.category_obj.view_category_details()
                elif user_choice == "8" :
                    self.category_obj.create_category()
                elif user_choice == "9" : 
                    self.track_asset_obj.menu_options()
                elif user_choice == "10" :
                    return
                else :
                    print(StatementsConfig.invalid_input + "\n")             
