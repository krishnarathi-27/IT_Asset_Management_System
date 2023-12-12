""" Module provides all the operations on assets """
import logging
#local imports
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from config.queries import Header
from config.app_config import AppConfig
from controllers.asset_controllers import AssetControllers
from utils.common_helper import CommonHelper
from utils.validations import InputValidations

logger = logging.getLogger('auth_views')

class AssetViews:
    """
        Class that contains methods to perform operations on assets
    """
    def __init__(self) -> None:
        self.obj_common_helper = CommonHelper()
        self.obj_asset_controller = AssetControllers()

    def input_asset_type(self) -> None:
        """ Method that takes asset type as input """

        while True:
            asset_type_choice = input(PromptConfig.ASSET_ASSIGNABLE_PROMPT)
            if asset_type_choice == '1':
                return AppConfig.ASSIGNABLE_ASSET_TYPE
            elif asset_type_choice == '2':
                return AppConfig.UNASSIGNABLE_ASSET_TYPE
            else:
                print(PromptConfig.INVALID_INPUT)

    def add_asset(self) -> None:   
        """ Method that takes asset data as input and adds asset to inventory """
        
        data = self.obj_asset_controller.display_mapping_id()

        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:            
            CommonHelper.display_table(data,Header.SCHEMA_MAPPING_CATGEORY_VENDOR_TABLE)
            mapping_id = InputValidations.input_mapping_id()
            purchased_date = InputValidations.input_date() 
            asset_type = self.input_asset_type()

            if not self.obj_asset_controller.add_asset_to_inventory(asset_type,mapping_id,purchased_date):
                print(PromptConfig.NO_DATA_EXISTS)
            else:
                print(PromptConfig.ASSET_ADDED_SUCCESS)
                logging.info(LogsConfig.LOG_ASSET_ADDED)
    
    def view_asset(self) -> None:
        """ Method that displays asset if exists in database """

        data = self.obj_asset_controller.view_asset()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)

    def check_assign_asset(self) -> None:
        """ Method that checks if assets can be assigned or not """

        data = self.obj_asset_controller.view_assignable_asset()

        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:

            CommonHelper.display_table(data,Header.SCHEMA_ASSIGNABLE_ASSET_DETAILS)
            asset_id = InputValidations.input_asset_id()

            self.obj_common_helper.display_user_details()
            user_id = InputValidations.input_user_id()

            if self.obj_asset_controller.assign_asset(asset_id,user_id):
                print(PromptConfig.ASSET_ASSIGN_SUCCESS)
                logger.info(LogsConfig.LOG_ASSET_ASSIGNED)
            else:
                print(PromptConfig.NO_DATA_EXISTS)

    def check_unassign_asset(self) -> None:
        """ Methods that checks if assets are unassigned or not """

        data = self.obj_asset_controller.view_unassignable_asset()

        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:

            CommonHelper.display_table(data,Header.SCHEMA_ASSET_TABLE)
            asset_id = InputValidations.input_asset_id()
            
            if self.obj_asset_controller.unassign_asset(asset_id):
                print(PromptConfig.ASSET_UNASSIGN_SUCCESS)
                logger.info(LogsConfig.LOG_ASSET_UNASSIGNED)
            else:
                print(PromptConfig.NO_DATA_EXISTS)
