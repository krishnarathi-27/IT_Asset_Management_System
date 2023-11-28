"""Module for taking input from manager for various functionalities"""
import logging
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from controllers.asset_data_controller import AssetDataController

logger = logging.getLogger('manager_views')

class ManagerViews:
    """
        Class that contains menu options for taking input from manager to perform manager operations
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        user_id = user id of the user that logged in the system
        Methods
        -------
        manager_operations() -> containing loop for displaying manager menu
        manager_menu() -> contains menu options for taking input from manager
    """
    def __init__(self,user_id) -> None:
        logger.info(LogsConfig.LOG_MANAGER_LOGGED_IN)
        print(PromptConfig.WELCOME_MANAGER)
        self.user_id = user_id
        self.obj_common_helper = CommonHelper()
        self.asset_data_obj = AssetDataController()

    def manager_operations(self) -> None:
        """
            Method that contains loop for displaying manager menu
            Parameters : self
            Return type : None
        """
        logger.info("Manager menu displayed")         
        while True:
            if self.manager_menu():
                break

    @error_handler
    def manager_menu(self) -> bool:
        """
            Method that takes input from manager to perform operations, along with error handler decorator 
            Parameters : self
            Return type : bool
        """
        user_choice = input(PromptConfig.MANAGER_PROMPT + "\n")
        if user_choice == "1" : 
            self.obj_common_helper.display_user_details()
        elif user_choice == "2" :
            if not self.asset_data_obj.view_vendor():
                print("No data exists")
        elif user_choice == "3" :
            self.asset_data_obj.create_vendor()
            print("Data added successfully")
        elif user_choice == "4" :
            if not self.asset_data_obj.view_category():
                print("No data exists")
        elif user_choice == "5" :
            self.asset_data_obj.create_category()
            print("Category added successfully")
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
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
 