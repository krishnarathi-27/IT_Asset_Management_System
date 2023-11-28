"""Module for taking input from admin for various functionalities"""
import logging
from os import system
from controllers.admin_controller import AdminController
from utils.common_helper import CommonHelper
from utils.app_decorator import error_handler
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from controllers.asset_data_controller import AssetDataController

logger = logging.getLogger('admin_views')

class AdminViews:
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
        logger.info(LogsConfig.LOG_ADMIN_LOGGED_IN)
        print(PromptConfig.WELCOME_ADMIN)
        self.obj_common_helper = CommonHelper()
        self.obj_admin_controller = AdminController()
        self.asset_data_obj = AssetDataController()

    def admin_operations(self) -> None:
        """
            Method that contains loop for displaying admin menu
            Parameters : self
            Return type : None
        """
        logger.info("Admin menu displayed")
        while True:
            if self.admin_menu():
                break

    @error_handler
    def admin_menu(self) -> bool:
        """
            Method that takes input from admin to perform operations, along with error handler decorator 
            Parameters : self
            Return type : bool
        """
        user_choice = input(PromptConfig.ADMIN_PROMPT + "\n")
        # system('cls')
        if user_choice == "1" :
            self.obj_common_helper.display_user_details()
        elif user_choice == "2" :
            self.__select_new_user()
            print("Data added successfully")
        elif user_choice == "3" :
            if not self.asset_data_obj.view_vendor():
                print("No data exists")
        elif user_choice == "4" :
            self.__check_deactivate_vendor()
        elif user_choice == "5" :
            self.asset_data_obj.create_vendor()
            print("Data added successfully")
        elif user_choice == "6" :
            if not self.asset_data_obj.view_category():
                print("No data exists")
        elif user_choice == "7" :
            if self.asset_data_obj.create_category():
                print("Category added successfully")
        elif user_choice == "8" : 
            self.track_asset_obj.menu_options()
        elif user_choice == "9" :
            return True
        else :
            print(PromptConfig.INVALID_INPUT + "\n") 
            logger.info("Invalid input entered")
        
        return False
    
    def __select_new_user(self) -> None:
        """
            Method that takes input from admin to select user role and create new user 
            Parameters : self
            Return type : None
        """
        while True:
            role = input(PromptConfig.CREATE_NEW_USER_ROLE + "\n") 
            if role == '1':
                user_role = AppConfig.ASSET_MANAGER
                return self.obj_admin_controller.create_new_user(user_role)           
            elif role == '2':
                user_role = AppConfig.EMPLOYEE
                return self.obj_admin_controller.create_new_user(user_role)
            else:
                print(PromptConfig.INVALID_INPUT + "\n")

    def __check_deactivate_vendor(self) -> None:     
        """
            Method that checks that vendor can be deactivated 
            Parameters : self
            Return type : None
        """
        if self.obj_admin_controller.deactivate_vendor():
            print("Vendor deactivated successfully")
        else:
            print("No data exists of vendor")
