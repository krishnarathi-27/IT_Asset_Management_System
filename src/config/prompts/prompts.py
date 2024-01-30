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
    USER_ID_PREFIX = None
    ASSET_ID_PREFIX = None
    VENDOR_ID_PREFIX = None
    CATEGORY_ID_PREFIX = None
    MAPPING_ID_PREFIX = None
    ISSUE_ID_PREFIX = None

    CONFLICT_MSG = None
    INTERNAL_SERVER_ERROR = None
    USERNAME_EXISTS = None
    SERVER_ERROR = None
    RESOURCE_NOT_FOUND = None

    VENDOR_NOT_EXISTS = None
    USER_NOT_EXISTS = None
    UNAUTHORISED = None
    BAD_REQUEST = None
    INVALID_CREDENTIALS_ENTERED = None
    PASSWORDS_NOT_MATCH = None
    ASSETS_NOT_EXISTS = None
    CATEGORY_NOT_EXISTS = None
    ASSET_ID_NOT_EXISTS = None
    VENDOR_ALREADY_EXISTS = None
    CATEGORY_ALREADY_EXISTS = None
    ISSUE_ALREADY_EXISTS= None
    ISSUE_NOT_EXISTS = None
    ASSET_CREATED = None
    ASSET_ASSIGNED = None
    ASSET_UNASSIGNED = None
    USER_LOGGED_IN = None
    CATEGORY_CREATED = None
    ISSUE_CREATED = None
    USER_CREATED = None
    PASSWORD_UPDATED = None
    VENDOR_CREATED = None
    VENDOR_DEACTIVATED = None

    @classmethod
    def load(cls) -> None:
        """
        This method loads all the data from yaml
        Parameters = cls
        Return Type = None
        """
        with open(AppConfig.PROMPT_FILE_LOCATION, "r") as file:
            data = yaml.safe_load(file)

            cls.USER_ID_PREFIX = data['USER_ID_PREFIX']
            cls.ASSET_ID_PREFIX = data['ASSET_ID_PREFIX']
            cls.VENDOR_ID_PREFIX = data['VENDOR_ID_PREFIX']
            cls.CATEGORY_ID_PREFIX = data['CATEGORY_ID_PREFIX']
            cls.MAPPING_ID_PREFIX = data['MAPPING_ID_PREFIX']
            cls.ISSUE_ID_PREFIX = data['ISSUE_ID_PREFIX']

            cls.CONFLICT_MSG = data['CONFLICT_MSG']
            cls.INTERNAL_SERVER_ERROR = data['INTERNAL_SERVER_ERROR']
            cls.USERNAME_EXISTS = data['USERNAME_EXISTS']
            cls.SERVER_ERROR = data['SERVER_ERROR']
            cls.RESOURCE_NOT_FOUND = data['RESOURCE_NOT_FOUND']

            cls.VENDOR_NOT_EXISTS = data['VENDOR_NOT_EXISTS']
            cls.USER_NOT_EXISTS = data['USER_NOT_EXISTS']
            cls.UNAUTHORISED = data['UNAUTHORISED']
            cls.BAD_REQUEST = data['BAD_REQUEST']
            cls.INVALID_CREDENTIALS_ENTERED = data['INVALID_CREDENTIALS_ENTERED']
            cls.PASSWORDS_NOT_MATCH = data['PASSWORDS_NOT_MATCH']
            cls.ASSETS_NOT_EXISTS = data['ASSETS_NOT_EXISTS']
            cls.CATEGORY_NOT_EXISTS = data['CATEGORY_NOT_EXISTS']
            cls.ASSET_ID_NOT_EXISTS = data['ASSET_ID_NOT_EXISTS']
            cls.VENDOR_ALREADY_EXISTS = data['VENDOR_ALREADY_EXISTS']
            cls.CATEGORY_ALREADY_EXISTS = data['CATEGORY_ALREADY_EXISTS']
            cls.ISSUE_ALREADY_EXISTS = data['ISSUE_ALREADY_EXISTS']
            cls.ISSUE_NOT_EXISTS = data['ISSUE_NOT_EXISTS']
            cls.ASSET_CREATED = data['ASSET_CREATED']
            cls.ASSET_ASSIGNED = data['ASSET_ASSIGNED']
            cls.ASSET_UNASSIGNED = data['ASSET_UNASSIGNED']
            cls.USER_LOGGED_IN = data['USER_LOGGED_IN']
            cls.CATEGORY_CREATED = data['CATEGORY_CREATED']
            cls.ISSUE_CREATED = data['ISSUE_CREATED']
            cls.USER_CREATED = data['USER_CREATED']
            cls.PASSWORD_UPDATED = data['PASSWORD_UPDATED']
            cls.VENDOR_CREATED = data['VENDOR_CREATED']
            cls.VENDOR_DEACTIVATED = data['VENDOR_DEACTIVATED']
