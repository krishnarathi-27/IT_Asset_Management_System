"""Module for taking input from admin for various functionalities"""
import logging
from os import system
from controllers.admin_controllers import AdminControllers
from controllers.asset_data_controllers import AssetDataControllers
from utils.common_helper import CommonHelper
from config.queries import Header
from utils.validations import InputValidations
from utils.app_decorator import error_handler
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from views.asset_data_views import AssetDataViews

logger = logging.getLogger('admin_views')

class AdminViews(AssetDataViews):
    """
        Class that contains menu options for taking input from admin to perform admin operations
        ...
        Attributes
        ----------
        obj_common_helper = object of class CommonHelper
        Methods
        -------
        admin_operations() -> containing loop for displaying admin menu
        admin_menu() -> contains menu options for taking input from admin
    """
    def __init__(self) -> None:
        super().__init__()
        logger.info(LogsConfig.LOG_ADMIN_LOGGED_IN)
        print(PromptConfig.WELCOME_ADMIN)
        self.obj_asset_data = AssetDataControllers()
        self.obj_common_helper = CommonHelper()
        self.obj_admin_controller = AdminControllers()

    def admin_operations(self) -> None:
        """ Method that contains loop for displaying admin menu """
        logger.info("Admin menu displayed")
        while True:
            if self.admin_menu():
                break

    @error_handler
    def admin_menu(self) -> bool:
        """ Method that takes input from admin to perform operations, along with error handler decorator """
        user_choice = input(PromptConfig.ADMIN_PROMPT + "\n")
        # system('cls')
        if user_choice == "1" :
            self.obj_common_helper.display_user_details()
        elif user_choice == "2" :
            self.create_user()
        elif user_choice == "3" :
            self.display_vendors()
        elif user_choice == "4" :
            self.check_deactivate_vendor()
        elif user_choice == "5" :
            self.check_vendor_created()
        elif user_choice == "6" :
            self.display_category()
        elif user_choice == "7" :
           self.check_category_created()
        elif user_choice == "8" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
    
    def create_user(self) :
        username = InputValidations.input_name() 
        password =  InputValidations.input_password() 
        while True:
            role = input(PromptConfig.CREATE_NEW_USER_ROLE + "\n") 
            if role == '1':
                user_role = AppConfig.ASSET_MANAGER
                break         
            elif role == '2':
                user_role = AppConfig.EMPLOYEE
                break
            else:
                print(PromptConfig.INVALID_INPUT + "\n")

        self.obj_admin_controller.create_new_user(user_role,username,password)
        print("User added successfully")

    def check_deactivate_vendor(self) -> None:     
        """ Method that checks that vendor can be deactivated """
        data = self.obj_asset_data.view_vendor()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data,Header.SCHEMA_VENDOR_TABLE)
            vendor_email = InputValidations.input_email()
            if self.obj_admin_controller.deactivate_vendor(vendor_email):
                print("Vendor deactivated successfully")
            else:
                print("No data exists of vendor")
