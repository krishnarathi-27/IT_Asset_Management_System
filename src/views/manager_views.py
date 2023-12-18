"""Module for taking input from manager for various functionalities"""
import logging

# local imports
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from controllers.manager_controllers import ManagerControllers
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler, loop
from views.asset_views import AssetViews
from views.track_asset_views import TrackAssetViews
from views.maintenance_views import MaintenanceViews
from views.asset_data_views import AssetDataViews

logger = logging.getLogger("manager_views")


class ManagerViews(AssetDataViews):
    """
    Class that contains menu options for taking input from manager to perform manager operations
    """

    def __init__(self, user_id) -> None:
        super().__init__()
        logger.info(LogsConfig.LOG_MANAGER_LOGGED_IN)
        print(PromptConfig.WELCOME_MANAGER)
        self.user_id = user_id
        self.obj_common_helper = CommonHelper()
        self.obj_asset = AssetViews()
        self.obj_track_asset = TrackAssetViews()
        self.obj_manager_controller = ManagerControllers()
        self.obj_maintenance = MaintenanceViews(user_id)

    @loop
    @error_handler
    def manager_menu_operations(self) -> bool:
        """Method that takes input from manager to perform operations, along with error handler decorator"""

        logger.info(LogsConfig.LOG_MANAGER_MENU)
        user_choice = input(PromptConfig.MANAGER_PROMPT + "\n")

        if user_choice == "1":
            self.obj_common_helper.display_user_details()
        elif user_choice == "2":
            self.display_vendors()
        elif user_choice == "3":
            self.check_vendor_created()
        elif user_choice == "4":
            self.display_category()
        elif user_choice == "5":
            self.check_category_created()
        elif user_choice == "6":
            self.obj_asset.add_asset()
        elif user_choice == "7":
            self.obj_asset.view_asset()
        elif user_choice == "8":
            self.obj_asset.check_assign_asset()
        elif user_choice == "9":
            self.obj_asset.check_unassign_asset()
        elif user_choice == "10":
            self.obj_track_asset.track_asset_menu_operations()
        elif user_choice == "11":
            self.obj_maintenance.maintenance_menu_operations()
        elif user_choice == "12":
            return True
        else:
            print(PromptConfig.INVALID_INPUT + "\n")
            logger.info(LogsConfig.LOG_INVALID_INPUT)

        return False
