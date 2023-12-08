"""Module for taking input from manager for various functionalities"""
import logging
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from controllers.asset_data_controllers import AssetDataControllers
from controllers.manager_controllers import ManagerControllers
from views.asset_views import AssetViews
from views.track_asset_views import TrackAssetViews
from views.maintenance_views import MaintenanceViews

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
        self.obj_asset = AssetViews()
        self.obj_asset_data = AssetDataControllers()
        self.obj_track_asset = TrackAssetViews()
        self.obj_manager_controller = ManagerControllers()
        self.obj_maintenance = MaintenanceViews(user_id)

    def check_category_created(self)->None:
        if self.obj_asset_data.create_category():
            print("Category added successfully")
        else:
            print("Data already exists")

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
            if not self.obj_asset_data.view_vendor():
                print(PromptConfig.NO_DATA_EXISTS)
        elif user_choice == "3" :
            self.obj_asset_data.create_vendor()
            print("Vendor added successfully")
        elif user_choice == "4" :
            if not self.obj_asset_data.view_category():
                print(PromptConfig.NO_DATA_EXISTS)
        elif user_choice == "5" :
            self.check_category_created()
        elif user_choice == "6" :
            self.obj_asset.add_asset()
        elif user_choice == "7" :
            self.obj_asset.view_asset()
        elif user_choice == "8" :
            self.obj_asset.check_assign_asset()
        elif user_choice == "9" : 
            self.obj_asset.check_unassign_asset()
        elif user_choice == "10":
            self.obj_track_asset.track_asset_operations()
        elif user_choice == "11":
            self.obj_maintenance.maintenance_operations()
        elif user_choice == "12":
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
 