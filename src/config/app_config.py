"""This module contains all the app constants"""


class AppConfig:
    """Class is used to load all the appconfig constants"""

    DATABASE_LOCATION = r"src\models\asset_management.db"
    PROMPT_FILE_LOCATION = r"src\config\prompts\prompts.yaml"
    LOG_FILE_LOCATION = r"src\config\log_prompts\logs_config.yaml"
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
    UNASSIGNABLE_ASSET_TYPE = "nassignable"
    UNAVAILABLE_STATUS = "unavailable"
    AVAILABLE_STATUS = "available"
    ASSET_LOCATION = "warehouse"
