"""This module contains logs to load for the project"""
#third party imports
import yaml

#local imports
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
        
    #common
    LOG_CATEGORY_ADDED = None
    LOG_VENDOR_ADDED = None

    #authentication logs
    PROVIDE_ROLE_BASED_ACCESS = None
    LOG_INVALID_LOGIN = None
    LOG_STARTING_APPLICATION = None
    LOG_DEFAULT_PASSWORD = None

    #admin
    LOG_CREATE_NEW_USER = None
    LOG_ADMIN_LOGGED_IN = None
    LOG_VENDOR_DEACTIVATED = None

    #database
    LOG_ERROR_CONNECTING_DATABASE = None

    #employee 
    LOG_ISSUE_RAISED = None
    LOG_EMPLOYEE_LOGGED_IN = None

    #manager
    LOG_MANAGER_LOGGED_IN = None
    LOG_ASSET_ADDED = None
    LOG_ASSET_ASSIGNED = None
    LOG_ASSET_UNASSIGNED = None

    @classmethod
    def load(cls) -> None:
        """
        This method loads all the data from yaml
        Parameters = cls 
        Return Type = None
        """
        with open(AppConfig.LOG_FILE_LOCATION,'r') as file:
            data = yaml.safe_load(file)

            #common
            cls.LOG_CATEGORY_ADDED = data['LOG_CATEGORY_ADDED']
            cls.LOG_VENDOR_ADDED = data['LOG_VENDOR_ADDED']

            #authentication logs
            cls.PROVIDE_ROLE_BASED_ACCESS = data['PROVIDE_ROLE_BASED_ACCESS']
            cls.LOG_INVALID_LOGIN = data['LOG_INVALID_LOGIN']
            cls.LOG_STARTING_APPLICATION = data['LOG_STARTING_APPLICATION']
            cls.LOG_DEFAULT_PASSWORD = data['LOG_DEFAULT_PASSWORD']

            #admin
            cls.LOG_CREATE_NEW_USER = data['LOG_CREATE_NEW_USER']
            cls.LOG_ADMIN_LOGGED_IN = data['LOG_ADMIN_LOGGED_IN']
            cls.LOG_VENDOR_DEACTIVATED = data['LOG_VENDOR_DEACTIVATED']

            #database
            cls.LOG_ERROR_CONNECTING_DATABASE = data['LOG_ERROR_CONNECTING_DATABASE']

            #employee 
            cls.LOG_ISSUE_RAISED = data['LOG_ISSUE_RAISED']
            cls.LOG_EMPLOYEE_LOGGED_IN = data['LOG_EMPLOYEE_LOGGED_IN']

            #manager
            cls.LOG_MANAGER_LOGGED_IN = data['LOG_MANAGER_LOGGED_IN']
            cls.LOG_ASSET_ADDED = data['LOG_ASSET_ADDED']
            cls.LOG_ASSET_ASSIGNED = data['LOG_ASSET_ASSIGNED']
            cls.LOG_ASSET_UNASSIGNED = data['LOG_ASSET_UNASSIGNED']

