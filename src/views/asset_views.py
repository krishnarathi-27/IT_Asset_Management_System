"""Module provides all the operations on assets"""
import logging
from utils.common_helper import CommonHelper
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from config.app_config import AppConfig
from controllers.asset_controllers import AssetControllers

logger = logging.getLogger('auth_views')

class AssetViews:
    """
        Class that contains methods to perform operations on assets
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        Methods
        -------

    """
    def __init__(self) -> None:
        self.obj_common_helper = CommonHelper()
        self.obj_asset_controller = AssetControllers()

    def add_asset(self) -> None:               
        while True:
            asset_type_choice = input(PromptConfig.ASSET_ASSIGNABLE_PROMPT)
            if asset_type_choice == '1':
                return_value = self.obj_asset_controller.add_asset_to_inventory(AppConfig.ASSIGNABLE_ASSET_TYPE)
                break
            elif asset_type_choice == '2':
                return_value = self.obj_asset_controller.add_asset_to_inventory(AppConfig.UNASSIGNABLE_ASSET_TYPE)
                break
            else:
                print(PromptConfig.INVALID_INPUT)
        if return_value == False:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            print(PromptConfig.ASSET_ADDED_SUCCESS)
            logging.info(LogsConfig.LOG_ASSET_ADDED)
    
    def view_asset(self) -> None:
        if not self.obj_asset_controller.view_asset():
            print("Data do not exists")

    def check_assign_asset(self) -> None:
        if self.obj_asset_controller.assign_asset():
            print(PromptConfig.ASSET_ASSIGN_SUCCESS)
            logger.info(LogsConfig.LOG_ASSET_ASSIGNED)
        else:
            print(PromptConfig.NO_DATA_EXISTS)

    def check_unassign_asset(self) -> None:
        if self.obj_asset_controller.unassign_asset():
            print(PromptConfig.ASSET_UNASSIGN_SUCCESS)
            logger.info(LogsConfig.LOG_ASSET_UNASSIGNED)
        else:
            print(PromptConfig.NO_DATA_EXISTS)
