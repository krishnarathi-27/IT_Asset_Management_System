"""Module that have the functionality of interacting with user for asset's data or information"""
import logging
#local imports
from config.queries import Header
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from controllers.asset_data_controllers import AssetDataControllers
from utils.common_helper import CommonHelper
from utils.validations import InputValidations

logger = logging.getLogger('asset_data_views')

class AssetDataViews:

    def __init__(self) -> None:
        self.obj_asset_data = AssetDataControllers()

    def display_vendors(self) -> None:
        """ Method that displays all the vendor if exists """

        logger.info("Displays vendors of the system")

        data = self.obj_asset_data.view_vendor()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_VENDOR_TABLE)
    
    def display_category(self) -> None:
        """ Method that displays all the category of assets if exists """

        logger.info("Displays category of the system")
        
        data = self.obj_asset_data.view_category()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_CATEGORY_TABLE)

    def check_category_created(self) -> None:
        """ Method that inputs category data and check is category is created or not """

        category_name = input(PromptConfig.ENTER_CATEGORY_NAME).strip().lower()
        brand_name = input(PromptConfig.ENTER_BRAND_NAME).strip().lower()
        vendor_email = InputValidations.input_email()
        
        if self.obj_asset_data.create_category(category_name,brand_name,vendor_email):
            print(PromptConfig.CATEGORY_ADDED)
            logger.info(LogsConfig.LOG_CATEGORY_ADDED)
        else:
            print(PromptConfig.DATA_ALREADY_EXISTS)
            
    def check_vendor_created(self) -> None:
        """ Method that inputs vendor data and check if vendor is created or not """

        vendor_email = InputValidations.input_email()
        vendor_name = InputValidations.input_name()

        if self.obj_asset_data.create_vendor(vendor_email,vendor_name):
            print(PromptConfig.VENDOR_ADDED)
            logger.info(LogsConfig.LOG_VENDOR_ADDED)
        else:
            print(PromptConfig.DATA_ALREADY_EXISTS)