"""This module contains prompts to load for the project"""
# third party imports
import yaml

# local imports
from config.app_config import AppConfig


class PromptConfig:
    """
    This class contains method to load all the prompts
    ...
    Methods
    -------
    load():
        This method loads all the project prompts from the yaml file
    """

    # headers
    HEADER_USERID = None
    HEADER_USERNAME = None
    HEADER_ROLE = None
    HEADER_VENDOR_ID = None
    HEADER_VENDOR_NAME = None
    HEADER_VENDOR_EMAIL = None
    HEADER_ACTIVE_STATUS = None
    HEADER_ASSET_ID = None
    HEADER_ASSET_TYPE = None
    HEADER_ASSIGNED_TO = None
    HEADER_ASSET_STATUS = None
    HEADER_PURCHASED_DATE = None
    HEADER_MAPPING_ID = None
    HEADER_MAINTENANCE_ID = None
    HEADER_START_DATE = None
    HEADER_RETURN_DATE = None
    HEADER_CATEGORY_ID = None
    HEADER_CATEGORY_NAME = None
    HEADER_BRAND_NAME = None
    HEADER_ISSUE_ID = None

    ADMIN_PROMPT = None
    MANAGER_PROMPT = None
    EMPLOYEE_PROMPT = None
    CREATE_NEW_USER_ROLE = None
    ASSET_ASSIGNABLE_PROMPT = None
    TRACK_ASSETS_PROMPT = None
    MAINTENANCE_PROMPT = None

    STARTING_APPLICATION = None
    EXIT_SYSTEM_PROMPT = None
    EXITING_APPLICATION = None
    DATA_ALREADY_EXISTS = None
    INVALID_INPUT = None
    ENTER_VENDOR_EMAIL = None
    SELECT_FROM_TABLE = None
    ENTER_ASSET_ID = None
    ENTER_VENDOR_ID = None
    ENTER_USER_ID = None
    ENTER_CATEGORY_ID = None
    ENTER_MAINTENANCE_ID = None
    ENTER_MAPPING_ID = None
    ENTER_ISSUE_ID = None
    CATEGORY_ID_NOT_EXISTS = None
    USER_NOT_EXISTS = None
    VENDOR_NOT_EXISTS = None
    NO_DATA_EXISTS = None
    ASSET_ID_NOT_EXISTS = None
    MAPPING_ID_NOT_EXISTS = None
    CATEGORY_ADDED = None
    CATEGORY_VENDOR_EXISTS = None
    ENTER_CATEGORY_NAME = None
    ENTER_BRAND_NAME = None

    # authentication file
    INVALID_LOGIN = None
    INPUT_DEFAULT_PASSWORD = None
    INPUT_NEW_PASSWORD = None
    INPUT_CONFIRM_PASSWORD = None
    PASSWORD_NOT_MATCH = None
    DEFAULT_PASSWORD_UPDATED = None
    ENTER_USERNAME = None
    ENTER_PASSWORD = None
    ATTEMPTS_MESSAGE = None
    ATTEMPTS_EXHAUSTED = None
    STRONG_PASSWORD = None
    LOGIN_AGAIN = None
    WAIT_FOR_LOGIN = None

    # admin
    WELCOME_ADMIN = None
    DEACTIVATED_VENDOR = None
    USERNAME_EXISTS = None
    USER_ADDED_SUCCESS = None
    USER_DELETED_SUCCESS = None
    VENDOR_NOT_EXIST_TO_DELETE = None

    # employee
    WELCOME_EMPLOYEE = None
    ISSUE_RAISED = None

    # manager
    WELCOME_MANAGER = None
    INPUT_VENDOR_EMAIL = None
    INPUT_VENDOR_NAME = None
    VENDOR_ADDED = None
    INPUT_PURCHASED_DATE = None
    ASSET_ADDED_SUCCESS = None
    ASSET_ASSIGN_SUCCESS = None
    ASSET_UNASSIGN_SUCCESS = None
    SEND_FOR_MAINTENANCE = None
    RECIEVE_FROM_MAINTENANCE = None

    # database_message
    DB_ERROR_MESSAGE = None
    DB_INTEGRITY_ERROR = None
    DB_GENERAL_ERROR = None
    INVALID_INPUT_ERROR = None
    GENERAL_EXCEPTION_MSG = None

    @classmethod
    def load(cls) -> None:
        """
        This method loads all the data from yaml
        Parameters = cls
        Return Type = None
        """
        with open(AppConfig.PROMPT_FILE_LOCATION, "r") as file:
            data = yaml.safe_load(file)

            # headers
            cls.HEADER_USERNAME = data["HEADER_USERNAME"]
            cls.HEADER_USERID = data["HEADER_USERID"]
            cls.HEADER_ROLE = data["HEADER_ROLE"]
            cls.HEADER_VENDOR_ID = data["HEADER_VENDOR_ID"]
            cls.HEADER_VENDOR_NAME = data["HEADER_VENDOR_NAME"]
            cls.HEADER_VENDOR_EMAIL = data["HEADER_VENDOR_EMAIL"]
            cls.HEADER_ACTIVE_STATUS = data["HEADER_ACTIVE_STATUS"]
            cls.HEADER_ASSET_ID = data["HEADER_ASSET_ID"]
            cls.HEADER_ASSET_TYPE = data["HEADER_ASSET_TYPE"]
            cls.HEADER_ASSIGNED_TO = data["HEADER_ASSIGNED_TO"]
            cls.HEADER_ASSET_STATUS = data["HEADER_ASSET_STATUS"]
            cls.HEADER_PURCHASED_DATE = data["HEADER_PURCHASED_DATE"]
            cls.HEADER_MAPPING_ID = data["HEADER_MAPPING_ID"]
            cls.HEADER_MAINTENANCE_ID = data["HEADER_MAINTENANCE_ID"]
            cls.HEADER_START_DATE = data["HEADER_START_DATE"]
            cls.HEADER_RETURN_DATE = data["HEADER_RETURN_DATE"]
            cls.HEADER_CATEGORY_ID = data["HEADER_CATEGORY_ID"]
            cls.HEADER_CATEGORY_NAME = data["HEADER_CATEGORY_NAME"]
            cls.HEADER_BRAND_NAME = data["HEADER_BRAND_NAME"]
            cls.HEADER_ISSUE_ID = data["HEADER_ISSUE_ID"]

            cls.ADMIN_PROMPT = data["ADMIN_PROMPT"]
            cls.MANAGER_PROMPT = data["MANAGER_PROMPT"]
            cls.EMPLOYEE_PROMPT = data["EMPLOYEE_PROMPT"]
            cls.CREATE_NEW_USER_ROLE = data["CREATE_NEW_USER_ROLE"]
            cls.ASSET_ASSIGNABLE_PROMPT = data["ASSET_ASSIGNABLE_PROMPT"]
            cls.TRACK_ASSETS_PROMPT = data["TRACK_ASSETS_PROMPT"]
            cls.MAINTENANCE_PROMPT = data["MAINTENANCE_PROMPT"]

            cls.STARTING_APPLICATION = data["STARTING_APPLICATION"]
            cls.EXIT_SYSTEM_PROMPT = data["EXIT_SYSTEM_PROMPT"]
            cls.EXITING_APPLICATION = data["EXITING_APPLICATION"]
            cls.DATA_ALREADY_EXISTS = data["DATA_ALREADY_EXISTS"]
            cls.INVALID_INPUT = data["INVALID_INPUT"]
            cls.ENTER_VENDOR_EMAIL = data["ENTER_VENDOR_EMAIL"]
            cls.SELECT_FROM_TABLE = data["SELECT_FROM_TABLE"]
            cls.ENTER_ASSET_ID = data["ENTER_ASSET_ID"]
            cls.ENTER_VENDOR_ID = data["ENTER_VENDOR_ID"]
            cls.ENTER_USER_ID = data["ENTER_USER_ID"]
            cls.ENTER_CATEGORY_ID = data["ENTER_CATEGORY_ID"]
            cls.ENTER_MAINTENANCE_ID = data["ENTER_MAINTENANCE_ID"]
            cls.ENTER_MAPPING_ID = data["ENTER_MAPPING_ID"]
            cls.ENTER_ISSUE_ID = data["ENTER_ISSUE_ID"]
            cls.CATEGORY_ID_NOT_EXISTS = ["CATEGORY_ID_NOT_EXISTS"]
            cls.USER_NOT_EXISTS = data["USER_NOT_EXISTS"]
            cls.VENDOR_NOT_EXISTS = data["VENDOR_NOT_EXISTS"]
            cls.NO_DATA_EXISTS = data["NO_DATA_EXISTS"]
            cls.ASSET_ID_NOT_EXISTS = data["ASSET_ID_NOT_EXISTS"]
            cls.MAPPING_ID_NOT_EXISTS = data["MAPPING_ID_NOT_EXISTS"]
            cls.CATEGORY_ADDED = data["CATEGORY_ADDED"]
            cls.CATEGORY_VENDOR_EXISTS = data["CATEGORY_VENDOR_EXISTS"]
            cls.ENTER_CATEGORY_NAME = data["ENTER_CATEGORY_NAME"]
            cls.ENTER_BRAND_NAME = data["ENTER_BRAND_NAME"]

            # authentication file
            cls.INVALID_LOGIN = data["INVALID_LOGIN"]
            cls.INPUT_DEFAULT_PASSWORD = data["INPUT_DEFAULT_PASSWORD"]
            cls.INPUT_NEW_PASSWORD = data["INPUT_NEW_PASSWORD"]
            cls.INPUT_CONFIRM_PASSWORD = data["INPUT_CONFIRM_PASSWORD"]
            cls.PASSWORD_NOT_MATCH = data["PASSWORD_NOT_MATCH"]
            cls.DEFAULT_PASSWORD_UPDATED = data["DEFAULT_PASSWORD_UPDATED"]
            cls.ENTER_USERNAME = data["ENTER_USERNAME"]
            cls.ENTER_PASSWORD = data["ENTER_PASSWORD"]
            cls.ATTEMPTS_MESSAGE = data["ATTEMPTS_MESSAGE"]
            cls.ATTEMPTS_EXHAUSTED = data["ATTEMPTS_EXHAUSTED"]
            cls.STRONG_PASSWORD = data["STRONG_PASSWORD"]
            cls.LOGIN_AGAIN = data["LOGIN_AGAIN"]
            cls.WAIT_FOR_LOGIN = data["WAIT_FOR_LOGIN"]

            # admin
            cls.WELCOME_ADMIN = data["WELCOME_ADMIN"]
            cls.DEACTIVATED_VENDOR = data["DEACTIVATED_VENDOR"]
            cls.USERNAME_EXISTS = data["USERNAME_EXISTS"]
            cls.USER_ADDED_SUCCESS = data["USER_ADDED_SUCCESS"]
            cls.USER_DELETED_SUCCESS = data["USER_DELETED_SUCCESS"]
            cls.VENDOR_NOT_EXIST_TO_DELETE = data["VENDOR_NOT_EXIST_TO_DELETE"]

            # employee
            cls.WELCOME_EMPLOYEE = data["WELCOME_EMPLOYEE"]
            cls.ISSUE_RAISED = data["ISSUE_RAISED"]

            # manager
            cls.WELCOME_MANAGER = data["WELCOME_MANAGER"]
            cls.INPUT_VENDOR_EMAIL = data["INPUT_VENDOR_EMAIL"]
            cls.INPUT_VENDOR_NAME = data["INPUT_VENDOR_NAME"]
            cls.VENDOR_ADDED = data["VENDOR_ADDED"]
            cls.INPUT_PURCHASED_DATE = data["INPUT_PURCHASED_DATE"]
            cls.ASSET_ADDED_SUCCESS = data["ASSET_ADDED_SUCCESS"]
            cls.ASSET_ASSIGN_SUCCESS = data["ASSET_ASSIGN_SUCCESS"]
            cls.ASSET_UNASSIGN_SUCCESS = data["ASSET_UNASSIGN_SUCCESS"]
            cls.SEND_FOR_MAINTENANCE = data["SEND_FOR_MAINTENANCE"]
            cls.RECIEVE_FROM_MAINTENANCE = data["RECIEVE_FROM_MAINTENANCE"]

            # database_message
            cls.DB_ERROR_MESSAGE = data["DB_ERROR_MESSAGE"]
            cls.DB_INTEGRITY_ERROR = data["DB_INTEGRITY_ERROR"]
            cls.DB_GENERAL_ERROR = data["DB_GENERAL_ERROR"]
            cls.INVALID_INPUT_ERROR = data["INVALID_INPUT_ERROR"]
            cls.GENERAL_EXCEPTION_MSG = data["GENERAL_EXCEPTION_MSG"]
