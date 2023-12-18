"""Module for taking input from admin for various functionalities"""
import logging

# local imports
from config.app_config import AppConfig
from config.log_prompts.logs_config import LogsConfig
from config.prompts.prompts import PromptConfig
from config.queries import Header
from controllers.admin_controllers import AdminControllers
from controllers.asset_data_controllers import AssetDataControllers
from utils.app_decorator import error_handler, loop
from utils.common_helper import CommonHelper
from utils.validations import InputValidations
from views.asset_data_views import AssetDataViews

logger = logging.getLogger("admin_views")


class AdminViews(AssetDataViews):
    """
    Class that contains menu options for taking input from admin to perform admin operations
    """

    def __init__(self) -> None:
        super().__init__()
        self.obj_asset_data = AssetDataControllers()
        self.obj_common_helper = CommonHelper()
        self.obj_admin_controller = AdminControllers()

        logger.info(LogsConfig.LOG_ADMIN_LOGGED_IN)
        print(PromptConfig.WELCOME_ADMIN)

    @loop
    @error_handler
    def admin_menu_operations(self) -> bool:
        """Method that takes input from admin to perform operations, along with error handler decorator"""

        logger.info(LogsConfig.LOG_ADMIN_MENU)
        user_choice = input(PromptConfig.ADMIN_PROMPT + "\n")

        if user_choice == "1":
            self.obj_common_helper.display_user_details()
        elif user_choice == "2":
            self.create_user()
        elif user_choice == "3":
            self.display_vendors()
        elif user_choice == "4":
            self.check_deactivate_vendor()
        elif user_choice == "5":
            self.check_vendor_created()
        elif user_choice == "6":
            self.display_category()
        elif user_choice == "7":
            self.check_category_created()
        elif user_choice == "8":
            logger.info(LogsConfig.LOG_ADMIN_LOGGED_OUT)
            return True
        else:
            print(PromptConfig.INVALID_INPUT + "\n")
            logger.info(LogsConfig.LOG_INVALID_INPUT)

        return False

    def create_user(self) -> None:
        """Method to create new user in the system"""

        logger.info(LogsConfig.LOG_CREATE_NEW_USER)

        username = InputValidations.input_name()
        password = InputValidations.input_password()
        while True:
            role = input(PromptConfig.CREATE_NEW_USER_ROLE + "\n")
            if role == "1":
                user_role = AppConfig.ASSET_MANAGER
                break
            elif role == "2":
                user_role = AppConfig.EMPLOYEE
                break
            else:
                print(PromptConfig.INVALID_INPUT + "\n")

        self.obj_admin_controller.create_new_user(user_role, username, password)

        print(PromptConfig.USER_ADDED_SUCCESS)

    def check_deactivate_vendor(self) -> None:
        """Method that checks that vendor is deactivated or not"""
        logger.info(LogsConfig.LOG_TO_DEACTIVATE_VENDOR)
        
        data = self.obj_asset_data.view_vendor()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
        else:
            CommonHelper.display_table(data, Header.SCHEMA_VENDOR_TABLE)
            vendor_email = InputValidations.input_email()
            if self.obj_admin_controller.deactivate_vendor(vendor_email):
                print(PromptConfig.DEACTIVATED_VENDOR)
            else:
                print(PromptConfig.VENDOR_NOT_EXIST_TO_DELETE)
