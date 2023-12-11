"""Module for taking input from for tracking assets"""
import logging
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from config.queries import Header
from utils.validations import InputValidations
from controllers.manager_controllers import ManagerControllers
from controllers.asset_data_controllers import AssetDataControllers

logger = logging.getLogger('track_asset_views')

class TrackAssetViews:
    """
        Class that contains menu options for taking input from manager & admin to perform tracking operations
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        Methods
        -------
        track_asset_operations() -> containing loop for displaying track asset menu
        track_asset_menu() -> contains menu options for taking input from manager & admin
    """
    def __init__(self) -> None:
        self.obj_asset_data_controller = AssetDataControllers()
        self.obj_common_helper = CommonHelper()
        self.obj_manager_controller = ManagerControllers()

    def track_input_username(self) -> None:
        if not self.obj_common_helper.display_user_details():
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            user_id = InputValidations.input_user_id()
            data = self.obj_manager_controller.fetch_by_username(user_id)
            if not data:
                print(PromptConfig.NO_DATA_EXISTS)
            CommonHelper.display_table(data,Header.SCHEMA_ASSETS_BY_USER_ID)

    def track_input_category(self) -> None:
        if not self.obj_asset_data_controller.view_category():
            return
        else:
            CommonHelper.display_table(data,Header.SCHEMA_CATEGORY_TABLE)
            category_id = InputValidations.input_category_id()
            data = self.obj_manager_controller.fetch_by_category(category_id)
            if not data:
                print(PromptConfig.NO_DATA_EXISTS)
            else:
                CommonHelper.display_table(data,Header.SCHEMA_ASSETS_BY_CATEGORY_ID)

    def track_input_vendor(self) -> None:
        if not self.obj_asset_data_controller.view_vendor():
            return
        else:
            CommonHelper.display_table(data,Header.SCHEMA_VENDOR_TABLE)
            vendor_email = InputValidations.input_email()
            data = self.obj_manager_controller.fetch_by_vendor(vendor_email)
            if not data:
                print(PromptConfig.NO_DATA_EXISTS)
            else:
                CommonHelper.display_table(data,Header.SCHEMA_ASSETS_BY_VENDOR_EMAIL)

    def track_asset_available(self) -> None:
        data = self.obj_manager_controller.fetch_asset_available()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)

    def track_asset_maintenance(self) -> None:
        data =  self.obj_manager_controller.fetch_asset_maintenance()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)

    def track_asset_operations(self) -> None:
        """
            Method that contains loop for displaying track asset menu
            Parameters : self
            Return type : None
        """
        logger.info("Track asset menu displayed")         
        while True:
            if self.track_asset_menu():
                break

    @error_handler
    def track_asset_menu(self) -> bool:
        """
            Method that takes input to perform operations, along with error handler decorator 
            Parameters : self
            Return type : bool
        """
        user_choice = input(PromptConfig.TRACK_ASSETS_PROMPT + "\n")
        if user_choice == "1" : 
            self.track_input_username()
        elif user_choice == "2" :
            self.track_input_category()
        elif user_choice == "3" :
            self.track_input_vendor()
        elif user_choice == "4" :
            self.track_asset_available()
        elif user_choice == "5" :
            self.track_asset_maintenance()
        elif user_choice == "6" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
