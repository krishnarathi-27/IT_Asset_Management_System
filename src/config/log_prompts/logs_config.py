"""This module contains logs to load for the project"""
# third party imports
import yaml

# local imports
from config.app_config import AppConfig


class LogsConfig:
    """
    This class contains method to load all the logs
    ...
    Methods
    -------
    load():
        This method loads all the project logs from the yaml file
    """

    # common
    LOG_CATEGORY_ADDED = None
    LOG_VENDOR_ADDED = None
    LOG_EXITING_APPLICATION = None

    # authentication logs
    LOG_LOGIN_ATTEMPTS_RESETTING = None
    LOG_LOGIN_ATTEMPT_REDUCING = None
    LOG_LOGIN_EXHAUSTED = None
    PROVIDE_ROLE_BASED_ACCESS = None
    LOG_INVALID_LOGIN = None
    LOG_STARTING_APPLICATION = None
    LOG_DEFAULT_PASSWORD = None

    # admin
    LOG_TO_DEACTIVATE_VENDOR = None
    LOG_ADMIN_MENU = None
    LOG_CREATE_NEW_USER = None
    LOG_ADMIN_LOGGED_IN = None
    LOG_VENDOR_DEACTIVATED = None

    # database
    LOG_ERROR_CONNECTING_DATABASE = None

    #asset_data
    LOG_VENDOR_DISPLAYED = None

    # employee
    LOG_EMPLOYEE_MENU = None
    LOG_EMPLOYEE_LOGGED_OUT = None
    LOG_ISSUE_RAISED = None
    LOG_EMPLOYEE_LOGGED_IN = None

    # manager
    LOG_MANAGER_MENU = None
    LOG_MANAGER_LOGGED_IN = None
    LOG_ASSET_ADDED = None
    LOG_ASSET_ASSIGNED = None
    LOG_ASSET_UNASSIGNED = None
    ASSET_RECIEVED_MAINTENANCE = None
    ASSET_SEND_MAINTENANCE = None
    LOG_ASSET_ADDED_INVENTORY = None

    #validations
    LOG_INVALID_NAME = None
    LOG_INVALID_EMAIL = None
    LOG_INVALID_PASSWORD = None
    LOG_INVALID_USER_ID = None
    LOG_INVALID_ASSET_ID = None
    LOG_INVALID_VENDOR_ID = None
    LOG_INVALID_CATEGORY_ID = None
    LOG_INVALID_MAPPING_ID = None
    LOG_INVALID_ISSUE_ID = None
    LOG_INVALID_MAINTENANCE_ID = None
    LOG_INVALID_DATE = None

    @classmethod
    def load(cls) -> None:
        """
        This method loads all the data from yaml
        Parameters = cls
        Return Type = None
        """
        with open(AppConfig.LOG_FILE_LOCATION, "r") as file:
            data = yaml.safe_load(file)

            # common
            cls.LOG_INVALID_INPUT = data["LOG_INVALID_INPUT"]
            cls.LOG_CATEGORY_ADDED = data["LOG_CATEGORY_ADDED"]
            cls.LOG_VENDOR_ADDED = data["LOG_VENDOR_ADDED"]
            cls.LOG_EXITING_APPLICATION = data["LOG_EXITING_APPLICATION"]

            # authentication logs
            cls.LOG_LOGIN_ATTEMPTS_RESETTING = data['LOG_LOGIN_ATTEMPTS_RESETTING']
            cls.LOG_LOGIN_EXHAUSTED = data['LOG_LOGIN_EXHAUSTED']
            cls.PROVIDE_ROLE_BASED_ACCESS = data["PROVIDE_ROLE_BASED_ACCESS"]
            cls.LOG_LOGIN_ATTEMPT_REDUCING = data["LOG_LOGIN_ATTEMPT_REDUCING"]
            cls.LOG_INVALID_LOGIN = data["LOG_INVALID_LOGIN"]
            cls.LOG_STARTING_APPLICATION = data["LOG_STARTING_APPLICATION"]
            cls.LOG_DEFAULT_PASSWORD = data["LOG_DEFAULT_PASSWORD"]

            # admin
            cls.LOG_TO_DEACTIVATE_VENDOR = data["LOG_TO_DEACTIVATE_VENDOR"]
            cls.LOG_ADMIN_MENU = data["LOG_ADMIN_MENU"]
            cls.LOG_CREATE_NEW_USER = data["LOG_CREATE_NEW_USER"]
            cls.LOG_ADMIN_LOGGED_IN = data["LOG_ADMIN_LOGGED_IN"]
            cls.LOG_VENDOR_DEACTIVATED = data["LOG_VENDOR_DEACTIVATED"]
            cls.LOG_ADMIN_LOGGED_OUT = data["LOG_ADMIN_LOGGED_OUT"]
            cls.LOG_USER_CREATED = data["LOG_USER_CREATED"]

            # database
            cls.LOG_ERROR_CONNECTING_DATABASE = data["LOG_ERROR_CONNECTING_DATABASE"]
            
            #asset_data
            cls.LOG_VENDOR_DISPLAYED = data["LOG_VENDOR_DISPLAYED"]
            cls.LOG_CATEGORY_DISPLAYED = data["LOG_CATEGORY_DISPLAYED"]

            # employee
            cls.LOG_EMPLOYEE_MENU = data['LOG_EMPLOYEE_MENU']
            cls.LOG_EMPLOYEE_LOGGED_OUT = data['LOG_EMPLOYEE_LOGGED_OUT']
            cls.LOG_ISSUE_RAISED = data["LOG_ISSUE_RAISED"]
            cls.LOG_EMPLOYEE_LOGGED_IN = data["LOG_EMPLOYEE_LOGGED_IN"]

            # manager
            cls.LOG_MANAGER_MENU = data["LOG_MANAGER_MENU"]
            cls.LOG_MANAGER_LOGGED_IN = data["LOG_MANAGER_LOGGED_IN"]
            cls.LOG_ASSET_ADDED = data["LOG_ASSET_ADDED"]
            cls.LOG_ASSET_ASSIGNED = data["LOG_ASSET_ASSIGNED"]
            cls.LOG_ASSET_UNASSIGNED = data["LOG_ASSET_UNASSIGNED"]
            cls.ASSET_SEND_MAINTENANCE = data["ASSET_SEND_MAINTENANCE"]
            cls.ASSET_RECIEVED_MAINTENANCE = data["ASSET_RECIEVED_MAINTENANCE"]
            cls.LOG_ASSET_ADDED_INVENTORY = data["LOG_ASSET_ADDED_INVENTORY"]

            #validation
            cls.LOG_INVALID_NAME = data['LOG_INVALID_NAME']
            cls.LOG_INVALID_EMAIL = data['LOG_INVALID_EMAIL']
            cls.LOG_INVALID_PASSWORD = data['LOG_INVALID_PASSWORD']
            cls.LOG_INVALID_USER_ID = data['LOG_INVALID_USER_ID']
            cls.LOG_INVALID_ASSET_ID = data['LOG_INVALID_ASSET_ID']
            cls.LOG_INVALID_VENDOR_ID = data['LOG_INVALID_VENDOR_ID']
            cls.LOG_INVALID_CATEGORY_ID = data['LOG_INVALID_CATEGORY_ID']
            cls.LOG_INVALID_MAPPING_ID = data['LOG_INVALID_MAPPING_ID']
            cls.LOG_INVALID_ISSUE_ID = data['LOG_INVALID_ISSUE_ID']
            cls.LOG_INVALID_MAINTENANCE_ID  = data['LOG_INVALID_MAINTENANCE_ID'] 
            cls.LOG_INVALID_DATE = data['LOG_INVALID_DATE']  
