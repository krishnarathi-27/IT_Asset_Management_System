"""Module for validating user input by correct regex pattern"""
import re
import maskpass
import logging
from datetime import datetime
from config.app_config import AppConfig
from config.prompts.prompts import PromptConfig
from config.log_prompts.logs_config import LogsConfig
from utils.app_decorator import loop

logger = logging.getLogger("validations")


class InputValidations:
    """Class containing methods to validate user input using regex pattern."""

    @staticmethod
    @loop
    def input_name() -> str:
        """
        Method to validate user entered name using regex pattern
        Return type : str
        """
        name = input(PromptConfig.ENTER_USERNAME).strip().lower()
        if re.match(AppConfig.REGEX_NAME, name):
            return name
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_NAME)

    @staticmethod
    @loop
    def input_email() -> str:
        """
        Method to validate user entered email using regex pattern
        Return type : str
        """
        email = input(PromptConfig.INPUT_VENDOR_EMAIL).strip()
        if re.match(AppConfig.REGEX_EMAIL, email):
            return email
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_EMAIL)

    @staticmethod
    @loop
    def input_password() -> str:
        """
        Method to validate user entered password using regex pattern
        Return type : str
        """
        password = maskpass.askpass(PromptConfig.ENTER_PASSWORD).strip()
        if re.match(AppConfig.REGEX_PASSWORD, password):
            return password
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_PASSWORD)

    @staticmethod
    @loop
    def input_user_id() -> str:
        """
        Method to validate user entered user id using regex pattern
        Return type : str
        """
        user_id = input(PromptConfig.ENTER_USER_ID).strip()
        if re.match(AppConfig.REGEX_USER_ID, user_id):
            return user_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_USER_ID)

    @staticmethod
    @loop
    def input_asset_id() -> str:
        """
        Method to validate user entered asset id using regex pattern
        Return type : str
        """
        asset_id = input(PromptConfig.ENTER_ASSET_ID).strip()
        if re.match(AppConfig.REGEX_ASSET_ID, asset_id):
            return asset_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_ASSET_ID)

    @staticmethod
    @loop
    def input_vendor_id() -> str:
        """
        Method to validate user entered vendor id using regex pattern
        Return type : str
        """
        vendor_id = input(PromptConfig.ENTER_VENDOR_ID).strip()
        if re.match(AppConfig.REGEX_VENDOR_ID, vendor_id):
            return vendor_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_VENDOR_ID)

    @staticmethod
    @loop
    def input_category_id() -> str:
        """
        Method to validate user entered category id using regex pattern
        Return type : str
        """
        vendor_id = input(PromptConfig.ENTER_CATEGORY_ID).strip()
        if re.match(AppConfig.REGEX_CATEGORY_ID, vendor_id):
            return vendor_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_CATEGORY_ID)

    @staticmethod
    @loop
    def input_mapping_id() -> str:
        """
        Method to validate user entered mapping id using regex pattern
        Return type : str
        """
        mapping_id = input(PromptConfig.ENTER_MAPPING_ID).strip()
        if re.match(AppConfig.REGEX_MAPPING_ID, mapping_id):
            return mapping_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_MAPPING_ID)

    @staticmethod
    @loop
    def input_issue_id() -> str:
        """
        Method to validate user entered issue id using regex pattern
        Return type : str
        """
        issue_id = input(PromptConfig.ENTER_ISSUE_ID).strip()
        if re.match(AppConfig.REGEX_ISSUE_ID, issue_id):
            return issue_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_ISSUE_ID)

    @staticmethod
    @loop
    def input_maintenance_id() -> str:
        """
        Method to validate user entered maintenance id using regex pattern
        Return type : str
        """
        maintenance_id = input(PromptConfig.ENTER_MAINTENANCE_ID).strip()
        if re.match(AppConfig.REGEX_MAINTENANCE_ID, maintenance_id):
            return maintenance_id
        print(PromptConfig.INVALID_INPUT)
        logger.info(LogsConfig.LOG_INVALID_MAINTENANCE_ID)

    @staticmethod
    @loop
    def input_date() -> str:
        """
        Method to validate user entered date using datetime.strptime()
        Return type : str
        """
        purchased_date = input(PromptConfig.INPUT_PURCHASED_DATE).strip()
        try:
            datetime.strptime(purchased_date, AppConfig.DATE_FORMAT)
            return purchased_date
        except:
            print(PromptConfig.INVALID_INPUT)
            logger.info(LogsConfig.LOG_INVALID_DATE)
