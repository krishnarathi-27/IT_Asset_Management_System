"""dcf"""
import logging
from os import system
from utils.common_helper import CommonHelper
from config.queries import Header
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from utils.validations import InputValidations
from controllers.asset_data_controllers import AssetDataControllers

class AssetDataViews:

    def __init__(self):
        self.obj_asset_data = AssetDataControllers()

    def display_vendors(self) -> None:
        data = self.obj_asset_data.view_vendor()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_VENDOR_TABLE)
    
    def display_category(self) -> None:
        data = self.obj_asset_data.view_category()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_CATEGORY_TABLE)

    def check_category_created(self)->None:
        category_name = input(PromptConfig.ENTER_CATEGORY_NAME).strip().lower()
        brand_name = input(PromptConfig.ENTER_BRAND_NAME).strip().lower()
        vendor_email = InputValidations.input_email()
        if self.obj_asset_data.create_category(category_name,brand_name,vendor_email):
            print("Category added successfully")
        else:
            print("Data already exists")
            
    def check_vendor_created(self)->None:
        vendor_email = InputValidations.input_email()
        vendor_name = InputValidations.input_name()
        if self.obj_asset_data.create_vendor(vendor_email,vendor_name):
            print("Vendor added successfully")
        else:
            print("Data already exists")