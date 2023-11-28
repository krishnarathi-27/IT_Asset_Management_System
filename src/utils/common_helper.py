"""Module contains common utility functions which are accessed across different modules"""
import logging
import hashlib
from tabulate import tabulate
from utils.validations import InputValidations
from models.database_helper import DatabaseHelper
from config.queries import Header
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig

logger = logging.getLogger('common_helper')

class CommonHelper:
    """
        Class contains methods which are common and used across various files.
        ...
        Attributes
        ----------
        db_obj = object of DatabaseHelper class

        Methods
        -------
        change_default_password() = Methods that changes default password on first valid login 
    """
    def __init__(self) -> None:
        self.db_obj = DatabaseHelper()

    def change_default_password(self,username: str) -> None:
        """
            Method for changing default password of validated user
            Parameters : self, username
            Return type : None
        """
        while True:
            logger.info("Validated user changing default password")
            print(PromptConfig.STRONG_PASSWORD)
            new_password = InputValidations.input_password()
            print(PromptConfig.INPUT_CONFIRM_PASSWORD)
            confirm_password = InputValidations.input_password()
            if new_password != confirm_password:
                print(PromptConfig.PASSWORD_NOT_MATCH)
                logger.info("New password not matches confirm new password")
            else:
                new_hashed_password = hashlib.sha256(new_password.encode()).hexdigest()    
                self.db_obj.update_default_password((new_hashed_password,username))
                print(PromptConfig.DEFAULT_PASSWORD_UPDATED)
                logger.info(LogsConfig.LOG_DEFAULT_PASSWORD)
                return

    @staticmethod        
    def display_table(data: list, headers: list) -> None:
        """
            Method to display data in tabular format using tabulate
            Parameters : data, headers
            Return type : None
        """
        row_id = [i for i in range(1, len(data) + 1)]
        print(
                tabulate(
                    data,
                    headers,
                    showindex = row_id,
                    tablefmt = "simple_grid"
                )
            )

    def display_user_details(self) -> None:
        """
            Method to display details of users 
            Parameters : self
            Return type : None
        """
        data = self.db_obj.get_user_details()
        if not data:
            print(PromptConfig.NO_DATA_EXISTS)
            return
        CommonHelper.display_table(data, Header.SCHEMA_USER_TABLE)

    @staticmethod
    def input_category_details() -> tuple:
        """
            Method to input category details 
            Parameters : self
            Return type : tuple
        """
        category_name = input(PromptConfig.ENTER_CATEGORY_NAME).strip().lower()
        brand_name = input(PromptConfig.ENTER_BRAND_NAME).strip().lower()
        vendor_email = InputValidations.input_email()

        return (category_name,brand_name,vendor_email)