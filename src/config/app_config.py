"""This module contains all the app constants"""


class AppConfig:
    """Class is used to load all the appconfig constants"""

    DATABASE_LOCATION = r"models\asset_management.db"
    PROMPT_FILE_LOCATION = r"config\prompts\prompts.yaml"
    LOG_FILE_LOCATION = r"config\log_prompts\logs_config.yaml"
    MAX_LOGIN_ATTEMPTS = 3
    LOG_LOCATION = r"logs.txt"

    # roles of user
    ADMININSTRATOR = "admin"
    ASSET_MANAGER = "asset manager"
    EMPLOYEE = "employee"

    # regex patterns
    DATE_FORMAT = r"%Y-%m-%d"
    REGEX_USER_ID = r"^EMP[a-zA-Z0-9]{4}$"
    REGEX_ASSET_ID = r"^ASN[a-zA-Z0-9]{4}$"
    REGEX_CATEGORY_ID = r"^CAT[a-zA-Z0-9]{4}$"
    REGEX_MAPPING_ID = r"^MPN[a-zA-Z0-9]{4}$"
    REGEX_VENDOR_ID = r"^VEN[a-zA-Z0-9]{4}$"
    REGEX_ISSUE_ID = r"^ISN[a-zA-Z0-9]{4}$"
    REGEX_MAINTENANCE_ID = r"^MTN[a-zA-Z0-9]{4}$"
    REGEX_NAME = r"^([A-Za-z0-9]{3,20}.\s*)"
    REGEX_EMAIL = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
    REGEX_PASSWORD = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"

    ASSIGNABLE_ASSET_TYPE = "assignable"
    UNASSIGNABLE_ASSET_TYPE = "unassignable"
    UNAVAILABLE_STATUS = "unavailable"
    AVAILABLE_STATUS = "available"
    ASSET_LOCATION = "warehouse"

    #dictionary keys
    CATEGORY_ID = 'category_id'
    VENDOR_ID = 'vendor_id'
    MAPPING_ID = 'mapping_id'
    USER_ID = 'user_id'
    ASSET_ID= 'asset_id'
    USERNAME = 'username'
    PASSWORD = 'password'
    IS_CHANGED = 'is_changed'
    ROLE = 'role'
    CATEGORY_NAME = 'category_name'
    BRAND_NAME = 'brand_name'
    VENDOR_EMAIL = 'vendor_email'
    ASSET_TYPE = 'asset_type'
    MESSAGE = 'message'
    DESCRIPTION = 'description'
    ASSIGNED_TO = 'assigned_to'
    ASSET_STATUS = 'asset_status'
    ACCESS_TOKEN = 'access_token'
    OLD_PASSWORD = 'old_password'
    NEW_PASSWORD = 'new_password'
    CONFIRM_PASSWORD = 'confirm_password'
    VENDOR_NAME = 'vendor_name'

class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500
